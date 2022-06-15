import json
import math
import os
import os.path
import pickle
import re
import subprocess
import sys
import threading
import time
from datetime import datetime
from io import StringIO
from itertools import repeat
from typing import Any, Optional, Set, Tuple, TypeVar

import git
import pandas as pd
import requests
import ruamel.yaml as yaml
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pandas import Series, DataFrame


class RunCmd(threading.Thread):
    """Run a subprocess command, if it exceeds the timeout kill it.

    (without mercy)
    """

    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = subprocess.Popen(self.cmd)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()  # use self.p.kill() if process needs a kill -9
            self.join()


def build_spreadsheet_service():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "marking_and_admin/credentials.json", SCOPES
            )
            try:
                creds = flow.run_local_server()
            except OSError as e:
                print(e)
                creds = flow.run_console()
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("sheets", "v4", credentials=creds)
    return service


def write(service, data=[["These"], ["are"], ["some"], ["d", "entries"]]):
    comment_list = process_for_notes(data)
    # Writing values
    body = {"values": process_for_writing(data)}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=MARKING_SPREADSHEET_ID,
            range="testing!A2:Z100",
            valueInputOption="RAW",
            body=body,
        )
        .execute()
    )
    print(f"{result.get('updatedCells')} cells updated.")

    # Write comments
    body = {"requests": comment_list}
    result = (
        service.spreadsheets()
        .batchUpdate(spreadsheetId=MARKING_SPREADSHEET_ID, body=body)
        .execute()
    )
    print(f"{result.get('totalUpdatedCells')} cells updated.")


def process_for_writing(data):
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if type(item) is dict:
                data[i][j] = item.get("mark")
            elif type(item) is not str and math.isnan(item):
                data[i][j] = ""
    return data


def process_for_notes(data):
    comments = []
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if type(item) is dict:
                readable_comment: str = prepare_comment(item)
                ss_comment_package: dict = set_comment(j, i, readable_comment)
                comments.append(ss_comment_package)
    return comments


def prepare_comment(item: dict) -> str:
    if "results" not in item.keys():
        return f"⚠ {item['bigerror']} ⏱ {round(item['time'])}"
    test_results = []
    for r in item["results"]:
        icon = "👏" if r["value"] == 1 else "💩"
        test_results.append(f"{icon}: {r['name']}")
    tr = "\n".join(test_results)
    message = f"""{item['name']}
⏱ {round(item['time'])}
{tr}
{item['mark']}/{item['of_total']}"""
    return message


def set_comment(x, y, comment, y_offset=1):
    request: dict[str, Any] = {
        "repeatCell": {
            "range": {
                "sheetId": 1704890600,
                "startRowIndex": y + y_offset,
                "endRowIndex": y + 1 + y_offset,
                "startColumnIndex": x,
                "endColumnIndex": x + 1,
            },
            "cell": {"note": comment},
            "fields": "note",
        }
    }
    return request


def get_DF_from_CSV_URL(url, columnNames=False):
    """Get a csv of values from google docs."""
    r = requests.get(url)
    data = r.text
    if columnNames:
        return pd.read_csv(StringIO(data), header=0, names=columnNames)
    else:
        return pd.read_csv(StringIO(data))


def get_forks(
    org: str = "design-computing",
    repo: str = "me",
    force_inclusion_of_these_repos: list[str] = [],
) -> list[dict]:
    """Get a list of dicts of the user names and the git url for all the forks."""
    api = "https://api.github.com"
    limit = 100
    client_id = "040e86e3feed633710a0"
    secret = "69588d73388091b5ff8635fd1a788ea79177bf69"
    url = (
        f"{api}/repos/{org}/{repo}/forks?"
        f"per_page={limit}&"
        f"client_id={client_id}&"
        f"client_secret={secret}'"
    )
    print("get forks from:\n", url)
    r = requests.get(url)
    if r.status_code == 200:
        forks = r.json()
        repos = [
            {"owner": fork["owner"]["login"], "git_url": fork["git_url"]}
            for fork in forks
            # filter for this year's repos
            if (fork["created_at"][:4] == THIS_YEAR)
            # a list of repos to get that aren't this year's, to account for students retaking the course
            or (fork["owner"]["login"] in force_inclusion_of_these_repos)
        ]
        return repos
    else:
        rate_limit_message(r)
        raise Exception("GitHubFuckYouError")


def rate_limit_message(r):
    rate_limit = requests.get("https://api.github.com/rate_limit").json().get("rate")
    reset_time = str(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(rate_limit["reset"]))
    )
    print(
        r.status_code,
        r.reason,
        json.dumps(r.json(), indent=2),
        json.dumps(rate_limit, indent=2),
        "try again at" + reset_time,
        sep="\n",
    )


def update_repos(row: Series) -> str:
    """Git clone a repo, or if already cloned, git pull."""
    url = row["git_url"]
    owner = row["owner"]
    path = os.path.normpath(os.path.join(ROOTDIR, owner))
    t = datetime.now().strftime("%H:%M:%S")
    try:
        git.Repo.clone_from(url, path)
        print(f"{t}: new repo for {owner}")
        return ":) new"
    except git.GitCommandError as git_command_error:
        if "already exists and is not an empty directory" in git_command_error.stderr:
            if CHATTY:
                print(f"We already have {owner}, trying a pull. ({git_command_error})")
            try:
                repo = git.cmd.Git(path)
                try:
                    response = repo.pull()
                    print(f"{t}: pulled {owner}'s repo: {response}")
                    return str(response)
                except Exception as e:
                    repo.execute(["git", "fetch", "--all"])
                    repo.execute(["git", "reset", "--hard", "origin/main"])
                    print(e)
                    return "hard reset"
            except Exception as e:
                if CHATTY:
                    print(f"pull error: {row.name} {row.contactEmail}", e)
                return str(e)
        else:
            message = f"{row['owner']}: unexpected error: {git_command_error}"
            print(message)
            return message
    except Exception as spare_error:
        message = f"clone error other than existing repo: {spare_error}"
        if CHATTY:
            print(message, f"{row.name} {row.contactEmail}", spare_error)
        return message


def try_to_kill(file_path: str, CHATTY: bool = False):
    """Attempt to delete the file specified by file_path."""
    try:
        os.remove(file_path)
        print(f"deleted {file_path}")
    except Exception as e:
        if CHATTY:
            print(file_path, e)


def pull_all_repos(dirList, CHATTY: bool = False, hardcore_pull: bool = False):
    """Pull latest version of all repos."""
    of_total = len(dirList)
    for i, student_repo in enumerate(dirList):
        repo_is_here = os.path.join(ROOTDIR, student_repo)
        try:
            repo = git.cmd.Git(repo_is_here)
            if hardcore_pull:
                repo.execute(["git", "fetch", "--all"])
                repo.execute(["git", "reset", "--hard", "origin/main"])
            repo.pull()  # probably not needed, but belt and braces
            t = datetime.now().strftime("%H:%M:%S")
            print(f"{t}: {i}/{of_total} pulled {student_repo}'s repo")
        except Exception as e:
            print(student_repo, e)


def csv_of_details(dirList):
    """Make a CSV of all the students."""
    results = []
    for student_repo in dirList:
        path = os.path.join(ROOTDIR, student_repo, "aboutMe.yml")
        details = open(path).read()
        # replaces the @ symbol
        details = details.replace("@", "^AT^")
        # bumps unspaced values off the colon so that it parses
        details = re.sub(":(\w)", ": \g<1>", details)
        details = re.sub(" -", " None", details)
        details = details.replace("é", "e")
        details = details.replace("w:", "w: ")
        try:
            details = yaml.load(details, yaml.RoundTripLoader)
            details["repoName"] = student_repo
            details["error"] = False
            # if details["mediumUsername"][:4] != "^AT^":
            #     details["mediumUsername"] = "^AT^" + details["mediumUsername"]
            results.append(details)

            if details["studentNumber"] == "z1234567":
                print(student_repo, "hasn't updated")
        except Exception as e:
            print(details)
            results.append({"error": e, "repoName": student_repo})

    print("\n\nResults:")
    resultsDF = pd.DataFrame(results)
    # print(resultsDF)
    resultsDF.to_csv(os.path.join(CWD, "csv/studentDetails.csv"))
    fix_up_csv()


def fix_up_csv(path="csv/studentDetails.csv"):
    """Do replacements on csv.

    Mostly to undo tricks that were needed to deal with invalid yml
    """
    lines = []
    with open(path) as infile:
        for line in infile:
            line = line.replace("^AT^", "@")
            line = line.replace(",,", ",-,")
            lines.append(line)
    with open(path, "w") as outfile:
        for line in lines:
            print(line)
            outfile.write(line)


def log_progress(message, logfile_name):
    """Write a message to a logfile."""
    completed_students_list = open(logfile_name, "a")
    completed_students_list.write(message)
    completed_students_list.close()


def get_readmes(row, output="mark", print_labbooks=False):
    """Get the text, or the mark, or both related to log books."""
    # intro_set  = "TODO: Reflect on what you learned this set and what is still unclear."
    # intro_week = "TODO: Reflect on what you learned this week and what is still unclear."
    regex = r"TODO: Reflect.+unclear\."
    subst = ""
    path = os.path.join(ROOTDIR, row.owner)
    mark = 0
    all_readme = ""
    for i in range(1, 11):
        p = os.path.join(path, f"set{i}", "readme.md")
        if os.path.isfile(p):
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as f:
                    contents = f.read()
                    new = re.sub(regex, subst, contents, 0, re.MULTILINE).strip()
                    # print(i,"|", new, "|", len(new))
                    if len(new) > 0:
                        mark += 1
                        all_readme += f"w{i}: {new}\n\n"
                        if print_labbooks:
                            print(f"{row.owner}, w{i}: {new}")
            except UnicodeDecodeError:
                # if there's strange unicode in here, something must be going on!
                mark += 1

    if output == "mark":
        return mark
    elif output == "textList":
        return str(all_readme)
    else:
        return [mark, all_readme]


def test_in_clean_environment(
    row: Series,
    set_number: int,
    timeout: int = 5,
    logfile_name: str = "log.txt",
    temp_file_path: str = "temp_results.json",
    test_file_path: str = "test_shim.py",
) -> dict:
    pre = f"W{set_number}, {row.owner}:"
    marks_csv_exists = os.path.isfile(MARKS_CSV)
    if (
        "updated" in row.index
        and "Already up to date" in row.updated
        and not FORCE_MARKING
        and marks_csv_exists
    ):
        print(f"{pre} We don't need to mark this one")
        results_dict = get_existing_marks_from_csv(row, set_number)
    else:
        print(
            f"{pre} We need to mark this one ",
            "FORCE" if FORCE_MARKING else "🔰",
        )
        results_dict = mark_a_specific_person_week(
            row, set_number, timeout, logfile_name, temp_file_path, test_file_path
        )
    return results_dict


def get_existing_marks_from_csv(row: Series, set_number: int) -> dict:
    whole_csv_df = pd.read_csv(MARKS_CSV)
    this_person_df = whole_csv_df[whole_csv_df.owner == row.owner]
    try:
        # TODO: should this eval or json.loads?
        # json.loads has a problem because the strings in the keys are wrapped
        # in single quotes. I'm not sure how to save the csv with double quotes
        # as it's the default behaviour of to_csv.
        # results_dict = json.loads(str(this_person_df.iloc[0][f"set{set_number}"]))
        cell = this_person_df.iloc[0][f"set{set_number}"]
        results_dict = eval(str(cell))
        return results_dict
    except KeyError as k:
        print(f"no marks for set{set_number}", k)
        return {}
    except Exception as e:
        print(e)
        return {}


def mark_a_specific_person_week(
    row,
    set_number,
    timeout,
    logfile_name,
    temp_file_path,
    test_file_path,
):
    """Test a single student's work in a clean environment.

    This calls a subprocess that opens a fresh python environment, runs the
    tests and then saves the results to a temp file.

    Back in this process, we read that temp file, and then use its values to
    constuct a dictionary of results (or errors).

    The logging is just to see real time progress as this can run for a long
    time and hang the machine.
    """
    results_dict = {}
    log_progress(row.owner, logfile_name)
    start_time = time.time()

    python = sys.executable
    path_to_test_shim = get_safe_path("marking_and_admin", test_file_path)
    path_to_tests = get_safe_path("..", "course", f"set{set_number}", "tests.py")
    path_to_repo = get_safe_path(ROOTDIR, row.owner)

    test_args = [python, path_to_test_shim, path_to_tests, path_to_repo, row.owner]

    try:
        RunCmd(test_args, timeout).Run()  # this is unessarily complicated

        # full_path = os.path.join(LOCAL, temp_file_path)
        with open(
            temp_file_path, "r", encoding="utf-8", errors="ignore"
        ) as temp_results:
            contents = temp_results.read()
            results_dict = json.loads(contents)
            results_dict["bigerror"] = ":)"
        log_progress(f" good for w{set_number}\n", logfile_name)
    except Exception as e:
        results_dict = {
            "bigerror": str(e).replace(",", "~"),
            "name": row.owner,
        }  # the comma messes with the csv

        log_progress(f" bad {e} w{set_number}\n", logfile_name)

    elapsed_time = time.time() - start_time
    results_dict["time"] = elapsed_time
    return results_dict


def get_safe_path(*parts):
    joined = os.path.join(*parts)
    abs_path = os.path.abspath(joined)
    return abs_path


def prepare_log(logfile_name, firstLine="here we go:\n"):
    """Create or empty the log file."""
    completed_students_list = open(logfile_name, "w")
    completed_students_list.write(firstLine)
    completed_students_list.close()


def mark_work(dirList, set_number, root_dir, dfPlease=True, timeout=5):
    """Mark the set's exercises."""
    logfile_name = "temp_completion_log"
    prepare_log(logfile_name)
    r = len(dirList)  # for repeat count

    results = list(
        map(
            test_in_clean_environment,  # Function name
            dirList,  # student_repo
            repeat(root_dir, r),  # root_dir
            repeat(set_number, r),  # set_number
            repeat(logfile_name, r),  # logfile_name
            repeat(timeout, r),  # timeout
        )
    )

    resultsDF = pd.DataFrame(results)
    csv_path = f"csv/set{set_number}marks.csv"
    resultsDF.to_csv(os.path.join(CWD, csv_path), index=False)
    for _ in [1, 2, 3]:
        # this is pretty dirty, but it gets tricky when you have
        # ,,, -> ,-,, because each intance needs to be replaced multiple times
        # TODO; #makeitnice
        fix_up_csv(path=csv_path)
    print("\n+-+-+-+-+-+-+-+\n\n")
    if dfPlease:
        return resultsDF


def get_details(row: Series) -> dict:
    try:
        path_to_aboutMe = os.path.abspath(
            os.path.join(ROOTDIR, row.owner, "aboutMe.yml")
        )
        details_raw_yaml = open(path_to_aboutMe).read()
        details: dict = yaml.load(details_raw_yaml, yaml.RoundTripLoader)
        details["error"] = False
        details["owner"] = row.owner
        details["contactEmail"] = construct_contact_email(details)
        return dict(details)
    except Exception as e:
        print(row)
        return {"error": "|".join(str(e).splitlines()), "owner": row.owner}


def construct_contact_email(details: dict) -> str:
    return f"""{details["contactEmail"]["firstBit"]}@{details["contactEmail"]["otherBit"]}"""


def get_last_commit(row: Series) -> str:
    path = os.path.join(ROOTDIR, row.owner)
    repo = git.cmd.Git(path)
    d = str(repo.execute(["git", "log", "-1", "--format=%cd"]))
    return d


def mark_week(
    mark_sheet: DataFrame,
    set_number: int = 1,
    timeout: int = 10,
    active: bool = True,
):
    """Mark a single week for all students.

    Args:
        mark_sheet (Dataframe): A dataframe that describes who's going to get marked
        set_number (int, optional): The number of the set that we're marking. Defaults to 1.
        timeout (int, optional): number of seconds to try for before we cut this student off. Defaults to 10.
        active (bool, optional): Is this week being marked yet?. Defaults to True.

    Returns:
        Series: A series of the marks, or if not active yet, 0
    """
    if active:
        mark = mark_sheet.apply(
            test_in_clean_environment,
            args=(set_number, timeout),
            axis=1,
        )
        return mark
    else:
        return 0


def do_the_marking(
    this_year="2022",
    rootdir="../StudentRepos",
    chatty=False,
    force_marking=False,
    marking_spreadsheet_id="16tESt_4BUf-9-oD04suTprkd1O0oEl6WjzflF_avSKY",  # 2022
    marks_csv="marks.csv",
    mark_w1=True,
    mark_w2=False,
    mark_w3=False,
    mark_w4=False,
    mark_w5=False,
    mark_exam=False,
):

    global THIS_YEAR
    THIS_YEAR = this_year
    global ROOTDIR
    ROOTDIR = rootdir
    global CHATTY
    CHATTY = chatty
    global FORCE_MARKING
    FORCE_MARKING = force_marking
    global MARKING_SPREADSHEET_ID
    MARKING_SPREADSHEET_ID = marking_spreadsheet_id
    global MARKS_CSV
    MARKS_CSV = marks_csv

    start_time = time.time()

    if not os.path.exists(ROOTDIR):
        os.makedirs(ROOTDIR)
    print("listdir(ROOTDIR):\n", os.listdir(ROOTDIR))

    students = get_student_data()

    mark_sheet = pd.DataFrame(students)

    deets = pd.DataFrame(list(mark_sheet.apply(get_details, axis=1)))
    mark_sheet = mark_sheet.merge(deets, on="owner")

    mark_sheet["updated"] = mark_sheet.apply(update_repos, axis=1)
    mark_sheet["last_commit"] = mark_sheet.apply(get_last_commit, axis=1)

    mark_sheet["set1"] = mark_week(mark_sheet, set_number=1, timeout=10, active=mark_w1)
    mark_sheet["set2"] = mark_week(mark_sheet, set_number=2, timeout=10, active=mark_w2)
    mark_sheet["set3"] = mark_week(mark_sheet, set_number=3, timeout=25, active=mark_w3)
    mark_sheet["set4"] = mark_week(mark_sheet, set_number=4, timeout=45, active=mark_w4)
    mark_sheet["set5"] = mark_week(mark_sheet, set_number=5, timeout=45, active=mark_w5)
    mark_sheet["exam"] = mark_week(
        mark_sheet, set_number=8, timeout=45, active=mark_exam
    )

    mark_sheet["readme_mark"] = mark_sheet.apply(get_readmes, args=("mark",), axis=1)
    mark_sheet["readme_text"] = mark_sheet.apply(
        get_readmes, args=("textList",), axis=1
    )

    mark_sheet.to_csv(MARKS_CSV)

    data = [list(x) for x in mark_sheet.to_numpy()]
    service = build_spreadsheet_service()
    write(service, data=data)

    print("that took", (time.time() - start_time) / 60, "minutes")


def get_student_data():
    # TODO: instead of loading the pickle, load the marks.csv file so that
    # the dataframe is preloaded with values. Then it doesn't need to mark students
    # that haven't updated their work.
    students = None
    if os.path.exists("student.pickle"):
        with open("student.pickle", "rb") as sp:
            students = pickle.load(sp)
    else:
        students = get_forks()
        with open("student.pickle", "wb") as sp:
            pickle.dump(students, sp)
    return students

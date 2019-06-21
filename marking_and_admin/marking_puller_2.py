# -*- coding: UTF-8 -*-
"""Get the latest copy of all the repos.

This pulls the latest copy of all the repos
It can clone new repos if you set THERE_ARE_NEW_STUDENTS to true
"""
from datetime import datetime
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from io import StringIO
from itertools import repeat
import git
import json
import math
import os
import os.path
import pandas as pd
import pickle
import re
import requests
import ruamel.yaml as yaml
import subprocess
import sys
import threading
import time

rootdir = "../StudentRepos"


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


# The ID and range of a sample spreadsheet.
MARKING_SPREADSHEET_ID = "1wtTAM7A--ka7Lnog43L6jjo9kMCnDElCrTOBllEg4dA"


def build_spreadsheet_service():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ["*", "https://www.googleapis.com/auth/spreadsheets"]
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
    print("{0} cells updated.".format(result.get("updatedCells")))

    # Write comments
    body = {"requests": comment_list}
    result = (
        service.spreadsheets()
        .batchUpdate(spreadsheetId=MARKING_SPREADSHEET_ID, body=body)
        .execute()
    )
    print("{0} cells updated.".format(result.get("totalUpdatedCells")))


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
                comments.append(set_comment(j, i, json.dumps(item)))
    return comments


def set_comment(x, y, comment, y_offset=1):
    request = {
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


def getDFfromCSVURL(url, columnNames=False):
    """Get a csv of values from google docs."""
    r = requests.get(url)
    data = r.text
    if columnNames:
        return pd.read_csv(StringIO(data), header=0, names=columnNames)
    else:
        return pd.read_csv(StringIO(data))


def get_forks(org="design-computing", repo="me"):
    """Get a list of dicts of the user names and the git url for all the forks.
    """
    api = "https://api.github.com"
    url = (
        "{api}/repos/{org}/{repo}/forks?"
        "per_page={limit}&"
        "client_id={id}&"
        "client_secret={secret}'"
    ).format(
        api=api,
        org=org,
        repo=repo,
        limit=100,
        id="040e86e3feed633710a0",
        secret="69588d73388091b5ff8635fd1a788ea79177bf69",
    )
    print("get forks from:\n", url)
    r = requests.get(url)
    if r.status_code is 200:
        forks = r.json()
        repos = [{"owner": f["owner"]["login"], "git_url": f["git_url"]} for f in forks]
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


def update_repos(student, chatty=False, hardcore_pull=False):
    """Git clone a repo, or if already cloned, git pull."""
    url = student["git_url"]
    owner = student["owner"]
    path = os.path.join(rootdir, owner)
    t = datetime.now().strftime("%H:%M:%S")
    try:
        git.Repo.clone_from(url, path)
        print("{t}: new repo for {s}".format(t=t, s=owner))
    except git.GitCommandError as e:
        if chatty:
            print("We already have {s}, trying a pull. ({e})".format(s=owner, e=e))
        if "already exists and is not an empty directory" in e.stderr:
            try:
                repo = git.cmd.Git(path)
                try:
                    response = repo.pull()  # probably not needed, but belt and braces
                    print(
                        "{t}: pulled {s}'s repo: {r}".format(t=t, s=owner, r=response)
                    )
                except Exception as e:
                    repo.execute(["git", "fetch", "--all"])
                    repo.execute(["git", "reset", "--hard", "origin/master"])
                    print(e)
            except Exception as e:
                if chatty:
                    print("pull error:", student, e)
    except Exception as e:
        if chatty:
            print("clone error other than existing repo:", student, e)


def try_to_kill(file_path, chatty=False):
    """Attempt to delete the file specified by file_path."""
    try:
        os.remove(file_path)
        print("deleted {}".format(file_path))
    except Exception as e:
        if chatty:
            print(file_path, e)


def pull_all_repos(dirList, chatty=False, hardcore_pull=False):
    """Pull latest version of all repos."""
    of_total = len(dirList)
    for i, student_repo in enumerate(dirList):
        repo_is_here = os.path.join(rootdir, student_repo)
        try:
            repo = git.cmd.Git(repo_is_here)
            if hardcore_pull:
                repo.execute(["git", "fetch", "--all"])
                repo.execute(["git", "reset", "--hard", "origin/master"])
            repo.pull()  # probably not needed, but belt and braces
            t = datetime.now().strftime("%H:%M:%S")
            print("{}: {}/{} pulled {}'s repo".format(t, i, of_total, student_repo))
        except Exception as e:
            print(student_repo, e)


def csvOfDetails(dirList):
    """Make a CSV of all the students."""
    results = []
    for student_repo in dirList:
        path = os.path.join(rootdir, student_repo, "aboutMe.yml")
        details = open(path).read()
        details = details.replace("@", "^AT^")
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


def test_in_clean_environment(
    row,
    week_number,
    logfile_name="log.txt",
    timeout=5,
    temp_file_path="temp_results.json",
    test_file_path="test_shim.py",
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
    path_to_test_shim = os.path.abspath(
        os.path.join("marking_and_admin", test_file_path)
    )
    path_to_tests = os.path.abspath(
        os.path.join("..", "course", "week{}".format(week_number), "tests.py")
    )
    path_to_repo = os.path.abspath(os.path.join(rootdir, row.owner))

    test_args = [python, path_to_test_shim, path_to_tests, path_to_repo, row.owner]

    try:
        RunCmd(test_args, timeout).Run()  # this is unessarily complicated

        # full_path = os.path.join(LOCAL, temp_file_path)
        temp_results = open(temp_file_path, "r")
        contents = temp_results.read()
        results_dict = json.loads(contents)
        results_dict["bigerror"] = ":)"
        temp_results.close()
        log_progress(" good for w{}\n".format(week_number), logfile_name)
    except Exception as e:
        results_dict = {
            "bigerror": str(e).replace(",", "~"),
            "name": row.owner,
        }  # the comma messes with the csv

        log_progress(" bad {} w{}\n".format(e, week_number), logfile_name)

    elapsed_time = time.time() - start_time
    results_dict["time"] = elapsed_time
    return results_dict


def prepare_log(logfile_name, firstLine="here we go:\n"):
    """Create or empty the log file."""
    completed_students_list = open(logfile_name, "w")
    completed_students_list.write(firstLine)
    completed_students_list.close()


def mark_work(dirList, week_number, root_dir, dfPlease=True, timeout=5):
    """Mark the week's exercises."""
    logfile_name = "temp_completion_log"
    prepare_log(logfile_name)
    r = len(dirList)  # for repeat count

    results = list(
        map(
            test_in_clean_environment,  # Function name
            dirList,  # student_repo
            repeat(root_dir, r),  # root_dir
            repeat(week_number, r),  # week_number
            repeat(logfile_name, r),  # logfile_name
            repeat(timeout, r),  # timeout
        )
    )

    resultsDF = pd.DataFrame(results)
    csv_path = "csv/week{}marks.csv".format(week_number)
    resultsDF.to_csv(os.path.join(CWD, csv_path), index=False)
    for _ in [1, 2, 3]:
        # this is pretty dirty, but it gets tricky when you have
        # ,,, -> ,-,, because each intance needs to be replaced multiple times
        # TODO; #makeitnice
        fix_up_csv(path=csv_path)
    print("\n+-+-+-+-+-+-+-+\n\n")
    if dfPlease:
        return resultsDF


def get_details(row):
    path_to_aboutMe = os.path.abspath(os.path.join(rootdir, row.owner, "aboutMe.yml"))
    details = open(path_to_aboutMe).read()
    # who knows if I'll need this!?
    # details = details.replace("@", "^AT^")
    # details = re.sub(":(\w)", ": \g<1>", details)
    # details = re.sub(" -", " None", details)
    # details = details.replace("é", "e")
    # details = details.replace("w:", "w: ")
    try:
        details = yaml.load(details, yaml.RoundTripLoader)
        details["error"] = False
        details["owner"] = row.owner
        details["contactEmail"] = (
            details["contactEmail"]["firstBit"]
            + "@"
            + details["contactEmail"]["otherBit"]
        )
        # if details["mediumUsername"][:4] != "^AT^":
        #     details["mediumUsername"] = "^AT^" + details["mediumUsername"]
        return dict(details)
    except Exception as e:
        print(details)
        return {"error": "|".join(str(e).splitlines()), "owner": row.owner}


# def do_marking():
if not os.path.exists(rootdir):
    os.makedirs(rootdir)
print("listdir(rootdir):\n", os.listdir(rootdir))

start_time = time.time()

students = None
if os.path.exists("student.pickle"):
    with open("student.pickle", "rb") as sp:
        students = pickle.load(sp)
else:
    students = get_forks()
    with open("student.pickle", "wb") as sp:
        pickle.dump(students, sp)

for student in students:
    update_repos(student, hardcore_pull=True)

mark_sheet = pd.DataFrame(students)

deets = pd.DataFrame(list(mark_sheet.apply(get_details, axis=1)))
mark_sheet = mark_sheet.merge(deets, on="owner")

mark_sheet["week1"] = mark_sheet.apply(test_in_clean_environment, args=(1,), axis=1)
mark_sheet["week2"] = mark_sheet.apply(test_in_clean_environment, args=(2,), axis=1)
mark_sheet["week3"] = mark_sheet.apply(test_in_clean_environment, args=(3,), axis=1)
mark_sheet["week4"] = mark_sheet.apply(test_in_clean_environment, args=(4,), axis=1)
mark_sheet["week5"] = mark_sheet.apply(test_in_clean_environment, args=(5,), axis=1)
mark_sheet["exam"] = mark_sheet.apply(test_in_clean_environment, args=(8,), axis=1)
mark_sheet.to_csv("marks.csv")

data = [list(x) for x in mark_sheet.to_numpy()]
service = build_spreadsheet_service()
write(service, data=data)

print("that took", time.time() - start_time)

# dirList = os.listdir(rootdir)  # do we know if everyone's work got in?
# print("dir list", dirList, len(dirList))

# print("\nMark week 1's work")
# mark_work(dirList, 1, rootdir, dfPlease=False, timeout=5)

# print("\nMark week 2's work")
# mark_work(dirList, 2, rootdir, dfPlease=False, timeout=5)

# print("\nMark week 3's work")
# mark_work(dirList, 3, rootdir, dfPlease=False, timeout=25)

# print("\nMark week 4's work")
# mark_work(dirList, 4, rootdir, dfPlease=False, timeout=45)

# print("\nMark week 5's work")
# mark_work(dirList, 5, rootdir, dfPlease=False, timeout=45)
# return mark_sheet


# if __name__ == "__main__":
# do_marking()


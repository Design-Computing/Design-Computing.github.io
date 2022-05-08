import git
import os
import subprocess


def get_or_update(path, url):
    repo = -1
    try:
        # try to clone the repo
        repo = git.Repo.clone_from(me_url, "marking/tempMe")
        a = ""

    except git.GitCommandError as e:
        # If the repo is already there, update it.
        # This is unlikely if we're in a lambda
        print(e)
        repo = git.cmd.Git("marking/tempMe")
        repo.execute(["git", "fetch", "--all"])
        repo.execute(["git", "reset", "--hard", "origin/main"])
        repo.pull()  # probably not needed, but belt and braces
    except Exception as e:
        print(e)
    return repo


me_url = "https://github.com/Design-Computing/me.git"
course_url = "https://github.com/Design-Computing/course.git"

me_repo = get_or_update("marking/tempMe", me_url)
course_repo = get_or_update("marking/course", course_url)


print("We're starting in", os.getcwd())
meWorkingDir = os.path.join(os.getcwd(), "marking", "tempMe")
print("changing to", meWorkingDir)
os.chdir(meWorkingDir)
print("Now we're in", os.getcwd())
# for i in range(1, 2):
#     cmd = "python ../course/week{weekNumber}/tests.py".format(weekNumber=i)
#     os.system(cmd)

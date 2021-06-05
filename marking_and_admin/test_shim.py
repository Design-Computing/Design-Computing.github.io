# -*- coding: UTF-8 -*-
"""Run tests on a specific repo.

This file is called by marking_puller.py

Its job is to be set up and torn down for every student so that there is no
namespace pollution. Its run as a subprocess. The args are where the tests are,
and where the repo is. In almost all cases the tests are the teacher tests, and
the repo changes for each student.

"""
from importlib import import_module
import importlib.util

import json
import sys
import os


def do_the_test(repo_path):
    """Run tests on a student's repo."""
    try:
        spec = importlib.util.spec_from_file_location("tests", TEST_PATH)
        test = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test)
        print("about to test", repo_path)
        r = test.theTests(repo_path)
        r["localError"] = ":)"
        return r
    except Exception as e:
        return {
            "of_total": 0,
            "mark": 0,
            "localError": str(e).replace(",", "~"),  # .encode("utf-8"),
        }
        # the comma messes with the csv


def results_as_json(repo_path):
    """Save the results to a temporary json file."""
    results = do_the_test(repo_path)
    results["name"] = OWNER
    print("results:", results)
    return json.dumps(results)


TEST_PATH = os.path.normpath(sys.argv[1])
REPO_PATH = os.path.normpath(sys.argv[2])
OWNER = sys.argv[3]


# 0:'C:\\Users\\ben\\Anaconda3\\python.exe'
# TEST_PATH = "C:\\Users\\ben\\code1161\\course\\week1\\tests.py"
# REPO_PATH = "C:\\Users\\ben\\code1161\\StudentRepos\\notionparallax"
# OWNER = "notionparallax"


print("\n\n\n\n", "in the shim", TEST_PATH, REPO_PATH, OWNER, "\n", sep="\n")

with open("temp_results.json", "w") as temp_results:
    results = results_as_json(REPO_PATH)
    temp_results.write(results)

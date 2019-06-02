# -*- coding: UTF-8 -*-
from codeHelpers import loadExerciseFile
import imp
import importlib.util as importUtils
import inspect
import os
import sys


REPO_PATH = sys.argv[2]
LOCAL = os.path.dirname(os.path.realpath(__file__))


def do_the_test():
    try:
        test = imp.load_source("test", REPO_PATH)
        # loadExerciseFile(weekNumber=WEEK_NUMBER, exerciseNumber=0)
        r = inspect.getsourcelines(test.loops_7)
        return str(r)
    except Exception as e:
        print(e)


temp_results = open("temp_inspect.json", "w")
temp_results.write(do_the_test())
temp_results.close()

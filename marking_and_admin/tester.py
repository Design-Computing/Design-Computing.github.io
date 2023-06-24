# -*- coding: UTF-8 -*-
"""Run a lightweight test set on specific students."""
import os
import time

from marking_puller import RunCmd

LOCAL = os.path.dirname(os.path.realpath(__file__))
week_number = 1


repos = ["code1161benFork_fully_working_secret_squirel"]
times = []
repos = ["AlXu111"]
results = []
for name in repos:
    timeout_cap = 25
    args = [
        "python",
        "marking_and_admin\\test_shim.py",
        f"..\\course\\set{week_number}\\tests.py",
        f"..\\StudentRepos\\{name}",
        name,
    ]
    print(args)
    start_time = time.time()
    try:
        RunCmd(args, timeout_cap).Run()
        with open(os.path.abspath("temp_results.json"), "r", encoding="utf-8") as trf:
            results.append(trf.read())

    except Exception as e:
        print(e)
    elapsed_time = time.time() - start_time
    print("Time to test:", elapsed_time)
    times.append({"name": name, "time": elapsed_time})

print(results)
print(times)

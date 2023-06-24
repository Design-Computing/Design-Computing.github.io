# -*- coding: UTF-8 -*-
"""Get the latest copy of all the repos.

This pulls the latest copy of all the repos
It can clone new repos if you delete the students pickle
"""
import os

from mark_functions import do_the_marking

# The ID and range of a sample spreadsheet.
# MARKING_SPREADSHEET_ID = "1wtTAM7A--ka7Lnog43L6jjo9kMCnDElCrTOBllEg4dA"  # 2019
# MARKING_SPREADSHEET_ID = "1AjDu51VX26bIcLNMsr2iHq2BtrNEj91krxWKqjDW5aA"  # 2020
# MARKING_SPREADSHEET_ID = "17KKMNIseRSo9IVNp-iaUCyEqbAR9tTYAcegzcvVgJFM"  # 2021
# MARKING_SPREADSHEET_ID = "16tESt_4BUf-9-oD04suTprkd1O0oEl6WjzflF_avSKY"  # 2022
# MARKING_SPREADSHEET_ID = "1DPBVy9DiVkdFBArOTRtj3L--f62KTnxyFFZrUXrobV0"  # 2023
MARKING_SPREADSHEET_ID = os.getenv("GOOGLE_SHEETS_KEY", "")


if __name__ == "__main__":
    do_the_marking(
        this_year="2023",
        rootdir="../StudentRepos",
        chatty=False,
        force_marking=True,
        marking_spreadsheet_id=MARKING_SPREADSHEET_ID,
        marks_csv="marks.csv",
        mark_w1=True,
        mark_w2=True,
        mark_w3=False,
        mark_w4=False,
        mark_w5=False,
        mark_exam=False,
    )

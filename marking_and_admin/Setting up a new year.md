# Setting up a new year

The file `marking_puller_2.py` is the entry point.

## Set up the spreadsheet

- in Google drive, make a copy of last year's _Details & marking 2022_ file.
- update the `MARKING_SPREADSHEET_ID` const with the ID from that new spreadsheet's URL.

## To mark work for the first time

- if this is a new computer, run `git config --global url."https://github.com/".insteadOf git@github.com:` or the git library will have a tantrum
- update the `THIS_YEAR` const
- delete `student.pickle` so that it forces a fresh pull
- if you have a fresh pull of the repo, you'll need a new `credentials.json` file.
  - follow this guide https://developers.google.com/workspace/guides/create-credentials
  - You need to make a web app Oauth set of creds, download it, and paste it into `marking_and_admin/credentials.json`
  - There's one ready to do in the CoDewords project in the google dashboard
  - run it, it'll fail on the `flow.run_local_server()` so it'll run the `flow.run_console()` and then it'll let you in.
  - you might need to enable the api, look at the error message, it has a link

TODO:

- congratulate everyone who has a full set of passing tests


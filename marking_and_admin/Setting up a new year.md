# Setting up a new year

The file `marking_puller_2.py` is the entry point.

## Set up the spreadsheet

- in Google drive, make a copy of last year's _Details & marking 2021_ file.
- update the `MARKING_SPREADSHEET_ID` const with the ID from that new spreadsheet's URL.

## To mark work for the first time

- update the `THIS_YEAR` const
- delete `strudent.pickle` so that it forces a fresh pull
- if you have a fresh pull of the repo, you'll need a new `credentials.json` file.
  - follow this guide https://developers.google.com/workspace/guides/create-credentials
  - You need to make a web app Oauth set of creds, download it, and paste it into `marking_and_admin/credentials.json`
  - There's one ready to do in the CoDewords project in the google dashboard
  - run it, it'' fail on the `flow.run_local_server()` so it'll run the `flow.run_console()` and then it'll let you in.
  - you might need to enable the api, look at the error message, it has a link

TODO:

- contact students who are missing data from their about me files
- check test, why are there so many bad ones
- congratulate everyone who has a full set of passing tests
- show Alex how to do a pull

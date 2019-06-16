import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1wtTAM7A--ka7Lnog43L6jjo9kMCnDElCrTOBllEg4dA"


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


def write(service):
    # Call the Sheets API
    # sheet = service.spreadsheets()
    # result = (
    #     sheet.values()
    #     .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
    #     .execute()
    # )
    # values = result.get("values", [])

    # if not values:
    #     print("No data found.")
    # else:
    #     print(values[0])
    #     for row in values[1:]:
    #         print(row)

    # Writing values
    new_values = [["a", "These"], ["b", "are"], ["c", "some"], ["d", "entries"]]
    body = {"values": new_values}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range="testing!A1:Q1000",
            valueInputOption="RAW",
            body=body,
        )
        .execute()
    )
    print("{0} cells updated.".format(result.get("updatedCells")))

    # update formatting
    new_values = [["a", "These"], ["b", "are"], ["c", "some"], ["d", "entries"]]
    request = []
    for i, row in enumerate(new_values):
        request.append(set_comment(0, i, row[1]))

    body = {"requests": request}
    result = (
        service.spreadsheets()
        .batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body)
        .execute()
    )
    print("{0} cells updated.".format(result.get("totalUpdatedCells")))


def set_comment(x, y, comment):
    request = {
        "repeatCell": {
            "range": {
                "sheetId": 1704890600,
                "startRowIndex": y,
                "endRowIndex": y + 1,
                "startColumnIndex": x,
                "endColumnIndex": x + 1,
            },
            "cell": {"note": comment},
            "fields": "note",
        }
    }
    return request


if __name__ == "__main__":
    service = build_spreadsheet_service()
    write(service)

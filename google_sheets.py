from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# 📌 Deine Google Sheet ID & Tab-Name
SPREADSHEET_ID = "1mzQEea4-8mZ5ky68PguAAK0cMm-DXXTDT6JOtH_0vmg"
TAB_NAME = "Berechnung"

# 🔐 Google Sheets Service aufbauen
def get_service():
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)

# 📝 Neue Daten in Zeile 2 schreiben
def write_input_row(name, birth_date, birth_time, latitude, longitude):
    values = [[name, birth_date, birth_time, "", "", "", latitude, longitude]]
    range_ = f"{TAB_NAME}!A2:H2"
    body = {"values": values}

    service = get_service()
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_,
        valueInputOption="RAW",
        body=body
    ).execute()

# 📤 Zeichen (D2, I2, J2, K2) lesen und zurückgeben
def read_sheet_values():
    range_ = [
        f"{TAB_NAME}!D2",
        f"{TAB_NAME}!I2",
        f"{TAB_NAME}!J2",
        f"{TAB_NAME}!K2"
    ]

    service = get_service()
    result = service.spreadsheets().values().batchGet(
        spreadsheetId=SPREADSHEET_ID,
        ranges=range_
    ).execute()

    values = [r["values"][0][0] if "values" in r else "" for r in result["valueRanges"]]

    return {
        "entry": values[0],
        "support": values[1],
        "final": values[2],
        "eternal": values[3]
    }

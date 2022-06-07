from __future__ import print_function
from googleapiclient.discovery import build
from numpy import append
import google_secrets

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'googlesheet_keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = google_secrets.PROJECT_ID

def appendToSpreadsheet(data, spreadsheetId, spreadsheetName, spreadsheet):
    """
    given some data and the spreadsheet, append data to the spreadsheet
    
    this will write to the first empty row, keeping the same number of empty rows

    :param data: an array of arrays of data
    :param spreadsheetId: the id of the spreadsheet to append to
    :param spreadsheetName: the name of the spreadsheet to append to
    :param spreadsheet: the googlesheets called from .spreadsheets()
    """
    sheetRange = "{}!A1:D1".format(spreadsheetName)
    spreadsheet.values().append(spreadsheetId=spreadsheetId, range=sheetRange,
                                valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values": data}).execute()

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                             range="Inventory!A1:D3").execute()
    # values = result.get('values', [])
    # print(values)
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    # sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Inventory!A1:G1",
    #                       valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values": data}).execute()
    appendToSpreadsheet(data, SAMPLE_SPREADSHEET_ID, "Inventory", sheet)
if __name__ == '__main__':
    main()

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # service = build('sheets', 'v4', credentials=creds)

    # # Call the Sheets API
    # sheet = service.spreadsheets()
    # # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    # #                             range="Inventory!A1:D3").execute()
    # # values = result.get('values', [])
    # # print(values)
    # data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    # # sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Inventory!A1:G1",
    # #                       valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values": data}).execute()
    # appendToSpreadsheet(data, SAMPLE_SPREADSHEET_ID, "Inventory", sheet)
if __name__ == '__main__':
    main()
    
# input
input1 = input()
 
# output
print(input1)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_pandas import Spread, Client

# Inicialización
SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    "Reto1/archivos/keys.json")
CLIENT = gspread.authorize(CREDENTIALS)


class google_sheets_test:

    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.spread = Spread(sheet_name, creds=CREDENTIALS, scope=SCOPE)
        self.sheet = CLIENT.open(sheet_name)

    def getAllRecords(self, worksheet):
        worksheet = self.sheet.get_worksheet(worksheet)
        records = worksheet.get_all_records()
        return records

    def writeWorksheet(self, dataFrame, worksheet):
        worksheet = self.sheet.get_worksheet(worksheet)
        worksheet.update(dataFrame)

    def deleteWorksheet(self, worksheet):
        self.sheet.del_worksheet(self.sheet.get_worksheet(worksheet))

    def createWorksheet(self, title):
        worksheet = self.sheet.add_worksheet(
            title=title, rows="100", cols="100")
        return worksheet

    def getWorksheets():
        worksheet_list = self.sheet.worksheets()
        return worksheet_list

    def merge(self, worksheet, tupleFirst, tupleLast):
        self.spread.merge_cells(tupleFirst, tupleLast,
                                merge_type='MERGE_ALL', sheet=worksheet)

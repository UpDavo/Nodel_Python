import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Inicialización
SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    "project/Reto1/archivos/keys.json")
CLIENT = gspread.authorize(CREDENTIALS)


class google_sheets_test:

    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.sheet = CLIENT.open(sheet_name)

    def writeWorksheet(self, dataFrame, worksheet):
        worksheet = self.sheet.get_worksheet(worksheet)
        worksheet.update(dataFrame)

    def deleteWorksheet(self, worksheet):
        self.sheet.del_worksheet(self.sheet.get_worksheet(worksheet))

    def createWorksheet(self, title):
        worksheet = self.sheet.add_worksheet(
            title=title, rows="2000", cols="100")
        return worksheet


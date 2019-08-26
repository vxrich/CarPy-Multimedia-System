import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint 
from config import key_path, sheet_name

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
client = gspread.authorize(creds)

sheet = client.open('ProvaPython').sheet1

pp = pprint.PrettyPrinter()

row = 1 
while sheet.cell(row,1).value != '':
    row += 1

print(row)

sheet.update_cell(row, 1, "25/08/2019")


class Spreadsheet(object):

    def __init__(self):

        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
        self.client = gspread.authorize(creds)

        self.sheet = client.open(sheet_name).sheet1

        self.current_row = None


    def setValue(self, column, value):

        self.sheet.update_cell(self.current_row, column, value)

    def getvalue(self, row, column):

        return self.sheet.cell(row, column).value

    def selectNewRow(self):

        row = 0 
        
        while self.sheet.cell(i,1).value != '':
            row += 1

        self.current_row = row
        






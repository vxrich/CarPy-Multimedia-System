import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint 
from config import KEY_PATH, SHEET, DATE_COL, FUEL_COL, COST_COL, TRAVEL_COL

"""
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
"""

class Spreadsheet(object):

    def __init__(self):

        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(KEY_PATH, scope)
        self.client = gspread.authorize(self.creds)

        self.sheet = self.client.open(SHEET).sheet1

        self.current_row = None


    def setValue(self, column, value):

        self.sheet.update_cell(self.current_row, column, value)

    def getvalue(self, row, column):

        return self.sheet.cell(row, column).value

    def selectNewRow(self):

        row = 1

        while self.sheet.cell(row,1).value != '':
            row += 1
           
        self.current_row = row
        
    def setNewRecord(self, date, fuel, cost, travel):

        self.selectNewRow()
        self.sheet.update_cell(self.current_row, DATE_COL, date)
        self.sheet.update_cell(self.current_row, FUEL_COL, fuel)
        self.sheet.update_cell(self.current_row, COST_COL, cost)
        self.sheet.update_cell(self.current_row, TRAVEL_COL, travel)
        







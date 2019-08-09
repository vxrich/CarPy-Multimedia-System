import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('json/client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Consumi Doblò').sheet1

pp = pprint.PrettyPrinter()

consumi = sheet.cell(12,1).value

pp.pprint(consumi)
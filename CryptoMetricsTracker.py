"""
Cryptocurrency Metrics Tracker

"""

#### Import Programme Config Variables ####

import ConfigVariables

# Gmail variables
gmailcred = ConfigVariables.gmailcredentials
recipient = ConfigVariables.recipient
subject = ConfigVariables.subject

# Ezsheets variables
ezsheetscred = ConfigVariables.ezsheetscredentials
gsid = ConfigVariables.gsid

# CoinAPI variables
headers = ConfigVariables.headers
period_id = ConfigVariables.period_id
limit = ConfigVariables.limit
include_empty_items = ConfigVariables.include_empty_items
market_ids = ConfigVariables.market_ids

# delay for the programme
programme_delay = 2

#### Import modules ####

import requests
import json
import os

home = os.getcwd()

import time

# Log into Ezsheets
os.chdir(ezsheetscred)
import ezsheets

os.chdir(home)

# Log into Gmail
os.chdir(gmailcred)
import ezgmail

os.chdir(home)

#### Functions ####

# Downloads the relevant market information that is specified from CoinAPI
def CoinApiDownload(market):
    url = F"https://rest.coinapi.io/v1/ohlcv/{market}/latest?period_id={period_id}&limit={limit}&include_empty_items={include_empty_items}"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    jsondata = json.loads(response.text)
    jsondata = jsondata[0]

    market_ids[market] = jsondata

    print(F"Downloaded data for {market}...")
    print()


def initalizespreadsheet():
    sheetTitles = ss.sheetTitles
    initialsheets = ['Analysis', 'BaseData']

    for number, sheet_name in enumerate(initialsheets):
        if sheet_name not in sheetTitles:
            ss.createSheet(sheet_name, number)

    if 'Sheet1' in sheetTitles:
        ss['Sheet1'].delete()

    AnalysisSheet = ss['Analysis']
    row1 = AnalysisSheet.getRow(1)
    if 'Test Name' not in row1:
        AnalysisSheet[10, 1] = 'Test Name'
    if 'Logic Test Result' not in row1:
        AnalysisSheet[11, 1] = 'Logic Test Result'


# Creates a Google Sheet if market_id is not already included in google sheets
def createGoogleSheets(market, v):
    sheetTitles = ss.sheetTitles

    if market not in sheetTitles:
        ss.createSheet(market)
        sheet = ss[market]

        # create a heading row for the newly created sheet
        hs = []
        for heading in v.keys():
            hs.append(heading)

        sheet.updateRow(1, hs)
        print(F"Sheet and heading rows created for {market} ")
        print()


# Find first empty column in the sheet
def getFirstEmptyRow(market):
    sheet = ss[market]
    Column1 = sheet.getColumn(1)
    for i, entry in enumerate(Column1):
        if entry == '':
            firstEmptyRow = i + 1
            break
    return firstEmptyRow


# Adds the data to the relevant row on google sheets
def updateSheetData(v, firstEmptyRow):
    marketdata = []
    for value in v.values():
        marketdata.append(value)

    sheet = ss[market]
    sheet.updateRow(firstEmptyRow, marketdata)
    print(F"{market} sheet row {firstEmptyRow} updated with new data")
    print()


def appendToBaseData(market, v):
    baseDataSheet = ss['BaseData']

    # Finds the market row or first empty row on the BaseData sheet
    column1 = baseDataSheet.getColumn(1)
    for i, entry in enumerate(column1):
        if entry == market or entry == '':
            row = i + 1
            break

    # Acquire data to add to BaseData sheet
    info = [market]

    closeprice = v['price_close']
    info.append(closeprice)

    # Adds relevant data to the relevant row on the BaseData sheet
    baseDataSheet.updateRow(row, info)

    print(F"{market} data added to the BaseData sheet")
    print()


#### Programme ####

# Download CoinAPI Data

for market in market_ids.keys():
    CoinApiDownload(market)


# Log into Google Sheets

# Assign the ezsheets variable
ss = ezsheets.Spreadsheet(gsid)
print('Logged into Google Sheets')
print()

initalizespreadsheet()

for market in market_ids.keys():
    # extracts each dictionary out market_ids variable

    v = market_ids[market]
    createGoogleSheets(market, v)
    empty_row = getFirstEmptyRow(market)
    updateSheetData(v, empty_row)
    appendToBaseData(market, v)

time.sleep(programme_delay)
print(F"Programme delayed for {programme_delay} secs to allow for Google Sheets logic to be performed")
print()


# find Logic Test Result placeholder on the analysis spreadsheet in Google Sheets
sheet = ss['Analysis']
first_row = sheet.getRow(1)
result_column = first_row.index('Logic Test Result') + 1
logic_test_column = sheet.getColumn(result_column)

# find row position of any true Logic Result Test in Google Sheets
logic_results_position = []
for i, entry in enumerate(logic_test_column):
    if entry == 'TRUE':
        results_row = i
        logic_results_position.append(results_row)

# Find the Test Name with a true Logic Test Result in Google Sheets
tests = []
test_names_column_number = first_row.index('Test Name') + 1
tests_names_column = sheet.getColumn(test_names_column_number)
for index in logic_results_position:
    t = tests_names_column[index]
    tests.append(t)


if tests != []:

    # If True tests are returned then send an email notification

    body = F'''
True Test Values(s) returned for;

{tests}
 
Check Google sheet for more information'''

    ezgmail.send(recipient, subject, body)

    print('True Test values - email notification sent')
    print()
else:
    print('No True tests - NO email notification sent')
    print()

print('Programme Complete')

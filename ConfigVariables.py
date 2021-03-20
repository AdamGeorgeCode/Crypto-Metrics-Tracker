'''
CryptoMetricsTracker - Configuration Variables.py

# Add/adapt the variables below to configure the programme to
# work on your system and meet your requirements

'''

#### Gmail parameters ####

# Gmail credentials directory location
gmailcredentials = # ADD path to directory of saved gmail credentials

# email address to send notification to
recipient = # ADD recipient email address to receive email notification

subject = 'Crypto Metrics Tracker Alert!'

#### Ezsheets parameters ####

# Ezsheets credentials directory location
ezsheetscredentials = # ADD path to directory of saved ezsheets credentials

# gsid = Google Sheets Spreadsheet ID
gsid = # Add Google Sheet Spreadsheet ID from a newly created Google Sheet spreadsheet

#### CoinAPI parameters ####

# CoinAPI Key
headers = {'X-CoinAPI-Key': 'ADD CoinAPI API Key here'} # ADD CoinAPI API Key

# Adapt the period_id below for different timeframes
period_id = '2MIN'
limit = '1'
include_empty_items = 'false'

# Adapt the list below to include the markets that you want
# market_ids are obtained from extracting from CoinAPI

market_ids = {'BITFINEX_SPOT_BTC_USDT': '',
              'COINBASE_SPOT_BTC_USD': '',
              'POLONIEX_SPOT_BTC_USDT': '',
              }

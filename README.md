# crypto-metrics-tracker

# Cryptocurrency Metrics Tracker – Exchange Price Differentials

---

This programme is designed to download data on specified crypto markets using the CoinAPI RESTful APIs then add the retrieved data to a Google Sheet. Analysis can then be performed on the data using the built in Google Sheet functions. An email notification from the user’s gmail account will be sent if one of the analysis logic tests, which the user creates on the spreadsheet, returns a True value.

This version of the programme is currently configured to analyse the exchange price differentials between various BTC/USD and BTC/USDT pairs from multiple exchanges.

Additionally, the programme has been designed in a way that will allow the user edit their analysis logic tests, through the ‘Analysis’ page on the connected Google sheet, without having to edit the programmes core code directly after installation. One way this can be achieved is through adding a Google Sheet shortcut link to a mobile device like a phone to enable quick access to the spreadsheet.

For this programme to periodically collect real time data, it would be advised that this is set up on a device that can run indefinitely like a Raspberry Pi. The CryptoMetricsTracker.py can be added to the Raspberry Pi’s crontab to schedule it to run at predefined time intervals.

## Motivation

---

The motivation to create this programme was to enable to the user to download real-time data and enable them to perform their own analysis as required. Depending on the logic tests they create they may be able to make metrics that are not readily available through current free online sources. The user is notified if a test returns a true value, which could inform trading strategies (this is NOT financial advice).

## Example version of configured Google Sheet

---

An excel version of a configured Google sheet to analyse Exchange Price Differentials is included in the Github repository. This exact file is not required to run the programme however it is just included as a reference for the user to see what a setup version of the Google sheet could look like.

## How to use?

---

Once setup the user can create different types of analysis and logics tests as required to meet their needs. 

## Additional features

---

Additional features that could be added to increase the programmes functionality include;

- Twilio – for sending text notifications to the user’s phone.
- Web scrapers – using Beautiful Soup, to scrape/collate other relevant data from the internet.
- Increasing the programmes run frequency to collect more real-time data – through purchasing a higher tier API from CoinAPI to increase the amount of API calls per 24-hour period. A free API key allows for 100 API calls per 24 hours. One market data request counts as 1 call.
- A notification system to let the user know the programme is still running – could be scheduled to send a notification every couple of days or week.

## Licence

---

© Adam George

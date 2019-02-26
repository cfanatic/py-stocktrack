# py-stocktrack

This repository features a stock analysis tool which tracks the stock price development on [**Tradegate Exchange**](https://www.tradegate.de).

Following is a summary of the main features:
- [x] Retrieve stock price information
- [x] Download stock performance images
- [x] Export stock data to Excel sheet
- [x] Trigger notifications in case of market volatility

Run the script multiple times in order to generate statistics for multiple stocks:

![Price](https://raw.githubusercontent.com/cfanatic/py-stocktrack/master/res/2_price.png)

## Requirements
Developed and tested on the following setup: 
- Python 3.7.2
- beautifulsoup 4.7.1
- openpyxl 2.6.0
- pandas 0.24.1
- openpyxl 2.6.0

## Installation

I recommend to use Visual Studio Code. Make sure that Python is configured correctly.

Run the following command from Command Palette:
```
Python: Run Python File in Terminal
```

## Usage

You will see similar output for each stock you retrieve data for:

![Data](https://github.com/cfanatic/py-stocktrack/blob/master/res/3_data.png)

All stock performance images can be exported to Excel for an overall overview:

![Data](https://github.com/cfanatic/py-stocktrack/blob/master/res/1_overview.png)
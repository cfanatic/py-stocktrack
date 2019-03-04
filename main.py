"""
Track the stock performance on the stock market and store price development.
Trigger notifications to the user in case of high market volatility.
"""

from pprint import pprint
from stock import Stock
from getopt import getopt
import sys


def save(stocks):
    # Download stock performance images
    for stock in stocks:
        stock.getImage()
    # Save stock performance data
    for stock in stocks:
        stock.saveData()
    # Delete stock performance images
    Stock.deleteImages()
    # Save stock performance images
    Stock.saveImages()

def track(stocks):
    # Retrieve stock performance data
    for stock in stocks:
        pprint(stock.getData())

def main():
    # Open connection to stock exchange database
    microsoft = Stock("US5949181045")
    apple = Stock("US0378331005")
    google = Stock("US02079K3059")
    netflix = Stock("US64110L1061")
    stocks = [microsoft, apple, google, netflix]

    # Execute command line option parsing
    if len(sys.argv) == 1:
        print("Error@main: Not enough input arguments given!")
    else:
        opts, args = getopt(sys.argv[1:], "sth", ["save", "track", "help"])
        for opt, arg in opts:
            if opt in ("-s", "--save"):
                save(stocks)
            elif opt in ("-t", "--track"):
                track(stocks)
            elif opt in ("-h", "--help"):
                pass

if __name__ == "__main__":
    main()

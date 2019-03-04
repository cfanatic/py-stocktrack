"""
Track the stock performance on the stock market and store price development.
Trigger notifications to the user in case of high market volatility.
"""

from stock import Stock
from pprint import pprint


def main():
    # Open connection to stock exchange database
    microsoft = Stock("US5949181045")
    apple = Stock("US0378331005")
    google = Stock("US02079K3059")
    netflix = Stock("US64110L1061")
    # Retrieve stock performance data
    pprint(microsoft.getData())
    pprint(apple.getData())
    pprint(google.getData())
    pprint(netflix.getData())
    # Download stock performance images
    microsoft.getImage()
    apple.getImage()
    google.getImage()
    netflix.getImage()
    # Save stock performance data
    microsoft.saveData()
    apple.saveData()
    google.saveData()
    netflix.saveData()
    # Delete stock performance images
    Stock.deleteImages()
    # Save stock performance images
    Stock.saveImages()

if __name__ == "__main__":
    main()

"""
Track the stock performance on the stock market and store price development.
Trigger notifications to the user in case of high market volatility.
"""

from bs4 import BeautifulSoup as bs


class Stock():

    def __init__(self, id):
        self._id = id

    def getData(self):
        pass


def main():
    amazon = Stock("US0231351067")
    amazon.getData()


if __name__ == "__main__":
    main()

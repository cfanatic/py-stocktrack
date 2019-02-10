"""
Track the stock performance on the stock market and store price development.
Trigger notifications to the user in case of high market volatility.
"""

from bs4 import BeautifulSoup as html
from pprint import pprint
import requests


class Stock():

    URL = "https://www.tradegate.de/orderbuch.php?isin="

    def __init__(self, id):
        self._id = id
        self._query = Stock.URL + id
        self._html = requests.get(self._query)
        self._data = html(self._html.content, "html.parser")

    def getData(self):
        stock_data = {}
        stock_name = self._data.find("div", {"id": "col1_content"}).find("h2").text
        stock_data.update({"name": stock_name})
        tag_parent = self._data.find_all("td", class_="longprice")
        for item in tag_parent:
            if 'id' in item.attrs:
                key = item.attrs.get("id")
                value = item.text.replace(" ", "").replace(",", ".").replace("\xa0", "").replace("TEUR", " TEUR")
                stock_data.update({key: value})
            else:
                tag_child = item.find('strong')
                key = tag_child.attrs.get("id")
                value = item.text.replace(" ", "").replace(",", ".").replace("\xa0", "").replace("TEUR", " TEUR")
                stock_data.update({key: value})
        return stock_data


def main():
    amazon = Stock("US0231351067")
    microsoft = Stock("US5949181045")
    apple = Stock("US0378331005")
    pprint(amazon.getData())
    pprint(microsoft.getData())
    pprint(apple.getData())


if __name__ == "__main__":
    main()

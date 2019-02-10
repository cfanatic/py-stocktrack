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
        data = {}
        tag_parent = self._data.find_all("td", class_="longprice")
        for item in tag_parent:
            if 'id' in item.attrs:
                key = item.attrs.get("id")
                value = item.text.replace(" ", "").replace(",", ".").replace("\xa0", "").replace("TEUR", " TEUR")
                data.update({key: value})
            else:
                tag_child = item.find('strong')
                key = tag_child.attrs.get("id")
                value = item.text.replace(" ", "").replace(",", ".").replace("\xa0", "").replace("TEUR", " TEUR")
                data.update({key: value})
        return data


def main():
    amazon = Stock("US0231351067")
    data = amazon.getData()
    pprint(data)


if __name__ == "__main__":
    main()

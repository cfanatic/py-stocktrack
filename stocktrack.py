"""
Track the stock performance on the stock market and store price development.
Trigger notifications to the user in case of high market volatility.
"""

from bs4 import BeautifulSoup as html
from pprint import pprint
import os
import requests
import urllib


class Stock():

    URL_DOMAIN = "https://www.tradegate.de"
    URL_QUERY = URL_DOMAIN + "/orderbuch.php?isin="

    def __init__(self, id):
        self._id = id
        self._query = Stock.URL_QUERY + id
        self._html = html(requests.get(self._query).content, "html.parser")
        self._data = {}
        self._image = {}
        self._fetchData()
        self._fetchImage()

    def _fetchData(self):
        stock_data = {}
        stock_name = self._html.find("div", {"id": "col1_content"}).find("h2").text
        stock_data.update({"name": stock_name})
        tag_parent = self._html.find_all("td", class_="longprice")
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
        self._data = stock_data

    def _fetchImage(self):
        stock_image = []
        stock_intraday = self._html.find("img", {"id": "intraday"}).attrs
        stock_week = self._html.find("img", {"id": "woche"}).attrs
        stock_month = self._html.find("img", {"id": "monat"}).attrs
        stock_month6 = self._html.find("img", {"id": "monat6"}).attrs
        stock_year = self._html.find("img", {"id": "jahr"}).attrs
        self._image = {"intraday": stock_intraday,
                        "week": stock_week,
                        "month": stock_month,
                        "month6": stock_month6,
                        "year": stock_year}

    def getData(self, key = "all"):
        if (key == "all"):
            return self._data
        else:
            return self._data[key]

    def getImage(self, key = "all"):
        if (key == "all"):
            for key, value in self._image.items():
                self.getImage(key)
        else:
            image_name = self._image[key]["alt"].split(" - ")[-1].replace(" ", "_").lower() + ".png"
            image_url = Stock.URL_DOMAIN + self._image[key]["src"]
            image_path = os.getcwd() + "/misc/" + self.getData("name").split()[0].lower() + "/"
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            urllib.request.urlretrieve(image_url, image_path + image_name)


def main():
    # Open connection to stock exchange database
    amazon = Stock("US0231351067")
    microsoft = Stock("US5949181045")
    apple = Stock("US0378331005")
    # Retrieve stock performance data
    pprint(amazon.getData())
    pprint(microsoft.getData())
    pprint(apple.getData())
    # Download stock performance images
    amazon.getImage()
    microsoft.getImage()
    apple.getImage()


if __name__ == "__main__":
    main()

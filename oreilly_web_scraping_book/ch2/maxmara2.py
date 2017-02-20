from urllib.request import urlopen
from bs4 import BeautifulSoup

urlStr = "https://us.maxmara.com/store-finder/italy/milano"
html = urlopen(urlStr)
storeObj = BeautifulSoup(html.read(), "html.parser");

storeTable = storeObj.find("table", {"id":"store_locator"}) 
for address in storeTable.findAll("td", {"headers":"header3"}):
    print(address.get_text().split())

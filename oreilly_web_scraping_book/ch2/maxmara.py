from urllib.request import urlopen
from bs4 import BeautifulSoup

urlStr = "https://us.maxmara.com/store-finder/italy/milano"
html = urlopen(urlStr)
bsObj = BeautifulSoup(html.read(), "html.parser");

nameList = bsObj.findAll("div", {"class":"store_details"}) 
for name in nameList:
    print(name.get_text().split())

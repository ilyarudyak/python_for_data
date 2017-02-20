from urllib.request import urlopen
from bs4 import BeautifulSoup


htmlStr = urlopen("https://apod.nasa.gov/apod/archivepix.html").read()
bsObj = BeautifulSoup(htmlStr, "html.parser");

linkList = bsObj.findAll("a", limit=10) 
for link in linkList:
    print(link['href'])
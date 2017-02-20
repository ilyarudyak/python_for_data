from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup


baseUrl = "https://apod.nasa.gov/apod/archivepix.html"
archiveHtmlStr = urlopen(baseUrl).read()

for link in BeautifulSoup(archiveHtmlStr, "html.parser").findAll("a", limit=10):
    imgBaseUrl = urljoin(baseUrl, link['href'])
    # follow the link
    imgHtmlStr = urlopen(imgBaseUrl).read()
    imgUrl = urljoin(imgBaseUrl, BeautifulSoup(imgHtmlStr, "html.parser").img['src'])
    imgName = imgUrl.split('/')[-1]
    print(imgName)
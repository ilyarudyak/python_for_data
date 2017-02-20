from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os


baseUrl = "https://apod.nasa.gov/apod/archivepix.html"
archiveHtmlStr = urlopen(baseUrl).read()

for link in BeautifulSoup(archiveHtmlStr, "html.parser").findAll("a", limit=10):
    imgBaseUrl = urljoin(baseUrl, link['href'])
    
    # follow the link to image page
    imgHtmlStr = urlopen(imgBaseUrl).read()
    imgUrl = urljoin(imgBaseUrl, BeautifulSoup(imgHtmlStr, "html.parser").img['src'])
    imgName = imgUrl.split('/')[-1]
    print(imgName, imgUrl)

    # download and store image
    downloadDir = 'apod_pictures'
    urlretrieve(imgUrl, os.path.join(downloadDir, imgName))
    
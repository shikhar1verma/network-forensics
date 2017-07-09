#!/usr/bin/env python
'''
this scrip will download the images present
ina particular webpage. I took the webpage
of Narendra Modi's wikipage.
'''

from urllib import urlretrieve      #this helps to download the images
import urlparse                     #this will help to parse the page
from bs4 import BeautifulSoup       #used for webscrapping
import urllib2                      #this will help to open the URL

url = raw_input('Enter URL: ')                      #i took the sample page to be narender modis wikipage
soup = BeautifulSoup(urllib2.urlopen(url))
for img in soup.select('a.image > img'):
    print img['src']
    img_url = urlparse.urljoin(url, img['src'])
    file_name = img['src'].split('/')[-1]
    urlretrieve(img_url, file_name)                 #download the images to the folder  where the script resides

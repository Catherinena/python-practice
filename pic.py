#!/usr/bin/python
# -*- coding: utf-8 -*-

' crawl pictures '

__author__ = "zhengyunzhi"

import urllib.request
from bs4 import BeautifulSoup

count = 1

with urllib.request.urlopen("https://movie.douban.com/top250?start=0&filter=", data=None, timeout=10) as resu:
    soup = BeautifulSoup(resu, "lxml")
    for pic in soup.select('img'):
        web_pic = urllib.request.urlopen(pic.attrs['src'])
        web_pic_data = web_pic.read()
        local_file = open(str(count)+".png", 'wb')
        count = count + 1
        local_file.write(web_pic_data)
        local_file.close()


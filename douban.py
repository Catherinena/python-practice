#!/usr/bin/python
# -*- coding: utf-8 -*-

' crawl www.douban.com '

__author__ = "zhengyunzhi"

import urllib.request
from bs4 import BeautifulSoup

count = 0  # max 10


def my_filter(name):
    while name[0] == ' ' or name[0] == ' ':
        name = name[1:]
    if name[0] == '/':
        return 0
    return name


for i in range(0, 10):
    url = "https://movie.douban.com/top250?start=" + str(i*25) + "&filter="
    print("url = ", url)
    with urllib.request.urlopen(url, data=None, timeout=10) as resu:
        soup = BeautifulSoup(resu, "lxml")
        for item in soup.select('.item'):
            film = ""
            title_tmp = item.select('.title')
            if len(title_tmp) > 0:
                title_str = my_filter(title_tmp[0].string)
                if title_str != 0:
                    film = title_str + ": "
            description_tmp = item.select('.quote .inq')
            if len(description_tmp) > 0:
                film = film + description_tmp[0].string
            print(film)



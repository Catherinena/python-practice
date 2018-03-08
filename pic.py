#!/usr/bin/python
# -*- coding: utf-8 -*-

' crawl pictures '

__author__ = "zhengyunzhi"

import urllib.request
from bs4 import BeautifulSoup
import os

count = 1

if not os.path.exists("豆瓣电影图片"):
    os.makedirs("豆瓣电影图片")

with urllib.request.urlopen("https://movie.douban.com/top250?start=0&filter=", data=None, timeout=10) as resu:
    soup = BeautifulSoup(resu, "lxml")
    for pic in soup.select('img'):
        web_pic = urllib.request.urlopen(pic.attrs['src'])
        web_pic_data = web_pic.read()   # 打开单个图片，把内容读入到内存中
        local_file = open("豆瓣电影图片/" + str(count)+".png", 'wb')  # 打开本地文件
        count = count + 1
        local_file.write(web_pic_data)  # 把图片写到本地文件中
        local_file.close()


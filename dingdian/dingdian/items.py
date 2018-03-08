# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说名称
    name = scrapy.Field()
    #小说作者
    author = scrapy.Field()
    #小说链接
    novelUrl = scrapy.Field()
    #小说状态
    serialStatus = scrapy.Field()
    #小说字数
    serialNumber = scrapy.Field()
    #小说编号
    nameId = scrapy.Field()


    pass

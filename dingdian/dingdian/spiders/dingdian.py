import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem


class MySpider(scrapy.Spider):
    name = 'dingdian'
    allow_domains = ['x23us.com']
    bash_url = 'https://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        max_page = BeautifulSoup(response.text, 'lxml').select(".pagelink .last")[0].get_text()
        bashurl = str(response.url[:-7])
        for num in range(1, 11):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        trs = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor="#FFFFFF")
        for tr in trs:
            novel = tr.contents[1].contents[1]
            novel_title = novel.get_text()
            novel_link = novel['href']
            novel_author = tr.contents[5].get_text()
            novel_number = tr.contents[7].get_text()
            novel_status = tr.contents[11].get_text()
            item = DingdianItem()
            item['name'] = novel_title
            item['novelUrl'] = novel_link
            item['author'] = novel_author
            item['serialStatus'] = novel_status
            item['serialNumber'] = novel_number
            item['nameId'] = novel_link.split('/')[-2]
            return item



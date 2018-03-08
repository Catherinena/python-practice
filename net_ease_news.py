import os
import urllib.request
from bs4 import BeautifulSoup

' scrap netEase news '

__author__ = 'zhengyunzhi'

title = ['24小时点击排行', '本周点击排行', '本月点击排行']


def my_write_file(filename, newslist):
    save_path = '网易新闻'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file = open(save_path+"/"+filename+".txt", "w")
    for news in newslist:
        file.write(news+'\n')
    file.close()


def scrap(url):
    news = []
    type_list = []
    print("downloading", url, "...")
    with urllib.request.urlopen(url, data=None, timeout=10) as content:
        soup = BeautifulSoup(content, "html.parser", from_encoding='gb18030')
        for types in soup.select('.subNav'):
            for index, itype in enumerate(types.children):
                if index > 1:
                    type_list.append([itype.string, itype.attrs['href']])

        tab = soup.select('.area-half.left')
        if len(tab) > 0:
            tab_contents = tab[0].select('.tabBox .tabContents')
            for i in range(0, 3):
                news.append(str(title[i]))
                for single_news in tab_contents[i].find_all('a'):
                    news.append(single_news.string + ": " + single_news.get('href'))
            my_write_file('总榜', news)
            for news_type in type_list:
                print("downloading", news_type[1], "...")
                with urllib.request.urlopen(news_type[1], data=None, timeout=10) as my_news_content:
                    type_news_content = BeautifulSoup(my_news_content, "html.parser", from_encoding='gb18030')
                    type_tab = type_news_content.select('.area-half.left')
                    type_news = []
                    if len(type_tab) > 0:
                        type_content = type_tab[0].select('.tabBox .tabContents')
                        for i in range(0, 3):
                            type_news.append(str(title[i]))
                            for single_type_news in type_content[i].find_all('a'):
                                type_news.append(single_type_news.string + ": " + single_type_news.get('href'))
                        my_write_file(news_type[0], type_news)


if __name__ == '__main__':
    scrap("http://news.163.com/rank/")
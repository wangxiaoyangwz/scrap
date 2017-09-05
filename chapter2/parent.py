# -*- coding:utf-8 -*-
#父标签处理

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html)

print(bs0bj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
#parent-->父标签
#previous_sibling-->兄弟标签的最后一个标签，不包括自己
#got-text()-->消除标签，返回标签内包含文字的字符串，获取标签中的内容

#定位数据块的位置


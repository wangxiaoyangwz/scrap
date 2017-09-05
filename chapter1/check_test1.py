# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error  import HTTPError,URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:#捕获错误(网页错误、服务器链接错误)-->程序结束
        return None
    try:
        bs0bj = BeautifulSoup(html.read())
        title = bs0bj.body.h1
    except AttributeError as e:#捕获错误（标签不存在）
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:#如果title内容为空
    print("title could not be found")
else:
    print(title)

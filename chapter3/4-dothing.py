# -*- coding:utf-8 -*-
#创建一个爬虫，收集页面标题，正文的第一个段落，编辑页面的链接 
#1、观察网站页面-->2、拟定采集模式

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import io  
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
pages = set()

def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bs0bj = BeautifulSoup(html,"html.parser")

	try:
		print(bs0bj.h1.get_text())
		print(bs0bj.find(id="mw-content-text").findAll("p")[0])
		print(bs0bj.find(id="ca-edit").find("span").find("a").attrs['href'])
	except AttributeError:
		print("页面缺少一些属性！不过不用担心")

	for link in bs0bj.findAll("a",href = re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newpage = link.attrs['href']
				print("-------------------\n"+newpage)
				pages.add(newpage)
				getLinks(newpage)

getLinks("")

#不能保证每个页面都有要求数据，打印语句顺序是最有可能有的可能性降低
#异常梳理语句中包含多个语句是危险的，不能知道是哪个语句出现错误
#如果没有段落，但是有编辑按钮，编辑链接将不会获得

# -*- coding:utf-8 -*-
#递归处理链接

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
	global pages#全集变量集合
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bs0bj = BeautifulSoup(html,"html.parser")

	for link in bs0bj.findAll("a",href = re.compile("^(/wiki/)")):
		if 'href' in link.attrs:#链表中有href属性，就是链接
			if link.attrs['href'] not in pages:#如果链接不在pages中，是一个新链接
				newPage = link.attrs['href']#抽取新href属性，链接保存在newPage中
				print(newPage)#不在就打印新链接
				pages.add(newPage)#并将新链接加入pages列表中
				getLinks(newPage)#获得新网页中的链接


getLinks("")#wiki主页

#set()可以进行添加删除、交集、并集、集合操作 详情-->http://blog.csdn.net/business122/article/details/7541486
#python默认递归次数1000次，达到限制后就停止
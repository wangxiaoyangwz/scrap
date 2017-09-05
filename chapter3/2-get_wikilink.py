# -*- coding:utf-8 -*-

#构建从一个页面到另一个页面的爬虫，忽略了异常处理
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
#用系统当前时间生成一个随机生成器，可保证每次程序运行时是全新的路径
random.seed(datetime.datetime.now())#seed() 方法改变随机数生成器的种子，时间是改变的所以产生的随机序列是不同的

def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)#wiki域名+其中的一个网页获得BeautifulSoup对象
	bs0bj = BeautifulSoup(html)
	return bs0bj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))#抽取含有链接的a标签，将其返回

links = getLinks("/wiki/Kevin_Bacon")#链接列表

while len(links)>0:
	#随机选取一个链接，并将连接数减一，抽取其中的href属性
	newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)#打印这个链接
	links = getLinks(newArticle)#讲这个链接传递给getLin函数

#用随机数生成器随机选择每一页上的一个词条链接
#随机数种子会产生相同的随机序列，用时间最为随机数列生成的起点
#random.seed(datetime.datetime.now())-->seed() 方法改变随机数生成器的种子，时间是改变的所以产生的随机序列是不同的
#random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
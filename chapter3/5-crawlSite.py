# -*- coding:utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlparse#
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):#includeUrl-->内链
	includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc# scheme://netloc
	internalLinks = []
	#找出以“/”开头的链接
	#^(/|.*abc), 意思是匹配包括abc的字符串, 或者匹配以/开头的字符串
	for link in bsObj.findAll("a",href = re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] not None:
		#if 'href' in link.attrs:
			if link.attrs['href'] not in internalLinks:#有新链接
				if link.attrs['href'].startswith("/"):#startswith()查字符串是否是以指定子字符串开头
					internalLinks.append(includeUrl+link.attrs['href'])
				else:
					internalLinks.append(link.attrs['href'])#不是以/开头的链接加上href属性
	return internalLinks

#获取页面所有外链接
def getExternalLinks(bsObj,excludeUrl):
	externalLinks = []
	#开头是http或者www，且不包含当前url的链接
	for link in bsObj.findAll("a",href = re.compile("^(http|www)((?!"excludeUrl+").)*$")):#
		if link.attrs['href'] is not None:#如果链接包含href属性
			if link.attrs['href'] not in externalLinks:#如果链接不在列表里，是新链接
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	#http://www.runoob.com/python/att-string-replace.html
	addressParts = address.replace("http://","").split("/")#replac()字符串中的 old（旧字符串） 替换成 new(新字符串)
	return addressParts

def getRandomExternalLink(startingPage):#stratingPage-->主页
	html = urlopen("startingPage")
	bsObj = BeautifulSoup(html,"html.parser")
	externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)#获取（主页）startingPage中netloc部分的外链接
	if len(externalLinks)==0:#外链接列表长度为0-->找主页内链接
		print("No external links,looking around the site for one")
		domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc#startingPage的scheme://netloc
		internalLinks = getInternalLinks(bsObj,domain)#获取对象的scheme://netloc的内链接
		return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])#递归直到内链列表长度为零
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]#返回外链接列表

def followExternalOnly(startingSite):#
	externalLink = getRandomExternalLink(startingSite)#
	print("random external link is: "+externalLink)

followExternalOnly("http://oreilly.com")

# 从http://oreilly.com开始-->随机从一个外链跳到另一个外链
#不能保证一直可以发现外链，保证可以一直发现外链
	#用递归深入网站知道找到另一个外链

# #程序可视化为流程 
#                                           Y
# 	 获取网页生的所有外链--->还有外链吗？----> 返回到一个随机外链
# 	 			^
# 	            |                |N
# 	            |                |
#                 -------进入网页上的一个内链

#如果爬虫遇到一个外链都没有，可能性很小，这是程序一直运行跳不出去，知道达到递归上限

# urlparse模块主要是把url拆分为6部分，并返回元组。并且可以把拆分后的部分再组成一个url。
#主要有函数有urljoin、urlsplit、urlunsplit、urlparse等。
# URL的一般结构相关: scheme://netloc/path;parameters?query#fragment.
#协议://用户名@密码:子域名.域名.顶级域名:端口/目录/文件名.文件后缀？参数=值#标志
# 要得到正确的netloc值，则url必须以//开头，否则会被归到path值里去.

#顺序：
	#followExternalOnly()-->get随机获取startingSite中外链接--》
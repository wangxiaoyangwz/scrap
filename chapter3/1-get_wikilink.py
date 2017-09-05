#`六度分隔理论`-->两个不想管的主题，用一个总数不超过六条的主题链接起来

#埃德尔---->贝肯 需要最少的链接点击次数？
#对维基百科服务器的负载的影响
# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re #导入re库

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bs0bj = BeautifulSoup(html)
#所有a标签，且href属性满足compile
links = bs0bj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
for link in links:#链接在links中
	if 'href' in link.attrs:#如果link中有href属性
		print(link.attrs['href'])#打印href属性

#想要的所有链接都在其中，但是有许多并不需要的链接
#判断链接是否有对应的词条，指向词条页面的链接有共同点
	#1都在id是bodyContent的div标签中
	#2URL不包含：
	#3url都是以/wiki/开头
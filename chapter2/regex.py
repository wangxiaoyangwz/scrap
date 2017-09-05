# -*- coding:utf-8 -*-
#抓取网页中图片的链接
#使用regex
#fingAll("img")-->抓取所有的图片
	#问题：有多余的图片，隐藏图片（用于网页布局留白，元素对齐的空白图片）
	
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re #导入re库

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images: 
    print(image["src"])

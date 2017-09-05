# -*- coding:utf-8 -*-
#处理兄弟标签

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html)

for sibling in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
	print(sibling)

#next_siblings()结果标题行跳过
	#获得兄弟标签，不能包括该标签本身
	#只调用后面的兄弟标签

#找到兄弟标签的最后一个标签
	#previous_siblings()

#next_sibling()、previous_sibling()
	#返回的时单一标签
# -*- coding:utf-8 -*-
# os模块获取每个下载文件的目标文件夹，建立完整的路径

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"
#获得绝对地址，去掉外链
#duiurl链接进行清理和标准化
def getAbsoluteUrl(baseUrl,source):
	if source.startswith("http://www."):
		url = "http://"+source[11:]
	elif source.startswith("http://")
		url = source
	elif source.startswith("www."):
		url = "http://"+source[4:]
	else:
		url = baseUrl+"/"+source
	return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
	path = absoluteUrl.replace("www.","")#绝对地址去掉www.
	path = path.replace(baseUrl,"")# baseUrl去掉
	path = downloadDirectory+path
	directory = os.path.dirname(path)# 返回path的目录。其实就是os.path.split(path)的第一个元素。


	if not os.path.exists(directory):# 如果path存在，返回True；如果path不存在，返回False。
		os.makedirs(directory)
	return path

html = urlopen("http://pythonscraping.com")
bsObj = BeautifulSoup(html,"html.parser")
downloadList = bsObj.find(src=True)
#如果下载过了
for download in downloadList:
	fileUrl = getAbsoluteUrl(baseUrl,download["src"])
	if fileUrl is not None:
		print(fileUrl)
		urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))



#os.path.exists(path)

# 如果path存在，返回True；如果path不存在，返回False。

# >>> os.path.exists('c:\\')

# True

# >>> os.path.exists('c:\\csv\\test.csv')

# False

# os.path.dirname(path)

# 返回path的目录。其实就是os.path.split(path)的第一个元素。

# >>> os.path.dirname('c:\\csv\test.csv')

# 'c:\\'

# >>> os.path.dirname('c:\\csv')

# 'c:\\'
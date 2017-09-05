# -*- coding:utf-8 -*-

import csv

csvFile = open("../test.csv",'w+')#打开文件  ..-->代表上一级
try:
	writer = csv.writer(csvFile)#写文件
	writer.writerow(('number','number plus2','number times 2'))#写内容
	for i in range(10):
		writer.writerow((i,i+2,i*2))
finally:
	csvFile.close()#关文件

#python新建文件机制-->../test.csv，不存在自动创建文件，若存在覆盖


`API`:待解决

数据存储到`数据库`中  

`数据可视化`

python3

`网络服务器`

`HTTP协议`

`HTML语言`

`网络安全`

`图像处理`

`数据科学`


1、网络数据采集、网络爬行-->python库
2、编写爬虫时涉及的主题

# 第一部分



###&emsp;爬虫功能  
&emsp;&emsp;域名切换  
&emsp;&emsp;信息收集  
&emsp;&emsp;信息存储

###&emsp;思考爬虫的想法
&emsp;&emsp;1、通过网站域名获取HTML数据    
&emsp;&emsp;2、根据目标信息解析数据  
&emsp;&emsp;3、存储目标信息  
&emsp;&emsp;4、移动另一网页重复以上过程

#&emsp;&emsp;&emsp;&emsp;第一章--初见网络爬虫
&emsp;目的：  
&emsp;&emsp;不通过浏览器格式化和理解数据  
&emsp;互联网原理：  
&emsp;网络在做什么？  
&emsp;浏览器如何解释HTML、CSS、javascript  
&emsp;浏览器获取信息过程：  

>**&emsp;&emsp;Bob台式机想要链接Alice服务器** 

Bob电脑的行为：  
1、Bob电脑发送一串0和1比特值，表示电压高低，这些比特构成一种信息（包含请求头、消息体)  
&emsp;&emsp;`请求头`：中包含Bob本地路由器的MAC地址、AliceIP地址  
&emsp;&emsp;&emsp;&emsp;[MAC地址](https://www.zhihu.com/question/21546408)：或称为物理地址、硬件地址。用来定义网络设备的位置  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;前24位叫做组织唯一标志符：EEE的注册管理机构给不同厂家分配的代码，区分了不同的厂家。 
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;后24位称为扩展标识符：是由厂家自己分配的。同一个厂家生产的网卡中MAC地址后24位是不同的。
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;MAC地址则是下一跳的地址，每跳过一次路由器都会改变。  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;OSI模型中，第二层数据链路层则负责 MAC地址  
&emsp;&emsp;&emsp;&emsp;**`IP地址`**：IP协议就是使用这个地址在主机之间传递信息  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节）。  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IP地址通常用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;常见的IP地址，分为IPv4与IPv6两大类  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P地址本质上是终点地址，它在跳过路由器（hop）的时候不会改变  
&emsp;&emsp;`消息体`：中包含Bob对ALice服务器应用的请求

2、Bob本地路由器接受所有0和1比特值，并将其理解成数据包（packet），从Bob的MAC地址寄到Alice的IP地址
&emsp;&emsp;路由器把数据包盖上自己的IP地址作为发件地址，然后通过互联网发送出去

3、Bob数据包游历一些中介服务器，沿着正确的物理/电路路径前进，到Alice服务器

4、Alice服务器在她的IP地址收到数据包

5、Alice服务器读取数据包请求头里的目标端口，然后将它传递给对应的应用---网络服务器上  
&emsp;&emsp;&emsp;`目标端口`：网络应用的80端口，可理解为数据包的'房间号'，IP地址是"街道地址"

6、网络服务器应用从服务器处理器收到数据，数据是这样的：  
&emsp;&emsp;&emsp;-这是一个GET请求  
&emsp;&emsp;&emsp;-请求文件 index.html

7、网络服务器应用找到对应的HTML文件，将它打包成新的数据包发送给Bob，然后通过她的本地路由器发出去，同样的过程
传回到Bob的机器上

**浏览器做什么？**  
&emsp;&emsp;&emsp;创建信息的数据包、发送数据包、把获取的数据解释成图像、声音、视频、文字
&emsp;&emsp;&emsp;可以让服务器发送一些数据，到对接网络接口的应用上，像是语言的库文件
&emsp;&emsp;&emsp;浏览器就是代码，可以分解成基本组件，可重写、重用
```python
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
#输出源代码-->域名为http://www.pythonscraping.com的服务器上
#<网络域名根地址>/exercises文件夹里的HTML文件exercise1.html的源代码
```
网页中链接许多资源文件，会想服务器发起另一个请求，python程序中没有返回并向服务器`请求多个文件`的逻辑只能读取单个HTML文件  

## 1.2.3--可靠的网络连接
&emsp;&emsp;&emsp;一开始就估计可能出现的问题   

&emsp;&emsp;&emsp;`html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")`    
&emsp;&emsp;&emsp;&emsp;&emsp;这一行代码可能出现的问题  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;+网页在服务器中不存在  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;+服务器不存在  
**&emsp;&emsp;&emsp;&emsp;&emsp;处理异常:**  

第一种错误：抛出HTTPError错误
```python
try:
	html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
	print(e)
	#返回空值中断程序，或执行另一方案
else:
	#程序继续，如果捕获到错误，不执行else语句
```
第二种错误：服务器不存在，链接打不开，返回None对象
```python
if html is None:
	print("URL is not found")
else:
	#程序继续
```
网页获取成功，但是网页上的内容是否正确  
`标签检查条件`，保证标签存在，标签不存在，返回`None对象`，调用该标签下的子标签，发生`AttributeError错误`
```python
	try:
		badContent = bs0bj.nonExistingTag.anotherTag
	except .AttributeError as e:#捕获错误-->程序结束
		print("Tag was not found")#没有错误-->else
	else:
		if badContent == None:#子标签不存在
			print("Tag was not found")
		else:
			print(badContent)#子标签存在打印标签内容
```
















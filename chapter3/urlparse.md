# urlparse

>主要是用来 解析URL字符串

`主要方法`： urlprase
`次要方法`： urljoin urlsplit  urlunsplit等

**详解**
urlparse模块主要是把url拆分为6部分，并返回元组
并且可以把拆分后的部分再组成一个url

URL格式包含：
协议://用户名@密码:子域名.域名.顶级域名:端口/目录/文件名.文件后缀？参数=值#标志

urlparse.urlparse(urlstring[,scheme[, allow_fragments]])
`scheme `– 主要是用来 为不包含些一部分的URL`指定默认协议`,默认值为空字符串  

`allow_fragments`指示是否可以对地址进行`分片`，此参数的默认值为 True  
urlstring解析成6个部分，它从urlstring中取得URL，并返回`元组` (scheme, netloc, path, parameters,query, fragment)  

组件是一串字符，也有可能是空的。组件不能被解析为更小的部分  
分割符号并不是解析结果的一部分，除非用斜线转义  
`返回的这个元组`-->确定网络协议(HTTP、FTP等等 )、服务器地址、文件路径  

urlparse方法返回对象中的属性
索引值 值含义 默认值  备注  
scheme  0     协议    空字符串  
netloc  1  服务器地址 空字符串   
path    2     路径    空字符串   
parameters 3 参数     空字符串 
fragment 5  分片部分  空字符串 
username   \

用户名 None   

password   

密码 None   

hostname   

主机名 None   

port
端口 None 

>>> url = urlparse.urlsplit('http://www.baidu.com:80/index.html?src=fie')  

>>> url  

SplitResult(scheme='http',netloc='www.baidu.com:80', path='/index.html', query='src=fie', fragment='')  

>>> url = urlparse.urlparse('http://www.baidu.com:80/index.html?src=fie')  

   
>>> url  

ParseResult(scheme='http',netloc='www.baidu.com:80', path='/index.html', params='', query='src=fie',fragment='')
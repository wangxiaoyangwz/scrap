>## pymysql建立连接出错  
我的代码  
`conn = pymysql.connect(host = '127.0.0.1',unix_socket='/tmp/mysql.sock',user='root',passwd=' ',db='mysql')`  

错误`AttributeError: 'module' object has no attribute 'AF_UNIX'`

原因`windows系统不需要指定unix sock这个参数`

解决`conn = pymysql.connect(host='127.0.0.1', user='root', passwd=' ', db='mysql')`

[参考]( https://segmentfault.com/q/1010000008576366)
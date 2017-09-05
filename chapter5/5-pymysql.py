import pymysql
#创建连接对象
conn = pymysql.connect(host = '127.0.0.1',user='root',passwd=' ',db='mysql')
#创建游标对象（光标对象）
cur=conn.cursor()
# 执行SQL
cur.execute("USE scraping")#用scraping数据库
cur.execute("SELECT * FROM pages WHERE id = 1")
#fetchone()返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
print(cur.fetchone())#
cur.close()
conn.close()

#cur.fetchone()-->获取查询结果
#jilu = cur.fetchone()  ##此时 通过 jilu[0],jilu[1],jilu[2]可以依次访问
#如果select本身取的时候有多条数据时：cursor.fetchone()：将只取最上面的第一条结果，返回单个元组如('id','title')，然后多次使用cursor.fetchone()，依次取得下一条结果，直到为空。
#cursor.fetchall() :将返回所有结果，返回二维元组，如(('id','title'),('id','title')),
# 如果select本身取的时候只有一条数据时：
# cursor.fetchone()：将只返回一条结果，返回单个元组如('id','title')。
# cursor.fetchall() :也将返回所有结果，返回二维元组，如(('id','title'),),
#参考：http://blog.csdn.net/jian_yun_rui/article/details/73692331

# 连接模式-->连接数据库、发送数据库信息、处理回滚操作、创建新的光标对象
# 	回滚：查询中断时，数据库需要回到初始状态，用于事务控制手段实现状态回滚、
# 光标模式-->

# 一个链接可以有多个光标
# 一个光标跟踪一种状态信息-->数据库的使用状态
# 有多个数据库，都需要写数据-->需要多个光标处理
# 光标还会包含最后一次查询执行结果
# 光标函数cur.fetchone()-->获取查询结果

# 一定要关闭光标和连接
# Python startswith()方法
用于检查字符串是否是以指定子字符串开头  
是则返回 True，否则返回 False  
参数 beg 和 end 指定值，则在指定范围内检查

`str.startswith(str, beg=0,end=len(string));`  

参数
`str` -- 检测的字符串。
`strbeg` -- 可选参数用于设置字符串检测的起始位置。
`strend` -- 可选参数用于设置字符串检测的结束位置。

str = "this is string example....wow!!!";
print str.startswith( 'this' );
print str.startswith( 'is', 2, 4 );
print str.startswith( 'this', 2, 4 );
以上实例输出结果如下：
True
True
False
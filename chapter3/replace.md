# Python replace()方法  

Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。 

>str.replace(old, new[, max])

参数
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次  

返回值  
生成的新字符串  

str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);
以上实例输出结果如下：
thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string  

参考：http://www.runoob.com/python/att-string-replace.html
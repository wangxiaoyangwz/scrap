# 第二章--复杂HTML解析
　　找到目标信息前，敲掉不需要的信息  
>　　**该章介绍从复杂网页中抽取需要的信息**  

`页面解析`：  
>　　　　**网站修改后代码失效问题**  

　　　　 解决该问题：  
　　　　　　　　
1. 找网站是否有友好的移动版（自己的请求头设置成处于移动设备的状态）接受网站的移动版
　　　　　　　　2. 找javascript文件信息，需查看网页加载的javascript文件
　　　　　　　　3. 从网页的URL链接中获取  
　　　　　　　　4. 找其他数据源
    
> 　　　**通过属性查找标签、标签组的使用、标签解析树的导航过程**    

　　　　　　每个网站都有`层叠样式表css：`  
　　　　　　　　-->css让相同HTML元素变现为不同的样式通过class属性

>　　　　**findAll函数:**  

 　　　　　　　　`findAll("标签名"，{"属性"}):`可`以获取所有指定标签
>　　　　**get_text函数:** 

　　　　　　　　get\_text()：函数清除HTML文档中所有标签，返回只含有文字的字符串
　　　　　　　　　　　　　如果正在处理含有超链接等，标签会清除，返回字符串 　　
　　　　　　　　在打印、存储、操作数据时，应最后使用该函数　　

>　　　　**find()和findall():**  
　　　　
　　　　通过标签属性查找指定标签　　
　　　　`find\findAll(tag,attributes,recursibe,text,limit,keywords)`  

　　　　　　　　`tag`:标签参数，一个标签或多个标签组成的列表  
　　　　　　　　`.findAll({"h1","h2"...}) ` 
　　　　　　　　`attributes参数`：字典封装，标签的若干个属性和对应的属性值  
　　
　　　　　　　　
```python 
　　　　　　　　findAll("span",{"class":{"green","red"}}) #返回HTML文档中，s颜色是蓝色和红色的 span标签  
```

　　　　　　　　　`recursibe参数：`是布尔值，设为True&emsp;findAll根据要求查询标签参数的all子标签，以及子标签的子标签 
　　　　　　　　　　　　　　　　　　　　　　设为false：findall查询一级标签,  
　　　　　　　　　　　　　　　　　 默认是True  
　　　　　　　　　`文本参数text`：用标签的文本内容匹配，不是标签属性  
　　　　　　　　　　　　　　　　　例如查找标签中含有“某某内容”的标签  
```python
　　　　　　　　　　　　nameList = bs0bj.findAll("text="the prince")
                        print(len(nameList))
```

　　　　　　　　　   `范围限制参数limit：`只适用于findAll，find相当于limit=1的情况  
　　　　　　　　　　　　　　　　　　　对网页的前x项有兴趣，可以设置ｘ  
　　　　　　　　　　`关键词参数keyword：`可选择具有制定属性的标签   
　　　　　　　　　　　　　　　　　　　关键字参数完成任务　　

## 2.2.2--BeautifulSoup对象
　　　bs0bj  
　　　标签tag对象  
　　　Beautifulsoup通过find、findAll获取对象

　　　　



  






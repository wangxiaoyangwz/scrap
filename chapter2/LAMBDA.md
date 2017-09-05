# LAMBDA表达式
>lambda如何在网络中进行数据采集  

lambda实质是函数，可最为其它函数的变量使用，f(g(x),y) or f(g(x),h(x))
`soup.findAll(lambda tag: len(tag.attrs) == 2)`-->参数是lambda函数，lambda函数是tag的属性有两个，并且用字典方式存储

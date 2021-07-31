第一部分：数据未分离

origin	最基础的get，post请求
primary	面向对象方式的get，post请求
start	unittest方式的get，post请求
work	HTMLTestRunner方式的get，post请求

第二部分：数据分离

work_keyword	

第一组（网上抄的用法）
===============================================
data	存放请求的参数
config	存放url的配置文件
api_keyword	存放通用的get，post请求

api_demo 最基础的数据分离的get，post请求
cases	 unittest方式的数据分离的get，post请求
===============================================

第二组（加上了RunMain方法）

===============================================
data	存放请求的参数
config	存放url的配置文件
keyword_demo	存放通用的get，post请求

下面的四个文件夹，对应数据未分离的四个部分
keyword_origin 
keyword_primary
keyword_start
keyword_work	 
===============================================

第三部分：数据分离和批量处理用例
work_keyword_all

	
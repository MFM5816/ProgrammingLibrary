

- **写一个程序，读取文件时，一次读取十行，把读取的内容放到生成器，然后打印出生成器中的内容**

  ```python
  
  ```



**编写代码，实现输入num为四位数，并按如下的规则进行加密**

```python
1、每一位分别加5，然后分别将其替换为该数除以10取余后的结果
2、将该数的第1位和第4位互换，第二位和第三位互换
3、最后合起来作为加密后的整数输出
# 例如：输入：1234，输出：9876

```



- **请写出一段Python代码实现删除一个list里面的重复元素**

```python
原始数据: [1,2,3,4,5,1,2,3,2,3,4]
最终结果: [1,2,3,4,5]
```



- **要求用递归方式实现每隔1秒在屏幕输出一次: hello world**

```python
函数: get_world(3)
```



- **定义一个list，打印出每个元素出现的次数**

```python
L = [1,2,3,4,5,1,2,1,2]
L.count(1)
```



- **用Python写出计算一个文件中大写字母数的代码（代码需要保证在文件大小远大于内存的条件下仍能正常工作）**

```python
file1.md
Take Me To Your Heart
Take Me To Your Heart

[A-Z]
```



- **请解释什么是装饰器，并写出一个装饰器示例用来打印函数的执行时间**

```python
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象

```



- **一条SQL语句查询出每门课都大于80分的学生姓名**

```python
表名:grade
name      course        score
张三       语文           81
张三       数学           85
李四       语文           76

# 建库建表
use govdb;
create table grade(
name varchar(20),
course varchar(20),
score float(5,2)
)charset=utf8;
insert into grade values
('张三','语文',81),('张三','数学',85),('李四','语文',76);

# 答案1:
select name from grade group by name having min(score)>80;
# 答案2:
select distinct name from grade where name not in(select name from grade where score<=80);
```



- **写一个线程计时器，每隔n秒在屏幕打印当前时间，时间格式为HH:MM:SS**

  ```python
  
  ```



- **说说下面几个概念:同步,异步, 阻塞,非阻塞?**

  ```python
  # 1. 同步
  多个任务之间有先后顺序执行，一个执行完下个才能执行
  # 2. 异步
  多个任务之间没有先后顺序，可以同时执行
  # 3. 阻塞
  如果卡住了调用者，调用者不能继续往下执行，就是说调用者阻塞了
  # 4. 非阻塞
  如果不会卡住，可以继续执行，就是说非阻塞的
  
  同步异步相对于多任务而言，阻塞非阻塞相对于代码执行而言
  ```



- **TCP和UDP的区别？为何基于tcp协议的通信比基于udp协议的通信更可靠？**

  ```python
  # 区别
  TCP: 面向连接，保证高可靠性传输层协议
  UDP：无连接、无秩序的传输层协议
  
  # 原因
  TCP：可靠，因为只要对方回了确认收到信息，才发下一个，如果没收到确认信息就重发
  UDP：不可靠，它是一直发数据，不需要对方回应
  
  # 简述三次握手四次挥手的过程
  1、三次握手 - 建立连接
      1、客户端先向服务端发起一次询问建立连接的请求，并随机生成一个值作为标识
      2、服务端向客户端先回应第一个标识，再重新发一个确认标识
      3、客户端确认标识，建立连接，开始传输数据
  2、四次挥手 - 断开连接
      1、客户端向服务端发起请求断开连接的请求
      2、服务端向客户端确认请求
      3、服务端向客户端发起断开连接请求
      4、客户端向服务端确认断开请求
  ```



- **创建两个线程，其中一个输出1-52，另外一个输出A-Z。输出格式要求：12A 34B 56C 78D**

  ```python
  1、两个线程,一个输出12 34 56,另一个输出A-Z
  2、控制线程之间的切换
  ```



- **如何使用Python来进行查询和替换一个文本字符串？请写出示例**

  ```python
  # 正则sub()
  # sub(需要被替换文件, 替换成什么, 字符串)
  
  ```



- **xpath解析题**

  ```python
  <?xml version="1.0"encoding="ISO-8859-1"?>
  
  <bookstore>
    <book>
  		<title lang="eng">Harry Potter<title>
  		<price>29.99</price>
  		<author>赵六</author>
    </book>
    <book>
  		<title lang="eng">Learning XML</title>
  		<price>39.95</price>
  		<author>张三</author>
  	</book>
  	<book>
    	<title lang="eng">ORACLE”</title>
     	<price>40.32</price>
     	<author>Lary</author>
  	</book>
  </bookstore>
  
  # 写出表达式
  1.选取bookstore中的book子节点的所有title子节点，且其中的price元素的值须大于35.0
    # //bookstore/book[price>35.0]/title
  2.选取属于bookstore元素的后代的所有book元素，而不管它们位于bookstore之下的什么位置
    # //bookstore//book
  ```

- **在scrapy框架中,如何使用FormRequest方法来发送一个post请求（请写出具体示例爬虫文件代码,以访问淘宝网站为例：http://www.taobao.com/login）**

```python
import scrapy
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowd_domains = ['www.taobao.com']
    start_urls = ['']
    
    def start_requests(self):
        yield scrapy.FormRequest(
        	url='',
            formdata={Form表单数据},
            callback=self.parse
        )
        
    def parse(self,response):
        pass
```



- **列表L: 请写出实现正序排列，倒序排列，逆序排列**

  ```python
  L = [1,3,2,8,7]
  正序: L.sort()
  倒序: L.sort(reverse=True)
  逆序: L.reverse()
  ```

- **MySQL查询**

  ```python
  # 表A - 产品信息表
  ID,产品编号,产品名称,产品价格,产品具体信息
  id  gid     name    price    info
  # 表B - 购买记录表
  ID,产品编号,购买数量,购买时间
  id  gid     gnum   gtime
  # 表C - 购买统计表
  ID,产品编号,购买次数
  id   gid     gc
  
  问题:
  1、查询表A中按照产品价格升序,产品编号倒序的前100数据
    # select * from A order by pirce,gid desc limit 100;
  2、查询表B中购买数量总和超过100的产品编号
    # select gid from B group by gid having sum(gnum)>100;
  3、查询表B中购买数量总和超过100的产品编号,产品名称,产品价格,产品具体信息
    # select B.gid,A.name,A.price,A.info from B group by gid having sum(gnum)>100 inner join A on A.gid=B.gid;
  
  4、更新表A中产品的产品名称为 产品名称+'热',当该产品在B表中购买总数超过100的产品并且购买时间在2011-01-01之前
    # update A set name=concat(name,'热') where gid in(select gid from B where gtime<'2011-01-01' group by gid having sum(gnum)>100);
  
  5、假设在开发过程中在用户购买页面进行购买操作的时候,后台需要做一下操作,请根据步骤写出具体语句
  产品编号:89 购买数量:100 时间2011-01-01将购买信息插入到表B中
    # insert into B(gid,gnum,gtime) values(89,100,'2011-01-01');
  ```


徐铭  -  魔方达人






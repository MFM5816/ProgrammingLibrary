## **回顾**

### **可迭代对象、迭代器和生成器**

- **可迭代对象**

```python
1、定义 ：可通过for循环迭代读取数据供我们使用的对象
2、本质 ：可迭代对象通过__iter__()方法向我们提供一个迭代器
3、示例
name_list = ['紫衫龙王','金毛狮王','白眉鹰王','青翼蝠王']
name_iterator = name_list.__iter__() # 提供该可迭代对象(name_list)的迭代器
for name in name_iterator:
    print(name)
    
4、__iter__()函数与__next()__函数的作用是什么?
  1、__iter()__函数: 获取可迭代对象的迭代器
  2、__next()__函数：对迭代器不断使用__next()__函数来获取下一条数据,完成之后再次调用会抛出StopIteration异常
```

- **迭代器**

```python
一个实现了__iter__()方法和__next__()方法的对象，就是迭代器
```

- **生成器**

```python
1、函数中有yield关键字,就称为生成器
2、yield作用
  1、保存当前运行状态(断点),然后暂停执行,即将生成器（函数）挂起
  2、将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
3、如何启动生成器
  next()：单纯的获取生成器中的一个值
4、示例
def f1():
    for i in range(3):
        yield i
g = f1()
print(next(g))
```

### **并发和并行**

```python
# 1. 并发
同时处理多个任务,内核在任务间不断地切换,达到好像多个任务同时被执行的效果,实际上每一时刻只有1个任务在占有CPU

# 2. 并行
一起执行,多个任务利用计算机的多核资源同时执行,此时多个任务之间是并行关系

# 3. 示例
在计算机系统中,并行和并发是同时存在的
计算机 ：2核
任务   ：QQ、微信、爱奇艺、英雄联盟、Chrome
并发   ：这5个任务间存在着并发关系
并行   ：第1核(QQ)、第2核(微信)
```

### **进程、线程、协程**

```python
# 1. 进程
程序的运行过程,是CPU分配资源的最小单位

# 2. 线程
最小执行单位,是系统分配内核的最小单位,由所属进程管理,一个进程可有多个线程

# 3. 协程
1、定义 ：微线程,协程允许在不同的位置暂停或者开始执行,简单来说,协程就是可以暂停执行的函数
2、原理 ：记录一个函数栈的上下文,进行协程的切换调度,当一个函数暂停执行时,会将上下文栈帧保存起来
3、本质 ：单线程,资源消耗小,无须线程间切换的开销,无需加互斥锁
4、协程模块 ：greenlet、gevent、... ...
```

**基于协程的多任务并发？**

```python

```

```python

```

## **Python中的那些锁**

- **GIL锁**

  ```python
  # 1. GIL是什么？ - CPython
  全局解释器锁,限制多线程同时执行,保证同一时间内只有一个线程在执行
  
  # 2. 作用
  同一进程中线程是数据共享，当各个线程访问数据资源时会出现竞争状态，即数据可能会同时被多个线程占用，造成数据混乱，这就是线程的不安全。而解决多线程之间数据完整性和状态同步最简单的方式就是加锁。GIL能限制多线程同时执行，保证同一时间内只有一个线程在执行
  
  # 3. 影响
  影响多线程效率
  
  # 4. 如何避免？
  1、用多进程 代替 多线程
  2、更换解释器
  ```

- **互斥锁**

  ```python
  # 1. 问题原因
  多个线程共享数据时，如果数据不进行保护，则可能出现数据不一致现象
  # 2. 解决方案
  使用一把锁把代码保护起来，以牺牲性能换取代码的安全性
  # 3. 示例
  ```
  
- **死锁**

  ```python
  多个进程/线程在执行过程中,因争夺资源而造成的一种互相等待的现象,若无外力作用,它们都无法进行下去,此时称系统处于死锁状态
  ```

**产生死锁**

```python

```

**避免死锁**

```python

```

## **MySQL数据库**

- **数据库的三范式**

  ```python
  # 1. 三范式
    1NF:字段不可拆分
    2NF:有主键，非主键字段依赖主键
    3NF:非主键字段不能相互依赖
  
  # 2. 解释 
    1NF:原子性 字段不可再分,否则就不是关系数据库
    2NF:唯一性 一个表只说明一个事物
    3NF:每列都与主键有直接关系，不存在传递依赖
      
  # 3. 解释
  1NF:
    符合1NF:   用户ID  用户名  密码   姓名  电话
    不符合1NF：用户ID  用户名  密码   用户信息(包含姓名和电话)
  
  2NF:
    第二范式是在第一范式的基础之上建立起来的,满足第二范式前提必须满足第一范式,要求数据库表中的每个实例或行都能被唯一区分,建立主键
  
  3NF:
    1、满足第三范式必须先满足第二范式
    2、要求：属性不依赖于其他非主属性，简而言之为如果表的信息能被推导出来,就不能单独设计一个字段来存放
    3、如果一个实体中出现其他实体的非主属性，可以将这两个实体用外键关联，而不是将另一张表的非主属性直接写在当前表中
    
  表1：
  商品名称 价格 描述   有效期    分类     分类描述
  雪碧      3   甜    2020   酒水饮料   碳酸饮料
  
  重新设计后:
  表1:商品信息表(product)  
  商品ID 商品名称 价格 描述 有效期       
    1     雪碧    3   甜   2020           
  
  表2:分类信息表(product_type)    
  分类ID  分类     分类描述
    1   酒水饮料   碳酸饮料    
      
  表3:中间表 - 做外键关联
  商品ID  分类ID
    1       1
      
  问题:
  1、写出两条创建外键关联的语句
    foreign key(pid) references product(id) on delete cascade on update cascade,
    foreign key(tid) references type(id) on delete cascade on update cascade
  2、查询商品名称和所属类别
     雪碧    酒水饮料
     可乐    酒水饮料
     小浣熊  零食
     select product.name,type.type from product
      inner join middle
      on product.id=middle.pid
      inner join type 
      on middle.tid=type.id;
  
  3、查询所有的酒水饮料的商品
     雪碧   酒水饮料
     可乐   酒水饮料
     select product.name,type.type from product inner join middle on product.id=middle.pid inner join type  on middle.tid=type.id where type.type='酒水饮料';
  ```

- **关联查询**

  ```python
  1、内连接(inner join)
  2、左外连接(left join):以左表为主显示查询结果
  3、右外连接(right join):以右表为主显示查询结果
  select xxx from 表1 inner|left|right join from 表2 on 条件;
  4、问题: 查询商品的名称(name)、价格(price)以及所属分类(type)???
  ```

- **子查询**

  ```python
  把外层命令的查询结果作为内层查询的查询条件,就是一条查询语句中又嵌套了查询语句
  select xxx from 表名 where 字段名<(select x);
  ```

- **索引的优缺点及建立原则**

  ```python
  # 1. 优点
  1、提高检索速度
  2、唯一性索引可保证数据库表中每一行数据的唯一性
  3、使用分组和排序子句进行数据检索时，可以显著减少查询中分组和排序的时间
  
  # 2.缺点
  1、创建索引和维护索引需要耗费时间；
  2、索引需要占用物理空间
  3、当对表进行增、删、改、的时候索引也要动态维护，这样就降低了数据的维护速度
  
  # 3. 建立原则
  1、频繁用来查询的字段上建立索引
  2、需要排序的字段上建立索引
  3、频繁使用条件判断的字段建立索引
  ```

- **常用存储引擎及特点**

  ```python
  1、InnoDB: 外键、事务、行级锁,写操作多
  2、MyISAM: 表级锁,读操作多
  3、MEMORY: 表记录存储在内存,临时表
  ```

- **MySQL数据库的优化**

  ```python
  1、存储引擎优化
     1、读操作多: MyISAM
     2、写操作多: InnoDB
     3、临时表  : MEMORY
  2、索引优化
     经常查询、排序、条件判断的字段建立索引
  3、SQL语句优化 - 避免全表扫描
     导致: * 、in 、not in 、or
     解决: 查询指定字段、union all、between and 
  ```

- **MySQL锁**

  ```python
  1、锁类型分类: 读锁、写锁
     读锁: 别人能读不能写
     写锁: 不能读也不能写
  2、锁粒度分类: 表级锁、行级锁
     表级锁: 锁整张表
     行级锁: 锁对应表记录
  # 自动加锁和释放锁,无须手动操作
  ```

- **MySQL数据库重置密码**

```python
1、sudo -i
2、/etc/init.d/mysql stop
3、cd /etc/mysql/mysql.conf.d
4、vi mysqld.cnf  在 [mysqld]下添加如下语句后保存退出
   skip-grant-tables
5、/etc/init.d/mysql start
6、命令行：mysql
7、切换库：use mysql
8、重置密码：
    update user set authentication_string=password('新密码') where user='root';
9、去掉配置文件中刚添加的 skip-grant-tables
10、重启mysql服务登录 /etc/init.d/mysql restart
```

**mysql数据库改密码**

```python
SET PASSWORD FOR 'root'@'localhost'='123456';
```

## **基础面试题**

- **Python2和Python3的区别**

  ```python
  # 1、编码格式区别
  python2: 默认编码格式是ascii,如果代码中使用中文需加如下声明:
  #!coding=utf-8 或者 #!-*- coding=utf-8 -*-
  python3: 默认编码为utf-8,并且引入了字节串
    
  # 2、函数区别
  1、print
     python2中是关键字,print "hello world"
     python3中是函数,print()
  2、input
     python2中有input()数值和raw_input()字符串
     python3中只有input() - 都是字符串
  3、range
     python2中range得到列表,xrange得到迭代器
     python3中只有range,得到迭代器
      
  # 3、运算修改
  python2中: 3/2=1  3.0/2=1.5
  python3中: 3/2=1.5 3.0/2=1.5
    
  # 4、数据类型
  1、python3中引入字节串
  2、python3: 只有int,长度无上限
     python2: int 和 long(无上限)
  python2中int类型:
  在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1；
  在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1；
  
  # 5、语法变化
  1、异常: python2中异常和异常对象用逗号隔开
     except Exception,e
  2、python3中更加严格的缩进规则,在python2中tab和对应数量空格等同,python3中则不可以
  ```

- **深拷贝和浅拷贝**

  ```python
  # 1、浅拷贝定义及特点
  1、定义: 对另外一个变量的内存地址引用的拷贝，这两个变量指向同一个内存地址的变量值
  2、特点: 
    公用一个值
    这两个变量的内存地址一样
    对其中一个变量值改变,另一个变量的值也会改变
  # 2、深拷贝定义及特点
  1、定义: 一个变量对另外一个变量的值拷贝
  2、特点:
    两个变量的内存地址不同
    两个变量各有自己的值，且互不影响 
    对其任意一个变量的值的改变不会影响另外一个
    
  # 3、python中如何实现？
  浅拷贝: copy.copy()
  深拷贝: copy.deepcopy()
    
  # 简单总结
  1、拷贝使用Python标准库模块 copy 实现
  2、copy.copy()内部拷贝了可变类型当时的引用,而copy.deepcopy()所有元素都拷贝
  ```



**面试题:**

```python
写一个程序,读取文件时,一次读取10行,把读取的内容放到生成器,然后打印出生成器中内容
```














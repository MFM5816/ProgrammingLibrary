## **常用Linux操作系统**

```python
RedHat(红帽)：6.5、7 
CentOS：6.5、7
Ubuntu：16.04、18.04
```

## **远程连接工具-xshell**

```python
# 1、定义
xshell: 安装终端模拟软件
# 2、使用
文件-新建-输入服务器IP地址-输入用户名-输入密码-确认连接
# 3、文件互传
sudo apt-get install lrzsz
Windows -> Linux：rz 
Linux -> Windows: sz filename
```

## **默认已熟练使用的Linux命令**

```python
1、pwd
2、cd    -- cd .. 、cd
3、ls    -- ll
4、mkdir
5、touch
6、tar 
7、cp    -- cp -r
8、mv
```

## **常用命令**

```python
1、ifconfig
  查看IP地址和MAC地址
  Windows中命令为:ipconfig  或者 ipconfig/all
  Ubuntu18.04纯净版不能使用ifconfig命令,需要安装: sudo apt-get install net-tools

2、ping IP/域名 [-c n]
  测试网络连通性,-c指定连接次数

3、nslookup 域名
  解析域名对应的IP地址

4、ls -lh file
   ls -lhd directory
  显示文件权限及详细信息

5、tar -zcvf filename.tar.gz file1 file2 directory3
  将文件|目录打包并压缩
 
6、tar -zxvf filename.tar.gz [-C path]
  解压缩,默认解压到当前路径,-C可指定路径

7、ps -aux
  显示进程命令(包含PID号)  ps -aux | grep 'mysql'

8、kill PID
  杀死某个进程
  eg: ps -aux | grep 'mysql'
      sudo kill PID号
      kill -9 PID号  # -9 表示强制杀死进程

9、chmod 权限 file
  给文件指定或者增加某权限
  -rw-rw-rw- tarena tarena
   前3位: 文件所有者权限
   中3位: 同组其他用户对文件权限
   尾3位: 其他组用户对文件权限
   # 权限分类
   r : 读(4)
   w : 写(2)
   x : 执行(1)
   # 设置权限方法
   chmod 664 xxx.txt # rw-rw-r--
   chmod 666 xxx.txt # rw-rw-rw-
   chmod 644 xxx.txt # rw-r--r--
   # 修改权限方法(user group other all)
   chmod g-x xxx.txt
   chmod o+x xxx.txt
    
10、chown user:group file
  更改属主和属组
  eg: chown root:root file
       
11、find path -name filename
  在某个路径下查找文件
  eg: find /home/tarena/ -name '*.avi'
  # 其他选项
  -type f|d
  -size +1M|-1G|+10K
12、ssh user@IP
  远程连接到服务器
  eg: ssh tarena@172.40.91.138
    
13、scp file user@IP:绝对路径
  本地文件复制到远程
  eg: scp python.tar.gz tarena@172.40.91.138:/home/tarena/
```

## **vi及vim使用**

```python
文本编辑器,vim是vi的升级版
# 使用流程
1、vi filename
初始(不能编辑,浏览模式)  -> 按 a/i/o(可编辑,插入模式) -> 编辑内容 -> 按ESC,然后shift+:(命令行模式) -> 输入wq!(保存并退出)、或q!(不保存直接退出)

# 常用
1、查找
  浏览模式 -> 输入 /  -> 输入查找内容 -> Enter  (n表示下1个,shift+n表示上1个)
2、复制+删除+粘贴+撤销
  yy：复制光标所在行(2yy复制两行内容)
   p：粘贴
  dd：删除(剪切)光标所在行(3dd删除(剪切)3行内容）
   u: 撤销

# 光标的跳转(浏览模式)：
  行首： home
  行尾： end
  全文的首行：gg
  全文的最后一行：G
  全文的12行：12G
```

**练习**		

```python
1、在用户主目录下新建目录(mkdir):  你的名字(比如:MrRight)
   # cd
   # mkdir Mr
2、在目录MrRight中新建文件song.txt(可使用touch命令,或者直接使用vim)
   # cd Mr
   # touch song.txt
3、在song.txt中写入一首你最喜欢的诗,保存并退出
4、把/etc/passwd文件拷贝到MrRight目录一份(cp命令)
   # sudo cp /etc/passwd ~/Mr
5、在 /home/tarena/MrRight/passwd 文件中筛选 tarena 用户的信息(grep命令)
   # cat ~/Mr/passwd | grep "tarena"
6、查看passwd文件的权限,并将其权限修改为所有用户都可读可写但是不可执行(chmod命令)
   # ls -l passwd
   # chmod 666 passwd
7、将 MrRight 目录打包压缩,MrRight-你的名字.tar.gz
   # tar -zcvf Mr.tar.gz Mr
8、将此压缩包远程复制到 主讲机 | 同桌 计算机的电脑上
   IP: 172.40.91.124
   位置: /home/tarena/homework/
   # scp Mr.tar.gz tarena@172.40.91.124:/home/tarena/homework/
```

## **Linux命令-Go on**

```python
# 14、管道操作  | ：  
  将前面命令的输出，传递给后面命令，作为后面命令的参数
  查看 /etc/passwd 文件的 第6-10行？ - cat、head、tail
  # head 和 tail的用法
  tail -5 /etc/passwd
  head -10 /etc/passwd
  #答案: cat /etc/passwd | head -10 | tail -5
  
# 15、统计目录总共的占用空间的大小
  du -sh 目录

# 16、查看磁盘使用情况(根分区使用情况)
  df -h

# 17、常见通配符使用
  *：任意多个字符
  ？：单个字符
  eg1: rm -rf /home/tarena/test/*
  eg2: ls *.jpg

# 18、重定向: 将前面命令的输出，写入到文本文件中
  >：覆盖重定向
  >>：追加重定向
    
# 19、创建用户(会创建同名组)
  sudo useradd username

# 20、设置密码
  sudo passwd 用户名

# 21、删除用户
  sudo userdel 用户名
  -r：递归删除，删除用户的家目录以及用户的邮件文件
```

## **Linux-Go on**

```python
# 22、统计文件的行数
  wc -l
  eg1: wc -l /etc/passwd
	
# 23、对文件中内容进行排序
  sort 文件名
  
# 24、去除重复行,并统计每行出现的次数(相邻行)
  uniq -c
  sort 文件名 | uniq -c
```

## **周期性计划任务**

```python
# 1、进入周期性计划任务
crontab -e (首次进入按2 - 找vim)

# 用法: 
* * * * *  python3 /home/tarena/spider.py

# 设置周期性计划任务
* * * * *  : 五个*号代表  分 时 日 月 周
分 ：0-59
时 ：0-23
日 ：1-31
月 ：1-12
周 ：0-6

# 开始设置 : 
1、'*' 代表所有可能值
2、',' 指定多个时间点
3、'/' 指定时间间隔频率
4、'-' 指定一个时间段

# 示例
1、每月的1日和5日两天: * * 1,5 * * 
2、每10分钟: */10 * * * * 
3、0点-6点每小时执行: 0 0-6/1 * * *
4、每分钟执行: * * * * *

# 练习
1、每小时的第3分钟和第15分钟执行
  3,15 * * * *
2、每周六、周日的0点执行一个 01.py 文件
  0 0 * * 6,0
6、每天18:00到23:00之间每小时执行 01.py 文件
  0 18-23/1 * * *
```

## **文本处理工具 - awk**

**语法格式**

```python
awk 选项 '动作' 文件列表
```

**常用方式**

```python
Linux命令  |   awk  选项  '动作'
```

**使用方法**

```python
# 示例
awk '{print "abc"}' ip.txt
# 思考: 这个会输出什么？
df -h | awk '{print $1}'

# -F：指定分隔符
awk -F ":" '{print $2}'  # 显示 : 分隔后的第2列

# 示例1: 输出当前Linux操作系统的所有用户
# 练习:
输出本机的IP地址

```

**练习**

```python
# nginx的访问日志目录 ： /var/log/nginx/access.log
问题1: 把访问过自己的IP地址输出
       # awk '{print $1}' access.log
问题2: 统计有多少个IP访问过我
       # awk '{print $1}' access.log | sort | uniq | wc -l
问题3: 统计每个IP地址的访问次数,输出前10个访问量最大的用户IP
       # awk '{print $1}' access.log | sort | uniq -c | sort  -rn -k 1 | head -10
```

**grep命令之正则表达式**

```python
# 正则表达式元字符集 - 使用grep命令
^    :   以 ... 开头
$    :   以 ... 结尾
.    :   任何1个字符
*    :   任意0到多个字符

# 正则表达式扩展字符集 - 使用 egrep 命令
+    :   1次或多次
{n} :   出现n次
()  ：  分组

[a-z]  :  所有小写字母
[A-Z]  :  所有大写字母
[a-Z]  :  所有字母
[0-9]  : 所有数字
[a-Z0-9]  : 所有的字母和数字
```

**应用场景**

```python
# Mac地址正则匹配
([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}
ifconfig | egrep "([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}" | awk '{print $2}'
```

## **常见服务的端口号**

```python
# 需要记住
MySQL - 3306
MongoDB - 27017
Redis - 6379
redis-sentinel - 26379
SSH - 22
HTTP - 80 
NGINX - 80
HTTPS - 443
TELNET - 23
FTP - 21
```


















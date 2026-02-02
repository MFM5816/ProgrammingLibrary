## PHP的常见语法
**PHP代码执行方式**：

- 在服务器端执行，然后返回给用户结果。如果直接使用浏览器打开，就会解析为文本。
    
- 意思是说，需要浏览器通过 http请求，才能够执行php页面。

### 注释

php 注释的写法跟 js 一致。

```
<?php
	//这是单行注释
	/*
		这是多行注释
	*/
?>
```

### 变量

- 变量以`$`符号开头，其后是变量的名称。大小写敏感。
    
- 变量名称必须以字母或下划线开头。
    

举例：

```
	$a1;
	$_abc;
```
### 数据类型

PHP支持的数据类型包括：

- 字符串
    
- 整数
    
- 浮点数
    
- 布尔
    
- 数组
    
- 对象
    
- NULLL
    

定义字符串时需要注意：

- 单引号`` ：内部的内容只是作为字符串。
    
- 双引号"" ：如果内部是PHP的变量,那么会将该变量的值解析。如果内部是html代码，也会解析成html。
    

说白了，单引号里的内容，一定是字符串。双引号里的内容，可能会进行解析。

```
	echo "<input type=`button` value=`smyhvae`>";
```

上面这个语句，就被会解析成按钮。

```
	// 字符串
	$str = '123';

	// 字符串拼接
	$str2 = '123'.'哈哈哈';


	// 整数
	$numA = 1; //正数
	$numB = -2;//负数

	// 浮点数
	$x = 1.1;

	// 布尔
	$a = true;
	$b = false;

	// 普通数组：数组中可以放 数字、字符串、布尔值等，不限制类型。
	$arr1 = array('123', 123);
	echo $arr1[0];

	// 关系型数组：类似于json格式
	$arr2 = $array(`name`=>`smyhvae`, `age`=>`26`);
	echo $arr2[`name`];  //获取时，通过  key 来获取

```

上方代码中注意，php 中字符串拼接的方式是 `.`。要注意哦。
### 运算符

PHP 中的运算符跟 JavaScript 中的基本一致，用法也基本一致。

- 算数运算符：`+`、`-`、`/`、`*`、`%`
    
- 赋值运算符：`x = y`、`x += y`,`x -= y`等。
    

举例：

```
<?php
	$x = 10;
	$y = 6;

	echo ($x + $y); // 输出 16
	echo ($x - $y); // 输出 4
	echo ($x * $y); // 输出 60
	echo ($x / $y); // 输出 1.6666666666667
	echo ($x % $y); // 输出 4
?>
```
### 函数的定义

语法格式：

```

	function functionName() {
	  //这里写代码
	}
```

（1）有参数、无返回值的函数：

```
	function sayName($name){
	    echo $name.'你好哦';
	}
	// 调用
	sayName('smyhvae');
```

（2）有参数、参数有默认值的函数：

```
	function sayFood($food='西兰花'){
	    echo $food.'好吃';
	}
	// 调用
	sayFood('西葫芦');// 如果传入参数,就使用传入的参数
	sayFood();// 如果不传入参数,直接使用默认值
```

（3）有参数、有返回值的函数：

```
	function sum($a,$b){
		return $a+$b
	}
	sum(1,2);// 返回值为1+2 = 3
```
### 类和对象

PHP中允许使用对象这种**自定义**的数据类型。必须先声明，实例化之后才能够使用。

定义最基础的类：

```
	class Fox{

	        public $name = 'itcast';
	        public $age = 10;
	}

	$fox = new $fox;
	// 对象属性取值
	$name = $fox->name;
	// 对象属性赋值
	$fox->name = '小狐狸';
```

带构造函数的类：

```
	class fox{
	    // 私有属性,外部无法访问
	    var $name = '小狐狸';
	    // 定义方法 用来获取属性
	    function Name(){
	    return $this->name;
	    }
	    // 构造函数,可以传入参数
	    function fox($name){
	    $this->name = $name
	    }
	}

    // 定义了构造函数 需要使用构造函数初始化对象
    $fox = new fox('小狐狸');
    // 调用对象方法,获取对象名
    $foxName = $fox->Name();
```

### 内容输出

- `echo`：输出字符串。
    
- `print_r()`：输出复杂数据类型。比如数组、对象。
    
- `var_dump()`：输出详细信息。
    

```
	$arr =array(1,2,'123');

	echo'123';
	//结果：123


	print_r($arr);
	//结果：Array ( [0] => 1 [1] => 2 [2] => 123 )

	var_dump($arr);
	/* 结果：
	array
	  0 => int 1
	  1 => int 2
	  2 => string '123' (length=3)
	*/
```
### 循环语句

这里只列举了`foreach`、`for`循环。

for 循环：

```
	for ($x=0; $x<=10; $x++) {
	  echo "数字是：$x <br>";
	}

```

foreach 循环：

```
	$colors = array("red","green","blue","yellow");

	foreach ($colors as $value) {
	  echo "$value <br>";
	}
```

上方代码中，参数一：循环的对象。参数二：将对象的值挨个取出，直到最后。

如果循环的是对象，输出的是对象的属性的值。
## php中的header()函数

浏览器访问http服务器，接收到响应时，会根据响应**报文头**的内容进行一些具体的操作。在php中，我们可以根据 **header** 来设置这些内容。

**header()函数的作用**：用来向客户端(浏览器)发送报头。直接写在php代码的第一行就行。

下面列举几个常见的 header函数。

（1）设置编码格式：

```
	header('content-type:text/html; charset= utf-8');
```

例如：

```
<?php
	header('content-type:text/html; charset= utf-8');
	echo "我的第一段 PHP 脚本";
?>
```

（2）设置页面跳转：

```
	header('location:http://www.baidu.com');
```

设置页面刷新的间隔：

```
	header('refresh:3; url=http://www.xiaomi.com');
```
## php中的 get 请求和 post 请求
### get 请求

可以通过`$_GET`对象来获取。

**举例**：下面是一个简单的表单代码，通过 get 请求将数据提交到01.php。

（1）index.html:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<!-- 通过 get 请求，将表单提交到 php 页面中 -->
<form action="01.php" method="get">
    <label for="">姓名：
        <input type="text" name="userName"></label>
    <br/>
    <label for="">邮箱：
        <input type="text" name="userEmail"></label>
    <br/>
    <input type="submit" name="">
</form>

</body>
</html>
```

（2）01.php：

```
<?php
	header('content-type:text/html; charset= utf-8');
    echo "<h1>php 的get 请求演示</h1>";
    echo '用户名：'.$_GET['userName'];
    echo '<br/>';
    echo '邮箱：'.$_GET['userEmail'];
 ?>
```

上方代码可以看出，`$_GET`是关系型数组，可以通过 **$_GET[`key`]**获取值。这里的 key 是 form 标签中表单元素的 name 属性的值。

### post 请求

可以通过`$_POST`对象来获取。

**举例**：下面是一个简单的表单代码，通过 post 请求将数据提交到02.php。

（1）index.html：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<!-- 通过 post 请求，将表单提交到 php 页面中 -->
<form action="02.php" method="post" >
  <label for="">姓名：
      <input type="text" name= "userName"></label>
      <br/>
  <label for="">邮箱：
      <input type="text" name= "userEmail"></label>
      <br/>
      <input type="submit" name="">
</form>

</body>
</html>
```

（2）02.php：

```
<?php
	header('content-type:text/html; charset= utf-8');
    echo "<h1>php 的 post 请求演示</h1>";
    echo '用户名：'.$_POST['userName'];
    echo '<br/>';
    echo '邮箱：'.$_POST['userEmail'];
 ?>
```

上方代码可以看出，`$_POST`是关系型数组，可以通过 **$_POST[`key`]获取值。这里的 key 是 form 标签中表单元素的 name 属性的值。**

实际开发中，可能不会单独写一个php文件，常见的做法是：在 html 文件中嵌入 php 的代码。

比如说，原本 html 中有个 li 标签是存放用户名的：

```
	<li>smyhvae</li>
```

嵌入 php后，用户名就变成了动态获取的：

```
	<li><?php
		echo $_POST[`userName`]
		?></li>
```
## php 中文件相关的操作
### 文件上传 `$_FILES`

上传文件时，需要在html代码中进行如下设置：

（1）在html表单中，设置`enctype="multipart/form-data"`。该值是必须的。

（2）只能用 post 方式获取。

代码如下：

（1）index.html:

```
  <form action="03-fileUpdate.php" method="post" enctype="multipart/form-data">
	  <label for="">照片:
	      <input type="file" name = "picture" multiple=""></label>
	  <br/>
	  <input type="submit" name="">
  </form>

```

（2）在 php 文件中打印 file 的具体内容：

```
<?php
  sleep(5);// 让服务器休息一会
  print_r($_FILES);  //打印 file 的具体内容
?>
```

现象可以看出：

- 点击提交后，服务器没有立即出现反应,而是休息了一会`sleep(5)`。
    
- 在`wamp/tmp`目录下面出现了一个`.tmp`文件。
    
- .tmp文件一会就被自动删除了。
    
- 服务器返回的内容中有文件的名字`[name] => computer.png`，以及上传文件保存的位置`D:\wamp\tmp\php3D70.tmp`。服务器返回的内容如下：
    

```
	Array ( [upFile] => Array ( [name] => yangyang.jpg [type] => image/jpeg [tmp_name] => D:\wamp\tmp\phpCC56.tmp [error] => 0 [size] => 18145 ) )
```

### 文件保存

我们尝试一下，把上面的例子中的`临时目录`下面的文件保存起来。这里需要用到 php 里的 `move_uploaded_file()`函数。[#(opens new window)](http://www.w3school.com.cn/php/func_filesystem_move_uploaded_file.asp)

格式如下：

```
	move_uploaded_file($_FILES['photo']['tmp_name'], './images/test.jpg');
```

参数解释：参数一：移动的文件。参数二：目标路径。

（1）index.html：（这部分的代码保持不变）

```
	<form action="03.fileUpdate.php" method="post" enctype="multipart/form-data">
      <label for="">照片:
          <input type="file" name = "picture" multiple=""></label>
      <br/>
      <input type="submit" name="">
  	</form>
```
## PHP 中：json 字符串 <--> js 对象
- **json_decode()**方法：将`json`字符串转化为变量。
    
- **json_encode()**方法：将变量转化为`json`字符串。
    

代码举例：

```
<?php
    header("Content-Type:text/html;charset=utf-8");
    // json字符串
    $jsonStr = '{"name":"itcast","age":54,"skill":"歌神"}';
    // 字符串转化为 php对象
      print_r(json_decode($jsonStr));

      echo "<br>";
      // php数组
      $arrayName = array('name' =>'littleFox' ,'age' => 13 );
      // php对象 转化为 json字符串
      print_r(json_encode($arrayName));
 ?>
```
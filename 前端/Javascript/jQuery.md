## jQuery 的介绍
### 引入 jQuery 的原因

在用 js 写代码时，会遇到一些问题：

- window.onload 事件有事件覆盖的问题，因此只能写一个事件。
    
- 代码容错性差。
    
- 浏览器兼容性问题。
    
- 书写很繁琐，代码量多。
    
- 代码很乱，各个页面到处都是。
    
- 动画效果很难实现。
    

![[引入 jQuery 的原因.png]]
### 什么是 jQuery

jQuery 是 js 的一个库，封装了我们开发过程中常用的一些功能，方便我们调用，提高开发效率。

js库是把我们常用的功能放到一个单独的文件中，我们用的时候，直接引用到页面里即可。

以下是jQuery的相关信息：

- 官网：[http://jquery.com/(opens new window)](http://jquery.com/)
    
- 官网API文档：[http://api.jquery.com/(opens new window)](http://api.jquery.com/)
    
- 中文汉化API文档：[http://www.css88.com/jqapi-1.9/(opens new window)](http://www.css88.com/jqapi-1.9/)
    

### [#](https://web.qianguyihao.com/04-JavaScript%E5%9F%BA%E7%A1%80/47-jQuery%E7%9A%84%E4%BB%8B%E7%BB%8D%E5%92%8C%E9%80%89%E6%8B%A9%E5%99%A8.html#%E5%AD%A6%E4%B9%A0jquery-%E4%B8%BB%E8%A6%81%E6%98%AF%E5%AD%A6%E4%BB%80%E4%B9%88)学习jQuery，主要是学什么

初期，主要学习如何使用jQuery操作DOM，其实就是学习jQuery封装好的那些API。

这些API的共同特点是：几乎全都是方法。所以，在使用jQuery的API时，都是方法调用，也就是说要加小括号()，小括号里面是相应的参数，参数不同，功能不同。

### jQuery初体验

现在用原生 js 来写下面这一段代码：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            height: 100px;
            background-color: pink;
            margin: 10px;
            display: none;
        }
    </style>

    <script>
        //原生js
        window.onload = function () {
            var btn = document.getElementsByTagName("button")[0];
            var divArr = document.getElementsByTagName("div");

            btn.onclick = function () {
                for (var i = 0; i < divArr.length; i++) {
                    divArr[i].style.display = "block";
                    divArr[i].innerHTML = "生命壹号";
                }
            }
        }
    </script>
</head>
<body>

<button>显示五个div盒子和设置内容</button>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>

</body>
</html>
```

如果用 jQuery 来写，保持其他的代码不变，`<script>`部分的代码修改为：（需要提前引入 ）

```
    <script src="jquery-1.11.1.js"></script>
    <script>

        //jquery版
        $(document).ready(function () {
            //获取元素
            var jQbtn = $("button");//根据标签名获取元素
            var jQdiv = $("div");//根据标签名获取元素
            //绑定事件
            jQbtn.click(function () {
                jQdiv.show(1000);//显示盒子。
                jQdiv.html("tomorrow！");//设置内容
                //上面的两行可以写成链式编程：jQdiv.show(3000).html(1111);

            });//事件是通过方法绑定的。

        });
    </script>
```

### jQuery 的两大特点

（1）**链式编程**：比如`.show()`和`.html()`可以连写成`.show().html()`。

链式编程原理：return this。

通常情况下，只有设置操作才能把链式编程延续下去。因为获取操作的时候，会返回获取到的相应的值，无法返回 this。

（2）**隐式迭代**：隐式 对应的是 显式。隐式迭代的意思是：在方法的内部会为匹配到的所有元素进行循环遍历，执行相应的方法；而不用我们再进行循环，简化我们的操作，方便我们调用。

如果获取的是多元素的值，大部分情况下返回的是第一个元素的值。
## jQuery 的使用

### 使用 jQuery 的基本步骤

（1）引包

（2）入口函数

（3）功能实现代码（事件处理）

如下图所示：
![[使用 jQuery 的基本步骤.png]]
主要，导包的代码一定要放在js代码的最上面。
## jQuery 的入口函数和 `$` 符号

### 入口函数（重要）

原生 js 的入口函数指的是：`window.onload = function() {};` 如下：

```
        //原生 js 的入口函数。页面上所有内容加载完毕，才执行。
        //不仅要等文本加载完毕，而且要等图片也要加载完毕，才执行函数。
       window.onload = function () {
           alert(1);
       }
```

而 jQuery的入口函数，有以下几种写法：

写法一：

```
       //1.文档加载完毕，图片不加载的时候，就可以执行这个函数。
       $(document).ready(function () {
           alert(1);
       })
```

写法二：（写法一的简洁版）

```
       //2.文档加载完毕，图片不加载的时候，就可以执行这个函数。
       $(function () {
           alert(1);
       });
```

写法三：

```
       //3.文档加载完毕，图片也加载完毕的时候，在执行这个函数。
       $(window).ready(function () {
           alert(1);
       })
```

**jQuery入口函数与js入口函数的区别**：

区别一：书写个数不同：

- Js 的入口函数只能出现一次，出现多次会存在事件覆盖的问题。
    
- jQuery 的入口函数，可以出现任意多次，并不存在事件覆盖问题。
    

区别二：执行时机不同：

- Js的入口函数是在**所有的文件资源加载**完成后，才执行。这些**文件资源**包括：页面文档、外部的js文件、外部的css文件、图片等。
    
- jQuery的入口函数，是在文档加载完成后，就执行。文档加载完成指的是：DOM树加载完成后，就可以操作DOM了，不用等到所有的**外部资源**都加载完成。
    

文档加载的顺序：从上往下，边解析边执行。

### jQuery的`$`符号

jQuery 使用 `$` 符号原因：书写简洁、相对于其他字符与众不同、容易被记住。

jQuery占用了我们两个变量：`$` 和 jQuery。当我们在代码中打印它们俩的时候：

```
    <script src="jquery-1.11.1.js"></script>
    <script>

        console.log($);
        console.log(jQuery);
        console.log($===jQuery);


    </script>
```
从打印结果可以看出，$ 代表的就是 jQuery。

那怎么理解jQuery里面的 `$` 符号呢？

**`$` 实际上表示的是一个函数名** 如下：

```
	$(); // 调用上面我们自定义的函数$

	$(document）.ready(function(){}); // 调用入口函数

	$(function(){}); // 调用入口函数

	$(“#btnShow”) // 获取id属性为btnShow的元素

	$(“div”) // 获取所有的div标签元素

```

如上方所示，jQuery 里面的 `$` 函数，根据传入参数的不同，进行不同的调用，实现不同的功能。返回的是jQuery对象。

jQuery这个js库，除了`$` 之外，还提供了另外一个函数：jQuery。jQuery函数跟 `$` 函数的关系：`jQuery === $`。

## js中的DOM对象 和 jQuery对象 比较（重点，难点）

### 二者的区别

通过 jQuery 获取的元素是一个**数组**，数组中包含着原生JS中的DOM对象。举例：

针对下面这样一个div结构：

```
<div></div>
<div class="box"></div>
<div id="box"></div>
<div class="box"></div>
<div></div>
```

通过原生 js 获取这些元素节点的方式是：

```
    var myBox = document.getElementById("box");           //通过 id 获取单个元素
    var boxArr = document.getElementsByClassName("box");  //通过 class 获取的是数组
    var divArr = document.getElementsByTagName("div");    //通过标签获取的是数组
```

通过 jQuery 获取这些元素节点的方式是：（获取的都是数组）

```
    //获取的是数组，里面包含着原生 JS 中的DOM对象。
    var jqBox1 = $("#box");
    var jqBox2 = $(".box");
    var jqBox3 = $("div");
```
### 二者的相互转换

**1、 DOM 对象 转为 jQuery对象**：

```
	$(js对象);
```

举例：（拿上一段的代码举例）

```
	//转换。
	jqBox1 = $(myBox);
	jqBox2 = $(boxArr);
	jqBox3 = $(divArr);
```

DOM 对象转换成了 jquery 对象之后，上面的功能可以直接调用。

**2、jQuery对象 转为 DOM 对象**：

```
	jquery对象[index];      //方式1（推荐）

	jquery对象.get(index);  //方式2
```

jQuery对象转换成了 DOM 对象之后，可以直接调用 DOM 提供的一些功能。如：

```
    //jquery对象转换成 DOM 对象之后
    jqBox3[0].style.backgroundColor = "black";
    jqBox3.get(4).style.backgroundColor = "pink";
```

**总结**：如果想要用哪种方式设置属性或方法，必须转换成该类型。

### [#](https://web.qianguyihao.com/04-JavaScript%E5%9F%BA%E7%A1%80/47-jQuery%E7%9A%84%E4%BB%8B%E7%BB%8D%E5%92%8C%E9%80%89%E6%8B%A9%E5%99%A8.html#%E4%B8%BE%E4%BE%8B-%E9%9A%94%E8%A1%8C%E5%8F%98%E8%89%B2)举例：隔行变色

代码如下：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        //入口函数
        jQuery(function () {
            var jqLi = $("li");
            for (var i = 0; i < jqLi.length; i++) {
                if (i % 2 === 0) {
                    //jquery对象，转换成了js对象
                    jqLi[i].style.backgroundColor = "pink";
                } else {
                    jqLi[i].style.backgroundColor = "yellow";
                }
            }
        });
    </script>
</head>
<body>
<ul>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
</ul>
</body>
</html>
```
## jQuery 选择器

我们以前在CSS中学习的选择器有：
![[CSS中学习的选择器.png]]
### 1、jQuery 的基本选择器
![[jQuery 的基本选择器.png]]
![[jQuery 的基本选择器2.png]]
```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        //入口函数
        jQuery(document).ready(function () {

            //三种方式获取jquery对象
            var jqBox1 = $("#box");
            var jqBox2 = $(".box");
            var jqBox3 = $("div");

            //操作标签选择器
            jqBox3.css("width", 100);
            jqBox3.css("height", 100);
            jqBox3.css("margin", 10);
            jqBox3.css("background", "pink");

            //操作类选择器(隐式迭代，不用一个一个设置)
            jqBox2.css("background", "red");

            //操作id选择器
            jqBox1.css("background", "yellow");

        });
    </script>
</head>
<body>

<div></div>
<div class="box"></div>
<div id="box"></div>
<div class="box"></div>
<div></div>

</body>
</html>
```
### 2、层级选择器
![[层级选择器.png]]
![[层级选择器2.png]]
```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //获取ul中的li设置为粉色
            //后代：儿孙重孙曾孙玄孙....
            var jqLi = $("ul li");
            jqLi.css("margin", 5);
            jqLi.css("background", "pink");

            //子代：亲儿子
            var jqOtherLi = $("ul>li");
            jqOtherLi.css("background", "red");
        });
    </script>
</head>
<body>
<ul>
    <li>111</li>
    <li>222</li>
    <li>333</li>
    <ol>
        <li>aaa</li>
        <li>bbb</li>
        <li>ccc</li>
    </ol>
</ul>
</body>
</html>
```
### 3、基本过滤选择器
![[过滤选择器.png]]
![[过滤选择器2.png]]
```
 <script src="jquery-1.11.1.js"></script>
    <script>
        $(document).ready(function () {

            // :odd
            $("li:odd").css("background", "red");

            // :even
            $("li:even").css("background", "green");

            // :eq(index)
            $("ul li:eq(3)").css("font-size", "30px");  //设置第四个li的字体

            // :lt(index)
            $("li:lt(6)").css("font-size", "30px");

            // :gt(index)
            $(".ulList1 li:gt(7)").css("font-size", "40px");

            // :first
            $(".ulList li:first").css("font-size", "40px");

            // :last
            $("li:last").css("font-size", "40px");
        });
    </script>
```

### 4、属性选择器
![[属性选择器.png]]
### 5、筛选选择器
![[筛选选择器.png]]
```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(function () {
            var jqul = $("ul");

            //find(selector); 从jquery对象的后代中查找
            //必须制定参数，如果不指定获取不到元素。length === 0
            jqul.find("li").css("background", "pink");
            console.log(jqul.find());

            //chidlren(selector); 从jquery对象的子代中查找
            //不写参数代表获取所有子元素。
            jqul.children("li").css("background", "green");

            //eq(索引值); 从jquery对象的子代中查找该索引值的元素
            //要写该数组中的第几个。
            jqul.children().eq(0).css("background", "red");

            //next(); 该元素的下一个兄弟元素
            jqul.children().eq(0).next().css("background", "yellow");

            //siblings(selector); 该元素的所有兄弟元素
            jqul.children().eq(0).next().siblings().css("border", "1px solid blue");

            //parent(); 该元素的父元素（和定位没有关系）
            console.log(jqul.children().eq(0).parent());
        });
    </script>
</head>
<body>

<ul>
    <li>生命壹号，永不止步</li>
    <li class="box">生命壹号，永不止步</li>
    <span>生命壹号，永不止步</span>
    <li class="box">生命壹号，永不止步</li>
    <i>生命壹号，永不止步</i>
    <li>生命壹号，永不止步</li>
    <a id="box" href="#">生命壹号，永不止步</a>
    <ol>
        <li>我是ol中的li</li>
        <li>我是ol中的li</li>
        <li>我是ol中的li</li>
        <li>我是ol中的li</li>
    </ol>
</ul>

</body>
</html>
```


### 举例1：鼠标悬停时，弹出下拉菜单【重要】

完整版代码：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        ul {
            list-style: none;
        }

        .wrap {
            width: 330px;
            height: 30px;
            margin: 100px auto 0;
            padding-left: 10px;
            background-color: pink;
        }

        .wrap li {
            background-color: yellowgreen;
        }

        .wrap > ul > li {
            float: left;
            margin-right: 10px;
            position: relative;
        }

        .wrap a {
            display: block;
            height: 30px;
            width: 100px;
            text-decoration: none;
            color: #000;
            line-height: 30px;
            text-align: center;
        }

        .wrap li ul {
            position: absolute;
            top: 30px;
            display: none;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        //入口函数
        $(document).ready(function () {
            //需求：鼠标放入一级li中，让他里面的ul显示。移开隐藏。
            var jqli = $(".wrap>ul>li");

            //绑定事件
            jqli.mouseenter(function () {
                //这个位置用到了this.
                // console.log(this);  //打印结果是js中的dom对象。注意：jquery对象绑定的事件中，this指js中的dom对象。【重要】

                //让this中的ul显示出来。
//                原生 js 的做法是：this.children[1].style.display = "block";
                //把js的dom对象包装为jquery对象，然后用jquery方法操作
                $(this).children("ul").show();
            });

            //绑定事件：鼠标移开时，隐藏下拉菜单
            jqli.mouseleave(function () {
                $(this).children("ul").hide();
            });
        });
    </script>

</head>
<body>
<div class="wrap">
    <ul>
        <li>
            <a href="javascript:void(0);">一级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单1</a></li>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">一级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单1</a></li>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">一级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单1</a></li>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
            </ul>
        </li>
    </ul>
</div>
</body>
</html>
```
**this的用法：**

上方代码中，核心的一行代码是：

```
	$(this).children("ul").show();

	$(this).children("ul").hide();
```

如果我把这行代码中的this直接写成 DOM对象：

```
	jqli.children("ul").show();

	jqli.children("ul").hide();
```
### 举例2：鼠标悬停时变色

完整版代码如下：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {

            //需求；隔行变色；鼠标悬停时，还要变色。
            var jqli1 = $("li:odd");
            var jqli2 = $("li:even");
            jqli1.css("background", "#cccccc");
            jqli2.css("background", "white");

            //鼠标悬停时变色
            var color = "";
            $("li").mouseenter(function () {
                color = $(this).css("background");  //先把之前的颜色保存下来，鼠标离开时还原
                $(this).css("background", "green");
            });
            //鼠标离开时，恢复为原来的颜色
            $("li").mouseleave(function () {
                $(this).css("background", color);
            });
        });
    </script>
</head>
<body>

<ul>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
    <li>生命壹号，永不止步</li>
</ul>

</body>
</html>
```
### 举例3：突出显示

要求：鼠标悬停时，突出显示这个li，让其他的li都半透明。

用 jQuery的选择起来实现，会发现非常方便。

完整版代码如下：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        ul {
            list-style: none;
        }

        body {
            background: #000;
        }

        .wrap {
            margin: 100px auto 0;
            width: 630px;
            height: 394px;
            padding: 10px 0 0 10px;
            background: #000;
            overflow: hidden;
            border: 1px solid #fff;
        }

        .wrap li {
            float: left;
            margin: 0 10px 10px 0;

        }

        .wrap img {
            display: block;
            border: 0;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(window).ready(function () {
            //需求：鼠标放入li中，其他的li半透明，当前盒子的opacity值为1
            $(".wrap").find("li").mouseenter(function () {
                //链式编程
                $(this).css("opacity", 1).siblings("li").css("opacity", 0.4);
            });

            //离开wrap的时候所有的li的全部opacity值为1；
            $(".wrap").mouseleave(function () {
                $(this).children().children("li").css("opacity", 1);
//                $(".wrap li").css("opacity",1);
            });
        });
    </script>
</head>
<body>
<div class="wrap">
    <ul>
        <li><a href="#"><img src="images/01.jpg" alt=""/></a></li>
        <li><a href="#"><img src="images/02.jpg" alt=""/></a></li>
        <li><a href="#"><img src="images/03.jpg" alt=""/></a></li>
        <li><a href="#"><img src="images/04.jpg" alt=""/></a></li>
        <li><a href="#"><img src="images/05.jpg" alt=""/></a></li>
        <li><a href="#"><img src="images/06.jpg" alt=""/></a></li>
    </ul>
</div>
</body>
</html>
```
### 举例4：手风琴效果

完整版代码：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {padding: 0;margin: 0;}
        ul { list-style-type: none;}

        .parentWrap {
            width: 200px;
            text-align:center;

        }

        .menuGroup {
            border:1px solid #999;
            background-color:#e0ecff;
        }

        .groupTitle {
            display:block;
            height:20px;
            line-height:20px;
            font-size: 16px;
            border-bottom:1px solid #ccc;
            cursor:pointer;
        }

        .menuGroup > div {
            height: 200px;
            background-color:#fff;
            display:none;
        }

    </style>
    <script src="jquery-1.11.1.min.js"></script>
    <script>
        $(function () {
            //需求：鼠标点击span，让他下面的div显示出来。让其他的div隐藏。
            $(".parentWrap span").click(function () {
//                $(this).next().show();
//                //让其他的隐藏
//                //点击的span的父亲li，的所有的兄弟元素li，的孩子元素div全部隐藏。
//                $(this).parent("li").siblings("li").children("div").hide();
                //连式编程
                $(this).next().show().parent("li").siblings("li").find("div").hide();
            });
        })
    </script>
</head>
<body>
<ul class="parentWrap">
    <li class="menuGroup">
        <span class="groupTitle">标题1</span>
        <div>我是弹出来的div1</div>
    </li>
    <li class="menuGroup">
        <span class="groupTitle">标题2</span>
        <div>我是弹出来的div2</div>
    </li>
    <li class="menuGroup">
        <span class="groupTitle">标题3</span>
        <div>我是弹出来的div3</div>
    </li>
    <li class="menuGroup">
        <span class="groupTitle">标题4</span>
        <div>我是弹出来的div4</div>
    </li>
</ul>
</body>
</html>
```
### 举例5：淘宝精品服饰广告

完整版代码：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
            font-size: 12px;
        }

        ul {
            list-style: none;
        }

        a {
            text-decoration: none;
        }

        .wrapper {
            width: 298px;
            height: 248px;
            margin: 100px auto 0;
            border: 1px solid pink;
            overflow: hidden;
        }

        #left, #center, #right {
            float: left;
        }

        #left li, #right li {
            background: url(images/lili.jpg) repeat-x;
        }

        #left li a, #right li a {
            display: block;
            width: 48px;
            height: 27px;
            border-bottom: 1px solid pink;
            line-height: 27px;
            text-align: center;
            color: black;
        }

        #left li a:hover, #right li a:hover {
            background-image: url(images/abg.gif);
        }

        #center {
            border-left: 1px solid pink;
            border-right: 1px solid pink;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(function () {
            //需求：鼠标放入两侧的li中，让中间的ul中对应索引值的li显示出来，其他的隐藏。（右侧的li要+9）
            //左侧先绑。获取绑mouseenter
            $("#left li").mouseenter(function () {
                //显示对应索引值的中间的li
                //alert($(this).index());  获取索引值
                $("#center li").eq($(this).index()).show().siblings("li").hide();
            });

            //右侧
            $("#right li").mouseenter(function () {
                //显示对应索引值的中间的li
                //alert($(this).index());  获取索引值
                $("#center li:eq(" + ($(this).index() + 9) + ")").show().siblings("li").hide();
            });
        });
    </script>
</head>
<body>
<div class="wrapper">

    <ul id="left">
        <li><a href="#">女靴</a></li>
        <li><a href="#">雪地靴</a></li>
        <li><a href="#">冬裙</a></li>
        <li><a href="#">呢大衣</a></li>
        <li><a href="#">毛衣</a></li>
        <li><a href="#">棉服</a></li>
        <li><a href="#">女裤</a></li>
        <li><a href="#">羽绒服</a></li>
        <li><a href="#">牛仔裤</a></li>
    </ul>
    <ul id="center">
        <li><a href="#"><img src="images/女靴.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/雪地靴.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/冬裙.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/呢大衣.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/毛衣.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/棉服.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/女裤.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/羽绒服.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/牛仔裤.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/女包.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/男包.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/登山鞋.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/皮带.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/围巾.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/皮衣.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/男毛衣.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/男棉服.jpg" width="200" height="250"/></a></li>
        <li><a href="#"><img src="images/男靴.jpg" width="200" height="250"/></a></li>
    </ul>
    <ul id="right">
        <li><a href="#">女包</a></li>
        <li><a href="#">男包</a></li>
        <li><a href="#">登山鞋</a></li>
        <li><a href="#">皮带</a></li>
        <li><a href="#">围巾</a></li>
        <li><a href="#">皮衣</a></li>
        <li><a href="#">男毛衣</a></li>
        <li><a href="#">男棉服</a></li>
        <li><a href="#">男靴</a></li>
    </ul>
</div>
</body>
</html>
```
## jQuery动画

### 显示动画

方式一：

```
	$("div").show();
```

解释：无参数，表示让指定的元素直接显示出来。其实这个方法的底层就是通过`display: block;`实现的。

方式二：

```
	$("div").show(2000);
```

解释：通过控制元素的宽高、透明度、display属性，逐渐显示，2秒后显示完毕。

方式三：

```
	$("div").show("slow");
```

参数可以是：

- slow 慢：600ms
    
- normal 正常：400ms
    
- fast 快：200ms
方式四：

```
    //show(毫秒值，回调函数;
    $("div").show(5000,function () {
        alert("动画执行完毕！");
    });
```

解释：动画执行完后，立即执行回调函数。
### 隐藏动画

方式参照上面的show()方法的方式。如下：

```
	$(selector).hide();

	$(selector).hide(1000);

	$(selector).hide("slow");

	$(selector).hide(1000, function(){});
```

**显示和隐藏的来回切换：**

显示和隐藏的来回切换采用的是toggle()方法：就是先执行show()，再执行hide()。

同样是四种方式：

```
$(selector).toggle();
```

### 滑入和滑出

**1、滑入动画效果**：（类似于生活中的卷帘门）

```
	$(selector).slideDown(speed, 回调函数);
```

解释：下拉动画，显示元素。

注意：省略参数或者传入不合法的字符串，那么则使用默认值：400毫秒（同样适用于fadeIn/slideDown/slideUp）

**2 滑出动画效果：**

```
	$(selector).slideUp(speed, 回调函数);
```

解释：上拉动画，隐藏元素。

**3、滑入滑出切换动画效果：**

```
	$(selector).slideToggle(speed, 回调函数);
```

参数解释同show()方法。

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 300px;
            height: 300px;
            display: none;
            background-color: pink;
        }
    </style>

    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //点击按钮后产生动画
            $("button:eq(0)").click(function () {

                //滑入动画： slideDown(毫秒值，回调函数[显示完毕执行什么]);
                $("div").slideDown(2000, function () {
                    alert("动画执行完毕！");
                });
            })

            //滑出动画
            $("button:eq(1)").click(function () {

                //滑出动画：slideUp(毫秒值，回调函数[显示完毕后执行什么]);
                $("div").slideUp(2000, function () {
                    alert("动画执行完毕！");
                });
            })

            $("button:eq(2)").click(function () {
                //滑入滑出切换（同样有四种用法）
                $("div").slideToggle(1000);
            })

        })
    </script>
</head>
<body>
<button>滑入</button>
<button>滑出</button>
<button>切换</button>
<div></div>

</body>
</html>
```

### 淡入淡出动画

1、淡入动画效果：

```
	$(selector).fadeIn(speed, callback);
```

作用：让元素以淡淡的进入视线的方式展示出来。

2、淡出动画效果：

```
	$(selector).fadeOut(1000);
```

作用：让元素以渐渐消失的方式隐藏起来

3、淡入淡出切换动画效果：

```
	$(selector).fadeToggle('fast', callback);
```

作用：通过改变透明度，切换匹配元素的显示或隐藏状态。

参数的含义同show()方法。

代码举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 300px;
            height: 300px;
            display: none;
            /*opacity: 1;*/
            background-color: pink;
        }
    </style>

    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //点击按钮后产生动画
            $("button:eq(0)").click(function () {
//                //淡入动画用法1:   fadeIn();   不加参数
                $("div").fadeIn();

//                //淡入动画用法2:   fadeIn(2000);   毫秒值
//                $("div").fadeIn(2000);
//                //通过控制  透明度和display

                //淡入动画用法3:   fadeIn(字符串);   slow慢：600ms   normal正常:400ms   fast快：200ms
//                $("div").fadeIn("slow");
//                $("div").fadeIn("fast");
//                $("div").fadeIn("normal");

                //淡入动画用法4:   fadeIn(毫秒值，回调函数[显示完毕执行什么]);
//                $("div").fadeIn(5000,function () {
//                    alert("动画执行完毕！");
//                });
            })

            //滑出动画
            $("button:eq(1)").click(function () {
//                //滑出动画用法1:   fadeOut();   不加参数
//                $("div").fadeOut();

//                //滑出动画用法2:   fadeOut(2000);   毫秒值
//                $("div").fadeOut(2000);  //通过这个方法实现的：display: none;
//                //通过控制  透明度和display

                //滑出动画用法3:   fadeOut(字符串);   slow慢：600ms   normal正常:400ms   fast快：200ms
//                $("div").fadeOut("slow");
//                $("div").fadeOut("fast");
//                $("div").fadeOut("normal");

                //滑出动画用法1:   fadeOut(毫秒值，回调函数[显示完毕执行什么]);
//                $("div").fadeOut(2000,function () {
//                    alert("动画执行完毕！");
//                });
            })

            $("button:eq(2)").click(function () {
                //滑入滑出切换
                //同样有四种用法
                $("div").fadeToggle(1000);
            })

            $("button:eq(3)").click(function () {
                //改透明度
                //同样有四种用法
                $("div").fadeTo(1000, 0.5, function () {
                    alert(1);
                });
            })
        })
    </script>
</head>
<body>
<button>淡入</button>
<button>淡出</button>
<button>切换</button>
<button>改透明度为0.5</button>
<div></div>

</body>
</html>
```

### 自定义动画

```
	$(selector).animate({params}, speed, callback);
```

作用：执行一组CSS属性的自定义动画。

- 第一个参数表示：要执行动画的CSS属性（必选）
    
- 第二个参数表示：执行动画时长（可选）
    
- 第三个参数表示：动画执行完后，立即执行的回调函数（可选）
    

代码举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            position: absolute;
            left: 20px;
            top: 30px;
            width: 100px;
            height: 100px;
            background-color: pink;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(function () {
            $("button").click(function () {
                var json = {"width": 500, "height": 500, "left": 300, "top": 300, "border-radius": 100};
                var json2 = {
                    "width": 100,
                    "height": 100,
                    "left": 100,
                    "top": 100,
                    "border-radius": 100,
                    "background-color": "red"
                };

                //自定义动画
                $("div").animate(json, 1000, function () {
                    $("div").animate(json2, 1000, function () {
                        alert("动画执行完毕！");
                    });
                });

            })
        })
    </script>
</head>
<body>
<button>自定义动画</button>
<div></div>
</body>
</html>
```

### 停止动画

```
	$(selector).stop(true, false);
```

**里面的两个参数，有不同的含义。**

第一个参数：

- true：后续动画不执行。
    
- false：后续动画会执行。
    

第二个参数：

- true：立即执行完成当前动画。
    
- false：立即停止当前动画。
    

PS：参数如果都不写，默认两个都是false。实际工作中，直接写stop()用的多。

**stop方法的总结**

当调用stop()方法后，队列里面的下一个动画将会立即开始。 但是，如果参数clearQueue被设置为true，那么队列面剩余的动画就被删除了，并且永远也不会执行。

如果参数jumpToEnd被设置为true，那么当前动画会停止，但是参与动画的每一个CSS属性将被立即设置为它们的目标值。比如：slideUp()方法，那么元素会立即隐藏掉。如果存在回调函数，那么回调函数也会立即执行。

注意：如果元素动画还没有执行完，此时调用stop()方法，那么动画将会停止。并且动画没有执行完成，那么回调函数也不会被执行。

举例：右下角的弹出广告

代码实现：

```
<!DOCTYPE html>
<html>

<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        .ad {
            position: fixed;
            right: 0;
            bottom: 0;
            width: 230px;
            height: 120px;
            background-image: url(images/ad.jpg);
            display: none;
        }

        .ad span {
            position: absolute;
            right: 0;
            top: 0;
            width: 40px;
            height: 18px;
            background-image: url(images/h.jpg);
            cursor: pointer;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //需求：然广告ad部分，先滑入，在滑出，在淡入。然后绑定事件，点击span弹出
            //步骤：
            $(".ad").slideDown(1000).slideUp(1000).fadeIn(1000).children("span").click(function () {
                $(this).parent().fadeOut(1000);
            });


            //第二种写法
//            $(".ad").slideDown(1000, function () {
//                $(".ad").slideUp(1000, function () {
//                    $(".ad").fadeIn(1000, function () {
//                        $(".ad").children("span").click(function () {
//                            $(this).parent().fadeOut(1000, function () {
//                                alert("执行完毕！");
//                            });
//                        });
//                    });
//                });
//            })
        })
    </script>
</head>

<body>

<div class="ani">我是内容</div>
<div class="ad">
    <span></span>
</div>

</body>
</html>
```

## 操作DOM
### 样式操作和类操作

作用：设置或获取元素的样式属性值。

#### 样式操作

**1、设置样式：**

```

    //设置单个样式：  css(属性，值);
    $("div").css("background-color","red");

    //设置多个样式：  css(json);
	 $("div").css({"width":100,"height":100,"background-color":"pink"});



```

**2、获取样式：**

```
    //获取样式：css(属性);
    //获取的时候如果有很多个，那么获取jquery对象中的第一个
    alert($("div").css("width"));
```
#### 类操作（className）

**1、添加类样式：**

```
	$(selector).addClass("liItem");  //为指定元素添加类className
```

注意：此处类名不带点，所有类操作的方法类名都不带点。

**2、移除类样式：**

```
	$(selector).removeClass("liItem");  //为指定元素移除类 className
	$(selector).removeClass();          //不指定参数，表示移除被选中元素的所有类
```

**3、判断有没有类样式：**

```
	$(selector).hasClass("liItem");   //判断指定元素是否包含类 className
```

此时，会返回true或false。jquery对象中，只要有一个带有指定类名的就是true，所有都不带才是false。

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: pink;
        }

        .current {
            background-color: red;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            $("button").eq(0).click(function () {
                //添加类
                $("div").addClass("current");
                //判断类
                alert($("div").hasClass("current"));
            });

            $("button").eq(1).click(function () {
                //删除类
                $("div").removeClass("current");
                //判断类
                alert($("div").hasClass("current"));
            });
            //alert($("div").hasClass("current"));//jquery对象中只要有一个带有类名的就是true，所有都不带才是false。
        })
    </script>
</head>
<body>
<button>添加</button>
<button>删除</button>
<div></div>
<div></div>
<div></div>
<div class="current"></div>
</body>
</html>

```

**4、切换类样式：**

```
$(selector).toggleClass(“liItem”);    //为指定元素切换类 className，该元素有类则移除，没有指定类则添加。
```

解释：为指定元素切换类 className，该元素有类则移除，没有指定类则添加。

如果采用采用正常的思路实现上面这句话，代码是：

```
   if($("div").hasClass("current")){
       //如果有类名，那么删除
       $("div").removeClass("current")
   }else{
       //如果没有类名，那么添加
       $("div").addClass("current")
   }
```

现在有了toggleClass()方法，一行代码即可实现。

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: green;
        }
        .current {
            background-color: red;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            $("button").click(function () {
                //需求：点击按钮 ，切换背景
                //切换类（toggleCLass）
                $("div").toggleClass("current");
            });
        })
    </script>
</head>
<body>
<button>切换背景</button>
<div></div>
</body>
</html>
```
#### 样式操作和类操作的比较

- 操作的样式非常少，那么可以通过`.css()`实现。
    
- 操作的样式很多，建议通过使用类 class 的方式来操作。
    
- 如果考虑以后维护方便（把CSS从js中分离出来）的话，推荐使用类的方式来操作。
    

**举例**：addClass+removeClass

代码实现：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        ul {
            list-style: none;
        }

        .wrapper {
            width: 1000px;
            height: 475px;
            margin: 0 auto;
            margin-top: 100px;
        }

        .tab {
            border: 1px solid #ddd;
            border-bottom: 0;
            height: 36px;
            width: 320px;
        }

        .tab li {
            position: relative;
            float: left;
            width: 80px;
            height: 34px;
            line-height: 34px;
            text-align: center;
            cursor: pointer;
            border-top: 4px solid #fff;
        }

        .tab span {
            position: absolute;
            right: 0;
            top: 10px;
            background: #ddd;
            width: 1px;
            height: 14px;
            overflow: hidden;
        }

        .products {
            width: 1002px;
            border: 1px solid #ddd;
            height: 476px;
        }

        .products .main {
            float: left;
            display: none;
        }

        .products .main.selected {
            display: block;
        }

        .tab li.active {
            border-color: red;
            border-bottom: 0;
        }

    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(window).ready(function () {
            //需求:鼠标放到那个li上，让该li添加active类，下面的对应的.main的div添加selected
            $(".tab>li").mouseenter(function () {
                //不用判断，当前的li添加active类，其他的删除active类
                $(this).addClass("active").siblings("li").removeClass("active");
                //对应索引值的div添加selected类，其他的删除selected类
                //【重要】根据tab的索引值获取下方图片div的索引值
                $(".products>div").eq($(this).index()).addClass("selected").siblings("div").removeClass("selected");
            });
        });
    </script>
</head>
<body>
<div class="wrapper">
    <ul class="tab">
        <li class="tab-item active">国际大牌<span>◆</span></li>
        <li class="tab-item">国妆名牌<span>◆</span></li>
        <li class="tab-item">清洁用品<span>◆</span></li>
        <li class="tab-item">男士精品</li>
    </ul>
    <div class="products">
        <div class="main selected">
            <a href="###"><img src="images/guojidapai.jpg" alt=""/></a>
        </div>
        <div class="main">
            <a href="###"><img src="images/guozhuangmingpin.jpg" alt=""/></a>
        </div>
        <div class="main">
            <a href="###"><img src="images/qingjieyongpin.jpg" alt=""/></a>
        </div>
        <div class="main">
            <a href="###"><img src="images/nanshijingpin.jpg" alt=""/></a>
        </div>
    </div>
</div>

</body>
</html>
```

### jQuery 的节点操作
#### 动态创建元素


方式一：

```
	var $spanNode1 = $("<span>我是一个span元素</span>");  // 返回的是 jQuery对象
```

此方法类似于 原生 js 中的`document.createElement("标签名");`

方式二：（推荐）

```
	var node = $("#box").html("<li>我是li</li>");
```

此方法类似于 原生 js 中的`innerHTML`。

举例：

```
    //方式一：      $("标签")             :类比于js中的document.createElement("li");
    console.log($("<li class='aaa'>我是li标签</li>"));

    //方式二：      $("ul").html("");     :类比innerHTML属性。因为此属性，识别标签。
    $("ul").html("<li>我是html方法穿件出来的li标签</li>")
```
#### 添加元素

jQuery 添加元素的方法非常多，最重要的方法是`append()`。格式如下：

```
// 方式一：在$(selector)中追加$node
$(selector).append($node);   //参数是 jQuery对象

// 方式二：在$(selector)中追加div元素，
$(selector).append('<div></div>');  //参数是 htmlString

```

作用：在被选元素内部的最后一个子元素（或内容）后面插入内容（存在或者创建出来的元素都可以）。

通俗的解释：**在盒子里的最末尾添加元素**。

- 如果是页面中存在的元素，那调用append()后，会把这个元素放到相应的目标元素里面去；但是，原来的这个元素，就不存在了。
    
- 如果是给多个目标追加元素，那么方法的内部会复制多份这个元素，然后追加到多个目标里面去。
    

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(document).ready(function () {
            $("button").click(function () {
                //创建一个新的jquery对象li
                var jqNewLi = $("<li>我是jquery创建出来的li。用的是append方法添加</li>");

                //append();  在盒子里的最末尾添加与严肃
                $("ul").append(jqNewLi);    //把新创建的 li 塞进已知的 ul 中
                //jqNewLi.appendTo($("ul")); //方式二：把新创建的li塞进ul中。作用同上
            })
        });
    </script>
</head>
<body>
<button>添加li</button>

<ul>
    <li>我是土著li</li>
</ul>

</body>
</html>
```
**其他的添加元素的方法：**

方法2：

```
	$(selector).appendTo(node);
```

作用：同append()，只不过是反着写的。

方法3：

```
	$(selector).prepend(node);
```

作用：在元素的第一个子元素前面追加内容或节点。

方法4：

```
	$(selector).after(node);
```

作用：在被选元素之后，作为**兄弟元素**插入内容或节点。

**方法5：**

```
	$(selector).before(node);
```

作用：在被选元素之前，作为**兄弟元素**插入内容或节点。
#### 清空元素

方式一：没有参数

```
	$(selector).empty();
	$(selector).html("");
```

解释：清空指定元素的所有子元素（光杆司令）。

方式二：

//

```
	$(selector).remove();
```

解释：“自杀” 。把自己以及所有的内部元素从文档中删除掉。

#### 复制元素

格式：

```
	复制的新元素 = $(selector).clone();
```

解释：复制$(selector)这个元素。是深层复制。

#### 总结

推荐使用 `html("<span></span>")` 方法来创建元素或者 `html("")` 清空元素。

#### 案例：选择水果

完整版代码：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        select {
            width: 170px;
            height: 240px;
            font-size: 18px;
            background-color: #a4ff34;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {

            //步骤：
            //1.将左侧的子标签全部移动到右侧。
            $("button").eq(0).click(function () {
                //右侧标签.append(左侧标签);
                $("#sel2").append($("#sel1 option"));
            });

            //2.将右侧的子标签全部移动到左侧。
            $("button").eq(1).click(function () {
                //左侧标签.append(右侧标签);
                $("#sel1").append($("#sel2 option"));
            });

            //第二步：获取子元素的时候要注意，获取的必须是，被选中的元素。
            //技术点：怎么获取被选中的子元素呢？？？答案：option:selected;
            //1.将左侧被选中的子标签移动到右侧
            $("button").eq(2).click(function () {
                //右侧标签.append(左侧标签);
                $("#sel2").append($("#sel1 option:selected"));
            });

            //2.将右侧被选中的子标签移动到左侧
            $("button").eq(3).click(function () {
                //右侧标签.append(左侧标签);
                $("#sel1").append($("#sel2 option:selected"));
            });

        })
    </script>
</head>
<body>
<select id="sel1" size="10" multiple>
    <option value="0">香蕉</option>
    <option value="1">苹果</option>
    <option value="2">鸭梨</option>
    <option value="3">葡萄</option>
</select>
<button>>>></button>
<button><<<</button>
<button>></button>
<button><</button>
<select id="sel2" size="10" multiple>

</select>
</body>
</html>
```
#### 案例：动态添加表格项

代码如下：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        table {
            border-collapse: collapse;
            border-spacing: 0;
            border: 1px solid #c0c0c0;
        }

        th,
        td {
            border: 1px solid #d0d0d0;
            color: #404060;
            padding: 10px;
        }

        th {
            background-color: #09c;
            font: bold 16px "微软雅黑";
            color: #fff;
        }

        td {
            font: 14px "微软雅黑";
        }

        tbody tr {
            background-color: #f0f0f0;
        }

        tbody tr:hover {
            cursor: pointer;
            background-color: #fafafa;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            // 模拟从后台拿到的数据
            var data = [{
                name: "博客园",
                url: "http://www.cnblogs.com/smyhvae/",
                type: "程序员的精神家园"
            }, {
                name: "简书",
                url: "https://www.jianshu.com/u/4d2e6b4bf117",
                type: "写作平台"
            }, {
                name: "百度",
                url: "https://www.baidu.com/",
                type: "你就知道"
            }];

            //需求:点击按钮，然后生成tr里面生成三个td.数组元素个数个tr。然后放入tbody中
            //步骤：
            //1.绑定事件
            //2.利用for循环,把数组中的所有数据组合成一个字符串。
            //3.把生成的字符串设置为html内容添加进tbody中。


            //1.绑定事件
            $("input").click(function () {
                //写入到click事件中，每次点击以后把之前的str清空【重要】
                var str = "";
                //2.利用for循环,把数组中的所有数据组合成一个字符串。
                for(var i=0;i<data.length;i++){
                    //如何生成3组？？？
//                    str += "<tr><td>1</td><td>2</td><td>3</td></tr>";
                    //data[i] = 数组中的每一个json
                    //data[i].name = 数组中的每一个json的name属性值
                    str += "<tr><td>"+data[i].name+"</td><td>"+data[i].url+"</td><td>"+data[i].type+"</td></tr>";
                }

                //3.把生成的字符串设置为html内容添加进tbody中。
                $("#j_tbData").html(str);
            })
        })
    </script>
</head>

<body>
<input type="button" value="获取数据" id="j_btnGetData"/>
<table>
    <thead>
    <tr>
        <th>标题</th>
        <th>地址</th>
        <th>说明</th>
    </tr>
    </thead>
    <tbody id="j_tbData">
    <!--<tr>-->
    <!--<td>1</td>-->
    <!--<td>2</td>-->
    <!--<td>3</td>-->
    <!--</tr>-->
    </tbody>
</table>
</body>

</html>
```

### jQuery 设置和获取属性

jQuery 无法直接操作节点的属性和src等，我们需要借助attr()方法。下面介绍。

#### 属性操作

**（1）设置属性：**

```
	$(selector).attr("title", "千古壹号");
```

参数解释：第一个参数表示：要设置的属性名称。第二个参数表示：该属性名称对应的值。

**（2）获取属性：**

```
	$(selector).attr("title");
```

参数为：要获取的属性的名称，返回指定属性对应的值。

**总结**：两个参数是给属性赋值，单个参数是获取属性值。

**（3）移除属性：**

```
	$(selector).removeAttr("title");
```

参数为：要移除的属性的名称。

（4）form表单中的 `prop()`方法：

针对`checked、selected、disabled`属性，要使用 `prop()`方法，而不是其他的方法。

prop方法通常用来影响DOM元素的动态状态，而不是改变的HTML属性。例如：input和button的disabled特性，以及checkbox的checked特性。
以上四项的代码演示：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        .aaa {
            border: 1px solid red;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //获取元素，绑定属性
            var jqinp = $("input").eq(0);
            var jqinp2 = $("input:checkbox");
            var jqbtn = $("button");

            jqbtn.click(function () {
                //是绑定到jquery的衣服上，而不是标签上。所以没达到效果
//                jqinp.title = 111;
//                console.log(jqinp.title);

                //绑定到标签上
                jqinp.attr("title", 111);
                console.log(jqinp.attr("title"));

                jqinp.attr("aaa", 111);
                console.log(jqinp.attr("aaa"));

                //两个参数是给属性赋值，单个参数是获取属性值。
                jqinp.attr("class", "aaa");
                console.log(jqinp.attr("class"));

                jqinp.removeAttr("class");
                console.log(jqinp.attr("class"));

                //form中的特殊属性，用prop
                jqinp2.prop("checked", true);
//                jqinp2.attr("checked",true);//一次性的。鼠标多点击几次，就失效了。

            });
        })
    </script>
</head>
<body>
<button>绑定</button>
<input type="text"/>
<input type="checkbox"/>

</body>
</html>
```
**案例：表格案例全选反选**

完整版代码：

```
<!DOCTYPE html>
<html>

<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        * {
            padding: 0;
            margin: 0;
        }

        .wrap {
            width: 300px;
            margin: 100px auto 0;
        }

        table {
            border-collapse: collapse;
            border-spacing: 0;
            border: 1px solid #c0c0c0;
        }

        th,
        td {
            border: 1px solid #d0d0d0;
            color: #404060;
            padding: 10px;
        }

        th {
            background-color: #09c;
            font: bold 16px "微软雅黑";
            color: #fff;
        }

        td {
            font: 14px "微软雅黑";
        }

        tbody tr {
            background-color: #f0f0f0;
        }

        tbody tr:hover {
            cursor: pointer;
            background-color: #fafafa;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //需求1：点击上面的多选按钮，下面的所有多选按钮都和上面的一致
            //需求2：点击下面的多选按钮，判断下面的所有多选按钮都是否全部被选定只有全部被选定上面的才被选定


            //需求1：点击上面的多选按钮，下面的所有多选按钮都和上面的一致
            //步骤：绑定事件，直接让下面的所有按钮和上面的按钮属性值一模一样
            $("#j_cbAll").click(function () {
                //直接让下面的所有按钮和上面的按钮属性值一模一样
                $("#j_tb input:checkbox").prop("checked", $(this).prop("checked"));
            });

            //需求2：点击下面的多选按钮，判断下面的所有多选按钮都是否全部被选定只有全部被选定上面的才被选定
            //需求2：点击下面的多选按钮，判断下面的所有多选按钮都是否全部被选定只有全部被选定上面的才被选定
            $("#j_tb input:checkbox").click(function () {
                //判断，只有所有都背选定，上面的才被选定
                //技术点：带有checked属性的标签和checkbox个数一样多的时候
                if ($("#j_tb input:checkbox").length === $("#j_tb input:checked").length) {
                    //只有所有的都有checked属性，上面的才被选定
                    $("#j_cbAll").prop("checked", true);
                } else {
                    $("#j_cbAll").prop("checked", false);
                }
            });


        })
    </script>
</head>

<body>
<div class="wrap">
    <table>
        <thead>
        <tr>
            <th>
                <input type="checkbox" id="j_cbAll"/>
            </th>
            <th>课程名称</th>
            <th>所属团队</th>
        </tr>
        </thead>
        <tbody id="j_tb">
        <tr>
            <td>
                <input type="checkbox"/>
            </td>
            <td>JavaScript</td>
            <td>千古壹号</td>
        </tr>
        <tr>
            <td>
                <input type="checkbox"/>
            </td>
            <td>css</td>
            <td>千古壹号</td>
        </tr>
        <tr>
            <td>
                <input type="checkbox"/>
            </td>
            <td>html</td>
            <td>千古壹号</td>
        </tr>
        <tr>
            <td>
                <input type="checkbox"/>
            </td>
            <td>jQuery</td>
            <td>千古壹号</td>
        </tr>
        </tbody>
    </table>
</div>
</body>

</html>
```

#### val()方法和 text()方法

```
	$(selector).val();
```

作用：设置或返回 form 表单元素的value值，例如：input、select、textarea 的值。

```
	$(selector).text();
```

作用：设置或获取匹配元素的文本内容。不带参数表示，会把所有匹配到的元素内容拼接为一个**字符串**，不同于其他获取操作。

```
	$(selector).text("我是内容");
```

作用：设置的内容包含html标签，那么text()方法会把他们当作**纯文本**内容输出。

总结：

- text() 不识别标签。
    
- html() 识别标签。
    

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(document).ready(function () {
            //val();   获取标签中的value属性的值。带有参数是赋值(类比js中的value属性)
            console.log($("input").val());

            $("input").val("我是value()赋值的input内容");
            console.log($("input").val());

            console.log("-----------------");

            //text();  获取双闭合标签中的文本值。（不识别标签）(类比js中的innerText)
            console.log($("div").text());
            $("div").text("<li>我是text()赋值的</li>")
            console.log($("div").text());

            console.log("-----------------");

            //html();  获取双闭合标签中的文本值。（识别标签）(类比js中的innerHTML)
            console.log($("div").html());
            $("div").html("<li>我是html()赋值的</li>");
            console.log($("div").html());
        })
    </script>
</head>
<body>
<input type="text" value="我是input中已存在的 value内容"/>
<div>
    <li>你好</li>
</div>
</body>
</html>
```
## jQuery的事件机制和其他知识
### jQuery 设置宽度和高度

宽度操作：

```
	$(selector).height();     //不带参数表示获取高度
	$(selector).height(200);  //带参数表示设置高度
```

宽度操作：

```
	$(selector).width();     //不带参数表示获取宽度
	$(selector).width(200);  //带参数表示设置高宽度
```

**问题**：jQuery的css()获取高度，和jQuery的height获取高度，二者的区别？

答案：

```
	$("div").css();     //返回的是string类型，例如：30px

	$("div").height();  //返回得失number类型，例如：30。常用于数学计算。
```

如上方代码所示，`$("div").height();`返回的是number类型，常用于数学计算。
### jQuery 的坐标操作
#### offset()方法

```
	$(selector).offset();
	$(selector).offset({left:100, top: 150});
```

作用：获取或设置元素相对于 document 文档的位置。参数解释：

- 无参数：表示获取。返回值为：{left:num, top:num}。返回值是相对于document的位置。
    
- 有参数：表示设置。参数建议使用 number 数值类型。
    

注意：设置offset后，如果元素没有定位(默认值：static)，则被修改为relative。
#### position()方法

```
	$(selector).position();
```

作用：获取相对于其最近的**带有定位**的父元素的位置。返回值为对象：`{left:num, top:num}`。

注意：只能获取，不能设置。
#### scrollTop()方法

```
	scrollTop();
	$(selector).scrollTop(100);
```

作用：获取或者设置元素被卷去的头部的距离。参数解释：

- 无参数：表示获取偏移。
    
- 有参数：表示设置偏移，参数为数值类型。
#### scrollLeft()方法

```
	scrollLeft();
	$(selector).scrollLeft(100);
```

作用：获取或者设置元素水平方向滚动的位置。参数解释：

- 无参数：表示获取偏移。
    
- 有参数：表示设置偏移，参数为数值类型。
    

代码示范：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        body {
            height: 5000px;
        }

        .box1 {
            width: 300px;
            height: 300px;
            position: relative;
            margin: 10px;
            overflow: auto;
            background-color: pink;
        }

        .box2 {
            width: 200px;
            height: 400px;
            position: absolute;
            top: 50px;
            left: 50px;
            background-color: yellow;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //距离页面最顶端或者最左侧的距离和有没有定位没有关系
            $("button").eq(0).click(function () {
                alert($(".box2").offset().top);
            })

            //距离页面最顶端或者最左侧的距离和有没有定位没有关系
            $("button").eq(1).click(function () {
                $(".box2").offset({"left": 1000, "top": 1000});
            })

            //距离父系盒子中带有定位的盒子的距离(获取的就是定位值，和margin/padding无关)
            $("button").eq(2).click(function () {
                alert($(".box2").position().top);
            })

            //距离父系盒子中带有定位的盒子的距离(获取的就是定位值，和margin/padding无关)
            $("button").eq(3).click(function () {
                $(".box2").position().top = "100px";
            })

            //获取被选取的头部
            $("button").eq(4).click(function () {
                alert($(window).scrollTop());
            })

            //获取被选取的头部
            $("button").eq(5).click(function () {
                $(window).scrollTop(100);
            })

        })
    </script>

</head>
<body>


<div class="box1">
    <div class="box2"></div>
</div>

<button>offset().top获取</button>
<button>offset().top设置</button>
<button>position().top获取</button>
<button>position().top设置</button>
<button>scrollTop()</button>
<button>scrollTop()</button>

</body>
</html>
```

### jQuery的事件机制

#### 常见的事件绑定

- click(handler) 单击事件。
    
- blur(handler) 失去焦点事件。
    
- mouseenter(handler) 鼠标进入事件。
    
- mouseleave(handler) 鼠标离开事件。
    
- dbclick(handler) 双击事件。
    
- change(handler) 改变事件，如：文本框值改变，下拉列表值改变等。
    
- focus(handler) 获得焦点事件。
    
- keydown(handler) 键盘按下事件。
#### on方式绑定事件

最早采用的是 bind、delegate等方式绑定的。jQuery 1.7版本后，jQuery用on统一了所有的事件处理的方法，此方法兼容zepto(移动端类似于jQuery的一个库)。

格式举例：

```
        $(document).on("click mouseenter", ".box", {"name": 111}, function (event) {
            console.log(event.data);      //event.data获取的就是第三个参数这个json。
            console.log(event.data.name); //event.data.name获取的是name的值。
        });
```

参数解释：

- 第一个参数：events，绑定事件的名称可以是由空格分隔的多个事件（标准事件或者自定义事件）。上方代码绑定的是单击事件和鼠标进入事件。
    
- 第二个参数：selector, 执行事件的后代元素。
    
- 第三个参数：data，传递给事件处理函数的数据，事件触发的时候通过event.data来使用（也就是说，可以通过event拿到data）
    
- 第四个参数：handler，事件处理函数。
    

简单点的写法：

```
    $(document).on("click",".box", function () {
       alert(1);
    });
```

#### off方式解绑事件

```
    $(selector).off();      // 解绑匹配元素的所有事件

    $(selector).off("click");   // 解绑匹配元素的所有click事件

    $(selector).off( "click", "**" );   // 解绑所有代理的click事件，元素本身的事件不会被解绑
```

### jQuery的事件对象
event.data 传递给事件处理程序的额外数据

event.currentTarget 等同于this，当前DOM对象

event.pageX 鼠标相对于文档左部边缘的位置

event.target 触发事件源，不一定===this

event.stopPropagation()； 阻止事件冒泡

event.preventDefault(); 阻止默认行为

event.type 事件类型：click，dbclick…

event.which 鼠标的按键类型：左1 中2 右3

event.keyCode 键盘按键代码

代码演示：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            $(document).on("click", {}, function (event) {
                console.log(event.data);
                console.log(event.currentTarget);
                console.log(event.target);
                console.log(event.pageX);
                console.log(event.type);
                console.log(event.which);
                console.log(event.keyCode);
            });
        })
    </script>
</head>
<body>

</body>
</html>
```

上方代码中，我们通过event参数，获取了点击事件的各种event里的属性。
这个时候就要用到event参数，因为要获取event.keyCode，才能知道按下的是键盘上的哪个按键。

代码实现：

```
<!DOCTYPE html>
<html>

<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        .wrap {
            width: 400px;
            height: 400px;
            margin: 100px auto 0;
        }

        .wrap h1 {
            text-align: center;
        }

        .wrap div {
            width: 400px;
            height: 300px;
            background: pink;
            font-size: 30px;
            text-align: center;
            line-height: 300px;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            //需求：在页面上，按键.是哪个颜色的首写字母div就改变为该颜色，然后span内容赋值。
            //步骤：
            //1.给document绑定keyup事件
            //2.获取值，根据此值，给div和span上色和内容

            var div = $("#bgChange");
            var span = $("#keyCodeSpan");

            //绑定事件
            $(document).keyup(function (e) {  //键盘弹出时，触发事件
                //调用方法
                setColor(e.keyCode);
            });


            function setColor(keyCode) {
                //alert(e.keyCode);
                //2.获取值，根据此值，给div和span上色和内容
                switch (keyCode) {
                    case 80:
                        //修改内容pink
                        setEle("pink", keyCode);
                        break;
                    case 66:
                        //修改内容blue
                        setEle("blue", keyCode);
                        break;
                    case 79:
                        //修改内容orange
                        setEle("orange", keyCode);
                        break;
                    case 82:
                        //修改内容red
                        setEle("red", keyCode);
                        break;
                    case 89:
                        //修改内容yellow
                        setEle("yellow", keyCode);
                        break;
                    default :
                        alert("系统没有设置该颜色！");
                }

                function setEle(a, b) {
                    div.css("background-color", a);
                    span.text(b);
                }

            }

            //1.给document绑定keyup事件
//            $(document).keyup(function (e) {
//                //alert(e.keyCode);
//                //2.获取值，根据此值，给div和span上色和内容
//                switch (e.keyCode){
//                    case 80:
//                        //修改内容pink
//                        div.css("background-color","pink");
//                        span.text(e.keyCode);
//                        break;
//                    case 66:
//                        //修改内容blue
//                        div.css("background-color","blue");
//                        span.text(e.keyCode);
//                        break;
//                    case 79:
//                        //修改内容orange
//                        div.css("background-color","orange");
//                        span.text(e.keyCode);
//                        break;
//                    case 82:
//                        //修改内容red
//                        div.css("background-color","red");
//                        span.text(e.keyCode);
//                        break;
//                    case 89:
//                        //修改内容yellow
//                        div.css("background-color","yellow");
//                        span.text(e.keyCode);
//                        break;
//                    default :
//                        alert("系统没有设置该颜色！");
//                }
//            });
        })
    </script>
</head>

<body>

<div class="wrap">
    <h1>按键改变颜色</h1>
    <div id="bgChange">
        keyCode为：
        <span id="keyCodeSpan">80</span>
    </div>
</div>

</body>
</html>
```
### jQuery 的两大特点
（1）**链式编程**：比如`.show()`和`.html()`可以连写成`.show().html()`。

链式编程原理：return this。

通常情况下，只有设置操作才能把链式编程延续下去。因为获取操作的时候，会返回获取到的相应的值，无法返回 this。

```
    end(); // 结束当前链最近的一次过滤操作，并且返回匹配元素之前的状态。
```

（2）**隐式迭代**：隐式 对应的是 显式。隐式迭代的意思是：在方法的内部会为匹配到的所有元素进行循环遍历，执行相应的方法；而不用我们再进行循环，简化我们的操作，方便我们调用。

如果获取的是多元素的值，大部分情况下返回的是第一个元素的值。

**举例：**五角星评分

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>五角星评分案例</title>
    <style>
        * {
            padding: 0;
            margin: 0;
        }

        .comment {
            font-size: 40px;
            color: #ff3100;
        }

        .comment li {
            float: left;
            cursor: pointer;
        }

        ul {
            list-style: none;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script>
        $(function () {
            var star_none = '☆'; // 空心五角星
            var star_sel = '★'; // 实心五角星

            //需求1：鼠标放悬停时，当前的li和之前所有的li内容全部变为实心五角星，移开变为空心。
            $(".comment li").on("mouseenter", function () {
                //当前五角星，和之前的所有五角星，全部是实心的，其他的为空心

                //写法一：分两次写
//                $(this).text(star_sel).prevAll("li").text(star_sel);
//                $(this).nextAll("li").text(star_none);
                //写法二：一次性写完，但要用到end()，否则会出问题。【重要】
                $(this).text(star_sel).prevAll("li").text(star_sel).end().nextAll("li").text(star_none);
            });

            $(".comment li").on("mouseleave", function () {
                //bug：如果没有点击过li，那么会出现无法清除的现象，处理办法就是先判断，看看是否有current类
                if ($("li.current").length === 0) {
                    $(".comment li").text(star_none);
                } else {
                    //当鼠标移开的时候，谁有current类名，那么当前和之前所有的li前部是实心五角星，后面的所有li都是空心
                    $("li.current").text(star_sel).prevAll("li").text(star_sel).end().nextAll("li").text(star_none);
                }
            });


            //需求2：鼠标点击那个li，当你前li和之前所有的li都变成实心五角星，其他变为空心。
            $(".comment li").on("click", function () {
                //点击哪个li给他加一个类名。清空其他所有的li的类名
                $(this).attr("class", "current").siblings("li").removeAttr("class");
            });


        });
    </script>
</head>
<body>
<ul class="comment">
    <li>☆</li>
    <li>☆</li>
    <li>☆</li>
    <li>☆</li>
    <li>☆</li>
</ul>
</body>
</html>
```
### each的用法

大部分情况下是不需要使用each方法的，因为jQuery的隐式迭代特性。

但是，如果要对每个元素做不同的处理，这时候就用到了each方法。

格式如下：

```
    $(selector).each(function(index,element){});
```

参数解释：

- 参数一：表示当前元素在所有匹配元素中的索引号
    
- 参数二：参数二表示当前元素（是js 中的DOM对象，而不是jQuery对象）
    

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        li {
            width: 100px;
            height: 100px;
            margin: 20px;
            float: left;
            list-style: none;
            text-align: center;
            font: 50px/100px "simsun";
            color: white;
            background-color: black;
        }
    </style>

    <script src="jquery-1.11.1.js"></script>
    <script>
        jQuery(function () {
            //设置每个不一样的盒子透明度逐渐递增
            $("ul li").each(function (index, element) {
                $(element).css("opacity", (index + 1) / 10);
                console.log(index+"---"+element.tagName);

            });
        });
    </script>
</head>
<body>
<ul>
    <li class="aaa1">1</li>
    <li class="aaa2">2</li>
    <li class="aaa3">3</li>
    <li class="aaa4">4</li>
    <li class="aaa5">5</li>
    <li class="aaa6">6</li>
    <li class="aaa7">7</li>
    <li class="aaa8">8</li>
    <li class="aaa9">9</li>
    <li class="aaa10">10</li>
</ul>

</body>
</html>
```
### 多库共存

**多库共存**指的是：jQuery占用了 `$` 和 `jQuery` 这两个变量。当在同一个页面中引用了 jQuery 库以及其他的库（或者其他版本的jQuery库），恰好其他的库中也用到了 `$` 或者`jQuery`变量.那么，要保证每个库都能正常使用，就产生了多库共存的问题。

温馨提示：我们可以通过以下方式获取 jQuery 库的版本号。

```
    console.log($.fn.jquery);  //打印 jQuery 库的版本号
```

**办法一**：让 jQuery 放弃对 `$` 的使用权：

```
    $.noConflict();
```

办法二：同时放弃放弃两个符号的使用权，并定义一个新的使用权（如果有三个库时，可以这样用）

```
    $.noConflict(true);   //返回值是新的关键字
```
## jQuery 的插件机制

jQuery 库，虽然功能强大，但也不是面面俱到。jQuery 是通过插件的方式，来扩展它的功能：

- 当你需要某个插件的时候，你可以“安装”到jQuery上面，然后使用。
    
- 当你不再需要这个插件，那你就可以从jQuery上“卸载”它。
### 插件之改变颜色

jQuery的自定义动画方法animate()，在执行动画时，是不支持设置背景色这个属性的。这个时候可以借助`jQuery.color.js`这个插件。

举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: blue;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <script src="jquery.color.js"></script>
    <script>
        $(function () {
            //点击按钮，改变盒子的宽度和背景色
            $("button").on("click", function () {
                $("div").animate({"width": 200, "background-color": "red"}, 2000, function () {
                    alert("动画结束");
                });
            });
        })
    </script>
</head>
<body>
<button>变色</button>
<div></div>
</body>
</html>
```
上方代码中，因为加入了一行插件：（注意顺序是放在jQuery插件之后）

```
    <script src="jquery.color.js"></script>
```

否则的话，在动画执行的过程中，是无法设置背景色的。
### 插件之懒加载

懒加载：当打开一个网页时，只有当我看到某个部分，再加载那个部分；而不是一下子全部加载完毕。这样可以优化打开的速度。

比如说，我可以设置一张图片为懒加载，于是，这张图片会等我宠幸到它的时候，它再打开。

代码举例：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            height: 3000px;
            background-color: pink;
        }
    </style>
    <script src="jquery-1.11.1.js"></script>
    <!--懒加载的使用。第一步：导包(必须在jquery库的下方）-->
    <script src="jquery.lazyload.js"></script>
    <script>
        $(function () {


            //第二步骤：调用懒加载的方法实现功能。参数的不同，功能也不同。
            $("img.lazy").lazyload();
        })
    </script>
</head>
<body>
<div></div>
<!--需要实现将图片设置为懒加载模式-->
<img class="lazy" data-original="images/01.jpg" width="640" height="480">
</body>
</html>
```
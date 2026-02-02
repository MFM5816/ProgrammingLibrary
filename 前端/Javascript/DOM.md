### 获取元素

- document.querySelector("selector") 通过CSS选择器获取符合条件的第一个元素。
    
- document.querySelectorAll("selector") 通过CSS选择器获取符合条件的所有元素，以类数组形式存在。
### 类名操作

- Node.classList.add("class") 添加class
    
- Node.classList.remove("class") 移除class
    
- Node.classList.toggle("class") 切换class，有则移除，无则添加
    
- Node.classList.contains("class") 检测是否存在class
### 自定义属性

js 里可以通过 `box1.index=100;` `box1.title` 来自定义属性和获取属性。

H5可以直接在标签里添加自定义属性，**但必须以 `data-` 开头**。
## 常见概念
### JavaScript的组成

JavaScript基础分为三个部分：

- ECMAScript：JavaScript的语法标准。包括变量、表达式、运算符、函数、if语句、for语句等。
    
- **DOM**：文档对象模型（Document object Model），操作**网页上的元素**的API。比如让盒子移动、变色、轮播图等。
    
- **BOM**：浏览器对象模型（Browser Object Model），操作**浏览器部分功能**的API。比如让浏览器自动滚动。
### 节点

**节点**（Node）：构成 HTML 网页的最基本单元。网页中的每一个部分都可以称为是一个节点，比如：html标签、属性、文本、注释、整个文档等都是一个节点。

虽然都是节点，但是实际上他们的具体类型是不同的。常见节点分为四类：

- 文档节点（文档）：整个 HTML 文档。整个 HTML 文档就是一个文档节点。
    
- 元素节点（标签）：HTML标签。
    
- 属性节点（属性）：元素的属性。
    
- 文本节点（文本）：HTML标签中的文本内容（包括标签之间的空格、换行）。
    

节点的类型不同，属性和方法也都不尽相同。所有的节点都是Object。

### 什么是DOM

**DOM**：Document Object Model，文档对象模型。DOM 为文档提供了结构化表示，并定义了如何通过脚本来访问文档结构。目的其实就是为了能让js操作html元素而制定的一个规范。

DOM就是由节点组成的。

**解析过程**： HTML加载完毕，渲染引擎会在内存中把HTML文档，生成一个DOM树，getElementById是获取内中DOM上的元素节点。然后操作的时候修改的是该元素的**属性**。

**DOM树**：（一切都是节点）

DOM的数据结构如下：
![[DOM数据结构.png]]
### DOM可以做什么

- 找对象（元素节点）
    
- 设置元素的属性值
    
- 设置元素的样式
    
- 动态创建和删除元素
    
- 事件的触发响应：事件源、事件、事件的驱动程序
## 元素节点的获取

DOM节点的获取方式其实就是**获取事件源的方式**。关于事件，上一篇文章中已经讲到了。

想要操作元素节点，必须首先要找到该节点。有三种方式可以获取DOM节点：

```
var div1 = document.getElementById("box1"); //方式一：通过 id 获取 一个 元素节点（为什么是一个呢？因为 id 是唯一的）

var arr1 = document.getElementsByTagName("div"); //方式二：通过 标签名 获取 元素节点数组，所以有s

var arr2 = document.getElementsByClassName("hehe"); //方式三：通过 类名 获取 元素节点数组，所以有s
```

### DOM访问关系的获取

DOM的节点并不是孤立的，因此可以通过DOM节点之间的相对关系对它们进行访问。如下：
![[DOM访问关系的获取1.png]]
节点的访问关系，是以**属性**的方式存在的。

JS中的**父子兄**访问关系：
![[JS中的父子兄访问关系.png]]
### 获取父节点

调用者就是节点。一个节点只有一个父节点，调用方式就是

```
	节点.parentNode
```

### 获取兄弟节点

**1、下一个节点 | 下一个元素节点**：

> Sibling的中文是**兄弟**。

（1）nextSibling：

- 火狐、谷歌、IE9+版本：都指的是下一个节点（包括标签、空文档和换行节点）。
    
- IE678版本：指下一个元素节点（标签）。
    

（2）nextElementSibling：

- 火狐、谷歌、IE9+版本：都指的是下一个元素节点（标签）。

**总结**：为了获取下一个**元素节点**，我们可以这样做：在IE678中用nextSibling，在火狐谷歌IE9+以后用nextElementSibling，于是，综合这两个属性，可以这样写：

```
	下一个兄弟节点 = 节点.nextElementSibling || 节点.nextSibling
```

**2、前一个节点 | 前一个元素节点**：

> previous的中文是：前一个。

（1）previousSibling：

- 火狐、谷歌、IE9+版本：都指的是前一个节点（包括标签、空文档和换行节点）。
    
- IE678版本：指前一个元素节点（标签）。
    

（2）previousElementSibling：

- 火狐、谷歌、IE9+版本：都指的是前一个元素节点（标签）。

**总结**：为了获取前一个**元素节点**，我们可以这样做：在IE678中用previousSibling，在火狐谷歌IE9+以后用previousElementSibling，于是，综合这两个属性，可以这样写：

```
	前一个兄弟节点 = 节点.previousElementSibling || 节点.previousSibling
```

**3、补充**：获得任意一个兄弟节点：

```
	节点自己.parentNode.children[index];  //随意得到兄弟节点
```

### 获取单个的子节点

**1、第一个子节点 | 第一个子元素节点**：

（1）firstChild：

- 火狐、谷歌、IE9+版本：都指的是第一个子节点（包括标签、空文档和换行节点）。
    
- IE678版本：指第一个子元素节点（标签）。
    

（2）firstElementChild：

- 火狐、谷歌、IE9+版本：都指的是第一个子元素节点（标签）。

**总结**：为了获取第一个**子元素节点**，我们可以这样做：在IE678中用firstChild，在火狐谷歌IE9+以后用firstElementChild，于是，综合这两个属性，可以这样写：

```
	第一个子元素节点 = 节点.firstElementChild || 节点.firstChild
```

**2、最后一个子节点 | 最后一个子元素节点**：

（1）lastChild：

- 火狐、谷歌、IE9+版本：都指的是最后一个子节点（包括标签、空文档和换行节点）。
    
- IE678版本：指最后一个子元素节点（标签）。
    

（2）lastElementChild：

- 火狐、谷歌、IE9+版本：都指的是最后一个子元素节点（标签）。

**总结**：为了获取最后一个**子元素节点**，我们可以这样做：在IE678中用lastChild，在火狐谷歌IE9+以后用lastElementChild，于是，综合这两个属性，可以这样写：

```
	最后一个子元素节点 = 节点.lastElementChild || 节点.lastChild
```

### 获取所有的子节点

（1）**childNodes**：标准属性。返回的是指定元素的**子节点**的集合（包括元素节点、所有属性、文本节点）。是W3C的亲儿子。

- 火狐 谷歌等高本版会把换行也看做是子节点。

用法：

```
	子节点数组 = 父节点.childNodes;   //获取所有节点。
```

（2）**children**：非标准属性。返回的是指定元素的**子元素节点**的集合。【重要】

- 它只返回HTML节点，甚至不返回文本节点。
- 在IE6/7/8中包含注释节点（在IE678中，注释节点不要写在里面）。

虽然不是标准的DOM属性，但它和innerHTML方法一样，得到了几乎所有浏览器的支持。

用法：（**用的最多**）

```
	子节点数组 = 父节点.children;   //获取所有节点。用的最多。
```
## DOM节点的操作
### 创建节点

格式如下：

```
	新的标签(元素节点) = document.createElement("标签名");
```

比如，如果我们想创建一个li标签，或者是创建一个不存在的adbc标签，可以这样做：

```
<script type="text/javascript">
    var a1 = document.createElement("li");   //创建一个li标签
    var a2 = document.createElement("adbc");   //创建一个不存在的标签

    console.log(a1);
    console.log(a2);

    console.log(typeof a1);
    console.log(typeof a2);
</script>
```
### 插入节点

插入节点有两种方式，它们的含义是不同的。

方式1：

```
	父节点.appendChild(新的子节点);
```

解释：父节点的最后插入一个新的子节点。

方式2：

```
	父节点.insertBefore(新的子节点,作为参考的子节点)
```

解释：

- 在参考节点前插入一个新的节点。
- 如果参考节点为null，那么他将在父节点里面的最后插入一个子节点。
### 删除节点

格式如下：

```
	父节点.removeChild(子节点);
```

解释：**用父节点删除子节点**。必须要指定是删除哪个子节点。

如果我想删除自己这个节点，可以这么做：

```
	node1.parentNode.removeChild(node1);
```

### 复制节点（克隆节点）

格式如下：

```
	要复制的节点.cloneNode();       //括号里不带参数和带参数false，效果是一样的。

	要复制的节点.cloneNode(true);
```

括号里带不带参数，效果是不同的。解释如下：

- 不带参数/带参数false：只复制节点本身，不复制子节点。
    
- 带参数true：既复制节点本身，也复制其所有的子节点。
## 设置节点的属性

我们可以获取节点的属性值、设置节点的属性值、删除节点的属性。

我们就统一拿下面这个标签来举例：

```
	<img src="images/1.jpg" class="image-box" title="美女图片" alt="地铁一瞥" id="a1">
```

下面分别介绍。

### 1、获取节点的属性值

**方式1**：

```
	元素节点.属性名;
	元素节点[属性名];
```

举例：（获取节点的属性值）

```
<body>
<img src="images/1.jpg" class="image-box" title="美女图片" alt="地铁一瞥" id="a1">

<script type="text/javascript">
    var myNode = document.getElementsByTagName("img")[0];

    console.log(myNode.src);
    console.log(myNode.className);    //注意，是className，不是class
    console.log(myNode.title);

    console.log("------------");

    console.log(myNode["src"]);
    console.log(myNode["className"]); //注意，是className，不是class
    console.log(myNode["title"]);
</script>
</body>
```
**方式2**：

```
	元素节点.getAttribute("属性名称");
```

举例：

```
    console.log(myNode.getAttribute("src"));
    console.log(myNode.getAttribute("class"));   //注意是class，不是className
    console.log(myNode.getAttribute("title"));
```
### 2、设置节点的属性值

方式1举例：（设置节点的属性值）

```
    myNode.src = "images/2.jpg"   //修改src的属性值
    myNode.className = "image2-box";  //修改class的name
```

方式2：

```
	元素节点.setAttribute("属性名", "新的属性值");
```

方式2举例：（设置节点的属性值）

```
    myNode.setAttribute("src","images/3.jpg");
    myNode.setAttribute("class","image3-box");
    myNode.setAttribute("id","你好");
```

### 3、删除节点的属性

格式：

```
	元素节点.removeAttribute(属性名);
```

举例：（删除节点的属性）

```
    myNode.removeAttribute("class");
    myNode.removeAttribute("id");
```
## DOM对象的属性

### innerHTML和innerText的区别

- value：标签的value属性。
    
- **innerHTML**：双闭合标签里面的内容（包含标签）。
    
- **innerText**：双闭合标签里面的内容（不包含标签）。
### nodeType属性

这里讲一下nodeType属性。

- **nodeType == 1 表示的是元素节点**（标签） 。记住：在这里，元素就是标签。
    
- nodeType == 2 表示是属性节点。
    
- nodeType == 3 是文本节点。
    

nodeType、nodeName、nodeValue

我们那下面这个标签来举例：

```
<div id="box" value="111">
    生命壹号
</div>
```

上面这个标签就包含了三种节点：

- 元素节点（标签）
    
- 属性节点
    
- 文本节点
    

获取这三个节点的方式如下：

```
    var element = document.getElementById("box1");  //获取元素节点（标签）
    var attribute = element.getAttributeNode("id"); //获取box1的属性节点
    var txt = element.firstChild;                   //获取box1的文本节点

    var value = element.getAttribute("id");         //获取id的属性值

    console.log(element);
    console.log("--------------");
    console.log(attribute);
    console.log("--------------");
    console.log(txt);
    console.log("--------------");
    console.log(value);
```
既然这三个都是节点，如果我想获取它们的nodeType、nodeName、nodeValue，代码如下：

```
    var element = document.getElementById("box1");  //获取元素节点（标签）
    var attribute = element.getAttributeNode("id"); //获取box1的属性节点
    var txt = element.firstChild;                   //获取box1的文本节点

    //获取nodeType
    console.log(element.nodeType);       //1
    console.log(attribute.nodeType);     //2
    console.log(txt.nodeType);           //3

    console.log("--------------");

    //获取nodeName
    console.log(element.nodeName);       //DIV
    console.log(attribute.nodeName);     //id
    console.log(txt.nodeName);           //#text

    console.log("--------------");

    //获取nodeValue
    console.log(element.nodeValue);     //null
    console.log(attribute.nodeValue);   //box1
    console.log(txt.nodeValue);         //生命壹号
```
## 文档的加载

浏览器在加载一个页面时，是按照自上向下的顺序加载的，读取到一行就运行一行。如果将script标签写到页面的上边，在代码执行时，页面还没有加载，页面没有加载DOM对象也没有加载，会导致无法获取到DOM对象。

**onload 事件**：

onload 事件会在整个页面加载完成之后才触发。为 window 绑定一个onload事件，该事件对应的响应函数将会在页面加载完成之后执行，这样可以确保我们的代码执行时所有的DOM对象已经加载完毕了。

代码举例：

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title></title>
    <script type="text/javascript">
      // 【方式一：先加载，后执行】这段 js 代码是写在 <head> 标签里的，所以建议放在 window.onload 里面。
      window.onload = function() {
        // 获取id为btn的按钮
        var btn = document.getElementById("btn");
        // 为按钮绑定点击事件
        btn.onclick = function() {
          alert("hello");
        };
      };
    </script>
  </head>
  <body>
    <button id="btn">点我一下</button>

    <script type="text/javascript">
      // 【方式二：后加载，后执行】这段 js 代码是写在 <body> 标签里的，代码的位置是处在页面的下方。这么做，也可以确保：在页面加载完毕后，再执行 js 代码。

      // 获取id为btn的按钮
      var btn = document.getElementById("btn");
      // 为按钮绑定点击事件
      btn.onclick = function() {
        alert("hello");
      };
    </script>
  </body>
</html>


```

上方代码中，方式一和方式二均可以确保：在页面加载完毕后，再执行 js 代码。
## 通过style对象获取和设置行内样式
### style属性的获取和修改

在DOM当中，如果想设置样式，有两种形式：

- className（针对内嵌样式）
    
- style（针对行内样式）

style是一个对象，只能获取**行内样式**，不能获取内嵌的样式和外链的样式。例如：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        div {
            border: 6px solid red;
        }
    </style>
</head>
<body>

    <div class="box1" style="width: 200px;height: 100px;background-color: pink;"></div>

    <script>
        var box1 = document.getElementsByTagName("div")[0];

        console.log(box1.style.backgroundColor);
        console.log(box1.style.border);  //没有打印结果，因为这个属性不是行内样式
        console.log(typeof box1.style);  //因为是对象，所以打印结果是Object
        console.log(box1.style);         //打印结果是对象
    </script>
</body>
</html>
```

#### 通过 js 读取元素的样式

语法：（方式一）

```
    元素.style.样式名
```

备注：我们通过style属性读取的样式都是**行内样式**。

语法：（方式二）

```
    元素.style["属性"];  //格式

    box.style["width"];  //举例
```

方式二最大的优点是：可以给属性传递参数。
#### 通过 js 设置元素的样式

语法：

```
    元素.style.样式名 = 样式值;
```

举例：

```
    box1.style.width = "300px";
    box1.style.backgroundColor = "red"; // 驼峰命名法
```
备注：我们通过style属性设置的样式都是**行内样式**，而行内样式有较高的优先级。但是如果在样式中的其他地方写了`!important`，则此时`!important`会有更高的优先级。

#### style属性的注意事项

style属性需要注意以下几点：

（1）样式少的时候使用。

（2）style是对象。我们在上方已经打印出来，typeof的结果是Object。

（3）值是字符串，没有设置值是“”。

（4）命名规则，驼峰命名。

（5）只能获取行内样式，和内嵌和外链无关。

（6）box.style.cssText = “字符串形式的样式”。

`cssText`这个属性，其实就是把行内样式里面的值当做字符串来对待。在上方代码的基础之上，举例：

```
    <script>
        var box1 = document.getElementsByTagName("div")[0];

        //通过cssText一次性设置行内样式
        box1.style.cssText = "width: 300px;height: 300px;background-color: green;";

        console.log(box1.style.cssText);   //这一行更加可以理解,style是对象

    </script>
```

#### style的常用属性

style的常用属性包括：

- backgroundColor
    
- backgroundImage
    
- color
    
- width
    
- height
    
- border
    
- opacity 设置透明度 (IE8以前是filter: alpha(opacity=xx))
    

注意DOM对象style的属性和标签中style内的值不一样，因为在JS中，`-`不能作为标识符。比如：

- DOM中：backgroundColor
    
- CSS中：background-color
#### 通过 js 获取元素当前显示的样式

我们在上面的内容中，通过`元素.style.className`的方式只能获取**行内样式**。但是，有些元素，也写了**内嵌样式或外链样式**。

既然样式有这么多种，那么，如何获取元素当前显示的样式（包括行内样式、内嵌样式、外链样式）呢？我们接下来看一看。

#### 获取元素当前正在显示的样式

（1）w3c的做法：

```
    window.getComputedStyle("要获取样式的元素", "伪元素");
```

两个参数都是必须要有的。参数二中，如果没有伪元素就用 null 代替（一般都传null）。

（2）IE和opera的做法：

```
    obj.currentStyle;
```

注意：

- 如果当前元素没有设置该样式，则获取它的默认值。
    
- 该方法会返回一个**对象**，对象中封装了当前元素对应的样式，可以通过`对象.样式名`来读取具体的某一个样式。
    
- 通过currentStyle和getComputedStyle()读取到的样式都是只读的，不能修改，如果要修改必须通过style属性。
    

综合上面两种写法，就有了一种兼容性的写法，同时将其封装。代码举例如下：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            background-color: pink;
            /*border: 1px solid #000;*/
            padding: 10px;
        }
    </style>
</head>
<body>

<div style="width: 100px;height: 100px;"></div>

<script>

    var div1 = document.getElementsByTagName("div")[0];

    console.log(getStyle(div1, "width"));
    console.log(getStyle(div1, "padding"));
    console.log(getStyle(div1, "background-color"));

    /*
     * 兼容方法，获取元素当前正在显示的样式。
     * 参数：
     *      obj     要获取样式的元素
     *.     name    要获取的样式名
    */
    function getStyle(ele, attr) {
        if (window.getComputedStyle) {
            return window.getComputedStyle(ele, null)[attr];
        }
        return ele.currentStyle[attr];
    }

</script>
</body>
</html>
```
## JS动画
JS动画的主要内容如下：

1、三大家族和一个事件对象：

- 三大家族：offset/scroll/client。也叫三大系列。
    
- 事件对象/event（事件被触动时，鼠标和键盘的状态）（通过属性控制）。
    

2、动画(闪现/匀速/缓动)

3、冒泡/兼容/封装
### offset
js中有一套方便的**获取元素尺寸**的办法就是offset家族。offset家族包括：

- offsetWidth
    
- offsetHight
    
- offsetLeft
    
- offsetTop
    
- offsetParent

#### 1、offsetWidth 和 offsetHight

`offsetWidth` 和 `offsetHight`：获取元素的**宽高 + padding + border**，不包括margin。如下：

- offsetWidth = width + padding + border
    
- offsetHeight = Height + padding + border
    

这两个属性，他们绑定在了所有的节点元素上。获取元素之后，只要调用这两个属性，我们就能够获取元素节点的宽和高。
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
            padding: 10px;
            border: 10px solid #000;
            margin: 100px;
            background-color: pink;
        }
    </style>
</head>
<body>

<div class="box"></div>
<script>
    var div1 = document.getElementsByTagName("div")[0];

    console.log(div1.offsetHeight);          //打印结果：140（100+20+20）
    console.log(typeof div1.offsetHeight);   //打印结果：number

</script>
</body>
</html>
```

#### 2、offsetParent

`offsetParent`：获取当前元素的**定位父元素**。

- 如果当前元素的父元素，**有CSS定位**（position为absolute、relative、fixed），那么 `offsetParent` 获取的是**最近的**那个父元素。
    
- 如果当前元素的父元素，**没有CSS定位**（position为absolute、relative、fixed），那么`offsetParent` 获取的是**body**。
    


```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div class="box1" style="position: absolute;">
    <div class="box2" style="position: fixed;">
        <div class="box3"></div>
    </div>
</div>
<script>

    var box3 = document.getElementsByClassName("box3")[0];

    console.log(box3.offsetParent);
</script>
</body>
</html>
```

#### 3、offsetLeft 和 offsetTop

`offsetLeft`：当前元素相对于其**定位父元素**的水平偏移量。

`offsetTop`：当前元素相对于其**定位父元素**的垂直偏移量。

备注：从父亲的 padding 开始算起，父亲的 border 不算在内。

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        .box1 {
            width: 300px;
            height: 300px;
            padding: 100px;
            margin: 100px;
            position: relative;
            border: 100px solid #000;
            background-color: pink;
        }

        .box2 {
            width: 100px;
            height: 100px;
            background-color: red;
            /*position: absolute;*/
            /*left: 10px;*/
            /*top: 10px;*/
        }
    </style>
</head>
<body>
<div class="box1">
    <div class="box2" style="left: 10px"></div>
</div>

<script>

    var box2 = document.getElementsByClassName("box2")[0];

    //offsetTop和offsetLeft
    console.log(box2.offsetLeft);  //100
    console.log(box2.style.left);  //10px


</script>

</body>
</html>
```
在父盒子有定位的情况下，offsetLeft == style.left(去掉px之后)。

 
 offsetLeft 和 style.left 区别

（1）最大区别在于：

offsetLeft 可以返回无定位父元素的偏移量。如果父元素中都没有定位，则body为准。

style.left 只能获取行内样式，如果父元素中都没有设置定位，则返回""（意思是，返回空字符串）;

（2）offsetTop 返回的是数字，而 style.top 返回的是字符串，而且还带有单位：px。

比如：

```

div.offsetLeft = 100;
div.style.left = "100px";

```

（3）offsetLeft 和 offsetTop **只读**，而 style.left 和 style.top 可读写（只读是获取值，可写是修改值）

总结：我们一般的做法是：**用offsetLeft 和 offsetTop 获取值，用style.left 和 style.top 赋值**（比较方便）。理由如下：

- style.left：只能获取行内式，获取的值可能为空，容易出现NaN。
    
- offsetLeft：获取值特别方便，而且是现成的number，方便计算。它是只读的，不能赋值。

### 动画的种类
- 闪现（基本不用）
    
- 匀速（本文重点）
    
- 缓动（后续重点）
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
            position: absolute;
        }
    </style>
</head>
<body>
<button>动画</button>
<div class="box" style="left: 0px"></div>

<script>
    var btn = document.getElementsByTagName("button")[0];
    var div = document.getElementsByTagName("div")[0];

    //1、闪动
    //    btn.onclick = function () {
    //        div.style.left = "500px";
    //    }

    //2、匀速运动
    btn.onclick = function () {
        //定时器，每隔一定的时间向右走一些
        setInterval(function () {
            console.log(parseInt(div.style.left));
            //动画原理： 盒子未来的位置 = 盒子现在的位置 + 步长；
            //方法1：用offsetLeft获取值，用style.left赋值。
            div.style.left = div.offsetLeft + 100 + 'px';

            // 方法2：必须一开始就在DOM节点上添加 style="left: 0px;"属性，才能用方法2。否则， div.style.left 的值为 NaN
            // div.style.left = parseInt(div.style.left)+100+"px";  //方法2：
        }, 500);
    };
</script>
</body>
</html>
```

匀速动画的封装：每间隔30ms，移动盒子10px
```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        .box1 {
            margin: 0;
            padding: 5px;
            height: 300px;
            background-color: #ddd;
            position: relative;
        }

        button {
            margin: 5px;
        }

        .box2 {
            width: 100px;
            height: 100px;
            background-color: red;
            position: absolute;
            left: 195px;
            top: 40px;
        }

        .box3 {
            width: 100px;
            height: 100px;
            background-color: yellow;
            position: absolute;
            left: 0;
            top: 150px;
        }
    </style>
</head>
<body>
<div class="box1">
    <button>运动到 left = 200px</button>
    <button>运动到 left = 400px</button>
    <div class="box2"></div>
    <div class="box3"></div>
</div>

<script>
    var btnArr = document.getElementsByTagName("button");
    var box2 = document.getElementsByClassName("box2")[0];
    var box3 = document.getElementsByClassName("box3")[0];

    //绑定事件
    btnArr[0].onclick = function () {
        //如果有一天我们要传递另外一个盒子，那么我们的方法就不好用了
        //所以我们要增加第二个参数，被移动的盒子本身。
        animate(box2, 200);
        animate(box3, 200);
    }

    btnArr[1].onclick = function () {
        animate(box2, 400);
        animate(box3, 400);
    }

    //【重要】方法的封装：每间隔30ms，将盒子向右移动10px
    function animate(ele, target) {
        //要用定时器，先清除定时器
        //一个盒子只能有一个定时器，这样的话，不会和其他盒子出现定时器冲突
        //我们可以把定时器本身，当成为盒子的一个属性
        clearInterval(ele.timer);
        //我们要求盒子既能向前又能向后，那么我们的步长就得有正有负
        //目标值如果大于当前值取正，目标值如果小于当前值取负
        var speed = target > ele.offsetLeft ? 10 : -10;  //speed指的是步长
        ele.timer = setInterval(function () {
            //在执行之前就获取当前值和目标值之差
            var val = target - ele.offsetLeft;
            ele.style.left = ele.offsetLeft + speed + "px";
            //移动的过程中，如果目标值和当前值之差如果小于步长，那么就不能在前进了
            //因为步长有正有负，所有转换成绝对值来比较
            if (Math.abs(val) < Math.abs(speed)) {
                ele.style.left = target + "px";
                clearInterval(ele.timer);
            }
        }, 30)
    }
</script>
</body>
</html>
```

上方代码中的方法封装，可以作为一个模板步骤，要记住。其实，这个封装的方法，写成下面这样，会更严谨，更容易理解：（将if语句进行了改进）

```
    //【重要】方法的封装：每间隔30ms，将盒子向右移动10px
    function animate(ele, target) {
        //要用定时器，先清除定时器
        //一个盒子只能有一个定时器，这样的话，不会和其他盒子出现定时器冲突
        //我们可以把定时器本身，当成为盒子的一个属性
        clearInterval(ele.timer);
        //我们要求盒子既能向前又能向后，那么我们的步长就得有正有负
        //目标值如果大于当前值取正，目标值如果小于当前值取负
        var speed = target > ele.offsetLeft ? 10 : -10;  //speed指的是步长
        ele.timer = setInterval(function () {
            //在执行之前就获取当前值和目标值之差
            var val = target - ele.offsetLeft;

            //移动的过程中，如果目标值和当前值之差如果小于步长，那么就不能在前进了
            //因为步长有正有负，所有转换成绝对值来比较
            if (Math.abs(val) < Math.abs(speed)) {  //如果val小于步长，则直接到达目的地；否则，每次移动一个步长
                ele.style.left = target + "px";
                clearInterval(ele.timer);
            } else {
                ele.style.left = ele.offsetLeft + speed + "px";
            }
        }, 30)
    }
```

代码举例：轮播图的实现

完整版代码如下：（注释已经比较详细）

```
<!doctype html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>无标题文档</title>
    <style type="text/css">
        * {
            padding: 0;
            margin: 0;
            list-style: none;
            border: 0;
        }

        .all {
            width: 500px;
            height: 200px;
            padding: 7px;
            border: 1px solid #ccc;
            margin: 100px auto;
            position: relative;
        }

        .screen {
            width: 500px;
            height: 200px;
            overflow: hidden;
            position: relative;
        }

        .screen li {
            width: 500px;
            height: 200px;
            overflow: hidden;
            float: left;
        }

        .screen ul {
            position: absolute;
            left: 0;
            top: 0px;
            width: 3000px;
        }

        .all ol {
            position: absolute;
            right: 10px;
            bottom: 10px;
            line-height: 20px;
            text-align: center;
        }

        .all ol li {
            float: left;
            width: 20px;
            height: 20px;
            background: #fff;
            border: 1px solid #ccc;
            margin-left: 10px;
            cursor: pointer;
        }

        .all ol li.current {
            background: yellow;
        }

        #arr {
            display: none;
        }

        #arr span {
            width: 40px;
            height: 40px;
            position: absolute;
            left: 5px;
            top: 50%;
            margin-top: -20px;
            background: #000;
            cursor: pointer;
            line-height: 40px;
            text-align: center;
            font-weight: bold;
            font-family: '黑体';
            font-size: 30px;
            color: #fff;
            opacity: 0.3;
            border: 1px solid #fff;
        }

        #arr #right {
            right: 5px;
            left: auto;
        }
    </style>

    <script>
        window.onload = function () {

            //需求：无缝滚动。
            //思路：赋值第一张图片放到ul的最后，然后当图片切换到第五张的时候
            //     直接切换第六章，再次从第一张切换到第二张的时候先瞬间切换到
            //     第一张图片，然后滑动到第二张
            //步骤：
            //1.获取事件源及相关元素。（老三步）
            //2.复制第一张图片所在的li,添加到ul的最后面。
            //3.给ol中添加li，ul中的个数-1个，并点亮第一个按钮。
            //4.鼠标放到ol的li上切换图片
            //5.添加定时器
            //6.左右切换图片（鼠标放上去隐藏，移开显示）


            //1.获取事件源及相关元素。（老三步）
            var all = document.getElementById("all");
            var screen = all.firstElementChild || all.firstChild;
            var imgWidth = screen.offsetWidth;
            var ul = screen.firstElementChild || screen.firstChild;
            var ol = screen.children[1];
            var div = screen.lastElementChild || screen.lastChild;
            var spanArr = div.children;

            //2.复制第一张图片所在的li,添加到ul的最后面。
            var ulNewLi = ul.children[0].cloneNode(true);
            ul.appendChild(ulNewLi);
            //3.给ol中添加li，ul中的个数-1个，并点亮第一个按钮。
            for (var i = 0; i < ul.children.length - 1; i++) {
                var olNewLi = document.createElement("li");
                olNewLi.innerHTML = i + 1;
                ol.appendChild(olNewLi)
            }
            var olLiArr = ol.children;
            olLiArr[0].className = "current";

            //4.鼠标放到ol的li上切换图片
            for (var i = 0; i < olLiArr.length; i++) {
                //自定义属性，把索引值绑定到元素的index属性上
                olLiArr[i].index = i;
                olLiArr[i].onmouseover = function () {
                    //排他思想
                    for (var j = 0; j < olLiArr.length; j++) {
                        olLiArr[j].className = "";
                    }
                    this.className = "current";
                    //鼠标放到小的方块上的时候索引值和key以及square同步
//                    key = this.index;
//                    square = this.index;
                    key = square = this.index;
                    //移动盒子
                    animate(ul, -this.index * imgWidth);
                }
            }

            //5.添加定时器
            var timer = setInterval(autoPlay, 1000);

            //固定向右切换图片
            //两个定时器（一个记录图片，一个记录小方块）
            var key = 0;
            var square = 0;

            function autoPlay() {
                //通过控制key的自增来模拟图片的索引值，然后移动ul
                key++;
                if (key > olLiArr.length) {
                    //图片已经滑动到最后一张，接下来，跳转到第一张，然后在滑动到第二张
                    ul.style.left = 0;
                    key = 1;
                }
                animate(ul, -key * imgWidth);
                //通过控制square的自增来模拟小方块的索引值，然后点亮盒子
                //排他思想做小方块
                square++;
                if (square > olLiArr.length - 1) {//索引值不能大于等于5，如果等于5，立刻变为0；
                    square = 0;
                }
                for (var i = 0; i < olLiArr.length; i++) {
                    olLiArr[i].className = "";
                }
                olLiArr[square].className = "current";
            }

            //鼠标放上去清除定时器，移开后在开启定时器
            all.onmouseover = function () {
                div.style.display = "block";
                clearInterval(timer);
            }
            all.onmouseout = function () {
                div.style.display = "none";
                timer = setInterval(autoPlay, 1000);
            }

            //6.左右切换图片（鼠标放上去显示，移开隐藏）
            spanArr[0].onclick = function () {
                //通过控制key的自增来模拟图片的索引值，然后移动ul
                key--;
                if (key < 0) {
                    //先移动到最后一张，然后key的值取之前一张的索引值，然后在向前移动
                    ul.style.left = -imgWidth * (olLiArr.length) + "px";
                    key = olLiArr.length - 1;
                }
                animate(ul, -key * imgWidth);
                //通过控制square的自增来模拟小方块的索引值，然后点亮盒子
                //排他思想做小方块
                square--;
                if (square < 0) {//索引值不能大于等于5，如果等于5，立刻变为0；
                    square = olLiArr.length - 1;
                }
                for (var i = 0; i < olLiArr.length; i++) {
                    olLiArr[i].className = "";
                }
                olLiArr[square].className = "current";
            }
            spanArr[1].onclick = function () {
                //右侧的和定时器一模一样
                autoPlay();
            }


            function animate(ele, target) {
                clearInterval(ele.timer);
                var speed = target > ele.offsetLeft ? 10 : -10;
                ele.timer = setInterval(function () {
                    var val = target - ele.offsetLeft;
                    ele.style.left = ele.offsetLeft + speed + "px";

                    if (Math.abs(val) < Math.abs(speed)) {
                        ele.style.left = target + "px";
                        clearInterval(ele.timer);
                    }
                }, 10)
            }
        }
    </script>
</head>

<body>
<div class="all" id='all'>
    <div class="screen" id="screen">
        <ul id="ul">
            <li><img src="images/1.jpg" width="500" height="200"/></li>
            <li><img src="images/2.jpg" width="500" height="200"/></li>
            <li><img src="images/3.jpg" width="500" height="200"/></li>
            <li><img src="images/4.jpg" width="500" height="200"/></li>
            <li><img src="images/5.jpg" width="500" height="200"/></li>
        </ul>
        <ol>

        </ol>
        <div id="arr">
            <span id="left"><</span>
            <span id="right">></span>
        </div>
    </div>
</div>
</body>
</html>


```

### scroll相关属性
#### window.onscroll() 方法

当我们用鼠标滚轮，滚动网页的时候，会触发 window.onscroll() 方法。
#### 1、ScrollWidth 和 scrollHeight

`ScrollWidth` 和 `scrollHeight`：获取元素**整个滚动区域**的宽、高。包括 width 和 padding，不包括 border和margin。

**注意**：

`scrollHeight` 的特点是：如果内容超出了盒子，`scrollHeight`为内容的高（包括超出的内容）；如果不超出，`scrollHeight`为盒子本身的高度。`ScrollWidth`同理。
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
            padding: 10px;
            margin: 3px;
            border: 8px solid red;
        }
    </style>
</head>
<body>

<div class="box">
    静，能寒窗苦守；动，能点石成金。
    静，能寒窗苦守；动，能点石成金。
    静，能寒窗苦守；动，能点石成金。
    静，能寒窗苦守；动，能点石成金。
    静，能寒窗苦守；动，能点石成金。
    静，能寒窗苦守；动，能点石成金。
</div>
<script>

    var div = document.getElementsByTagName("div")[0];

    // `scrollHeight` 的特点是：如果内容超出了盒子，`scrollHeight`为内容的高（包括超出的内容）；如果不超出，`scrollHeight`为盒子本身的高度。
    //IE8以下（不包括IE8），为盒子本身内容的高度。
    console.log(div.scrollWidth);
    console.log(div.scrollHeight);

</script>
</body>
</html>
```
#### 2、scrollTop 和 scrollLeft

- `scrollLeft`：获取水平滚动条滚动的距离。
    
- `scrollTop`：获取垂直滚动条滚动的距离。
    

**实战经验**：

当某个元素满足`scrollHeight - scrollTop == clientHeight`时，说明垂直滚动条滚动到底了。

当某个元素满足`scrollWidth - scrollLeft == clientWidth`时，说明水平滚动条滚动到底了。

#### scrollTop 的兼容性

如果要获取页面滚动的距离，scrollTop 这个属性的写法要注意兼容性，如下。

（1）如果文档没有 DTD 声明，写法为：

```
    document.body.scrollTop
```

在没有 DTD 声明的情况下，要求是这种写法，chrome浏览器才能认出来。

（2）如果文档有 DTD 声明，写法为：

```
   document.documentElement.scrollTop
```

在有 DTD 声明的情况下，要求是这种写法，IE6、7、8才能认出来。

综合上面这两个，就诞生了一种兼容性的写法：

```
    document.body.scrollTop || document.documentElement.scrollTop //方式一

    document.body.scrollTop + document.documentElement.scrollTop  //方式二
```

另外还有一种兼容性的写法：`window.pageYOffset` 和 `window.pageXOffset`。这种写法无视DTD的声明。这种写法支持的浏览器版本是：火狐/谷歌/ie9+。

综合上面的几种写法，为了兼容，不管有没有DTD，**最终版的兼容性写法：**

```
    window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop;
```

#### 判断是否已经 DTD 声明

方法如下：

```
    document.compatMode === "CSS1Compat"   // 已声明
    document.compatMode === "BackCompat"   // 未声明
```

#### 将 scrollTop 和 scrollLeft 进行封装

这里，我们将 scrollTop 和 scrollLeft 封装为一个方法，名叫scroll()，返回值为 一个对象。以后就直接调用`scroll().top` 和 `scroll().left`就好。

代码实现：

```
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        body {
            height: 6000px;
            width: 5000px;
        }
    </style>
</head>
<body>

<script>

    //需求：封装一个兼容的scroll().返回的是对象，用scroll().top获取scrollTop，用scroll().left获取scrollLeft

    window.onscroll = function () {
//        var myScroll = scroll();
//        myScroll.top;
        console.log(scroll().top);
        console.log(scroll().left);
    }

    //函数封装（简单封装，实际工作使用）
    function scroll() {
        return { //此函数的返回值是对象
            left: window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop,
            right: window.pageXOffset || document.body.scrollLeft || document.documentElement.scrollLeft
        }
    }
</script>
</body>
</html>
```

上方代码中，函数定义的那部分就是要封装的代码。

另外还有一种比较麻烦的封装方式：（仅供参考）

```
function scroll() {  // 开始封装自己的scrollTop
    if(window.pageYOffset !== undefined) {  // ie9+ 高版本浏览器
        // 因为 window.pageYOffset 默认的是  0  所以这里需要判断
        return {
            left: window.pageXOffset,
            top: window.pageYOffset
        }
    }
    else if(document.compatMode === "CSS1Compat") {    // 标准浏览器   来判断有没有声明DTD
        return {
            left: document.documentElement.scrollLeft,
            top: document.documentElement.scrollTop
        }
    }
    return {   // 未声明 DTD
        left: document.body.scrollLeft,
        top: document.body.scrollTop
    }
}
```

#### 获取 html 文档的方法
获取title、body、head、html标签的方法如下：

- `document.title` 文档标题；
    
- `document.head` 文档的头标签
    
- `document.body` 文档的body标签；
    
- `document.documentElement` （这个很重要）。
    

`document.documentElement`表示文档的html标签。也就是说，基本结构当中的 `html 标签`而是通过`document.documentElement`访问的，并不是通过 document.html 去访问的。

#### scrollTop 举例：固定导航栏

完整版代码实现：

（1）index.html：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        * {
            margin: 0;
            padding: 0
        }

        img {
            vertical-align: top;
        }

        .main {
            margin: 0 auto;
            width: 1000px;
            margin-top: 10px;

        }

        #Q-nav1 {
            overflow: hidden;
        }

        .fixed {
            position: fixed;
            top: 0;
            left: 0;
        }
    </style>

    <!--引入工具js-->
    <script src="tools.js"></script>
    <script>
        window.onload = function () {
            //需求1：当我们滚动界面的时候，被卷曲的头部如果超过第二个盒子距离顶部的位置，那么直接给第二个盒子加类名.fixed
            //需求2：当我们滚动界面的时候，被卷曲的头部如果小于第二个盒子距离顶部的位置，那么直接给第二个盒子取消类名.fixed

            //1.老三步。
            var topDiv = document.getElementById("top");
            var height = topDiv.offsetHeight;
            var middle = document.getElementById("Q-nav1");
            var main = document.getElementById("main");

            window.onscroll = function () {
                //2.判断 ，被卷曲的头部的大小
                if (scroll().top > height) {
                    //3.满足条件添加类，否则删除类
                    middle.className += " fixed";
                    //第二个盒子也要占位置，为了避免重叠，我们给第三个盒子一个上padding的空间，把这个空间留给第二个盒子
                    main.style.paddingTop = middle.offsetHeight + "px";
                } else {
                    middle.className = "";
                    //清零
                    main.style.paddingTop = 0;
                }
            }

        }
    </script>
</head>
<body>
<div class="top" id="top">
    <img src="images/top.png" alt=""/>
</div>
<div id="Q-nav1">
    <img src="images/nav.png" alt=""/>
</div>
<div class="main" id="main">
    <img src="images/main.png" alt=""/>
</div>
</body>
</html>

```

上方代码中，有一个技巧：

```
main.style.paddingTop = middle.offsetHeight + "px";
```

仔细看注释就好。

（2）tools.js：

```
/**
 * Created by smyhvae on 2018/02/03.
 */
function scroll() {  // 开始封装自己的scrollTop
    if (window.pageYOffset !== undefined) {  // ie9+ 高版本浏览器
        // 因为 window.pageYOffset 默认的是  0  所以这里需要判断
        return {
            left: window.pageXOffset,
            top: window.pageYOffset
        }
    }
    else if (document.compatMode === "CSS1Compat") {    // 标准浏览器   来判断有没有声明DTD
        return {
            left: document.documentElement.scrollLeft,
            top: document.documentElement.scrollTop
        }
    }
    return {   // 未声明 DTD
        left: document.body.scrollLeft,
        top: document.body.scrollTop
    }
}
```

### 缓动动画

缓慢动画里，我们要用到三个函数，这里先列出来：

- Math.ceil() 向上取整
    
- Math.floor() 向下取整
    
- Math.round(); 四舍五入
    

#### 缓动动画的原理

缓动动画的原理就是：在移动的过程中，步长越来越小。

设置步长为：**目标位置和盒子当前位置的十分之一**。用公式表达，即：

```
    盒子位置 = 盒子本身位置 + (目标位置 - 盒子本身位置)/ 10；
```

代码举例：

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
            position: absolute;
        }
    </style>
</head>
<body>
<button>运动到left = 400px</button>
<div></div>

<script>

    var btn = document.getElementsByTagName("button")[0];
    var div = document.getElementsByTagName("div")[0];

    btn.onclick = function () {
        setInterval(function () {
            //动画原理：盒子未来的位置 = 盒子当前的位置+步长
            div.style.left = div.offsetLeft + (400 - div.offsetLeft) / 10 + "px";
        }, 30);
    }

</script>
</body>
</html>
```

#### window.scrollTo()方法举例：返回到顶部小火箭

（1）index.html：

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        img {
            position: fixed;
            bottom: 100px;
            right: 50px;
            cursor: pointer;
            display: none;
            border: 1px solid #000;
        }

        div {
            width: 1210px;
            margin: 100px auto;
            text-align: center;
            font: 500 26px/35px "simsun";
            color: red;
        }
    </style>
    <script src="tools.js"></script>
    <script>
        window.onload = function () {
            //需求：被卷去的头部超过100显示小火箭，然后点击小火箭屏幕缓慢移动到最顶端。
            //难点：我们以前是移动盒子，现在是移动屏幕，我们没有学过如何移动屏幕。
            //      技术点：window.scrollTo(x,y);浏览器显示区域跳转到指定的坐标
            //步骤：
            //1.老三步
            var img = document.getElementsByTagName("img")[0];
            window.onscroll = function () {
                //被卷去的距离大于200显示小火箭，否则隐藏
                //2.显示隐藏小火箭
                if (scroll().top > 1000) {
                    img.style.display = "block";
                } else {
                    img.style.display = "none";
                }
                //每次移动滚动条的时候都给leader赋值，模拟leader获取距离顶部的距离
                leader = scroll().top;
            }
            //3.缓动跳转到页面最顶端（利用我们的缓动动画）
            var timer = null;
            var target = 0; //目标位置
            var leader = 0; //显示区域自身的位置
            img.onclick = function () {
                //技术点：window.scrollTo(0,0);
                //要用定时器，先清定时器
                clearInterval(timer);
                timer = setInterval(function () {
                    //获取步长
                    var step = (target - leader) / 10;
                    //二次处理步长
                    step = step > 0 ? Math.ceil(step) : Math.floor(step);
                    leader = leader + step; //往上移动的过程中，step是负数。当前位置减去步长，就等于下一步的位置。
                    //显示区域移动
                    window.scrollTo(0, leader);
                    //清除定时器
                    if (leader === 0) {
                        clearInterval(timer);
                    }
                }, 25);
            }
        }
    </script>
</head>
<body>
<img src="images/Top.jpg"/>
<div>
    我是最顶端.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>
    生命壹号，永不止步.....<br>

</div>
</body>
</html>
```

（2）tools.js:

```
/**
 * Created by smyhvae on 2015/12/8.
 */

//函数：获取scrollTop和scrollLeft的值
function scroll() {  // 开始封装自己的scrollTop
    if (window.pageYOffset != null) {  // ie9+ 高版本浏览器
        // 因为 window.pageYOffset 默认的是  0  所以这里需要判断
        return {
            left: window.pageXOffset,
            top: window.pageYOffset
        }
    }
    else if (document.compatMode === "CSS1Compat") {    // 标准浏览器   来判断有没有声明DTD
        return {
            left: document.documentElement.scrollLeft,
            top: document.documentElement.scrollTop
        }
    }
    return {   // 未声明 DTD
        left: document.body.scrollLeft,
        top: document.body.scrollTop
    }
}
```

### client（可视区）相关属性
#### clientWidth 和 clientHeight

元素调用时：

- clientWidth：获取元素的可见宽度（width + padding）。
    
- clientHeight：获取元素的可见高度（height + padding）。
    

body/html 调用时：

- clientWidth：获取网页可视区域宽度。
    
- clientHeight：获取网页可视区域高度。
    

**声明**：

- `clientWidth` 和 `clientHeight` 属性是只读的，不可修改。
    
- `clientWidth` 和 `clientHeight` 的值都是不带 px 的，返回的都是一个数字，可以直接进行计算。
    

#### clientX 和 clientY

event调用：

- clientX：鼠标距离可视区域左侧距离。
    
- clientY：鼠标距离可视区域上侧距离。
    

#### clientTop 和 clientLeft

- clientTop：盒子的上border。
    
- clientLeft：盒子的左border。
    

### 三大家族 offset/scroll/client 的区别

区别1：宽高

- offsetWidth = width + padding + border
    
- offsetHeight = height + padding + border
    
- scrollWidth = 内容宽度（不包含border）
    
- scrollHeight = 内容高度（不包含border）
    
- clientWidth = width + padding
    
- clientHeight = height + padding
    

区别2：上左

offsetTop/offsetLeft：

- 调用者：任意元素。(盒子为主)
- 作用：距离父系盒子中带有定位的距离。

scrollTop/scrollLeft：

- 调用者：document.body.scrollTop（window调用）(盒子也可以调用，但必须有滚动条)
- 作用：浏览器无法显示的部分（被卷去的部分）。

clientY/clientX：

- 调用者：event
- 作用：鼠标距离浏览器可视区域的距离（左、上）。

函数封装：获取浏览器的宽高（可视区域）

函数封装如下：

```
//函数封装：获取屏幕可视区域的宽高
function client() {
    if (window.innerHeight !== undefined) {
        //ie9及其以上的版本的写法
        return {
            "width": window.innerWidth,
            "height": window.innerHeight
        }
    } else if (document.compatMode === "CSS1Compat") {
        //标准模式的写法（有DTD时）
        return {
            "width": document.documentElement.clientWidth,
            "height": document.documentElement.clientHeight
        }
    } else {
        //没有DTD时的写法
        return {
            "width": document.body.clientWidth,
            "height": document.body.clientHeight
        }
    }
}

```

**案例：根据浏览器的可视宽度，给定不同的背景的色。**

> PS：这个可以用来做响应式。

代码如下：（需要用到上面的封装好的方法）

```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

<script src="tools.js"></script>
<script>
    //需求：浏览器每次更改大小，判断是否符合某一标准然后给背景上色。
    //  // >960红色，大于640小于960蓝色，小于640绿色。

    window.onresize = fn;  //页面大小发生变化时，执行该函数。
    //页面加载的时候直接执行一次函数，确定浏览器可视区域的宽，给背景上色
    fn();

    //封装成函数，然后指定的时候去调用和绑定函数名
    function fn() {
        if (client().width > 960) {
            document.body.style.backgroundColor = "red";
        } else if (client().width > 640) {
            document.body.style.backgroundColor = "blue";
        } else {
            document.body.style.backgroundColor = "green";
        }
    }
</script>
</body>
</html>
```

上当代码中，`window.onresize`事件指的是：在窗口或框架被调整大小时发生。各个事件的解释如下：

- window.onscroll 屏幕滑动
    
- window.onresize 浏览器大小变化
    
- window.onload 页面加载完毕
    
- div.onmousemove 鼠标在盒子上移动（注意：不是盒子移动）
    

获取显示器的分辨率

比如，我的电脑的显示器分辨率是：1920*1080。

获取显示器的分辨率：

```
    window.onresize = function () {
        document.title = window.screen.width + "    " + window.screen.height;
    }
```
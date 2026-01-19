HTML，即超文本标记语言，是一种用于创建网页的标记语言。当你访问一个网站并看到段落、标题、链接、图像和视频等内容时，这些就是HTML。
- HTML（HyperText Markup Language）：超文本标记语言。从**语义**的角度描述页面的**结构**。相当于人的身体组织结构。
- CSS（Cascading Style Sheets）：层叠样式表。从**审美**的角度美化页面的**样式**。相当于人的衣服和打扮。
- JavaScript（简称JS）：从**交互**的角度描述页面的**行为**，实现业务逻辑和页面控制。相当于人的动作，让人有生命力。
再比如：
HTML 相当于人的身体组织结构：
![[Pasted image 20260118144623.png]]
CSS 相当于人的衣服和打扮：
![[Pasted image 20260118144705.png]]
JS 相当于人的行为：
![[20200322_2220.gif]]
## HTML基础
### 初识html
HTML 是超文本标记语言 (Hypertext Markup Language) 的缩写，是一种用于创建网页的标记语言。HTML 不是一种编程语言，是一种描述性的**标记语言**。当您访问网站并看到段落、标题、链接、图片和视频等内容时，这些内容就是 HTML。
* *概念：超文本*
有两层含义：
（1）图片、音频、视频、动画、多媒体等内容，被称为超文本，因为它们超出了文本的限制。
（2）不仅如此，它还可以从一个文件跳转到另一个文件，与世界各地主机的文件进行连接。即：超级链接文本。
* 标记语言
（1）**标记语言是一套标记标签**。比如：标签`<a>`表示超链接、标签`<img>`表示图片、标签`<h1>`表示一级标题等等，它们都是属于 HTML 标签。说的通俗一点就是：网页是由网页元素组成的，这些元素是由 HTML 标签描述出来，然后通过浏览器解析，就可以显示给用户看了。

（2）编程语言是有编译过程的，而标记语言没有编译过程，HTML标签是直接由浏览器解析执行。

- 网页 ：由各种标记组成的一个页面就叫网页。
- 主页(首页) : 一个网站的起始页面或者导航页面。
- 标记： 比如`<p>`称为开始标记 ，`</p>`称为结束标记，也叫标签。每个标签都规定好了特殊的含义。
- 元素：比如`<p>内容</p>`称为元素.
- 属性：给每一个标签所做的辅助信息。
- XHTML：符合XML语法标准的HTML。
- DHTML：dynamic，动态的。`javascript + css + html`合起来的页面就是一个 DHTML。
- HTTP：超文本传输协议。用来规定客户端浏览器和服务端交互时数据的一个格式。SMTP：邮件传输协议，FTP：文件传输协议。
### 语法
HTML 通过使用元素来表示网页的内容和结构。大多数元素都有一个开始标签和一个结束标签。有时，这些标签也被称为开始和结束标签。在这两个标签之间，是内容。这些内容可以是文本或其他 HTML 元素。
```html
<elementName>Content goes here</elementName>
```
起始标签和结束标签均以左尖括号 ( `<`) 开头，以右尖括号 ( `>`) 结尾，标签名称位于这两个尖括号之间。虽然 HTML 标签名称不区分大小写，但使用小写字母书写是广泛接受的惯例和最佳实践。

开始标签和结束标签的区别在于，结束标签的左尖括号后面紧跟一个斜杠（`/``\`）。有些 HTML 元素没有结束标签，这些元素被称为单标签。
```html
<img>

<img />

```

- **HTML 的作用**：HTML（超文本标记语言）是网页结构的基础，定义了网页的元素。

- **HTML元素**：用于表示页面上的内容。它们大多由一个开始标签和一个结束标签组成

- **HTML 结构**：HTML 由 `<head>`和` <body`>组成body，其中元数据、样式和内容都以结构化的方式呈现。
```html
 <!DOCTYPE html>
  <html lang="en">
	  <head>
		  <!--头部信息-->
		  <meta charset="utf-8">
		  <meta name="viewport" content="width=device-width,initial-scale=1.0">
		  <title>窗口标签</title>
	  </head>
	  <body>主体信息</body>
  </html>
```


- `<!DOCTYPE html>`文档声明头
任何一个标准的HTML页面，第一行一定是一个以`<!DOCTYPE ……>`开头的语句。这一行，就是文档声明头，即 DocType Declaration，简称DTD。
**DTD可告知浏览器文档使用哪种 HTML 或 XHTML 规范**。

| 标签名               | 定义     | 说明                             |
| ----------------- | ------ | ------------------------------ |
| `<html></html>`   | HTML标签 | 页面中最大的标签，我们成为根标签               |
| `<head></head>`   | 文档的头部  | 注意在head标签中我们必须要设置的标签是title     |
| `<title></title>` | 文档的标题  | 让页面拥有一个属于自己的网页标题               |
| `<body></body>`   | 文档的主体  | 元素包含文档的所有内容，页面内容 基本都是放到body里面的 |
* 页面语言 `lang`
最常见的语言类型有两种：
en：定义页面语言为英语。
zh-CN：定义页面语言为中文。
- 基本语法特性
（1）HTML对换行不敏感，对tab不敏感
HTML只在乎标签的嵌套结构，嵌套的关系。谁嵌套了谁，谁被谁嵌套了，和换行、tab无关。换不换行、tab不tab，都不影响页面的结构。
也就是说，HTML不是依靠缩进来表示嵌套的，而是看标签的嵌套关系。但是，我们发现有良好的缩进，代码更易读。建议大家都正确缩进标签。
![[Pasted image 20260118201000.png]]
 2）空白折叠现象
HTML中所有的**文字之间**，如果有空格、换行、tab都将被折叠为一个空格显示。
3）标签要严格封闭

标签不封闭的结果是灾难性的。
### 属性
属性是放置在 HTML 元素的开始标记内的值。属性与标记之间、各属性之间需要以空格隔开。属性提供有关元素的附加信息或指定元素的行为方式。以下是属性的基本语法：
```html
<element attribute="value"></element>
```
属性名称后跟等号 ( `=`) 和用引号括起来的值。该值可以是字符串或数字，具体取决于属性类型。
- ID ：HTML 元素的唯一元素标识符。每个 HTML 文档只能使用一次 ID 名称。
```HTML

# 属性
`id`
该`id`属性为 HTML 元素添加唯一标识符。
`h1`下面是带有 的元素`id`的示例`title`。

<h1 id="title">Movie Review Page</h1>
```
您可以在 JavaScript 或 CSS 中引用`id`的名称`title`。以下 CSS 示例引用 ，`id`将`title`文本更改`color`为`red`。
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>Review page Example</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <h1 id="title">Movie Review Page</h1>
  </body>
</html>
```
```css
#title {
  color: red;
}
```
`#`前面的井号 ( )`title`告诉计算机您希望使用`id`该值定位到 。`id`名称不应重复使用，并且应始终唯一。关于值，还有一点需要注意，即值中不能包含空格。以下是将单词和应用于属性值`id`的示例：`main``heading``id`
```html
<h1 id="main heading">Main heading</h1>
```
浏览器会将此空间视为其中的一部分，`id`这将在样式和脚本方面导致不必要的问题。`id`属性值应该只包含字母、数字、下划线和破折号。
- `class`
与属性相反`id`，`class`属性值不需要唯一并且可以包含空格。
```
html
<div class="box"></div>
```
如果您想为一个元素添加多个类名，可以用空格分隔它们。以下是一个将多个类名应用于一个`div`元素的更新示例。
```html
<div class="box red-box"></div>
```
### 计算机编码
计算机，不能直接存储文字，存储的是编码。

计算机只能处理二进制的数据，其它数据，比如：0-9、a-z、A-Z，这些字符，我们可以定义一套规则来表示。假如：A用110表示，B用111表示等。

**ASCII码：** 美国发布的，用1个字节(8位二进制)来表示一个字符，共可以表示2^8=256个字符。 美国的国家语言是英语，只要能表示0-9、a-z、A-Z、特殊符号。

**ANSI编码：** **每个国家为了显示本国的语言，都对ASCII码进行了扩展**。用2个字节(16位二进制)来表示一个汉字，共可以表示2^16＝65536个汉字。例如： 中国的ANSI编码是GB2312编码(简体)，对6763汉字进行编码，含600多特殊字符。另外还有GBK(简体)。 日本的ANSI编码是JIS编码。 台湾的ANSI编码是BIG5编码（繁体）。

**GBK：** 对GB2312进行了扩展，用来显示罕见的、古汉语的汉字。现在已经收录了2.1万左右。并提供了1890个汉字码位。K的含义就是“扩展”。

**Unicode编码(统一编码)：** 用4个字节(32位二进制)来表示一个字符，想法不错，但效率太低。例如，字母A用ASCII表示的话一个字节就够，可用Unicode编码的话，得用4个字节表示，造成了空间的极大浪费。A的Unicode编码是0000 0000 0000 0000 0000 0000 0100 0000

**UTF-8(Unicode Transform Format)编码：** 根据字符的不同，选择其编码的长度。比如：一个字符A用1个字节表示，一个汉字用2个字节表示。

毫无疑问，开发中，都用**UTF-8**编码吧，准没错。

**中文能够使用的字符集两种：**

- 第一种：UTF-8。UTF-8是国际通用字库，里面涵盖了所有地球上所有人类的语言文字，比如阿拉伯文、汉语、鸟语……
    
- 第二种：GBK（对GB2312进行了扩展）。gb2312 是国标，是中国的字库，里面**仅**涵盖了汉字和一些常用外文，比如日文片假名，和常见的符号。
    

字库规模： UTF-8（字很全） > gb2312（只有汉字）

**重点1：避免乱码**

我们用meta标签声明的当前这个html文档的字库，一定要和保存的文件编码类型一样，否则乱码（重点）。

拿 sublime编辑器举例，当我们不设置的时候，sublime默认类型就是UTF-8。而一旦更改为gb2312的时候，就一定要记得设置一下sublime的保存类型： `文件→ set File Encoding to → Chinese Simplified(GBK)`。VS Code 的道理一样。

**重点2：UTF-8和gb2312的比较**

保存大小：UTF-8（更臃肿、加载更慢） > gb2312 （更小巧，加载更快）

总结：

- UTF-8：字多，有各种国家的语言，但是保存尺寸大，文件臃肿；
- gb2312：字少，只用中文和少数外语和符号，但是尺寸小，文件小巧。

列出2个使用情形：

1） 你们公司是做日本动漫的，经常出现一些日语动漫的名字，网页要使用UTF-8。如果用gb2312将无法显示日语。 2） 你们公司就是中文网页，极度的追求网页的显示速度，要使用gb2312。如果使用UTF-8将每个汉字多一个byte，所以5000个汉字，多5kb。

我们亲测：

- qq网、网易、搜狐都是使用gb2312。这些公司，都追求显示速度。
- 新华网藏语频道，使用的是UTF-8，保证字符集的数量。

我们是怎么查看网页的编码方式的呢？在浏览器中打开网页，右键，选择“查看网页源代码”，找到meta标签中的charset属性即可。

那么，我们为什么可以查看网页的源代码呢？因为这个打开的html网页已经存到我的临时文件夹里了，临时文件夹里的html是纯文本文件，纯文本文件自然可以查看网页的源代码。

### 路径和链接行为

- **目标属性类型**：控制链接行为。
- **绝对路径与相对路径**：目录导航。
- **路径语法**：理解逗号`/`、句点`./`、方括号`../`等进行文件导航。
- **链接状态**：管理不同的链接交互（悬停、激活）。

### 语义化HTML的重要性

- **标题元素的结构层级**：使用正确的标题元素对于维护内容的结构层级至关重要。` `h1`<h1>` 元素是最高级别的标题，`<h2>``h6`元素是最低级别的标题。
- **展示型 HTML 元素**：定义内容外观的元素。例如，已弃用的 `<div>` `center`、 `<span> `big`` 和 ` `font`<div>` 元素。
- **语义化的 HTML 元素**：这些元素赋予内容结构意义。例如：
    - `<header>`：代表介绍性内容。
    - `<nav>`包含导航链接。
    - `<article>`：表示独立的内容。
    - `<aside>`用于侧边栏或相关内容。
    - `<section>`将文档中的相关内容分组。
    - `<footer>`：定义章节或文档的页脚。

## 标签

###  head标签
head元素用于包含有关文档的元数据，例如其标题、样式表链接和脚本。元数据是关于页面的信息，但不会直接显示在页面上。

头标签内部的常见标签如下：
- `<title>`：指定整个网页的标题，在浏览器最上方显示。
- `<base>`：为页面上的所有链接规定默认地址或默认目标。
- `<meta>`：提供有关页面的基本信息
- `<link>`：定义文档与外部资源的关系。
#### title标签
title元素决定浏览器在页面的标题栏或标签页中显示什么内

#### link 标签
  此元素用于链接到外部资源，例如样式表和站点图标。这是使用的基本语法 关联 外部 CSS 文件的元素：
```html
<link rel="stylesheet" href="./styles.css" />
```
rel属性用于指定链接资源和 HTML 文档之间的关系。
href属性用于指定外部资源的 URL 位置。
* 链接字体
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap"
  rel="stylesheet"
/>
```
* 链接到图标
```html
<link rel="icon" href="favicon.ico" />
```
网站图标（favicon）是“favourite icon”（最喜欢的图标）的缩写，它是一个通常显示在浏览器标签页网站标题旁边的小图标。许多网站会使用网站图标来展示其品牌标识。
#### meta标签
meta表示“元”。“元”配置，就是表示基本的配置项目。
常见的几种 meta 标签如下：

（1）字符集 charset：

```
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
```

字符集用meta标签中的`charset`定义，charset就是character set（即“字符集”），即**网页的编码方式**。

**字符集**(Character set)是多个字符的集合。计算机要准确的处理各种字符集文字，需要进行字符编码，以便计算机能够识别和存储各种文字。

上面这行代码非常关键， 是必须要写的代码，否则可能导致乱码。比如你保存的时候，meta写的和声明的不匹配，那么浏览器就是乱码。

utf-8是目前最常用的字符集编码方式，常用的字符集编码方式还有gbk和gb2312等。

（2）视口 viewport：

```
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

`width=device-width` ：表示视口宽度等于屏幕宽度。


（3）定义“关键词”：

举例如下：

```
<meta name="Keywords" content="网易,邮箱,游戏,新闻,体育,娱乐,女性,亚运,论坛,短信" />
```

这些关键词，就是告诉搜索引擎，这个网页是干嘛的，能够提高搜索命中率。让别人能够找到你，搜索到你。

（4）定义“页面描述”：

meta除了可以设置字符集，还可以设置关键字和页面描述。

只要设置Description页面描述，那么百度搜索结果，就能够显示这些语句，这个技术叫做**SEO**（search engine optimization，搜索引擎优化）。

设置页面描述的举例：

```
<meta name="Description" content="网易是中国领先的互联网技术公司，为用户提供免费邮箱、游戏、搜索引擎服务，开设新闻、娱乐、体育等30多个内容频道，及博客、视频、论坛等互动交流，网聚人的力量。" />
```

效果如下：

![[Pasted image 20260118151955.png]]

另外还有一个`<meta>`标签是需要记住的：

```
<meta http-equiv="refresh" content="3;http://www.baidu.com">
```

上面这个标签的意思是说，3秒之后，自动跳转到百度页面。
#### base标签
```html
<base href="/">
```
base 标签用于指定基础的路径。指定之后，所有的 a 链接都是以这个路径为基准。

### body标签
`<body>`标签的属性有：
- `bgcolor`：设置整个网页的背景颜色。
- `background`：设置整个网页的背景图片。
- `text`：设置网页中的文本颜色。
- `leftmargin`：网页的左边距。IE浏览器默认是8个像素。
- `topmargin`：网页的上边距。
- `rightmargin`：网页的右边距。
- `bottommargin`：网页的下边距。

### 布局标签
* `header`
用于定义文档或章节的头部。
```html
<header>
  <h1>Main Page Title Goes Here</h1>
  <img src="example-logo.png" alt="Example logo" />
</header>
```
* `nav`
nav元素用于提供文档或网站其他部分的导航链接。很多时候你会看到它被用作菜单或目录
```html
<nav>
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
```
* `main`
用于包含网页的主要内容
`article`
文章元素表示网页上的自包含内容。
```html
<article>
  <h1>Example heading</h1>
  <p>Example article text</p>
</article>
```

* `section`
用于将内容划分为更小的章节
section元素用于在文档中定义章节、页眉、页脚或任何其他部分。它是一个语义元素，有助于SEO和可访问性。
```html
<section>
  <h2>About Me</h2>
  <p>Hi, I am Jane Doe and I am a web developer.</p>
</section>
```
`section`在第一个元素下方添加另一个元素。然后在`section`元素内部添加一个`h2`和`p`元素。您可以使用任何您喜欢的文本，并在预览窗口中看到更改。
```html
<section>
  <h2>Mammals</h2>
  <p>Mammals are warm-blooded animals with fur or hair. Most give birth to live young.</p>
  <ul>
    <li>Lion</li>
    <li>Elephant</li>
    <li>Dolphin</li>
  </ul>
</section>
```
* `footer`
footer元素用于定义文档或章节的脚注。脚注通常包含关于文档作者的信息、版权数据、使用条款链接、联系信息等。

* `div`
此元素是一个通用的 HTML 元素，不包含任何语义含义。它用作通用容器，用于容纳其他 HTML 元素
```html
<div>
  <p>Example paragraph element.</p>

</div>
```
`div`当您需要对共享一组 CSS 样式的 HTML 元素进行分组时。
尽管该`div`元素在实际代码库中很常用，但您仍应注意不要过度使用它。有时其他元素可能更合适。
div标签的属性：
>`align="属性值"`：设置块儿的位置。属性值可选择：left、right、 center


* `span`
和div的作用一致，但不换行。span也是表达“小区域、小跨度”的标签，但只是一个**文本级**的标签。span里面只能放置文字、图片、表单元素。 span里面不能放p、h、ul、dl、ol、div。
### 文本标签
#### 转义字符
- `&nbsp;`：空格 （non-breaking spacing，不断打空格）
- `&lt;`：小于号`<`（less than）
- `&gt;`：大于号`>`（greater than）
- `&amp;`：符号`&`
- `&quot;`：双引号
- `&apos;`：单引号
- `&copy;`：版权`©`
- `&trade;`：商标`™`
- `&#32464;`：文字`绐`。其实，`#32464`是汉字`绐`的unicode编码

| 特殊字符 | 描述       | 字符的代码      |
| ---- | -------- | ---------- |
|      | 空格符      | `&nbsp;`   |
| <    | 小于号      | `&lt;`     |
| >    | 大于号      | `&gt;`     |
| &    | 和号       | `&amp;`    |
| ￥    | 人民币      | `&yen;`    |
| ©    | 版权       | `&copy;`   |
| ®    | 注册商标     | `&reg;`    |
| °    | 摄氏度      | `&deg;`    |
| ±    | 正负号      | `&plusmn;` |
| ×    | 乘号       | `&times;`  |
| ÷    | 除号       | `&divide;` |
| ²    | 平方2（上标2） | `&sup2;`   |
| ³    | 立方3（上标3） | `&sup3;`   |
#### 标题标签
HTML 中有六个标题元素。这 h1 通过 h6 标题元素用于表示其下方内容的重要性。数字越小，重要性越高，所以 h2 元素的重要性低于 h1 元素。具有align属性，属性值可以是：left、center、right。
```html
<h1>most important heading element</h1>
<h2>second most important heading element</h2>
<h3>third most important heading element</h3>
<h4>fourth most important heading element</h4>
<h5>fifth most important heading element</h5>
<h6>least important heading element</h6>
```
#### 文本标签
* `em`
要对特定的单词或短语进行强调，你可以使用em元素。
```html
<p>Cats <em>love</em> lasagna.</p> 
```
* `i`
用于突出显示替代语气或语气、来自其他语言的习语、技术术语和想法。
```html
<p>There is a certain <i lang="fr">je ne sais quoi</i> in the air.</p>
```
lang标签内的属性用于i指定内容的语言。
* `b`
通常用于突出显示摘要中的关键字或评论中的产品名称。通常，浏览器以粗体显示此文本。
```html
<p>
  We tested several products, including the <b>SuperSound 3000</b> for audio
  quality, the <b>QuickCharge Pro</b> for fast charging, and the
  <b>EcoClean Vacuum</b> for cleaning. The first two performed well, but the
  <b>EcoClean Vacuum</b> did not meet expectations.
</p>
```
* `strong`
strong元素用于表示某些文本具有重要性或紧急性。
```html
<p>
  <strong>Important:</strong> Before proceeding, make sure to wear your safety goggles. 
</p>
```
* `sup`
上标元素用于将一段文本显示为上标。上标是指显示在文本行上方的符号或字母。
```html
<p>2<sup>2</sup> (2 squared) is 4.</p>
```
上标字母是指以右上角标形式书写的字母，通常用于表示缩写。上标元素的常见用途包括表示指数、上标字母和序数。

* `sub`
要在 HTML 中表示化学方程式，可以使用下标元素。该元素使用下标来降低基线，从而使用更小的文本显示方程式。
```html
<p>CO<sub>2</sub></p>
```
* `code`
行内代码元素用于在文本中插入简短的代码片段。该代码元素的常见应用场景包括技术文章和文档页面。
```html
<p>
  To set the text color to blue in CSS, use the following code:
  <code>color: blue;</code>
</p>
```
浏览器将对元素内的内容应用默认样式`code`。默认样式为等宽字体。
该`code`元素用于表示单行代码。如果要表示多行代码，则需要将该`code`元素放置在预格式化文本元素内。
- pre
将保留标签内部所有的空白字符(空格、换行符)，原封不动地输出结果（告诉浏览器不要忽略空格和空行）。
```html
<pre>
  <code>
    body {
      color: red;
    }
  </code>
</pre>
```
使用该`pre`元素时，需要注意间距，因为它将完全按照 HTML 文档中的文本显示。
未明确标记 ( u ) 元素：用于表示一段内联文本，该文本应以表明其具有非文本标记的方式表示。

```html
<p>
  You can use the unarticulated annotation element to highlight
  <u>inccccort</u> <u>spling</u> <u>issses</u>.
</p>
```

Ruby Annotation( ruby​​ ) 元素：用于为文本添加表格或信息注释。例如，可用于东亚排版。
Ruby 回退 ( rp ) 元素：用于不支持显示 Ruby 文件浏览器的回退方案。
Ruby 文本（ rt ）元素：用于指示 Ruby 注释的文本。通常用于东亚排版中的发音或翻译细节。

```html
<ruby>
  明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp>
</ruby>
```

- 删除线 ( s ) 元素：用于表示不再准确或相关的内容。

```html
<p>
  <s>Tomorrow's hike will be meeting at noon.</s>
</p>
<p>
  Due to unforeseen weather conditions, the hike has been canceled.
</p>
```

* `abbreviation`
-缩写 ( abbr ) 元素：用于表示缩写或首字母缩略词。为了帮助用户理解缩写或首字母缩略词的含义，您可以使用 title 属性显示其完整形式，即易于理解的描述。
```HTML
<p><abbr>HTML</abbr> is the foundation of the web.</p>
<p><abbr title="HyperText Markup Language">HTML</abbr> is the foundation of the web.</p>
```
属性是可选的，但如果您决定包含它，它必须是缩写、首字母缩略词或首字母缩写词的人类可读的描述。

* `address`
联系地址元素用于表示网页上某个部分的联系信息。该`address`元素用途广泛，可用于商业页面、作者页面、个人网站等。

在构建网站的联系部分时，您应该使用语义`address`元素而不是通用元素（如）`div`。
```HTML
<address>
  <h2>Company Name</h2>
  <p>
    1234 Elm Street<br />
    Springfield, IL 62701<br />
    United States
  </p>
  <p>Phone: <a href="tel:+15555555555">+1 (555) 555-5555</a></p>
  <p>Email: <a href="mailto:contact@company.com">contact@company.com</a></p>
</address>
```
对于电话号码，我们有一个锚元素，其`href`值设置为电话号码。`tel:+`该`href`属性中的值会创建一个可点击的链接，用于在支持该功能的设备上发起电话呼叫。

对于电子邮件地址，使用另一个锚元素，其`href`值设置为`mailto`链接。HTML`mailto`文档中使用链接允许用户在他们喜欢的电子邮件客户端中打开新电子邮件。

使用链接的缺点之一`mailto`是用户通常会将其视为垃圾邮件。不幸的是，很多垃圾邮件发送者会利用这种方式向用户发送电子邮件。所以在使用时请务必牢记这一点。
* `time`
该`time`元素用于表示特定的时间时刻。
```HTML
<p>The reservations are for <time datetime="20:00">20:00 </time></p>
```
该`datetime`属性用于将日期和时间转换为机器可读的格式。

这很重要，因为它有助于搜索引擎结果并帮助浏览器更有效地处理日期和时间信息。

该属性的值`datetime`必须是有效年份、有效月份、有效时间、当地日期、全球日期或有效持续时间字符串。该属性的值`datetime`采用 ISO 8601 格式。ISO 8601 是表示日期和时间的国际标准。

该值的第一部分是年、月、日。值中的大写字母 T 是日期和时间之间的分隔符。

一千五点就是下午三点。

每当您需要表示事件、发布日期或约会时，最好使用该`time`元素。
- `<hr />`
水平分隔线（horizontal rule）可以在视觉上将文档分隔成各个部分。在网页中常常看到一些水平线将段落与段落之间隔开，使得文档结构清晰，层次分明。
属性介绍：
> `align="属性值"`：设定线条置放位置。属性值可选择：left right center。
> `size="2"`：设定线条粗细。以像素为单位，内定为2。
   `width="500"`或`width="70%"`：设定线条长度。可以是绝对值（单位是像素）或相对值。如果设置为相对值的话，内定为100%。
` color="#0000FF"`：设置线条颜色。
  `noshade`：不要阴影，即设定线条为平面显示。若没有这个属性则表明线条具阴影或立体。

-  `<br />`
如果希望某段文本强制换行显示，就需要使用换行标签。
```html
This <br/> is a para<br/>graph with line breaks
```

#### 段落标签
**作用**：可以把 HTML 文档分割为若干段落。在网页中如果要把文字有条理地显示出来，离不开段落标签。就如同我们平常写文章一样，整个网页也可以分为若干个段落。
```html
<p>This is a paragraph element.</p>
```
- `align="属性值"`：对齐方式。属性值包括left center right。
#### 超链接标签

##### 链接形式
1、外部链接：链接到外部文件
```html
<a href="02页面.html">点击进入另外一个文件</a>
```
a是英语`anchor`“锚”的意思，就好像这个页面往另一个页面扔出了一个锚。是一个文本级的标签。
2、锚链接

**锚链接**：给超链接起一个名字，作用是**在本页面或者其他页面的的不同位置进行跳转**。比如说，在网页底部有一个向上箭头，点击箭头后回到顶部，这个就可以利用锚链接。
##### 超链接属性
- `href`：目标URL
- `title`：悬停文本。
- `name`：主要用于设置一个锚点的名称。
- `target`：告诉浏览器用什么方式来打开目标页面。`target`属性有以下几个值：
    - `_self`：在同一个网页中显示（默认值）
    - `_blank`：**在新的窗口中打开**。
    - `_parent`：在父窗口中显示
    - `_top`：在顶级窗口中显示
##### 绝对路径与相对路径

- **路径定义**：路径是一个字符串，用于指定文件或目录在文件系统中的位置。在Web开发中，路径允许开发人员链接到图像、样式表、脚本和其他网页等资源。
- **路径语法**：需要了解三种关键的语法。首先是斜杠，根据操作系统不同，可以是反斜杠 ( `\`) 或正斜杠 ( )。其次是单点 ( )。最后是双点 ( )。斜杠被称为“路径分隔符”，用于指示文件夹或文件名之间的分隔符。单点指向当前目录，双点指向父目录。`/``.``..`

```md
public/index.html
./favicon.ico
../src/index.css
```

- **绝对路径**：绝对路径是指向资源的完整链接。它从根目录开始，包含所有其他目录，最后是文件名和扩展名。“根目录”指的是层级结构中的顶级目录或文件夹。绝对路径还包含协议（例如 `http://`、`http://``http`和`http://`）`https`以及`file`域名（如果资源位于网络上）。以下是一个指向 freeCodeCamp 徽标的绝对路径示例：

```html
<a href="https://design-style-guide.freecodecamp.org/img/fcc_secondary_small.svg">
  View fCC Logo
</a>
```

- **相对路径**：相对路径指定文件相对于当前文件所在目录的位置。它不包含协议或域名，因此更短，也更灵活，适用于同一网站内的内部链接。以下示例展示了如何从`about.html`页面链接到`contact.html`位于同一文件夹中的页面：

```html
<p>
  Read more on the
  <a href="about.html">About Page</a>
</p>
```

 ##### 链接状态

- **`:link`**这是默认状态。此状态表示用户尚未访问、点击或与之交互的链接。您可以将此状态理解为页面上所有链接的基础样式。其他状态均基于此状态构建。
- **`:visited`**：这适用于用户已访问过链接指向的页面的情况。默认情况下，链接会变成紫色，但您可以使用 CSS 为用户提供不同的视觉指示。
- **`:hover`**当用户将鼠标悬停在链接上时，此状态生效。此状态有助于提高用户对链接的关注度，确保用户确实打算点击该链接。
- **`:focus`**：当我们聚焦于某个链接时，就会出现这种状态。
- **`:active`**此状态适用于用户激活的链接。通常情况下，这意味着用户使用鼠标左键点击链接。



### 引用标签
- 引用块 ( blockquote ) 元素：用于表示从其他来源引用的部分。此元素有一个 cite 属性。该属性的 cite 值为来源的 URL。

```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
</blockquote>
```

- 引用（ cite ）元素：用于以生活方式为参考文献的来源。标记参考文献的标题。

```html
<div>
  <blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
  </blockquote>
  <p>
    -Quincy Larson, <cite>How to learn to Code and Get a Developer Job [Full Book].</cite>
  </p>
</div>
```

- 行内引用 ( q ) 元素：用于表示简短的行内引用。

```html
<p>
  As Quincy Larson said,
  <q cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Momentum is everything.
  </q>
</p>
```
### 列表标签
* 无序和有序列表
无序（ ul ) 和有序 ( ol ) 列表元素 ：要创建项目符号列表，您应该使用 ul 具有一个或多个元素  嵌套在其中的元素如下所示

```html
<ul>
  <li>catnip</li>
  <li>laser pointers</li>
  <li>lasagna</li>
</ul>
```

```html
<ol>
  <li>flea treatment</li>
  <li>thunder</li>
  <li>other cats</li>
</ol>
```
**ul属性：**
>`type="属性值"`。属性值可以选： `disc`(实心原点，默认)，`square`(实心方点)，`circle`(空心圆)。

**ol属性**
>- `type="属性值"`。属性值可以是：1(阿拉伯数字，默认)、a、A、i、I。结合`start`属性表示`从几开始`。

* 描述列表
描述列表非常适合以有组织且易于阅读的格式呈现术语和定义，例如在术语表或真正的词典中，您可以在其中找到单词及其相应的定义。
- 描述列表（ dl ）元素：用于表示术语描述包的列表。
- 描述术语（ dt ）元素：用于表示被定义的术语。
- 描述详情 ( dd ) 元素：用于表示术语的描述。
```HTML
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
  <!-- <dt>JS</dt>
  <dd>JavaScript</dd> -->
</dl>
```
术语是缩写词 HTML 和 CSS，详细信息是它们的扩展。细节也可以是定义或与术语相关的其他信息。
您将需要三个 HTML 元素来定义描述列表。首先，描述列表元素， dl ，它是整个列表的容器。您可以看到它包围了示例中描述列表的所有其他元素。
然后，一个描述术语元素， dt ，对于每个术语。在本例中，描述列表有两个术语：HTML 和 CSS，因此它有其中两个元素。
最后，在每个术语之后，您会找到一个描述详细信息元素， DD ，了解与该术语相关的描述或详细信息。在本例中，它们是超文本标记语言和级联样式表。
在浏览器中，您会看到每个术语及其相应的描述。默认情况下，描述稍微向右缩进，以便在视觉上区分它们。
但描述列表不仅限于术语和定义。它们的用途远不止于此。
### 表格标签
表格标签用`<table>`表示。 一个表格`<table>`是由每行`<tr>`组成的，每行是由每个单元格`<td>`组成的。 所以我们要记住，一个表格是由行组成的（行是由列组成的），而不是由行和列组成的。
- **表格元素**：用于创建 HTML 表格。
- **表格头部（`thead`）元素**：用于对 HTML 表格中的标题内容进行分组。
- **Table Row ( `tr`) 元素**：用于在 HTML 表格中创建行。
- **表格标题（`th`）元素**：用于在 HTML 表格中创建标题单元格。
- **表格主体（`tbody`）元素**：用于将 HTML 表格中的主体内容分组。
- **表格数据单元格 ( `td`) 元素**：用于在 HTML 表格中创建数据单元格。
- **表格页脚 ( `tfoot`) 元素**：用于将 HTML 表格中的页脚内容分组。
- **`caption`元素**：用于添加 HTML 表格的标题。
- **`colspan`属性**：用于指定表格单元格应跨越的列数
```html
<table id="quickfacts">
  <thead>
    <tr>
      <th colspan="2">Quick Facts: Software Developers, Quality Assurance Analysts, and Testers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2023 Median Pay</th>
      <td>
        $130,160 per year
        <br>$62.58 per hour
      </td>
    </tr>
    <tr>
      <th>Typical Entry-Level Education</th>
      <td>Bachelor's degree</td>
    </tr>
    <tr>
      <th>Work Experience in a Related Occupation</th>
      <td>None</td>
    </tr>
    <tr>
      <th>On-the-job Training</th>
      <td>None</td>
    </tr>
    <tr>
      <th>Number of Jobs, 2022</th>
      <td>1,795,300</td>
    </tr>
    <tr>
      <th>Job Outlook, 2022-32</th>
      <td>25% (Much faster than average)</td>
    </tr>
    <tr>
      <th>Employment Change, 2022-32</th>
      <td>451,200</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th>If this table had a footer it would be here.</th>
    </tr>
  </tfoot>
</table>
```
要为表格添加标题，可以使用caption元素。
```html
<table>
  <caption>Football Scores</caption>
</table>
```
表头元素，即`<thead>`标签，用于将表格中的标题内容分组。
```html
<table>
  <thead>
    <!-- header content goes here -->
  </thead>
</table>
```
表格头部元素由一个表行元素tr组成，该元素包含多个表头单元格
th。
```html
<table>
  <caption>Football Scores</caption>
  <thead>
    <tr>
      <th>Team</th>
      <th>Wins</th>
      <th>Losses</th>
    </tr>
  </thead>
</table>
```
表格数据元素td用于在表格中创建一个单元格。
```html
<tr>
  <td>1</td>
  <td>John Doe</td>
  <td>USA</td>
</tr>
```
colspan 属性用于指定单元格应跨越的列数。
```html
<tr>
  <td colspan="3">Total Points</td>
</tr>
```
scope 属性用于指定表头单元格是属于某一行、某一列，还是一个行或列的组。scope属性的另一个值是row，表示该表头单元格是一个整个行的标题。
```html
<th scope="col">Example Header</th>
```
**`<table>`的属性：**

- `border`：边框。像素为单位。
- `style="border-collapse:collapse;"`：单元格的线和表格的边框线合并（表格的两边框合并为一条）
- `width`：宽度。像素为单位。
- `height`：高度。像素为单位。
- `bordercolor`：表格的边框颜色。
- `align`：**表格**的水平对齐方式。属性值可以填：left right center。 注意：这里不是设置表格里内容的对齐方式，如果想设置内容的对齐方式，要对单元格标签`<td>`进行设置）
- `cellpadding`：单元格内容到边的距离，像素为单位。默认情况下，文字是紧挨着左边那条线的，即默认情况下的值为0。 注意不是单元格内容到四条边的距离哈，而是到一条边的距离，默认是与左边那条线的距离。如果设置属性`dir="rtl"`，那就指的是内容到右边那条线的距离。
- `cellspacing`：单元格和单元格之间的距离（外边距），像素为单位。默认情况下的值为0
- `bgcolor="#99cc66"`：表格的背景颜色。
- `background="路径src/..."`：背景图片。 背景图片的优先级大于背景颜色。
- `bordercolorlight`：表格的上、左边框，以及单元格的右、下边框的颜色
- `bordercolordark`：表格的右、下边框，以及单元格的上、左的边框的颜色 这两个属性的目的是为了设置3D的效果。
- `dir`：公有属性，单元格内容的排列方式(direction)。 可以 取值：`ltr`：从左到右（left to right，默认），`rtl`：从右到左（right to left） 既然说`dir`是共有属性，如果把这个属性放在任意标签中，那表明这个标签的位置可能会从右开始排列。
 `<tr>`**属性：**
 - `dir`：公有属性，设置这一行单元格内容的排列方式。可以取值：
    - `ltr`：从左到右（left to right，默认）
    - `rtl`：从右到左（right to left）
- `bgcolor`：设置这一行的单元格的背景色。 注：没有background属性，即：无法设置这一行的背景图片，如果非要设置，可以用css实现。
- `height`：一行的高度
- `align="center"`：一行的内容水平居中显示，取值：left、center、right
- `valign="center"`：一行的内容垂直居中，取值：top、middle、bottom
`<td>`**属性：**
- `align`：内容的横向对齐方式。属性值可以填：left right center。如果想让每个单元格的内容都居中，这个属性太麻烦了，以后用css来解决。
- `valign`：内容的纵向对齐方式。属性值可以填：top middle bottom
- `width`：绝对值或者相对值(%)
- `height`：单元格的高度
- `bgcolor`：设置这个单元格的背景色。
- `background`：设置这个单元格的背景图片。
### 表单标签
* `form`
用于创建供用户输入的 HTML 表单

```html

<form method="value-goes-here" action="url-goes-here">
  <!-- inputs go inside here -->
</form>

```

该`action`属性指定表单数据提交后将发送到哪里。要收集特定信息，例如姓名和电子邮件地址，您可以使用 `<form>``input`元素。
method 属性用于指定发送表单数据时使用的HTTP方法。最常见的方法是 GET和 POST
* `input`
用于创建用户输入的输入字段
属性

| 属性           | 说明                                                                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------------------------- |
| type         | 用于指定输入字段的类型,`text`, `email`, `number`, `radio`, `checkbox` `range` `password` `date`                                  |
| placeholeder | 用于向用户显示提示，告诉他们要在输入字段中输入什么内容。                                                                                          |
| value        | 用于指定输入的值。如果输入有一个 按钮 类型，即 价值 属性可用于设置按钮文本。                                                                              |
| name         | 用于为输入字段指定名称，作为提交表单数据时的键。对于单选按钮，给它们相同的 姓名 将它们分组在一起，因此一次只能选择组中的一个选项。在表单提交中，为每个可提交元素提供一个name属性是有用且良好的实践。该属性用于在表单提交时识别该元素 |
| size         | 用于定义用户在输入中键入时应可见的字符数                                                                                                  |
| min          | 可与输入类型一起使用，例如 数字 指定输入字段中允许的最小值。                                                                                       |
| max          | 可与输入类型一起使用，例如 数字 指定输入字段中允许的最大值。                                                                                       |
| minlength    | 用于指定输入字段中所需的最小字符数                                                                                                     |
| maxlength    | 用于指定输入字段中允许的最大字符数                                                                                                     |
| required     | 用于指定在提交表单之前必须填写输入字段                                                                                                   |
| disabled     | 用于指定应禁用输入字段。                                                                                                          |
| readonly     | 用于指定输入字段是只读的                                                                                                          |
```html

<!-- Text input -->
<input 
  type="text"
  id="name"
  name="name"
  placeholder="e.g. Quincy Larson" 
  size="20"
  minlength="5"
  maxlength="30"
  required
/>

<!-- Number input -->
<input 
  type="number"
  id="quantity"
  name="quantity"
  min="2"
  max="10"
  disabled
/>

<!-- Button -->
<input type="button" value="Show Alert" />

```
`
使用 type="password"，你可以通过 pattern 属性定义一个正则表达式，密码必须匹配该表达式才被视为有效。
在密码输入元素上添加一个pattern属性，要求输入必须匹配:[a-z0-9]{8,}。


* label`
用于为输入字段创建标签

| 属性  | 说明                                |
| --- | --------------------------------- |
| for | 可以通过将输入字段包装在标签内来将输入与标签关联起来 标签 元素。 |

- 隐式形式关联 ：可以通过将输入字段包装在标签内来将输入与标签关联起来 标签 元素。

```html
<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
```

- 显式形式关联 ：输入可以通过使用与标签相关联 为了 属性上的 标签 元素。

```html
<form action="">
  <label for="email">Email Address: </label>
  <input type="email" id="email" />
</form>
```
* button
`button`元素**：用于创建可点击的按钮。按钮还可以有一个属性`type`，用于控制按钮激活时的行为。例如：`submit`，`reset`。

示例代码

```html
<button type="button">Show Form</button>
<button type="submit">Submit Form</button>
<button type="reset">Reset Form</button>
```

- **`fieldset`元素**：用于将相关的输入组合在一起。
- **`legend`元素**：用于添加标题来描述一组输入内容。

示例代码

```html
<!-- Radio group -->
<fieldset>
  <legend>Was this your first time at our hotel?</legend>

  <label for="yes-option">Yes</label>
  <input id="yes-option" type="radio" name="hotel-stay" value="yes" />

  <label for="no-option">No</label>
  <input id="no-option" type="radio" name="hotel-stay" value="no" />
</fieldset>

<!-- Checkbox group -->
<fieldset>
  <legend>
    Why did you choose to stay at our hotel? (Check all that apply)
  </legend>

  <label for="location">Location</label>
  <input type="checkbox" id="location" name="location" value="location" />

  <label for="price">Price</label>
  <input type="checkbox" id="price" name="price" value="price" />
</fieldset>
```

- **聚焦状态**：这是用户选中输入字段时的状态。

### iframe框架标签
替换元素是指其内容由外部资源而非 CSS 本身决定的元素。CSS（层叠样式表）用于向网页添加样式。常见的替换元素包括图像、iframe 和视频元素。

使用替换元素，您可以控制元素的位置或布局。但您的 CSS 无法直接修改该元素的内容。通过一些示例可能更容易解释这一点。考虑一下图像元素，它将图像嵌入到您的网页中：
```html
<img src="example-img-url" alt="Descriptive text goes here">
```
元素本身被替换为外部对象：图像。CSS 可以控制图像的定位，或为其应用滤镜，但实际上无法修改图像本身。一个更强大的例子可能是将`iframe`外部网站嵌入到网页中的元素。
```html
<iframe width="400" height="200" src="https://www.youtube.com/embed/u43gJJrVa1I?si=BoDW_puFsy8OEr_Z" title="Professional Cloud Architect Certification Course – Pass the Exam! (YouTube video)" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```
属性`src`指定要嵌入的页面的 URL。`width`属性指定 的宽度`iframe`。`height`属性指定 的高度`iframe`。属性允许用户在全屏模式下`allowfullscreen`显示。为 指定属性也是一个好习惯，因为它对于可访问性很重要。`iframe``title``iframe`
使用该`iframe`元素的其他常见示例是将地图嵌入到页面上。
其中一个属性是 allow。它就像一个权限列表，告诉浏览器 iframe 允许使用哪些功能。
 referrer-policy。它是决定在页面连接到另一个页面时分享多少详细信息的规则。
```html
<iframe
  title="Map of the Royal Observatory, Greenwich, London"
  width="300"
  height="200"
  src="https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&amp;layer=mapnik">
</iframe>
```
元素本身会被替换为外部对象：网站。您的 CSS 可以更改嵌入网站的位置，但无法修改网站的内容。更进一步说，如果嵌入网站包含某个`h1`元素，您的 CSS 将无法为该`h1`元素设置样式。您无法更改其大小、字体颜色等等。

您可以包括 允许全屏 属性允许用户以全屏模式显示 iframe。

```html
<iframe
  src="video-url"
  width="width-value"
  height="height-value"
  allowfullscreen
></iframe>
```

要将视频嵌入到 内嵌框架 您可以直接从 YouTube 和 Vimeo 等流行视频服务复制它，或者使用 源代码 属性指向该视频的 URL。以下是嵌入 YouTube 上流行的 freeCodeCamp 课程的示例：

```html
<h1>A freeCodeCamp YouTube Video Embedded with the iframe Element</h1>

<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/PkZNo7MFNFg?si=-UBVIUNM3csdeiWF"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
```

还有一些其他被替换的元素，例如 视频 ， 和 嵌入 。并且某些元素在特定情况下表现为替换元素。这是一个例子 输入 元素与 类型 属性设置为 图像 :

```html
<input type="image" alt="Descriptive text goes here" src="example-img-url">
```

- 优化媒体 ：在网页上使用图像等媒体时需要考虑三个工具：大小、格式和压缩。压缩算法用于减小文件或数据的大小。
- 图片格式 ：两种最常见的文件格式是 PNG 和 JPG，但它们不再是提供图像的最理想格式。除非您需要支持较旧的浏览器，否则您应该考虑使用更优化的格式，例如 WEBP 或 AVIF。
- 图片许可 ：公共领域的图像不附带版权，可以不受任何限制地自由使用。根据 Creative Commons 0 许可证专门许可的图像被视为公共领域。某些图像可能会在宽松的许可证下发布，例如 Creative Commons 许可证或 freeCodeCamp 使用的 BSD 许可证。
- SVG ：可扩展矢量图形根据路径和方程跟踪数据以绘制点、直线和曲线。这真正意味着矢量图形（如 SVG）可以缩放到任何大小而不影响质量。
### 多媒体标签
#### 图像标签
img: 英文全称 image（图像），代表的是一张图片。
可以通过使用`<img>`元素将图片添加到网站。img元素有一个没有闭合标签的单标签，也称为单元素。
* src属性
img元素中的src属性指定了图像的URL(即图像所在的位置)。
```html
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_secondary.svg">
```
该`src`属性用于指定图像的位置。
* alt属性
alt属性用于为图像提供简短的描述性文本。

img元素上的加载（loading）属性可以被设置为"懒加载(lazy)"以告知浏览器在需要时(即当用户将图像拖拽至可视区域时)才获取图像资源。此外，懒加载元素在除非懒加载元素被加载完毕之前不会加载一一这意味着网络连接较慢的用户无需等待图像加载即可浏览页面内容。

* figure元素
figure元素表示自包含的内容，并允许您将图像与标题关联起来。
图形标题(figcaption)元素用于添加一个标题来描述包含在图形元素中的图像。
```html
<figure>
  <img src="image.jpg" alt="A description of the image">
  <figcaption>A cute cat</figcaption>
</figure>
```
#### 音频&视频
##### audio 
`audio`和元素`video`允许您向 HTML 文档添加声音和视频内容。`audio`元素支持 mp3、wav 和 ogg 等常见音频格式。`video`元素支持 mp4、ogg 和 webm 格式。

| 属性         | 说明                                                                             | 备注  |
| ---------- | ------------------------------------------------------------------------------ | --- |
| src属性      | 指向音频文件的位置                                                                      |     |
| controls属性 | 允许用户管理音频播放，包括调节音量、暂停或继续播放。该属性`controls`是一个布尔值，可以添加到元素以启用内置播放控件。如果省略，则不会显示任何控件。 |     |
| loop属性     | `loop`属性是一个布尔属性，用于使音频连续播放                                                      |     |
| muted属性    | 静音状态启动音频                                                                       |     |

```HTML
<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3" controls></audio>
```

音频文件类型，不同浏览器对不同类型支持程度有所不同。为了解决这个问题，您可以在元素`source`内部使用元素`audio`，浏览器会选择它能识别的第一个源。以下是`source`一个元素内部使用多个元素的示例`audio`：
```html
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
```

浏览器将首先从 ogg 类型开始，如果它无法播放音频，那么它将移动到列表中的下一个类型。

##### video

| 属性       | 说明        |     |
| -------- | --------- | --- |
| src属性    | 指向音频文件的位置 |     |
| loop     |           |     |
| controls |           |     |
| muted    |           |     |
| autoplay | 视频自动播放    |     |
| `poster` |           |     |


**注意**：`width`此处使用此属性是为了缩小视频尺寸，使其更适合预览窗口。
```HTML
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  width="400"
></video>
```
对于`src`或 source 属性，我们使用了来自 archive.org 的名为“Big Buck Bunny”的视频。如果您想在视频下载过程中显示图片，可以使用`poster`属性。此属性不适用于`audio`元素，并且是元素独有的。以下是使用peach.blender.org 提供的内容的属性`video`示例。
```html
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
  width="400"
></video>
```


### 使用 HTML 工具

- **HTML验证器**：一种检查HTML代码语法以确保其有效性的工具。
- **DOM 检查器**：一种可以检查和修改网页 HTML 结构的工具。
- **开发者工具**：一套直接内置于浏览器中的 Web 开发工具，可帮助您调试、分析和优化网页。
### 其他标签


#### script标签
该`script`元素用于嵌入可执行代码。大多数开发人员会使用它来执行 JavaScript 代码。JavaScript 用于为网页添加交互性。常见的 JavaScript 应用包括交互式游戏、图片滑块以及实时验证用户输入的动态表单。

`script`以下是在 HTML 文档中使用 元素的示例。删除`//`前面的`alert("Welcome to freeCodeCamp");`，您应该会看到一个弹出的警报。
```html
<body>html
  <script>
    // alert("Welcome to freeCodeCamp");
  </script>
</body>
```
虽然从技术上讲，你可以在标签内编写所有 JavaScript 代码，但最佳做法是链接到外部 JavaScript 文件。以下是使用元素链接到外部 JavaScript 文件`script`的示例：
```html
<script src="path-to-javascript-file.js"></script>
```
此处使用属性`src`来指定外部 JavaScript 文件的位置。`src`代表“源”。不建议将所有 JavaScript 代码都放在 HTML 文档中，是因为关注点分离。关注点分离是一种设计原则，它将程序分成不同的部分，每个部分处理不同的关注点。

#### 注释
HTML以<!--开头，包含任意数量的文本行，并以-->结尾。
```html
<!-- TODO: Remove h1 -->
```

HTML5有一些元素可以识别不同的内容区域。这些元素使你的HTML更容易阅读，并有助于搜索引擎优化(SEO)和可访问性。
`<main>`元素用于表示HTML文档主体内容的主要部分。`<main>`元素内的内容应该是文档特有的，不应在文档的其他部分中重复出现。

`<a></a>`
你可以使用锚点(a)元素链接到另一个页面。
```html
<a href="https://www.freecodecamp.org"></a>
```
要在新标签页中打开链接，可以使用目标属性在锚点(a)元素上。target属性指定要将链接文档打开的位置。`target="_blank"`在新标签页或窗口中打开链接文档。
```html
<a href="https://www.freecodecamp.org" target="_blank">freeCodeCamp</a>
```

## 任务

复习 HTML 表格和表单的相关主题和概念。

请完成作业

提交

求人

已导航至 HTML 表格和表单审核

下拉菜单
当您希望用户从下拉菜单中进行选择时，可以使用`<select>`和`<option>`元素。
```html
<label for="city">Choose a City: </label>
<select id="city" name="city">
  <option value="new-york">New York</option>
  <option value="los-angeles">Los Angeles</option>
  <option value="chicago">Chicago</option>
  <option value="miami">Miami</option>
</select>
```
要使某个选项默认被选中，可以向您希望被选中的选项元素添加 selected 属性。

`textarea`
如果你想让用户有更多空间来撰写评论，可以使用textarea元素
textarea元素是一种多行文本输入控件，允许用户输入比单行文本更长的内容。它可用于创建评论框、消息输入框或其他需要多行文本输入的界面元素。
```html
<textarea id="comments" name="comments" rows="4" cols="50"></textarea>
```


表单由用户可以输入数据的输入框组成。你可以使用fieldset 元素将相关的输入项分组在一起。
```html
<form action="/example-url">
  <fieldset>
    <legend>Personal Information</legend>
    <!-- inputs go inside here-->
  </fieldset>
</form>


```
在处理字段元素时，通常会使用标题来描述一组输入。你可以为此使用legend元素。


按钮有哪些类型，以及何时应该使用它们？

该`button`元素用于在激活时执行特定操作。以下是一个`button`按钮文本为“”的元素示例`Start Game`。

```html
<button>Start Game</button>
```

该元素的其他用途`button`包括提交表单、显示模态框或切换侧边菜单的打开和关闭。该`button`元素有一个`type`属性，用于控制按钮激活时的行为。该`type`属性的第一个可能值是type。以下是一个使用 type为type 且 text 为 text 的元素`button`示例：`button``button``Show Alert`

```html
<button type="button">Show Alert</button>
```

默认情况下，按钮激活后不会执行任何操作。但是，您可以添加一些 JavaScript 代码，使按钮具有交互功能，例如在本例中显示一个警告框。

点击`Show Alert`按钮，屏幕上会弹出提示信息。

**注意**：本交互式示例使用了 JavaScript，但您无需担心理解 JavaScript 代码。您将在后续模块中学习 JavaScript。

```html
<button type="button">Show Alert</button>
<script src="index.js"></script>
```

```js
const btn = document.querySelector("button");
btn.addEventListener("click", () => alert("You clicked on the alert button"));
```

该属性的另一个可能值`type`是value。以下是使用该类型的元素`submit`的示例。`button``submit`

```html
<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="submit">Submit form</button>
</form>
```

在这个`form`元素内部，包含一个用于输入用户电子邮件地址的元素。当用户点击提交按钮时，他们的数据将被发送到服务器进行处理。该属性的第三个可能值`label`是“已重置”和“已提交”按钮。以下是一个包​​含重置按钮和提交按钮的元素示例。`input``type``reset``form`

在预览窗口中，通过输入一个虚假的电子邮件地址来与电子邮件输入框互动。然后点击重置按钮，即可看到您的电子邮件地址从该字段中消失。

```html
<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="reset">Reset form</button>
  <button type="submit">Submit form</button>
</form>
```

在这个修改后的示例中，我们使用 `<a>``label`和`input``<input>` 元素来收集用户的电子邮件地址。当用户点击重置按钮时，所有输入的数据都会被清除。需要注意的是，重置按钮通常不是最佳选择，因为它们可能导致用户意外重置数据。此外，表单中过多的按钮也会使用户界面显得杂乱。

在 HTML 中创建按钮的另一种方法是使用 `<button> `input`` 元素。`<button>`input`元素还有一个 ` `type`value` 属性，其值可以是 `<button> submit、reset `<button>` 和`<button>`。以下是一个将 `value`设置为 `<button>` `button`的示例：`input` `type` `button`

```html
<input class="start-btn" type="button" value="Start Game" />
<script src="index.js"></script>
```

```js
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector(".start-btn");
  btn.addEventListener("click", () => {
    const paraEl = document.createElement("p");
    const bodyEl = document.querySelector("body");

    bodyEl.appendChild(paraEl);
    paraEl.textContent = "The game has started!!!";
  });
});
```

该`value`属性用于显示按钮文本。那么，`<button>` `input`和`button``<a>` 元素之间有什么区别呢？`input` `<button>` 元素是空元素，这意味着它们不能包含子节点（例如文本），只能包含一个开始标签。另一方面，`<a>` `button`元素提供了更大的灵活性，因为您可以在其中嵌套文本、图像和图标。

HTML 表单中的客户端表单验证是什么？有哪些示例？

当用户在您的网站上填写表单时，务必确保他们以正确的格式填写所有必要信息。HTML 表单控件（例如输入框）内置了许多验证功能，您可以利用这些功能来检查无效数据。这将有助于确保用户在信息提交并被服务器处理之前修正这些错误。

“客户端”一词指的是在用户计算机或设备上发生的一切，例如用户直接交互的网站或应用程序部分。这包括布局、设计和任何交互功能。

“服务器端”一词指的是在托管网站或应用程序的服务器、计算机或系统上发生的一切活动。这包括处理数据、运行应用程序以及处理来自用户设备的请求。

虽然客户端验证很重要，但为了增强安全性，您还需要服务器端验证。恶意用户可以绕过客户端检查，因此强大的服务器端措施至关重要。您将在后续模块中了解更多相关内容。现在，让我们来看一些客户端表单验证的示例。

内置表单验证的一个常见例子是`required`在输入框中使用属性。该`required`属性指定用户需要填写表单的相应部分才能提交。以下是`required`在电子邮件输入框中使用该属性的示例。

如果未提供电子邮件地址而点击该`Submit Form`按钮，您将看到一条消息弹出，提示您填写该字段。

```html
<form action="">
  <label for="email">Email Address (Required field):</label>
  <input required type="email" name="email" id="email" />
  <button type="submit">Submit Form</button>
</form>
```

每个浏览器都有自己显示此警告信息的样式。

使用电子邮件输入框的另一个优点是，电子邮件输入框具有一些基本的验证功能，以确保电子邮件地址格式正确。例如，如果您输入一些随机词语并点击提交，浏览器会弹出提示，指出`@`缺少某个标识。

在邮箱地址栏中输入`abc`地址，然后点击提交按钮。此时应该会弹出一条消息，提示该邮箱地址无效。

```html
<form action="">
  <label for="email">Email Address (Required field):</label>
  <input required type="email" name="email" id="email" />
  <button type="submit">Submit Form</button>
</form>
```

需要注意的是，浏览器仅对标准电子邮件地址进行基本验证。您需要自行添加额外的验证层，这将在后续模块中学习。

其他验证电子邮件输入的方式是使用 ` `minlength`and``maxlength`属性。以下是一个使用额外验证的示例。

在文本框中输入内容`b@m`，然后点击提交按钮。你会看到一个弹出消息，因为文本长度未达到要求的最低长度。

```html
<form action="">
  <label for="email">Email Address (Required field):</label>
  <input
    required
    type="email"
    name="email"
    id="email"
    minlength="4"
    maxlength="64"
  />
  <button type="submit">Submit Form</button>
</form>
```

`minlength``min`和 ` max`属性`maxlength`用于设置电子邮件输入框的最小和最大字符长度。如果未设置最小长度或超过最大字符长度，浏览器将显示警告信息。

不同的形态状态有哪些？它们为什么重要？

在 HTML 中，表单控件（如输入框）可以处于不同的阶段或状态，例如`focused`状态 1、`readonly`状态 2 或`disabled`状态 3。

第一种状态将被视为初始`default`状态。电子邮件地址输入框的默认状态是空白输入框。这是电子邮件输入框首次在页面上呈现时的样子。

```html
<input type="email" name="email" id="email" />
```

当用户点击表单控件或使用键盘上的 Tab 键选中它时，该控件就处于选中状态`focused`。在选中状态下`focused`，大多数浏览器会在输入框周围显示蓝色高亮边框。您也可以在 CSS 中添加其他样式。

点击预览窗口中的任意空白区域，然后按下`tab`按键即可查看焦点状态。

```html
<input type="email" name="email" id="email" />
```

表单的另一种状态是“`disabled`无法聚焦或激活”状态。此状态会向用户显示某个输入框无法获得焦点或激活。

尝试点击电子邮件输入框，你会发现它将不再获得焦点。

```html
<input disabled type="email" name="email" id="email" />
```

与状态类似，您可以使用 CSS`focused`为状态添加其他样式。`disabled`

表单的另一种状态是只读状态`readonly`。在这种状态下，表单控件（例如输入框）对用户不可编辑。以下示例演示如何将电子邮件输入框设置为只读。该`value`属性用于设置输入框内显示的值。

`example@email.com`尝试在预览窗口中编辑当前值，您会发现这是不可能的。

```html
<input
  readonly
  type="email"
  name="email"
  id="email"
  value="example@email.com"
/>
```

`disabled`国家和政权之间的一个关键区别`readonly`在于，前者`readonly`可以集中精力，而`disabled`后者则不能。

了解表单的不同状态非常重要，因为它们可以在处理错误时提供清晰的反馈和指导，从而确保流畅的用户体验。



# 实践
```
# 建立食谱页面

构建一个功能类似于此示例项目的应用程序。尽量不要照搬示例项目，赋予其你自己的个人风格。

**目标：**满足以下用户故事并通过所有测试以完成实验。

**用户故事：**

1. 你应该有一个`!DOCTYPE html`声明。
2. 您应该有一个设置`html`为 的元素。`lang``en`
3. 您应该有一个`head`元素，其中包含`title`具有您的食谱名称的元素，以及一个属性设置为的`meta`元素。`charset``UTF-8`
4. 你应该有一个`body`元素。
5. 您应该有一个`h1`带有您的食谱名称的元素。
6. 您应该`p`在下方有一个介绍菜谱的元素`h1`。
7. 您应该有一个包含成分部分`h2`文本的元素。`Ingredients`
8. 您应该有一个无序列表（`ul`元素），其中至少有四个列表项（`li`元素），在第一个`h2`元素下方列出您的成分。
9. 您应该有第二个元素，其中包含说明部分的`h2`文本。`Instructions`
10. 您应该有一个有序列表（`ol`元素），其中至少有四个列表项，按顺序列出配方步骤，位于第二个列表项下方`h2`。
11. 您应该有一个`img`元素，其`src`属性设置为有效图像（`https://cdn.freecodecamp.org/curriculum/labs/recipe.jpg`如果愿意，您可以使用），以及一个`alt`描述图像的属性。
```

```
# 建立旅行社页面

构建一个功能类似于此示例项目的应用程序。尽量不要照搬示例项目，赋予其你自己的个人风格。

**目标：**满足以下用户故事并通过所有测试以完成实验。

**用户故事：**

1. 你应该有一个`DOCTYPE`声明。
2. 您应该有一个设置`html`为 的元素。`lang``en`
3. 您应该有一个`head`元素，其中包含设置为`meta`的 void 元素和带有文本的。`charset``utf-8``title``Travel Agency Page`
4. `meta`您的元素中应该有一个标签`head`，其中包含您网站的简短描述，用于 SEO。
5. 您应该有一个`h1`元素来展示您的旅行目的地。
6. 您应该在元素下方添加一段`h1`介绍旅行机会的段落。
7. 您应该有一个`h2`带有文本的元素`Packages`。
8. 您应该有一个`p`元素来简要介绍各种包。
9. 您应该有一个包含两个列表项的无序列表元素。这两个列表项分别应包含文本`Group Travels`和`Private Tours`。每个列表项的文本应包含在一个锚元素中。
10. 您应该有一个`h2`带有文本的元素`Top Itineraries`。
11. 您应该至少有三个`figure`元素，每个元素包含一个锚元素和一个`figcaption`元素。
12. 这三个锚点元素应该包含一个`img`具有适当`alt`属性的元素，以及一个设置为有效图像的属性作为其内容。如果您愿意，`src`可以使用`https://cdn.freecodecamp.org/curriculum/labs/colosseo.jpg`、`https://cdn.freecodecamp.org/curriculum/labs/alps.jpg`和。`https://cdn.freecodecamp.org/curriculum/labs/sea.jpg`
13. 所有五个锚元素都应具有一个`href`值为 的属性`https://www.freecodecamp.org/learn`和一个`target`值为 的属性`_blank`。
```

```
# 构建 HTML 音频和视频播放器

构建一个功能类似于此示例项目的应用程序。尽量不要照搬示例项目，赋予其你自己的个人风格。

**目标：**满足以下用户故事并通过所有测试以完成实验。

**用户故事：**

1. 您应该有一个`h1`元素作为页面的主标题。
2. 你应该有两个`section`元素。
3. 在第一个`section`元素中，您应该有一个`h2`用于播放视频标题的元素。
4. 元素下方`h2`应该有一个具有和属性的`video`元素。属性应设置为。`controls``width``width``640`
5. 在元素内部`video`，您应该有一个`source`元素，该元素具有`src`指向视频文件的属性和`type`属性。
    - 您可以使用`https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4`。
6. 在第二个`section`元素中，您应该有一个`h2`用于播放歌曲标题的元素。
7. 在该`h2`元素下方，您应该有一个具有和属性`audio`的元素，以及一个指向音频文件的属性。 `controls``loop``src`
    - 您可以使用`https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3`。
    - 或者`https://cdn.freecodecamp.org/curriculum/js-music-player/we-are-going-to-make-it.mp3`。
```

```
# 调试宠物领养页面
宠物领养店老板莎莉已经建立了她的第一个网页，但存在一些问题。

您的工作是修复所有错误，以便 Sally 可以继续构建她的页面。

**目标：**满足以下用户故事并通过所有测试以完成实验。

**用户故事：**

1. Sally 想使用一些猫的图片，但显示不正确。您需要在`img`元素中修复以下问题：
    - `href`用图像源的正确属性替换该属性。
    - `att`用代表图像的简短描述性文本的正确属性替换该属性。
    - 删除`</img>`结束标签，因为`img`元素是空元素并且没有结束标签。
2. Sally 想使用一些链接将用户引导至狗和猫的页面。但这些链接无法正常工作。您需要修复`a`元素中的以下问题：
    - 将这两个`src`属性替换为用于指定 URL 的正确属性。
```html
<h1>Welcome XYZ Pet Adoption!</h1>

<p>Consider adopting a pet today. We have cats, dogs, rabbits and more.</p>

  

<h2>See our cats!</h2>

<img href="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" att="Two tabby kittens sleeping together on a couch."></img>

  

<h2>Adopt a cat!</h2>

<a src="/cats">Visit cats page</a>

  

<h2>Adopt a dog!</h2>

<a src="/dogs">Visit dogs page</a>
```
```
# 构建活动中心

构建一个功能与此示例项目类似的应用程序。尽量不要照搬示例项目，要融入你自己的风格。

在本实验中，你将利用语义化的HTML元素来创建网页结构。你将添加内容和图片，使其看起来像一个真实的活动中心。

**目标：**完成以下用户故事，并通过所有测试以完成实验。

**用户故事：**

1. 你应该有一个`header`元素。
    
2. 在元素内部`header`，应该有一个`h1`包含文本的元素`Event Hub`和一个`nav`元素。
    
3. 在该`nav`元素内部，您应该有一个包含两个项目的无序列表，每个项目都包含指向页面不同部分的链接。第一个项目应该包含文本`Upcoming Events`，第二个项目应该包含文本`Past Events`。
    
4. `a`每个链接都应该由一个带有属性的元素表示，该属性分别`href`链接到页面的相应部分。`#upcoming-events``#past-events`
    
5. 你应该有一个`main`元素，其中包含页面的各个部分。
    
6. 该元素内部`main`应该有两个`section`元素。
    
7. 第一个`section`元素应该有一个`id`值为的属性。`upcoming-events`
    
8. 该`#upcoming-events`部分内容应包含：
    
    - `h2`包含文本的元素`Upcoming Events`。
    - 两个`article`要素。每篇文章应代表一个事件，并且应包含：
        - `h3`用于设置活动标题的元素。
        - 事件描述元素`p`。您可以根据需要添加底部日期。
9. 第二个`section`元素应该有一个`id`值为 的属性`past-events`。
    
10. 该`#past-events`部分内容应包含：
    
    - `h2`包含文本的元素`Past Events`。
    - 两个`article`要素。文章的每个要素都应代表一个过去的事件，并且应包含：
        - `h3`事件标题元素
        - 事件描述元素`p`。您可以根据需要添加底部日期。
        - 一个图像元素，其`src`属性指向图像文件，其`alt`属性包含图像描述。

**注：**活动描述和日期可以使用任何文本。图片可以使用以下图片链接（如有需要）：

- `https://cdn.freecodecamp.org/curriculum/labs/past-event1.jpg`。
- `https://cdn.freecodecamp.org/curriculum/labs/past-event2.jpg`。
```

```
# 构建结账页面

构建一个功能与此示例项目类似的应用程序。尽量不要照搬示例项目，要融入你自己的风格。

**目标：**完成以下用户故事，并通过所有测试以完成实验。

**用户故事：**

1. 你应该有一个`h1`包含文本的元素`Checkout`。
2. `section`该元素之后应该紧跟两个元素`h1`。
3. 第一部分中应该包含一个`h2`带有文本的元素。`Your Cart`
4. 第一部分应该包含一张物品图片，并配上合适的替代文字。您可以使用这张图片：`https://cdn.freecodecamp.org/curriculum/labs/cube.jpg`
5. 你应该在第二个部分中添加一个`h2`包含文本的元素。`Payment Information`
6. `form`第二部分中应该包含一个元素。
7. 你的表单中应该有一个带有 ` `id`and`和 ` `name`of` 的输入框，以及一个与它关联的 ` a` 。`card-name``type``text``label`
8. 你的表单中应该有一个带有 ` `id`and`和 ` `name`of` 的输入框，以及一个与它关联的 ` a` 。`card-number``type``text``label`
9. 至少应该有两个`input`元素具有该`required`属性。
10. 您应该在每个必填输入框的元素内添加一个包含`span`文本的元素`*`，并将`aria-hidden`其设置为，以便直观地显示必填字段。`true``label`
11. 您应该`p`在卡号输入框后紧跟一个包含帮助文本的元素，解释所需的卡号格式。该元素`p`应该有一个`id`属性`card-number-help`，并由卡号输入框引用`aria-describedby`。
```
```
# 设计电影评论页面

构建一个功能与此示例项目类似的应用程序。尽量不要照搬示例项目，要融入你自己的风格。

**目标：**完成以下用户故事，并通过所有测试以完成实验。

**用户故事：**

1. 你应该有一个`main`元素。
2. 在元素内部`main`，应该有一个`h1`用于显示电影标题的元素。
3. 在元素下方`h1`，您应该添加一个`img`显示电影封面的元素。该`img`元素应包含描述`alt`图片的文字说明。您可以随意使用以下图片`https://cdn.freecodecamp.org/curriculum/labs/rise-beyond-2.png`：
4. 你应该添加一个`p`包含简短电影介绍的元素。
5. 您应该添加另一个`p`元素来显示电影评分。在该元素内，您应该按以下顺序包含这些项目：
    - `strong`包含文本的元素`Movie Rating:`。
    - 一个`span`元素，其`aria-hidden`属性设置为`true`包含使用星级的评分的视觉表示`⭐⭐⭐⭐⭐⭐⭐⭐⭐☆`。
    - `9.2/10`跨度后的括号内为数值，表示评分（例如）。
6. 你应该有一个`h2`包含文本的元素`Cast Members`。
7. 你应该有一个`ul`元素。
8. 在元素内部`ul`，你应该有多个`li`元素，每个元素都包含一个`strong`演员姓名元素，后跟相应的角色名称，前面加上文本`as`。（例如，`James Holloway as Ethan Carter`）。
```
```
调试 Camperbot 的个人资料页面

Camperbot 正在尝试构建一个个人资料页面。他们请一位朋友检查了他们的代码，结果发现有一些错误。

你的任务是修复 Camperbot 的所有错误，以便他们能够继续构建个人资料页面。请完成以下用户故事中的项目，然后点击“运行测试”来查看是否已修复所有错误。

**用户故事：**

1. Camperbot 正在尝试使用某个`heading2`元素，但该元素不存在。请修复这些标签，使其使用正确的二级标题元素。
2. Camperbot 正在尝试添加两个带有 的段落`pp`，但它们也不存在。请修复它们，使其使用正确的段落标签。
3. Camperbot 正在使用一个`h3`元素作为`Background and Interests`副标题，但该元素存在语法错误。请找出问题并解决。
```html
<h1>Hello from Camperbot!</h1>

  

<heading2>About</heading2>

  

<pp>My name is Camperbot and I love learning new things.</pp>

  

<h3>Background and Interests<h3/>

<pp>I enjoy solving puzzles.</pp>
```

```

# 构建多媒体播放器

构建一个功能与此示例项目类似的应用程序。尽量不要照搬示例项目，要融入你自己的风格。

在之前的课程中，你已经学习了如何使用音频`audio`和`video`文本元素。在本实验中，你将构建一个多媒体播放器，用于显示`audio`音频文件及其`video`对应的文字稿。

对于该`audio`元素，您需要包含一个`source`用于指定所用媒体的元素。

以下是一个例子：

```html
<audio controls aria-label="descriptive label goes here">
  <source src="url-to-audio-goes-here" type="audio/mpeg">
</audio>
```

该元素也可以像这样在元素`source`中使用：`video`

```html
<video controls width="600" aria-label="descriptive label goes here">
  <source src="link-to-mp4-goes-here" type="video/mp4">
  <!-- Remaining code goes here -->  
</video>
```

**目标：**完成以下用户故事，并通过所有测试以完成实验。

**用户故事：**

1. `h1`页面主标题应该有一个元素。
2. 你应该包含三个`section`要素。
3. 在第一个`section`元素中，应该有一个`h2`用于显示正在播放歌曲标题的元素。
4. 该元素下方`h2`应该有一个带有属性和另一个属性的`audio`元素。`controls``aria-label`
5. 在元素内部`audio`，您应该有一个`source`元素，该元素带有一个`src`指向音频文件的属性和一个`type`属性。您可以随意使用此音频 URL：`https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3`
6. 在第二个`section`元素中，应该有一个`h2`用于显示正在播放视频标题的元素。
7. 在元素下方`h2`，应该有一个带有属性和属性的`video`元素。`controls``width``aria-label`
8. 在元素内部`video`，您应该有一个`source`元素，该元素带有一个`src`指向视频文件的属性和一个`type`属性。您可以随意使用此视频 URL：`https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4`
9. 在元素下方`source`，您应该有一个`track`元素，该元素具有`src`指向字幕文件的属性、一个`kind`属性、一个`srclang`属性和一个`label`属性。
10. 在第三个`section`元素中，您应该有一个`h2`用于显示章节标题的元素，例如“成绩单”。
11. 该元素下方`h2`应该有一个`p`包含视频文字稿的元素。

## CSS基础知识

- **什么是 CSS？：**层叠样式表 (CSS) 是一种用于为 HTML 元素应用样式的标记语言。CSS 用于设置颜色、背景图像、布局等等。
- CSS 的另一个重要特性是其层叠特性，这也是其名称中“层叠”一词的由来。这意味着样式可以被继承和覆盖，从而实现样式的层级结构。
- **CSS 规则的基本结构**：CSS 规则由两部分组成：选择器和声明块。选择器是 CSS 中用于识别和定位特定 HTML 元素以应用样式的模式。声明块(花括号)为给定的选择器（或多个选择器）应用一组样式。
```css

selector {
  property: value;
}
```
在声明块内，你会看到一系列声明。每个声明都包含一个属性和一个值。
该属性是 CSS 标识符，用于指定要设置样式的功能。例如，`<feature>` 属性就是一个示例`background-color`。
该值是应用于该属性的具体设置。例如，如果属性名为 `<property>` `background-color`，则其值可以是 `<value>` `purple`，这会将背景颜色设置为紫色。
在每个属性名称后面要加冒号，在每个值后面要加分号。
如果要将同一组样式应用于多个选择器，可以创建一个选择器列表，每个选择器之间用逗号分隔。

以下是设置多个选择器样式的示例：

```html
<link rel="stylesheet" href="styles.css">

<h1 id="title">Example heading</h1>
<h2 class="subheading">Example subheading</h2>
<p>This paragraph is not affected by the selector.</p>
```

```css
#title,
.subheading {
  color: navy;
}
```
在这个选择器列表中，有一个选择器指向值为 的`id`HTML 元素。所有选择器都必须以井号 (#) 开头。`id``title``id``#`

然后是一个逗号，后面跟着一个选择器，该选择器会选中所有值为 `<class>` 的`class`HTML 元素。所有类选择器都必须以点号开头。`class``subheading``.`

- **`meta name="viewport"`元素**：此`meta`元素向浏览器提供指令，说明如何控制页面在不同设备上的尺寸和缩放，尤其是在手机和平​​板电脑上。
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
这`width=device-width`部分代码指示浏览器将页面宽度设置为与设备屏幕宽度相匹配。这对于创建能够适应不同屏幕尺寸的响应式布局至关重要。

此`initial-scale=1.0`参数设置页面首次加载时的初始缩放级别。值为 1.0 表示页面以`100%`默认缩放比例显示，不进行任何缩放。

通过使用 meta viewport 元素，您可以确保网页在移动设备上正确显示。

如果没有它，移动浏览器通常会以桌面屏幕宽度渲染页面，然后再缩小，这会导致文本过小、难以阅读，从而造成糟糕的用户体验。

meta viewport 元素还可以控制用户是否可以放大和缩小您的网页。

虽然可以通过`user-scalable=no`属性禁用缩放功能，但出于辅助功能方面的考虑，通常建议避免这样做。

许多用户依靠缩放功能来提高阅读体验，尤其是那些有视力障碍的用户。
- **默认浏览器样式**：每个 HTML 元素都会应用默认浏览器样式。这通常包括默认边距和内边距等设置。


## 内联、内部和外部 CSS

- **内联 CSS**：这些样式直接使用属性写入 HTML 元素中`style`。大多数情况下，由于关注点分离的原则，您不会使用内联 CSS。
- **内部 CSS**：这些样式写在HTML 文档的 `<style>` `<head>` 标签内`head`。这对于创建简短的代码示例很有用，但通常情况下，您不会使用内部 CSS。当您需要将样式应用于特定页面而非多个页面时，最好使用内部 CSS。它适用于单页网站或样式无需在其他地方重复使用的情况。
- **外部 CSS**：这些样式写在单独的 CSS 文件中，并通过 ` `link`<head>` 元素链接到 HTML 文档的 `<head>` 部分`head`。对于大多数项目，您会使用外部 CSS 文件而不是内部或内联 CSS。
```html

<link rel="stylesheet" href="styles.css" />

<nav class="navbar">
    <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>
```
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', sans-serif;
  background-color: #f4f4f4;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 1rem 2rem;
  color: white;
}

.navbar .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #ff9800;
}
```

## `width`与`height`属性合作
可以用不同的单位定义，例如像素（`px`）、百分比（`%`）、视口单位（`vw`、`vh`）等等。
- **`width`属性**：此属性指定元素的宽度。如果未指定宽度，则默认值为 0。`auto`这样，浏览器将根据元素的内容、父元素和显示类型来确定元素的宽度。
- **`min-width`属性**：此属性指定元素的最小宽度。
- **`max-width`属性**：此属性指定元素的最大宽度。
- **`height`属性**：此属性指定元素的高度。同样，高度默认`auto`为 1，这意味着它会根据内部内容自动调整。
- **`min-height`属性**：此属性指定元素的最小高度。
- **`max-height`属性**：此属性指定元素的最大高度。
```html
<head>
  <style>
    .box {
      width: 50px;
      min-width: 100px;
      height: 50px;
      min-height: 100px;
      background-color: lightcoral;
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
```
即使盒子的宽度`width`和高度都`height`设置为 50px，它的实际宽度也会是`100px`100px `100px`。这是因为盒子的宽度`min-width`和高度`min-height`都被设置为100px `100px`，这比指定的宽度`width`和高度要大`height`。
## 行内元素、块级元素和行内块级元素

- **行内元素**：行内元素仅占用所需的宽度，且不另起一行。这些元素融入内容中，允许文本和其他行内元素与其并排显示。常见的行内元素包括 `<div>`、`<span>` `span`和`anchor` ` `img `<div>` 元素。行内元素默认应用 CSS 属性`display: inline;`。此属性确保元素始终位于内容流中，不会换行显示。行内元素只占用所需的空间。它们融入周围的内容中，不会换行显示,无法控制其大小
- **块级元素**：默认情况下，块级元素会占据容器的全部宽度，横跨整个容器。一些常见的块级元素包括 `<div>` `div`、`paragraph` `<span>` 和`section` `<div>` 元素。
- 块级元素`display: block;`默认应用 CSS 属性。此属性确保元素拉伸以填充容器宽度，并显示在新的一行。
- **行内块级元素**`inline-block`：您可以使用属性将元素设置为行内块级`display`元素。这些元素的行为类似于行内元素，但可以拥有 `<div>` 标签`width`并`height`像块级元素一样进行设置。


## CSS 特异性

- **内联 CSS 优先级**：内联 CSS 具有最高的优先级，因为它直接应用于元素。它会覆盖任何内部或外部 CSS。内联样式的优先级值为 (1, 0, 0, 0)。
- **内部 CSS 优先级**：内部 CSS 定义`style`在 HTML 文档的 `<head> `元素内 `head`。它的优先级低于内联样式，但可以覆盖外部样式。
- **外部 CSS 优先级**`link`：外部 CSS 通过`<head>` 元素链接到 `<head>`head`部分，并编写在单独的`.css`文件中。它的优先级最低，但对于大型项目而言，可维护性最佳。
- **通用选择器 ( `*`)**：一种特殊的 CSS 选择器，可以匹配文档中的任何元素。它通常用于将样式应用于页面上的所有元素，这对于在不同浏览器中重置或规范样式非常有用。通用选择器的优先级最低，其优先级值的所有部分均为 0 (0, 0, 0, 0)。
- **类型选择器**：这类选择器根据元素的标签名称来选择元素。与其他选择器相比，类型选择器的特异性相对较低。类型选择器的特异性值为 (0, 0, 0, 1)。
- **类选择器**：这类选择器由句点 ( `.`) 后跟类名定义。类选择器的优先级值为 (0, 0, 1, 0)。这意味着类选择器可以覆盖类型选择器，但可以被 ID 选择器和内联样式覆盖。
- **ID 选择器**：ID 选择器由井号 (#) 后跟 ID 名称定义`#`。ID 选择器的优先级非常高，高于类型选择器和类选择器，但低于内联样式。ID 选择器的优先级值为 (0, 1, 0, 0)。
- **`!important`关键字**：用于赋予样式规则最高优先级，使其能够覆盖属性的任何其他声明。使用后，它会强制浏览器应用指定的样式，而忽略其他选择器的优先级。使用时应谨慎，`!important`因为它可能会使 CSS 更难维护和调试。
- **层叠算法**：层叠算法是浏览器在多个样式指向同一元素时，决定应用哪些 CSS 规则的过程。它确保根据一组定义明确的规则，使用最合适的样式。这个过程始于**相关性判断**。浏览器首先会筛选所有 CSS 规则，找到真正适用于目标元素的规则。这包括匹配选择器，并考虑可能生效的媒体查询。媒体查询是一种 CSS 技术，用于根据设备或视口的特征（例如宽度、高度或方向）应用样式。接下来，算法会考虑样式**的来源和重要性**。CSS 可以来自不同的来源：浏览器的默认样式（用户代理）、用户设置的样式以及作者（您）编写的样式。在考虑规则来源之后，该算法会评估每条规则的重要性，优先考虑标有 的规则`!important`，这些规则会覆盖其他规则，而不管它们的来源如何。在按来源和重要性进行筛选后，算法会考虑**特异性**。当两条规则来源和重要性级别相同时，将采用特异性更高的规则。特异性是衡量选择器针对性强弱的指标，更具体的选择器优先于更一般的选择器。最后，如果其他条件相同，则**规则的出现顺序**会起作用。当两条规则的优先级相同时，CSS 中最后出现的那条规则会被应用。
```html
<link rel="stylesheet" href="styles.css">

<p>example paragraph</p>
```

```css
p {
  color: blue;
}

p {
  color: green; 
}
```

第一条规则将所有段落元素的文本颜色设置为蓝色，第二条规则将所有段落元素的文本颜色设置为绿色。

那么，将使用哪种颜色呢？段落元素将使用绿色。

通过考虑相关性、来源和重要性、特异性、范围和出现顺序，层叠算法确保您的 CSS 行为可预测，使您能够设计更复杂、更细致的网页。
- **CSS 继承**：
样式从父元素传递到子元素的过程。继承允许你在文档树的更高层级定义样式，并使其应用于多个元素，而无需为每个元素显式指定样式。
在 CSS 中，并非所有属性都会默认继承。例如，`textcolor` `color`、 `text `font-family`-color` 和`text-color` 等属性`line-height`是会继承的。这意味着，如果您设置了父元素的文本颜色，除非您明确地覆盖它，否则其所有子元素都会继承该颜色。
```html
<div style="color: blue;">
  This is the parent element.
  <p>This is the child element inheriting the color.</p>
</div>
```
在这种情况下，父元素`div`和子元素`p`都会以蓝色显示文本，因为颜色是继承的。

另一方面，诸如`margin`` `padding`<style> `、`<style>`、`<style>``border`和`<style>` 之类的属性`background`默认情况下不会被继承。如果您希望子元素继承这些样式，则需要显式地设置它们，可以直接在子元素上设置，也可以使用 ` `inherit`setStyles` 关键字。
`inherit`可以使用关键字强制从父元素继承属性，即使该属性通常不会被继承。

例如，如果您希望某个子元素`padding`与其父元素具有相同的属性，则可以`padding: inherit`在该子元素上进行设置：

```html
<div style="padding: 20px;">
  This is the parent element with padding.
  <p style="padding: inherit;">This is the child element inheriting the padding.</p>
</div>
```

在这种情况下，子`p`元素将继承`20px`父`div`元素的内边距。

继承对于保持样式表的一致性和减少冗余尤其有用。

与其为多个元素编写相同的样式规则，不如在父元素上定义一次，子元素就会继承它。这样可以使你的 CSS 代码更简洁，更易于管理。

但是，需要注意的是，继承是单向的——从父元素到子元素。如果您覆盖子元素的样式，它不会影响父元素。

## 单位
### 绝对单位
1 `in`=2.54`cm`=25.4`mm`=72`pt`=6`pc`
对长度单位的长度是固定的，不与其他任何事物相关。
- **`px`像素（Pixels）**：这是 CSS 中的一个绝对单位，用于精确控制尺寸。这意味着 1 像素始终等于 1/96 英寸。
- **`in`（英寸）**：此绝对单位等于 96px。
- **`cm`（厘米）**：该绝对单位等于 25.2/64 英寸。
- **`mm`（毫米）**：该绝对单位等于 1/10 厘米。
- **`q`（四分之一毫米）**：该绝对单位等于 1/40 厘米。
- **`pc`（派卡）**：该绝对单位等于 1/6 英寸。
- **`pt`（分数）**：该绝对单位等于 1/72 英寸。

### 相对单位
相对长度单位则是指长度相对于其他事物（例如屏幕大小或父元素大小）而言的。
- **百分比**：这些相对单位允许您将大小、尺寸和其他属性定义为其父元素的比例。例如，如果您将`width: 50%;`某个元素的宽度设置为 1，它将占据其父容器宽度的一半。
- **`em`单位**：这些单位相对于元素的字体大小。如果您将此属性`ems`用于文本`font-size`，则文本大小将相对于父元素的字体大小。
- **`rem`单位**：这些单位是相对于根元素（即元素）的字体大小而言的`html`。
- **`vh`单位**：`vh`表示`"viewport height"`并`1vh`等于视口高度的 1%。
- **`vw`单位**：`vw`代表视口宽度的 1% `"viewport width"`，`1vw`等于视口宽度的 1%。

### `calc`功能

- **`calc()`功能**：借助此`calc()`功能，您可以直接在样式表中执行计算，从而动态确定属性值。这意味着您可以根据视口大小或其他元素计算尺寸，从而创建灵活且响应迅速的用户界面。

## CSS中处理颜色的不同方法

- **命名颜色**：这些颜色是浏览器可识别的预定义颜色名称。例如`blue`， `darkred`、`lightgreen`...
```css
background-color: red;
```
- **`rgb()`功能**：RGB 代表红色、绿色和蓝色——光的三原色。。r、g、b的值，每个值的取值范围0~255，一共256个值。这三种颜色以不同的强度组合，可以创造出丰富的色彩。该`rgb()`功能允许您使用 RGB 颜色模型定义颜色。
```css
element {
  color: rgb(red, green, blue);
}
```
> **RGB色彩模式：**
> - 自然界中绝大部分颜色都可以用红、绿、蓝(RGB)这三种颜色波长的不同强度组合而得，这就是人们常说的三原色原理。
> - RGB三原色也叫加色模式，这是因为当我们把不同光的波长加到一起的时候，可以得到不同的混合色。例：红+绿=黄色，红+蓝＝紫色，绿+蓝=青。
> - RGB各有256级(0-255)亮度，256级的RGB色彩总共能组合出约1678万种色彩，即256×256×256=16777216。
> 在数字视频中，对RGB三基色各进行8位编码就构成了大约1678万种颜色，这就是我们常说的真彩色。所有显示设备都采用的是RGB色彩模式。


- **`rgba()`功能**：此函数添加了第四个值——alpha——来控制颜色的透明度。`alpha` 值的范围从`0` （完全透明）到`1`（完全不透明）。
- **`hsl()`功能**：HSL 代表色相、饱和度和亮度——定义颜色的三个关键组成部分。
```css
element {
  color: hsl(hue, saturation, lightness);
}
```
HSL颜色模型的主要优点之一是其直观性。它可以通过调整饱和度和亮度值来轻松调整颜色的鲜艳度或明度，而无需改变核心颜色（色调）。
- **`hsla()`功能**：此函数添加第四个值 -alpha-，用于控制颜色的不透明度。
```css
element {
  background-color: hsla(hue, saturation, lightness, alpha);
}
```
>- `H` 色调，取值范围 0~360。0或360表示红色、120表示绿色、240表示蓝色。
>- `S` 饱和度，取值范围 0%~100%。值越大，越鲜艳。
>- `L` 亮度，取值范围 0%~100%。亮度最大时为白色，最小时为黑色。
>- `A` 透明度，取值范围 0~1。
![[色盘.png]]

[配色宝典](https://www.uisdc.com/how-to-create-color-palettes)

- **十六进制**：十六进制代码（简称十六进制代码）是一个六字符字符串，用于表示 RGB 颜色模型中的颜色。“十六进制”指的是以 16 为基数的计数系统，该系统使用数字 0 到 9 和字母 A 到 F。
**十六进制可以简化为3位，所有#aabbcc的形式，能够简化为#abc**。
```css
	background-color:#ff0000;
```

等价于：

```css
	background-color:#f00;
```
##  CSS 选择器
### id选择器
ID 选择器是 CSS 中最强大的选择器之一，它允许开发人员使用唯一标识符将样式应用于特定元素。这使得它们在针对需要独特样式设计的单个元素方面非常有效。
`#`ID 选择器由井号 ( #) 后跟 ID 名称定义。它们在 HTML 文档中必须是唯一的，也就是说，任何两个元素都不应该拥有相同的 ID。
```html
<link rel="stylesheet" href="styles.css">
<p id="unique">Example paragraph</p>
<p>Another paragraph</p>
<p>Yet another paragraph</p>
```

```css
#unique {
  color: purple;
}
```
ID 选择器的特异性非常高，高于类型选择器和类选择器，但低于内联样式。ID 选择器的特异性值为`(0, 1, 0, 0)`。

### class选择器
类选择器是 CSS 的关键组成部分，它允许开发人员使用相同的类属性来定位多个元素，并应用一致的样式。这使得它们用途广泛且效率极高，可以有效地在整个网站上应用样式。类选择器由句点 ( ) 后跟类名定义`.`。它们可以应用于 HTML 文档中的任何元素。
```html
<link rel="stylesheet" href="styles.css">
<p class="highlight">Example paragraph</p>
```

```css
.highlight {
  color: green;
}
```
类选择器的优先级高于类型选择器，但低于 ID 选择器和内联样式。
类选择器的特异性值为`(0, 0, 1, 0)`。这意味着类选择器可以覆盖类型选择器，但可以被 ID 选择器和内联样式覆盖。

### 标签选择器
类型选择器，也称为元素选择器，根据元素的标签名称来选择目标元素。这些选择器是 CSS 的基础，允许你将样式应用于特定 HTML 元素的所有实例。类型选择器使用起来很简单，只需写成要设置样式的元素的标签名称即可。
```html
<link rel="stylesheet" href="styles.css">

<p>Paragraph one</p>
<p>Paragraph two</p>
<p>Paragraph three</p>
```

```css
p {
  color: blue;
}
```
与其他选择器相比，类型选择器的特异性相对较低。类型选择器的特异性值为`(0, 0, 0, 1)`。
### 属性选择器
该选择器根据给定的属性值来选择元素。
```CSS
.radio-group input[type="radio"] {
}
```
-**合并选择器以匹配同时具有`href`和`title`属性的**链接：合并多个属性选择器。
```css
a[href][title] {
  display:block;
  color: green;
}
```
`[attr~=value]`这里使用语法来定位所有 class 属性包含单词的锚元素`"primary"`。
```CSS
a[class~="primary"] {
  color: red;
  font-weight: bold;
}

```

如果您需要定位某个元素，并且该元素的属性值带有特定前缀，则可以使用`[attr^=value]`以下语法。
```css
a[href^="https://"] {
  color: green;
  text-decoration: underline;
}
```


要定位属性值以特定值结尾的元素，可以使用以下`[attr$=value]`语法。
```css
a[href$=".com"] {
  color: darkgreen;
  text-decoration: underline dotted;
}
```
 **匹配包含子字符串的值**：目标链接包含`https`值中的任何位置。
 ```css
a[href*="https"] {
  color: teal;
}
 ```
 使用`lang`and`data-lang`属性定位元素
- **`lang`属性**：此属性用于 HTML 中，以指定元素内内容的语言。您可能需要根据元素所使用的语言来设置不同的样式，尤其是在多语言网站上。

```css
p[lang="en"] {
  font-style: italic;
}
```

- **`data-lang`属性**：自定义数据属性（例如`data-lang`属性）通常用于在元素中存储附加信息，例如指定特定文本部分使用的语言。以下是如何根据`data-lang`属性设置元素样式：

```css
div[data-lang="fr"] {
  color: blue;
}
```

使用属性选择器、有序列表元素和`type`属性

- **`type`属性**：在 HTML 中使用有序列表时，该`type`属性允许您指定使用的编号样式，例如数字、字母或罗马数字。

```css
/*Example targeting uppercase alphabetical numbering*/
ol[type="A"] {
  color: purple;
  font-weight: bold;
}

/*Example targeting lowercase Roman numerals*/
ol[type="i"] {
  color: green;
}
```
### 通用选择器
通用选择器（`*`）是一种特殊的 CSS 选择器，可以匹配文档中的任何元素。它通常用于将样式应用于页面上的所有元素，这对于在不同浏览器中重置或规范样式非常有用。通用选择器可用于选择特定上下文中的所有元素，或选择整个文档中的所有元素
```html
<link rel="stylesheet" href="styles.css">

<h1>Heading element</h1>
<p>example paragraph element</p>
```

```css
* {
  margin: 0;
  padding: 0;
}
```
在这个代码示例中，`*`选择器将所有元素的边距和内边距重置为零，这是 CSS 重置中常用的一种技术。通用选择器的特异性值是所有选择器中最低的，它对特异性值的所有组成部分的贡献均为0 `(0, 0, 0, 0)`。这意味着任何其他选择器，包括类型选择器、类选择器、ID 选择器和内联样式，都将覆盖通用选择器设置的样式。

### !important
CSS 中的关键字`!important`用于赋予样式规则最高优先级，使其能够覆盖属性的任何其他声明。
使用后，它会强制浏览器应用指定的样式，而不管其他选择器的特异性如何。
```html
<link rel="stylesheet" href="styles.css">

<p class="para" style="background-color: lightblue; color: black;">
  This is a paragraph.
</p>
```

```css
.para {
  background-color: black !important;
  color: white !important;
}
```
关键字`!important`用在 CSS 值之后、分号之前。
CSS 中的关键字`!important`用于赋予样式规则最高优先级，从而有效地覆盖其他声明，包括具有更高优先级的声明和内联样式。

然而，`!important`关键字并不会改变 CSS 选择器本身的优先级。它只是确保`!important`即使存在优先级更高的冲突规则，也会应用带有关键字的规则。


可以通过创建一个选择器列表，将同一组样式添加到多个元素上。每个选择器之间用逗号分隔，格式如下:
```css
selector1, selector2 {
  property: value;
}
```

### 交集选择器
![[交集选择器.png]]
```
<style type="text/css"> h3.special{ color:red; } </style>
```
选择的元素要求同时满足两个条件：必须是h3标签，然后必须是special标签。
注意，交集选择器没有空格。所以，没有空格的`div.red`（交集选择器）和有空格的`div .red`（后代选择器）不是一个意思。
### 组合选择器
CSS组合器用于定义CSS选择器之间的关系。它们有助于根据元素与其他元素的关系来选择元素，从而实现更精确、更高效的样式设置。

- **后代组合器**：此组合器用于定位指定父元素的后代元素。
    
- **子组合器（`>`）**：此组合器用于选择指定父元素的直接子元素。
    此组合器仅针对具有特定父元素的元素，使您的 CSS 规则更加精确，并防止对更深层嵌套元素进行意外样式设置。

```
<link rel="stylesheet" href="styles.css">

<div class="container">
  <p>First</p>
  <div>
    <p>Second</p>
  </div>
  <div>
    <p>Third</p>
  </div>
</div>

css
.container > p {
  color: blue;
}

```





在上面的例子中，我们只针对`container`类的直接子元素。这将使直接子元素的文本颜色为`blue`。

因为另外两个段落元素嵌套在`div`元素内，所以它们不被视为该类的直接子元素`container`，因此不会获得蓝色文本颜色。

- **下一个兄弟组合器（`+`）**：此组合器选择紧随指定兄弟元素之后的元素。
```html
<link rel="stylesheet" href="styles.css">

<figure>
  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="A cute orange cat lying on its back."
  />
  <figcaption>A cute orange cat lying on its back.</figcaption>
</figure>
```


```css
img + figcaption {
  border: 4px solid black;
}
```

在这个例子中，下一个兄弟元素组合器（`+`）选择`figcaption`紧随该元素之后的元素`img`。应用的 CSS 规则`4px solid black border`在该元素周围添加了一个`figcaption`。
- **后续兄弟组合器（`~`）**：此组合器选择指定元素之后的所有兄弟元素。
```html
<link rel="stylesheet" href="styles.css">

<div class="container">
  <h2>Subheading</h2>
  <p>First paragraph.</p>
  <p>Second paragraph.</p>
  <p>Third paragraph.</p>
  <p>Another paragraph element</p>
</div>
```

```css
h2 ~ p {
  color: green;
}
```

在这个例子中，该元素之后的所有段落元素的`h2`文本颜色都将是绿色。

后续兄弟组合器（`~`）以元素之后出现的所有段落兄弟为目标`h2`，无论它们是否是直接兄弟。

### 用户操作伪类

- **伪类定义**：这些是特殊的 CSS 关键字，允许您根据元素的特定状态或位置来选择元素。
- 要使用伪类，您需要在选择器中使用冒号 ( `:`)，后跟伪类的名称
- ```css
selector:pseudo-class {
  /* CSS properties */
}
```
- **用户操作伪类**：这些是特殊的关键字，允许您根据用户交互改变元素的外观，从而改善整体用户体验。
- **`:active`伪类**：此伪类允许您选择元素的活动状态，例如单击按钮。
- **`:hover`伪类**：此伪类定义元素的悬停状态。
- **`:focus`伪类**：此伪类在元素获得焦点时应用样式，通常是通过键盘导航或用户单击表单输入时。
- **`:focus-within`伪类**：此伪类用于在元素或其任何后代获得焦点时为其应用样式。

### 输入伪类

- **输入伪类**：这些伪类用于`input`根据用户交互前后 HTML 元素的状态来定位它们。
- **`:enabled`伪类**：此伪类用于定位当前已启用的表单按钮或其他元素。
- **`:disabled`伪类**：此伪类允许您在禁用模式下设置交互式元素的样式。
- **`:checked`伪类**：此伪类用于向用户指示它已被选中。
- **`:valid`伪类**：此伪类针对符合验证标准的输入字段。
- **`:invalid`伪类**：此伪类针对不符合验证标准的输入字段。
- **`:in-range`伪`:out-of-range`类**：这些伪类根据元素的值是否在指定的范围约束内或外，对元素应用样式。
- **`:required`伪类**：此伪类针对`input`具有该属性的元素`required`。它向用户发出信号，表明他们必须填写该字段才能提交表单。
- **`:optional`伪类**：此伪类应用样式，用于设置非必需且可以留空的输入元素。
- **`:autofill`伪类**：此伪类将样式应用于浏览器自动填充已保存数据的输入字段。

### 位置伪类

- **位置伪类**：这些伪类用于设置当前文档中目标链接和元素的样式。
- **`:any-link`伪类**`:link`：此伪类是 `<a>`和`<b>` 伪类的组合`:visited`。因此，它匹配任何带有 href 属性的锚元素，无论该元素是否被访问。
- **`:link`伪类**：此伪类允许您定位网页上所有未访问的链接。您可以使用它在用户点击链接之前为其设置不同的样式。
- **`:local-link`伪类**：此伪类用于指定指向同一文档的链接。当您想要区分内部链接和外部链接时，它非常有用。
- **`:visited`伪类**：此伪类指向用户访问过的链接。
- **`:target`伪类**：此伪类用于为 URL 片段的目标元素应用样式。

### 树状结构伪类

- **树状结构伪类**：这些伪类允许您根据元素在文档树中的位置来定位和设置元素样式。
- **`:root`伪类**：这个伪类通常是根`html`元素。它可以帮助你将目标定位到文档的最高层级，从而将通用样式应用于整个文档。 
- **`:empty`伪类**：空元素，即除了空格之外没有其他子元素的元素，也会被包含在文档树中。这就是为什么需要使用`:empty`伪类来定位空元素的原因。
- **`:nth-child(n)`伪类**：此伪类允许您根据元素在父元素中的位置来选择元素。计数`n`可以是特定的数字，也可以是关键字，例如 odd或even。这在根据位置（例如奇数和偶数）设置表格单元格样式时非常有用。
- **`:nth-last-child(n)`伪类**：此伪类允许您通过从末尾开始计数来选择元素。
- **`:first-child`伪类**：此伪类选择父元素或文档中的第一个元素。
- **`:last-child`伪类**：此伪类选择父元素或文档中的最后一个元素。
- **`:only-child`伪类**：此伪类选择父元素或文档中的唯一元素。
- **`:first-of-type`伪类**：此伪类选择其父元素中特定元素类型的第一个出现位置。
- **`:last-of-type`伪类**：此伪类选择其父元素中特定元素类型的最后一个出现位置。
- **`:nth-of-type(n)`伪类**：此伪类允许您根据元素在同类型同级元素中的位置，选择其父元素内的特定元素。
- **`:only-of-type`伪类**：此伪类选择父元素中唯一具有该类型的元素。

### 函数式伪类

- **函数式伪类**：函数式伪类允许您根据更复杂的条件或关系选择元素。与基于状态（例如，`isState`、`isFactory` 和 `isState`）选择元素的常规伪类不同`:hover`，`:focus`函数式伪类接受参数。
- **`:is()`伪类**：此伪类接受一个选择器列表（例如`ol`，`ul`），并选择与列表中的某个选择器匹配的元素。
```html
<p class="example">This text will change color.</p>
<p>This text will not change color.</p>
<p>This text will not change color.</p>
<p class="this-works-too">This text will change color.</p>
```

```css
p:is(.example, .this-works-too) {
    color: red;
}
```
- **`:where()`伪类**：此伪类接受一个选择器列表（例如 `{{ }` `ol`、`ul``{{ }`），并选择与列表中某个选择器匹配的元素。`{{ }``:is`和`{{ }` 的区别`:where`在于后者具有 0 的特异性。
```css
:where(h1, h2, h3) {
    margin: 0;
    padding: 0;
}
```
- **`:has()`伪类**：这个伪类通常被称为`"parent"`选择器，因为它允许你设置包含选择器列表中指定的子元素的元素的样式。
```css
article:has(h2) {
    border: 2px solid hotpink;
}
```
* - **`:not()`伪类**：此伪类用于选择与提供的选择器不匹配的元素。
```css
p:not(.example) {
  color: blue;
}
```
### 伪元素
CSS 最有趣的方面之一就是伪元素的使用。这里的“伪”指的是“非真实的”，因此伪元素是虚拟的或合成的元素，它们并不直接对应任何实际的 HTML 元素。伪元素允许你设置元素特定部分的样式，或者插入内容而无需添加额外的 HTML 代码。
要应用伪元素，请使用双冒号 ( `::`) 将其附加到原始元素的选择器上。请注意，选择器可以是任何类型，例如类选择器或 ID 选择器。以下是伪元素的基本语法：

```css
selector::pseudo-element {
  property: value;
}
```

双冒号是伪元素与伪类的区别所在，伪类使用单冒号。

伪元素允许您设置元素内容的特定部分样式，或在其前后插入内容，但它们不能独立存在。伪元素所附加的元素称为其源元素。
- **`::before`伪元素**：此伪元素使用该`content`属性在元素之前插入图标等装饰性内容。
- **`::after`伪元素**：此伪元素使用该`content`属性在元素后插入图标等装饰性内容。
- **`::first-letter`伪元素**：此伪元素定位元素内容的第一个字母，允许您设置其样式。
- **`::marker`伪元素**：此伪元素允许您选择列表项的标记（项目符号或编号）以设置样式。

内容属性用于设置或覆盖元素的内容。默认情况下，由`.before`和`after选择器创建的伪元素是空的，这意味着它们不会在页面上被呈现。通过将内容属性设置为空字符串，可以确保这些伪元素被呈现出来，同时仍保持其空态。

## 注释
```css
/* comment here */
```

## 字体样式

### 字体
- 字号 font-size
- 字体：（font-family就是“字体”，family是“家庭”的意思）
须将英语字体放在最前面，这样所有的中文，就不能匹配英语字体，就自动的变为后面的中文字体
- color 颜色


```css
	font-size: 50px; 		/*字体大小*/
	line-height: 30px;      /*行高*/
	font-family: 幼圆,黑体; 	/*字体类型：如果没有幼圆就显示黑体，没有黑体就显示默认*/
	font-style: italic ;		/*italic表示斜体，normal表示不倾斜*/
	font-weight: bold;	/*粗体*/
	font-variant: small-caps;  /*小写变大写*/
```

- font-weight 字体粗细
属性值

| 值                                                                             | 描述                                       |
| ----------------------------------------------------------------------------- | ---------------------------------------- |
| normal                                                                        | 默认值。定义标准的字符。                             |
| bold                                                                          | 定义粗体字符。                                  |
| bolder                                                                        | 定义更粗的字符。                                 |
| lighter                                                                       | 定义更细的字符。                                 |
| - 100<br>- 200<br>- 300<br>- 400<br>- 500<br>- 600<br>- 700<br>- 800<br>- 900 | 定义由细到粗的字符。400 等同于 normal，而 700 等同于 bold。 |
| inherit                                                                       | 规定应该从父元素继承字体的粗细。                         |

- font-style

| 值       | 描述                  |
| ------- | ------------------- |
| normal  | 默认值。浏览器显示一个标准的字体样式。 |
| italic  | 浏览器会显示一个斜体的字体样式。    |
| oblique | 浏览器会显示一个倾斜的字体样式。    |
| inherit | 规定应该从父元素继承字体样式。     |
- font-weight 字体加粗
```css
font-weight: normal; /*正常*/
	font-weight: bold;  /*加粗*/
	font-weight: 100;
	font-weight: 200;
	font-weight: 900;
```
在设置字体是否加粗时，属性值既可以填写`normal`、`bold`这样的加粗字体，也可以直接填写 100至900 这样的数字。`normal`的值相当于400，`bold`的值相当于700。
### 文本

- letter-spacing 字符间距

| 值        | 描述                              |
| -------- | ------------------------------- |
| normal   | 默认。规定字符间没有额外的空间。                |
| _length_ | 定义字符间的固定空间（允许使用负值）。             |
| inherit  | 规定应该从父元素继承 letter-spacing 属性的值。 |
|          |                                 |

- word-spacing 单词之间的间距
- 
- text-align 水平对齐
属性值

| 值       | 描述                          |
| ------- | --------------------------- |
| left    | 把文本排列到左边。默认值：由浏览器决定。        |
| right   | 把文本排列到右边。                   |
| center  | 把文本排列到中间。                   |
| justify | 实现两端对齐文本效果。                 |
| inherit | 规定应该从父元素继承 text-align 属性的值。 |

- vertical-align 垂直对齐
小技巧：如果一段文本只有一行，如果此时设置**行高 = 盒子高**，就可以保证单行文本垂直居中。这个很好理解。

上面这个小技巧，只适用于单行文本垂直居中，不适用于多行。如果想让多行文本垂直居中，还需要计算盒子的padding。
![[多行垂直居中.png]]
属性值

| 值           | 描述                                     |
| ----------- | -------------------------------------- |
| baseline    | 默认。元素放置在父元素的基线上。                       |
| sub         | 垂直对齐文本的下标。                             |
| super       | 垂直对齐文本的上标                              |
| top         | 把元素的顶端与行中最高元素的顶端对齐                     |
| text-top    | 把元素的顶端与父元素字体的顶端对齐                      |
| middle      | 把此元素放置在父元素的中部。                         |
| bottom      | 使元素及其后代元素的底部与整行的底部对齐。                  |
| text-bottom | 把元素的底端与父元素字体的底端对齐。                     |
| length      | 将元素升高或降低指定的高度，可以是负数。                   |
| %           | 使用 "line-height" 属性的百分比值来排列此元素。允许使用负值。 |
| inherit     | 规定应该从父元素继承 vertical-align 属性的值         |


- text-indent 缩进
属性值

| 值        | 描述                          |
| -------- | --------------------------- |
| _length_ | 定义固定的缩进。默认值：0。              |
| _%_      | 定义基于父元素宽度的百分比的缩进。           |
| inherit  | 规定应该从父元素继承 text-indent 属性的值 |

- text-shadow 文本阴影属性
语法

```
text-shadow: _h-shadow v-shadow blur color_;
```

**注意：** text-shadow属性连接一个或多个遮蔽文本。属性是遮蔽，指定的每2或3个长度值和一个可选的颜色值用于分隔分隔开来。已丢失时有效的长度为0。

| 值          | 描述                                                                                    |
| ---------- | ------------------------------------------------------------------------------------- |
| _h-shadow_ | 水平遮蔽的位置。允许负值。                                                                         |
| _v-shadow_ | 仅需。垂直遮挡的位置。允许负值。                                                                      |
| _模糊_       | 任选。模糊的距离。                                                                             |
| _颜色_       | 任选。阴影的颜色。参见[CSS颜色值](https://www.runoob.com/cssref/css-colors-legal.html "CSS 合法颜色值")。 |

- text-transform  文本转换属性
属性值

| 值          | 描述                              |
| ---------- | ------------------------------- |
| none       | 默认。定义带有小写字母和大写字母的标准的文本。         |
| capitalize | 文本中的每个单词以大写字母开头。                |
| uppercase  | 定义仅有大写字母。                       |
| lowercase  | 定义无大写字母，仅有小写字母。                 |
| inherit    | 规定应该从父元素继承 text-transform 属性的值。 |

- `text-decoration` 设置文字的装饰效果
`none`：默认值，不设置任何装饰效果。  
`underline`：设置文字`下方`显示下划线  
`overline`：设置文字`上方`显示划线  
`line-through`：设置文字`中间`显示删除线  
`blink`：设置文字闪烁

- `line-height`属性。
该`line-height`属性用于调整单个列表项内文本行之间的垂直间距。

虽然它主要影响每个项目内文本行之间的间距，但如果项目仅包含一行文本，它也可以间接影响列表项之间的整体间距。
![[行高.png]]
为了严格保证字在行里面居中，我们的工程师有一个约定： **行高、字号，一般都是偶数**。这样可以保证，它们的差一定偶数，就能够被2整除。
如果列表项有多行文本，`line-height`则会影响这些行之间的间距，但不会直接调整各个列表项之间的间距。
```html
<link rel="stylesheet" href="styles.css">

<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

```css
li {
  line-height: 2; 
}
```


## 列表样式
- list-style
 CSS 中，该`list-style`属性用于控制网页上列表的外观。
该`list-style`属性都允许列表项的显示方式。
该`list-style`房产实际上是另外三个房产的简称：

- `list-style-type`
- `list-style-position`
- `list-style-image`

它们各自在定义列表外观方面发挥着不同的作用。
该`list-style-type`属性允许您定义列表中使用的项目符号或数字类型。

对于无序列表，您可以从多种项目符号样式中进行选择，例如圆点、圆形或方形。

对于有序列表，您可以使用不同的编号系统，例如十进制、罗马数字，甚至字母字符。

以下是使用示例`list-style-type`：

```html
<ul style="list-style-type: square;">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

在这个例子中，无序列表的符号变成了方块。

该`list-style-type`属性是这三个属性中最常用的，因为它直接影响列表中项目符号或编号样式的外观。

该`list-style-position`属性控制项目符号或编号相对于列表项内容的位置。您可以使用两个值：`inside`和`outside`。

使用值时`outside`，项目符号或数字会出现在内容之外，这是默认行为。

而且，当您使用该值时`inside`，项目符号或编号会出现在内容内部，这可能会导致文本换行并与项目符号或编号对齐。

以下是使用示例`list-style-position`：

```html
<ul style="list-style-position: inside;">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
<ul style="list-style-position: outside;">
  <li>Item 4</li>
  <li>Item 5</li>
  <li>Item 6</li>
</ul>
```

在这个例子中，两个不同的无序列表标签都提供了值`inside`。`outside`

`list-style-position`当您想要控制列表内容的对齐方式时，该属性非常有用，尤其是在单个列表项中包含多行文本的情况下。

该`list-style-image`属性允许您使用图片作为列表项的要点标记。这有助于为您的列表添加独特的视觉风格。

以下是使用示例`list-style-image`：

```html
<head>
  <style>
    ul {
      list-style-image: url('https://cdn.freecodecamp.org/platform/universal/freecodecamp-org-gravatar.jpeg');
      list-style-position: inside;
    }
  </style>
</head>
<body>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
```

在这个例子中，项目符号被替换成了 freeCodeCamp 的自定义徽标，为列表增添了个性化的元素。

使用时`list-style-image`，请确保选择的图片尺寸合适，并与网页设计风格相协调。如果图片过大或过于复杂，可能会影响列表的阅读。

您可以将这三个属性—— `list-style-type`、、`list-style-position`和`list-style-image`——合并为一个`list-style`简写属性。

简写中各个值的顺序并不重要，但三个值可以同时指定。

以下是使用简写属性的示例：

```html
<ul style="list-style: square inside url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

在这个例子中，列表项使用方形项目符号，位于内容内部，项目符号为自定义图像。

但是，如果图像不可用或无法渲染，则会使用方形圆点作为备用。

## 表格样式
创建一个表格选择器以定位您的表格。将"border-collapse"属性设为"collapse"，这将使单元格边框合并为一个整体边框，而非每个单元格周围都有边框。同时，将"border"属性设为0以隐藏边框本身。

## 背景样式
CSS 背景属性用于定义HTML元素的背景。
CSS 属性定义背景效果:
- background-color
- background-image
- background-repeat
- background-attachment
- background-position


### 背景颜色 
background-color 属性定义了元素的背景颜色.
```css
body {background-color:#b0c4de;}
```
CSS中，颜色值通常以以下方式定义:

- 十六进制 - 如："#ff0000"
- RGB - 如："rgb(255,0,0)"
- 颜色名称 - 如："red"
```css
h1 {background-color:#6495ed;}
p {background-color:#e0ffff;}
div {background-color:#b0c4de;}
```
### 背景图片
background-image 属性描述了元素的背景图像.
默认情况下，背景图像进行平铺重复显示，以覆盖整个元素实体.
```html
<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
  }
</style>
```
### 背景图像大小
background-size  设置背景图像的大小
利用此功能`contain`将图像放大到尽可能大的尺寸，而不会裁剪或拉伸。
```css
/* 宽、高的具体数值 */
	background-size: 500px 500px;

	/* 宽高的百分比（相对于容器的大小） */
	background-size: 50% 50%;   // 如果两个属性值相同，可以简写成：background-size: 50%;

	background-size: 100% auto;  //这个属性可以自己试验一下。

	/* cover：图片始终填充满容器，且保证长宽比不变。图片如果有超出部分，则超出部分会被隐藏。 */
	background-size: cover;

	/* contain：将图片完整地显示在容器中，且保证长宽比不变。可能会导致容器的部分区域为空白。  */
	background-size: contain;
```
### 水平或垂直平铺
background-repeat  背景图像重复出现
默认情况下，背景图片会在水平和垂直方向上重复排列，以填充整个元素。
你可以使用该`background-repeat`属性，并将值设置为`no-repeat`。
```html
<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    background-size: contain;
    background-repeat: no-repeat;
    min-height: 100px;
  }
</style>
```

将`background-size`设置为`contain`并将`background-repeat`设置为 后`no-repeat`，图像将不再在屏幕上重复显示。
如果要水平重复背景图像，可以使用`repeat-x`该`background-repeat`属性的值。
```html
<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    background-size: contain;
    background-repeat: repeat-x;
    min-height: 100px;
  }
</style>
```
如果要垂直重复背景图像，可以使用`repeat-y`该`background-repeat`属性的值。
```html
<style>
  body {
    background-image: url("https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg");
    background-size: contain;
    background-repeat: repeat-y;
    min-height: 100px;
  }
</style>
```
### 背景图像定位
background-position  背景图像定位
**1、用像素值描述属性值：**
格式如下：

```
	background-position:向右偏移量 向下偏移量;
```

属性值可以是正数，也可以是负数。比如：`100px 200px`、`-50px -120px`。
**2、用单词描述属性值：**

格式如下：

```
	background-position: 描述左右的词 描述上下的词;
```

- 描述左右的词：left、center、right
- 描述上下的词：top 、center、bottom

### 背景原点
`background-origin` 属性：控制背景从什么地方开始显示。
```css
/* 从 padding-box 内边距开始显示背景图 */
	background-origin: padding-box;           //默认值

	/* 从 border-box 边框开始显示背景图  */
	background-origin: border-box;

	/* 从 content-box 内容区域开始显示背景图  */
	background-origin: content-box;
```
![[背景原点.png]]
### 背景固定
background-attachment  确定背景图像是随内容滚动还是在页面滚动时保持固定。
- `background-attachment:scroll;` 设置背景图片是否固定。属性值可以是：
    - `fixed`（背景就会被固定住，不会被滚动条滚走）。
    - `scroll`（与fixed属性相反，默认属性）

### 背景延伸
`background-clip`属性：设置元素的背景（背景图片或颜色）是否延伸到边框下面
`background-clip: content-box;` 超出的部分，将裁剪掉。属性值可以是：

- `border-box` 超出 border-box 的部分，将裁剪掉
    
- `padding-box` 超出 padding-box 的部分，将裁剪掉
    
- `content-box` 超出 content-box 的部分，将裁剪掉
### 背景渐变
CSS中的背景渐变是指两种或多种颜色之间的平滑过渡，可以应用于元素的背景。渐变效果使您无需使用图片即可创建美观的背景。

CSS 中有两种主要类型的渐变：线性渐变和径向渐变。
- **线性渐变**：这种渐变方式沿着直线创建颜色之间的渐变过渡。您可以控制这条线的方向和使用的颜色。 **`linear-gradient()`功能**：此 CSS 函数用于创建沿直线的多种颜色之间的过渡效果。
```css

    background-image: linear-gradient(方向, 起始颜色, 终止颜色);

    background-image: linear-gradient(to right, yellow, green);
```
>- 方向可以是：`to left`、`to right`、`to top`、`to bottom`、角度`30deg`（指的是顺时针方向30°）。

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 500px;
            height: 100px;
            margin: 10px auto;
            border: 1px solid #000;
        }

        /* 语法：
            linear-gradient(方向，起始颜色，终止颜色);
            方向：to left   to right  to top   to bottom 　角度　30deg
            起始颜色
            终止颜色
        */
        div:nth-child(1) {
            background-image: linear-gradient(to right, yellow, green);
        }

        /* 不写方向，表示默认的方向是：从上往下 */
        div:nth-child(2) {
            background-image: linear-gradient(yellow, green);
        }

        /* 方向可以指定角度 */
        div:nth-child(3) {
            width: 100px;
            height: 100px;
            background-image: linear-gradient(135deg, yellow, green);
        }

        /* 0%的位置开始出现黄色，40%的位置开始出现红色的过度。70%的位置开始出现绿色的过度，100%的位置开始出现蓝色 */
        div:nth-child(4) {
            background-image: linear-gradient(to right,
            yellow 0%,
            red 40%,
            green 70%,
            blue 100%);

        }

        /* 颜色之间，出现突变 */
        div:nth-child(5) {
            background-image: linear-gradient(45deg,
            yellow 0%,
            yellow 25%,
            blue 25%,
            blue 50%,
            red 50%,
            red 75%,
            green 75%,
            green 100%
            );
        }

        div:nth-child(6) {
            background-image: linear-gradient(to right,
            #000 0%,
            #000 25%,
            #fff 25%,
            #fff 50%,
            #000 50%,
            #000 75%,
            #fff 75%,
            #fff 100%
            );

        }

    </style>
</head>
<body>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>
<div></div>
</body>
</html>
```

![[渐变2.png]]
- **径向梯度**：这些梯度会形成从中心点向外辐射的圆形或椭圆形梯度。- **`radial-gradient()`功能**：此 CSS 函数创建一个从特定点（如圆形或椭圆形）辐射的图像，并在多种颜色之间逐渐过渡。
```css
background-image: radial-gradient(辐射的半径大小, 中心的位置, 起始颜色, 终止颜色);

	background-image: radial-gradient(100px at center,yellow ,green);
```
>解释：围绕中心点做渐变，半径是150px，从黄色到绿色做渐变。
>中心点的位置可以是：at left right center bottom top。如果以像素为单位，则中心点参照的是盒子的左上角

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 250px;
            height: 250px;
            border: 1px solid #000;
            margin: 20px;
            float: left;
        }

        /*
            径向渐变：
            radial-gradient（辐射的半径大小, 中心的位置，起始颜色，终止颜色）;
            中心点位置：at  left  right  center bottom  top
        */

        /*辐射半径为100px，中心点在中间*/
        div:nth-child(1) {
            background-image: radial-gradient(100px at center, yellow, green);
        }

        /*中心点在左上角*/
        div:nth-child(3) {
            background-image: radial-gradient(at left top, yellow, green);
        }

        div:nth-child(2) {
            background-image: radial-gradient(at 50px 50px, yellow, green);
        }

        /*设置不同的颜色渐变*/
        div:nth-child(4) {
            background-image: radial-gradient(100px at center,
            yellow 0%,
            green 30%,
            blue 60%,
            red 100%);
        }

        /*如果辐射半径的宽高不同，那就是椭圆*/
        div:nth-child(5) {
            background-image: radial-gradient(100px 50px at center, yellow, green);
        }

    </style>
</head>
<body>
<div class="box"></div>
<div class="box"></div>
<div class="box"></div>
<div class="box"></div>
<div class="box"></div>
</body>
</html>
```
![[渐变3.png]]


![[渐变.png]]
线性渐变是指颜色沿直线过渡。您可以定义渐变的方向和涉及的颜色。

以下是基本语法：

```css
background: linear-gradient(direction, color-stop1, color-stop2, ...);
```

在这个例子中，我们使用了`background`CSS 属性，其值为`linear gradient`。

方向指定渐变的方向。它可以是角度（例如`45deg`），关键字（例如`to right`）`to bottom`，或边/角。

`color-stop`指定渐变过渡发生的颜色和位置。

为了更好地理解线性梯度是如何工作的，让我们来看下面的例子：

```html
<link rel="stylesheet" href="styles.css">
<div class="linear-gradient"></div>
```

```css
.linear-gradient{
  background: linear-gradient(to right, red, yellow);
  height: 40vh;
}
```

```css
#legend-gradient {

  background-image: linear-gradient(

    var(--color0) 0% 16%,

    var(--color1) 16% 32%,

    var(--color2) 32% 48%,

    var(--color3) 48% 64%,

    var(--color4) 64% 80%,

    var(--color5) 80% 100%);

}
```

这段 CSS 代码创建了一个线性渐变，从 ` `red`<div>` 元素过渡`left`到`yellow``<span>``right`元素。该渐变应用于高度为`40%`视口高度的 `1/2` 的元素。你将`vh`在后续课程中学习更多关于单位的知识。

方向`to right`表示渐变是从左到右水平方向的。

另一种梯度类型是`radial`梯度。

径向渐变是指颜色从原点（通常是中心）向外呈圆形或椭圆形辐射过渡。

以下是基本语法：

```css
background: radial-gradient(shape size at position, color-stop1, color-stop2, ...)
```

在语法上，`shape`指定渐变的形状，可以是`circle`或`ellipse`。

该参数`size`决定了渐变末端形状的大小，可以是`closest-side`, `closest-corner`, `farthest-side`, `farthest-corner`, `contain`, 或`cover`。

`position`确定梯度中心的位置，可以使用关键字（例如，，，`center`）或精确值（例如，）来指定。`top left``bottom right``50% 50%``10px 20px`

最后，颜色停止点是渐变过渡所经过的颜色列表。每个颜色停止点都可以选择性地包含一个位置值（百分比或长度），用于指示颜色应该放置的位置。

例如：

```html
<link rel="stylesheet" href="styles.css">
<div class="radial-gradient"></div>
```

```css
.radial-gradient{
  background: radial-gradient(circle closest-side at center, red, yellow 50%, green);
  height: 60vh;
}
```

这段 CSS 代码创建了一个以元素为中心的圆形径向渐变。它从`red`中心开始，过渡到`yellow`半径`50%`的 ，最后结束`green`。

该`closest-side`关键字使渐变的末端形状与元素的最近边相匹配。渐变应用于高度为`60%`视口高度的元素。

了解如何使用 CSS 渐变可以显著增强您的设计，无需图像即可提供视觉上吸引人的背景。

它们提供了多种选项，例如用于平滑过渡的线性渐变和用于圆形效果的径向渐变，为网页设计提供了灵活性和创造性。
你可以通过用逗号(，)分隔多个渐变来为一个元素添加多个渐变，
```css
gradient1(
  colors
),
gradient2(
  colors
);
```


### 不透明度
不透明度描述了某物的不透明程度或非透明性。例如，实心墙是不透明的，没有光线可以穿透。但一个喝水用的玻璃杯则透明得多，你可以透过玻璃看到另一侧。
使用CSS`opacity`属性，你可以控制元素的半透明程度。当值为0或0%时，元素是完全透明的;当值为1.0或100%时，元素是完全不透明的，就像默认设置一样。
`background: transparent;` 可以单独设置透明度，但设置的是完全透明（不可调节透明度）。
### 裁剪
`clip-path`属性可以创建一个只有元素的部分区域可以显示的剪切区域。区域内的部分显示，区域外的隐藏。
```css
.div1 {
        width: 320px;
        height: 320px;
        border: 1px solid red;
        background: url(http://img.smyhvae.com/20191006_1410.png) no-repeat;
        background-size: cover;

        /* 裁剪出圆形区域 */
        clip-path: circle(50px at 100px 100px);
        transition: clip-path .4s;
    }
    .div1:hover{
        /* 鼠标悬停时，裁剪出更大的圆形 */
        clip-path: circle(80px at 100px 100px);
    }
```
### 综合属性
如果你想将几个属性合并到一行中，可以使用简写`background`属性来实现。
```css
background:red url(1.jpg) no-repeat 100px 100px fixed;
```

等价于：

```css
	background-color:red;
	background-image:url(1.jpg);
	background-repeat:no-repeat;
	background-position:100px 100px;
	background-attachment:fixed;
```
![[背景综合.png]]
### 设置多个背景
```css
/* 给盒子加多个背景，按照背景语法格式书写，多个背景使用逗号隔开 */
            background: url(images/bg1.png) no-repeat left top,
            url(images/bg2.png) no-repeat right top,
            url(images/bg3.png) no-repeat right bottom,
            url(images/bg4.png) no-repeat left bottom,
            url(images/bg5.png) no-repeat center;
```
## 布局
### overflow 溢出
overflow溢出是指元素处理超出其自身大小的内容的方式。例如，`div`元素的文本内容可能会溢出其边界。

溢出是二维的，x 轴决定水平溢出，y 轴决定垂直溢出。
- `overflow-x` 轴决定水平溢出范围。
- `overflow-y` 轴决定垂直溢出量。
CSS overflow 属性可以控制内容溢出元素框时在对应的元素区间内添加滚动条。

overflow属性有以下值：

| 值       | 描述                           |
| ------- | ---------------------------- |
| visible | 默认值。内容不会被修剪，会呈现在元素框之外。       |
| hidden  | 内容会被修剪，并且其余内容是不可见的。          |
| scroll  | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。 |
| auto    | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。 |
| inherit | 规定应该从父元素继承 overflow 属性的值。    |
|         |                              |
**注意:**overflow 属性只工作于指定高度的块元素上


###  使用浮动

- **定义**：浮动用于将元素从其在页面上的正常流中移除，并将其定位到容器的左侧或右侧。发生这种情况时，文本会环绕浮动内容。
- ```css
float: left;
float: right;
```
- **清除浮动**：此`clear`属性用于确定元素是否需要移动到浮动内容下方。当多个浮动元素并排堆叠时，布局中可能会出现重叠和折叠问题。因此，`clearfix`我们创建了一个变通方法来解决这个问题。
```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```
### 定位
####  静态定位、相对定位和绝对定位
position：`static`, `absolute`, `relative`, `sticky` or `fixed`
CSS定位允许你设置元素在浏览器中的位置。它有一个position属性，你可以将其设为static、absolute、relative、sticky或fixed。
一旦你设置了元素的position属性，就可以通过设置一个像素或百分比值来移动该元素，这些值可以针对top、right、left或bottom属性中的一个或多个进行调整。
static是所有元素的默认定位方式。如果你将它分配给一个元素，你将无法通过 top、right、left 或 bottom 属性来移动该元素。

- **静态定位**：这是文档的正常布局流程。元素从上到下、从左到右依次排列。
- **相对定位**：您可以使用`top``--location` `left`、`--location``right`和`bottom``--location` 属性在正常的文档流中定位元素。您还可以使用相对定位使元素与其他页面上的元素重叠。
- **绝对定位**：这允许您将一个元素从正常的文档流中取出，使其独立于其他元素运行。

####  固定和粘性定位

- **固定定位**：当元素使用 `position: fixed` 定位时`position: fixed`，它会脱离正常的文档流，并相对于视口进行定位，这意味着即使用户滚动页面，它的位置也保持不变。这通常用于需要始终保持可见的元素，例如标题或导航栏。
- ```css
.navbar {
  position: fixed; 
  top: 0; 
  width: 100%; 
}
```
- **粘性定位**：这种定位方式会使元素在页面向下滚动时表现得像相对定位元素一样。如果指定了 `--sticky` `top`、`left``--fixed``right`或`bottom``--fixed` 属性，则元素将不再表现得像相对定位元素，而是表现得像固定定位元素一样。
```css
.positioned {
  position: sticky;
  top: 30px;
  left: 30px;
}
```
####  `z-index`与房产打交道

- **定义**：`z-index`CSS 中的该属性用于控制页面上重叠的定位元素的垂直堆叠顺序。




## 盒子模型

在 CSS 盒模型中，每个元素都被一个盒子包裹。这个盒子由四个部分组成：内容区域、边框`padding`、内边距、边框`border`。`margin`

![[盒子模型.png]]
盒模型允许我们在其它元素和周围元素边框之间的空间放置元素。
- **Margin(外边距)** - 边距是指元素边框之外的空间。它决定了元素与其周围其他元素之间的距离。
- **Border(边框)** - 在 CSS 盒模型中，边框是指元素的外部边缘或轮廓，它是元素的视觉边界。
- **Padding(内边距)** - 内边距是指内容区域之后紧邻的区域，也就是内容区域与元素边框之间的空间，内边距是透明的。
- **Content(内容)** - 内容区域是框的最内层部分。它是包含元素实际内容（例如文本或图像）的空间。

### 边距

- **`margin`属性**：此属性用于在元素外部、元素边框与周围元素之间添加空间。
- **`margin`简写**： 这四个不同的`margin`属性分别是`margin-top`，`margin-right`和。`margin-bottom``margin-left`
在简写中使用单个值时`margin`，该确切值将应用于目标元素的四个边。

以下是使用单个值进行速记的示例`margin`：

```html
<link rel="stylesheet" href="styles.css">

<span>Paragraph one</span>
<p>Paragraph two</p>
<span>Paragraph three</span>
```

```css
p {
  margin: 10px;
}
```

此代码示例将平等`10px`地`margin`应用于段落元素的四个边。

当使用两个值时，第一个值适用于元素的`top`上下边缘`bottom`，而第二个值适用于元素的`left`左右边缘。`right`

以下是使用两个值进行简写的示例`margin`：

```html
<link rel="stylesheet" href="styles.css">

<span>Paragraph one</span>
<p>Paragraph two</p>
<span>Paragraph three</span>
```

```css
p {
  margin: 10px 20px;
}
```

这会将`top`段落元素`bottom`的边距设置为0.05 和`10px`0.05，并将段落元素的边距`20px`设置为 0.05 和 0.05 。`left``right`

如果提供了三个值，则第一个值适用于边距`top`，第二个值适用于边框`left`边距`right`，第三个值适用于边框`bottom`边距。

以下示例有助于更好地理解：

```html
<link rel="stylesheet" href="styles.css">

<span>Paragraph one</span>
<p>Paragraph two</p>
<span>Paragraph three</span>
```

```css
p {
  margin: 10px 20px 30px;
}
```

这样`10px`就为`top`、`20px`和`left`以及`right`设定了边距`30px`。`bottom`

使用四个值时，您可以更好地控制，因为您可以独立地为目标元素的每一边指定边距值。

第一个值针对的是`top`，第二个值针对的是`right`，第三个值针对的是`bottom`，第四个值针对的是`left`。

以下是使用四个值的边距简写形式的示例：

```html
<link rel="stylesheet" href="styles.css">

<span>Paragraph one</span>
<p>Paragraph two</p>
<span>Paragraph three</span>
```

```css
p {
  margin: 10px 20px 30px 40px;
}
```

可以通过将它的margin-left和margin-right属性设置为auto来实现。可以将margin想象为一个元素周围的无形空间。使用这两个margin属性，将#menu元素在body元素内居中。


- **`padding`属性**：此属性用于在元素内部，即内容与其边框之间添加空间。
- **`padding`简写**：这四个`padding`属性分别是`padding-top`，，`padding-right`和。`padding-bottom``padding-left`
`padding`以下是如何为段落元素设置样式的示例：

```html
<link rel="stylesheet" href="styles.css">

<span>Paragraph one</span>
<p>Paragraph two</p>
<span>Paragraph three</span>
```

```css
p {
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 30px;
  padding-left: 40px;
  border: 2px solid black;
}
```

这会将边距设置为，`10px`对于，对于，对于，以及对于。`top``20px``right``30px``bottom``40px``left`

如您所见，该属性`padding`应用于边框内的内容，而`margin`该属性应用于边框外的内容。

就像`margin`房产名称一样，您也可以选择使用`padding`房产名称的缩写。

您也可以在简写属性中指定一个、两个、三个或四个值`padding`。

`padding`以下是使用前面提到的段落元素简写形式的示例：

```html
<link rel="stylesheet" href="styles.css">

<span>Paragraph one</span>
<p>Paragraph two</p>
<span>Paragraph three</span>
```

```css
p {
  padding: 10px 20px 30px 40px;
  border: 2px solid black;
}
```

在这个例子中，使用简写代码会将段落元素的内边距设置为`10px`，`top`将`20px`段落元素的内边距设置为，将段落元素的内边距设置为`right`，`30px`将段落元素的内边距设置为`bottom`，将段落元素的`40px`内边距设置为`left`。


### 边框
给图像添加边框最直接的方法是使用边框`border`属性。该属性是一种简写方式，可以一次性设置边框的宽度、样式和颜色。
```html
<link rel="stylesheet" href="styles.css">

<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute cat lying on its back.">
```

```css
img {
  border: 2px solid red;
}
```
您可以根据设计需要`img`调整边框的宽度、样式（例如`dashed`、dotted）和double

如果需要对边框的各个边进行更精细的控制，可以使用每个边的特定边框属性：
```css
border-left: width style color;
```

```html
<link rel="stylesheet" href="styles.css">

<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute cat lying on its back.">
```

```css
img {
  border-top: 10px solid red;
  border-right: 10px dashed green;
  border-bottom: 10px dotted blue;
  border-left: 10px double purple;
  border-left-width: 10px;
  border-left-style: solid;
  border-left-color: black;
}
```

这样，您就可以为图像的每一边创建独特的边框样式。

创建边框效果的另一种方法是使用 ` `outline`outline` 属性。虽然与边框类似，但轮廓不会影响元素的尺寸或布局：

```html
<link rel="stylesheet" href="styles.css">

<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute cate lying on its back.">
```

```css
img {
  outline: 3px solid gold;
}
```

如果要创建圆角边框，可以`border-radius`结合使用 border 属性：

```html
<link rel="stylesheet" href="styles.css">

<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute cate lying on its back.">
```

```css
img {
  border: 2px solid black;
  border-radius: 10px;
}
```

border-style 属性用于指定要显示的边框类型。
允许的值如下：

- dotted：定义点状边框。
- dashed：定义虚线边框。
- solid：定义实线边框。
- double：定义双线边框。
- groove：定义三维沟槽边框。效果取决于 border-color 的值。
- ridge：定义三维脊状边框。效果取决于 border-color 的值。
- inset：定义三维嵌入边框。效果取决于 border-color 的值。
- outset：定义三维突出边框。效果取决于 border-color 的值。
- none：定义无边框。
- hidden：定义隐藏边框。
```html
<p class="none">无边框。</p>
<p class="dotted">虚线边框。</p>
<p class="dashed">虚线边框。</p>
<p class="solid">实线边框。</p>
<p class="double">双边框。</p>
<p class="groove"> 凹槽边框。</p>
<p class="ridge">垄状边框。</p>
<p class="inset">嵌入边框。</p>
<p class="outset">外凸边框。</p>
<p class="hidden">隐藏边框。</p>
<p class="mix">混合边框</p>
```
```css
p.none {border-style:none;}
p.dotted {border-style:dotted;}
p.dashed {border-style:dashed;}
p.solid {border-style:solid;}
p.double {border-style:double;}
p.groove {border-style:groove;}
p.ridge {border-style:ridge;}
p.inset {border-style:inset;}
p.outset {border-style:outset;}
p.hidden {border-style:hidden;}
p.mix {border-style: dotted dashed solid double;}
```
![[边框样式.png]]
### 阴影
box-shadow 阴影
```css
box-shadow: offsetX offsetY blurRadius spreadRadius color;
```

| 值          | 说明                           |
| :--------- | :--------------------------- |
| _h-shadow_ | 仅需的允许。水平遮蔽的位置。负值             |
| _v-shadow_ | 仅需的允许。垂直遮挡的位置。负值             |
| _模糊_       | 任选。模糊距离                      |
| _传播_       | 任选。 亮度的大小                    |
| _颜色_       | 任选。阴影的颜色。在CSS 颜色值中查找颜色值的完整列表 |
| 插入         | 任选。从外层的遮光（开始时）改变内层的遮光        |
### 边距折叠
**定义**：当相邻元素的垂直边距重叠时，就会出现这种行为，最终合并成一个边距，其值等于两者中较大的那个。这种行为仅适​​用于垂直边距（上边距和下边距），不适用于水平边距（左边距和右边距）可以使用overflow:hidden 来解决

### 盒子大小
- **`box-sizing`属性**：此属性用于确定如何计算 HTML 元素的最终`width`值。`height`
- **`content-box`值**：在`content-box`模型中，您为元素设置的`width`和`height`决定了内容区域的尺寸，但它们不包括`padding`、`border`或`margin`。
- **`border-box`值**：对于元素`border-box`，其`width`和包括内容区域、和，但不包括。`height``padding``border``margin`

## 弹性盒子

 **定义**：CSS flexbox 是一种一维布局模型，允许您在容器内按行和列排列元素。
 **弹性模型**：该模型定义了弹性元素在弹性容器内的排列方式。每个弹性容器都有两个轴：主轴和交叉轴。
弹性容器是一种具有弹性布局的 HTML 元素。您可以在弹性容器内以各种方式排列和对齐元素。要将 HTML 元素设置为弹性容器，您需要`display: flex`在其 CSS 样式中添加相应的属性。
弹性元素是弹性容器的直接子元素。这些元素可以根据弹性容器的属性在容器内进行排列和对齐。它们还可以缩小或放大以适应可用空间。
![[flexbox1.png]]
![[flexbox2.png]]



![[flex-grow.png]]

![[flex-shrink.png]]


### 弹性盒子
弹性属性。这些属性决定了弹性项目在弹性容器内的排列、调整大小和分布方式。
#### flex-direction
* `flex-direction`属性--属性设置主轴方向
![[flex-direction.png]]
语法
flex - direction ：row|row-reverse|column|column-reverse​​

`flex-direction`的值有：

- row：横向从左右到排列（左对齐），默认的排列方式。
- row-reverse：产品横向排列（右对齐，从后往前排，最后一个排在最前面。
- column：纵向排列。
- column-reverse：食品纵向排列，从后往前排，最后一个排在最上面。

#### justify-content 属性
![[justify-content.png]]
内容坐标（justify-content）属性应用在弹性容器上，把弹性项沿着弹性容器的主轴线（主轴）对齐。

justify-content 语法如下：

justify - content : flex - start | flex - end | center | space - between | space - around | space-evenly

各个值解析：

- flex - start：**  
    
    弹性项目向行头紧挨着填充。这是默认值。第一个弹性项的主起始外边距边线被放置在该行的主起始边线上，而后续弹性项依次平齐支架。
    
- **柔性端：**  
    
    弹性项目向行尾紧挨着填充。第一个弹性项的主端外边距边线被放置在该行的主端边线上，而后续弹性项依次平齐货架。
    
- **中心：**  
    
    弹性项目居中紧挨着填充。（如果剩余的自由空间是负的，则弹性项目将在两个方向上同时溢出）。
    
- **间距：**  
    
    弹性项目平均分配在该行上。如果剩余空间为负或者只有一个弹性项，则该值接着于flex-start。否则，第1个弹性项的外边距和行的主起始边线对齐，而最后1个弹性项的外边距和行的主端边线对齐，然后剩余的弹性项分配在该行上，项目相邻的间隔对齐。
    
- **周围空间：**  
    弹性项目沿主轴均匀分布，并在第一个项目之前和最后一个项目之后添加间距。此额外间距为相邻项目之间间距的一半。如果只有一个项目需要分布，则该项目将居中放置。
* space-evenly 它将元素沿主轴均匀分布。元素之间的间距与第一个和最后一个元素前后的间距完全相同
#### align-items对齐项目属性
`align-items`设置或搜索弹性盒子元素在侧轴（纵轴）方向上的视觉方式。

![[align-items.png]]


语法
对齐方式：flex - start | flex - end | center | baseline | stretch​ 

各个值解析：

- flex-start：弹性盒子元件的侧轴（纵轴）初始位置的边界紧靠住该行的侧轴初始边界。
- flex-end：弹性盒子元件的侧轴（纵轴）起始位置的边界紧靠住该行的侧轴结束边界。
- 中心：弹性盒子元素在该行的侧轴（纵轴）上居中放置。（如果该行的尺寸小于弹性盒子元素的尺寸，底座向两个方向重叠相同的长度）。
- 基线：如弹性盒子元素的行内轴与侧轴为同一条，则该值与'flex-start'对应。其他情况下，该值将参与基线坐标。
- stretch：如果指定侧轴大小的属性为'auto'，则其值使得项目的边距盒的尺寸解答接近行的尺寸，但同时会遵照'min/max-width/height'属性的限制。

#### flex-wrap 属性
![[flex-wrap.png]]
**flex-wrap**属性弹性项目在弹性容器内的换行方式，以适应可用空间。。

语法

flex - wrap ：nowrap | wrap | wrap - reverse | initial | inherit ；

各个值解析：

- **nowrap** - 默认，弹性容器为单行。该情况下弹性子项可能会溢出容器。
- wrap 该情况下弹性子项溢出的部分会被放置到新行，子项内部会发生断**行**
- **wrap-reverse** - 反转排列。

#### `align-content` 对齐内容属性
![[align=content.png]]
`align-content`属性用于修改 `flex-wrap`属性的行为。类似`align-items`，但它不是设置弹性子元素的排列，而是设置各个行的排列。

语法

对齐内容：flex - start | flex - end | center | space - between | space - around | stretch​ 

各个值解析：

- `stretch`- 默认情况下。各行将竭尽全力占用剩余的空间。
- `flex-start`- 各行向弹性盒容器的初始位置。
- `flex-end`- 各行向弹性盒容器的结束位置具有。
- `center`-各行向弹性盒容器的中间位置具有。
- `space-between`-各行在弹性盒容器中平均分配。
- `space-around`- 各行在弹性盒子容器中平均分配，末端保留子元素与子元素之间大小的一半。
### 弹性元素
#### order
![[order.png]]
- `<integer>`：用整数值来定义顺序，数值小的列在前面。可以为负值。

#### align-self
![[align-self.png]]
`align-self`属性用于设置弹性元素本身在侧轴（纵轴）方向上的扫描方式。

语法

align - self : auto | flex - start | flex - end | center | baseline | stretch   

各个值解析：

- auto：如果'align-self'的值为'auto'，则其计算值为'align-items'元素的父元素，如果其没有父元素，则其计算值为'stretch'。
- flex-start：弹性盒子元件的侧轴（纵轴）初始位置的边界紧靠住该行的侧轴初始边界。
- flex-end：弹性盒子元件的侧轴（纵轴）起始位置的边界紧靠住该行的侧轴结束边界。
- 中心：弹性盒子元素在该行的侧轴（纵轴）上居中放置。（如果该行的尺寸小于弹性盒子元素的尺寸，底座向两个方向重叠相同的长度）。
- 基线：如弹性盒子元素的行内轴与侧轴为同一条，则该值与'flex-start'对应。其他情况下，该值将参与基线坐标。
- stretch：如果指定侧轴大小的属性为'auto'，则其值使得项目的边距盒的尺寸解答接近行的尺寸，但同时会遵照'min/max-width/height'属性的限制。
#### flex
`flex`属性用于指定弹性子元素如何分配空间。

 语法

flex : auto | initial | none | inherit | [ flex - grow ] || [ flex - shrink ] || [ flex - basis ]        

各个值解析：

- auto: 计算值 1 1 auto
- 初始值： 计算值 0 1 自动
- 无：计算值为 0 0 auto
- 继承：从父元素继承
- [ flex-grow ]：定义弹性盒子元素的扩展。
- [ flex-shrink ]：定义弹性盒子元素的缩小范围。
- [ flex-basis ]：定义弹性盒子元素的默认基准值。

gap: npx  间隙  
row-gap
column-gap
## CSS网格

- **定义**：CSS Grid 是一种二维布局系统，用于在网页中创建复杂的布局。网格由行和列组成，行和列之间留有间隙。要定义网格布局，您需要将属性设置`display`为`grid`。

```css
.container {
  display: grid;
}
```

- **`fr`（分数）单位：**此单位表示网格容器内空间的一部分。您可以使用此`fr`单位创建灵活的网格。**
```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 20px;
}
```
在这段代码中，我们告诉浏览器创建一个具有三个等宽列的网格，这就是它的含义`1fr 1fr 1fr`，并且我们在每个网格项之间添加了 20 像素的间隙。
- **在 CSS 网格中创建轨道间隙**：有三种方法可以在轨道之间创建间隙。您可以使用 ` `column-gap 属性在列之间创建间隙。您可以使用 ` `row-gap 属性在行之间创建间隙。或者，您可以使用`gap`简写属性在行和列之间创建间隙。
- **`repeat()`功能**：此函数用于重复播放曲目列表中的某些部分。`grid-template-columns: 1fr 1fr 1fr;`您可以使用此`repeat()`函数代替直接编写代码。

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 20px 1fr);
  column-gap: 10px;
}
```

- **显式网格**`grid-template-columns`：您可以使用or属性指定线数或轨道数`grid-template-rows`。
- **`grid-template-columns`**：用于设置网格轨道列的线条名称和大小。

```css
.container {
  display: grid;
  width: 100%;
  grid-template-columns: 30px 1fr;
}
```

- **`grid-template-rows`**：用于设置网格轨道行的线条名称和大小。
- **隐式网格**：当项目放置在网格之外时，会自动为这些外部元素创建行和列。控制浏览器隐式创建的列和行的属性是`grid-auto-columns`和`grid-auto-rows`。
- **`grid-auto-flow`**：这决定了自动放置的项目如何在网格中排列。

```css
.container {
  display: grid;
  width: 100%;
  grid-auto-flow: column;
}
```

- **`grid-auto-columns`**：用于设置隐式创建的列的大小。

```css
.container {
  display: grid;
  width: 100%;
  grid-auto-columns: auto;
}
```

- **`minmax()`功能**：此功能用于设置轨道的最小和最大尺寸。指定一行或一列可以占据多少空间。
以下是该函数的语法`minmax()`：

```css
minmax(min, max)
```

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(150px, auto);
}
```
 该`min`值确保网格轨道永远不会缩小到设定的尺寸以下。
 该`max`值限制了网格轨道可以增长的最大尺寸。
 
- **基于线条的放置**：所有网格都包含线条。要指定项目在线条上的起始位置，可以使用 `grid-column-start`和 ` `grid-row-start 属性。要指定项目在线条上的结束位置，可以使用 `grid-column-end`和 ` `grid-row-end属性。您也可以选择使用 `grid-column`或 ` `grid-row` 简写属性。
以下是该属性的语法`grid-row`：

```css
grid-row: <start-line> / <end-line>;
```
```css
grid-column: <start-line> / <end-line>;
```
`<start-line>`是项目起始的网格线，`<end-line>`是项目结束的网格线。两者都从 1 开始计数，也就是说，计数是从 1 开始，而不是从 0 开始。
```
.item1 {
  grid-column: 1 / 3;
}

```
可以使用`span`关键字来指定网格项要跨越的行和列
例如，1 / 3`相同`1 / span 2`
```css
.item1 {
  grid-column: 1 / span 2;
  grid-row: 1 / span 2;
}
```
请记住，grid-column属性决定了元素起始和结束的列位置。有时你可能会不确定网格究竟会有多少列，但希望某个元素能止于最后一列。为实现这一目标，你可以在结束列处使用-1。

- **`grid-template-areas`**该属性用于为要在网格上放置的项目提供名称。使用 grid-area 属性将标签分配给特定的网格项。换句话说，这些命名标签也称为“网格区域名称”。**
```css
grid-template-areas:
 'header header header'
 'left-sidebar main right-sidebar'
 'footer footer footer';
```
以下是掌握基本语法需要记住的几点：

- `header`诸如和 之类的值`main`是网格区域的名称。
    
- 字符串中每个以空格分隔的值都对应一列。
    
- 每个字符串代表网格中的一行。

```html
<div class="container">
  <div class="header">Header</div>
  <div class="sidebar">Sidebar</div>
  <div class="main">Main Content</div>
  <div class="footer">Footer</div>
</div>

```

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr; 
  grid-template-rows: auto 1fr auto; 
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer"; 
  gap: 20px; 
}

.header {
  grid-area: header; 
  background-color: #4CAF50;
  padding: 10px;
  color: white;
}

.sidebar {
  grid-area: sidebar;
  background-color: #f4f4f4;
  padding: 10px;
}

.main {
  grid-area: main; 
  background-color: #e0e0e0;
  padding: 10px;
}

.footer {
  grid-area: footer; 
  background-color: #4CAF50;
  padding: 10px;
  color: white;
}
```
- **`place-items`**：用于对齐块级和行内方向的元素。可用于同时设置 align-items和justify-items值。位置项属性接受一个或两个值。如果仅提供其中一个值，则该值将被用于both align-items和justify-items属性;如果提供两个值，则第一个值用于align-items属性，第二个值用于justify-items属性。
- **`align-items`**：用于设置网格容器中项目的对齐方式。
与Flexbox非常相似，借助CSS网格,您可以将网格项的内容进行对齐，具体可通过align-items和justify-items 属性实现。 align-items 会沿列轴对齐子元素，而justify-items会沿行轴对齐子元素。
您的.text元素不是CSS网格，但您可以通过使用column-width属性在不使用Grid的情况下创建元素内的列。

## 响应式网页设计

- **定义**：响应式设计的核心原则是适应性——网站能够根据浏览设备的屏幕尺寸和功能调整其布局和内容。
- **流式网格**：这种网格使用百分比等相对单位，而不是像素等固定单位，允许内容根据屏幕尺寸调整大小和重新排列。
- **弹性图像**：这些图像会根据其包含元素的大小自动调整大小，确保它们在较小的屏幕上不会超出容器范围。



## 媒体查询
CSS 中媒体查询的基本语法如下所示：

```css
@media mediatype and (feature: value) {
  /* CSS rules go here */
}
```
在此结构中，mediatype 指定查询适用的媒体类型，而 feature: value 对定义应用样式必须满足的条件。
- **定义**：这允许开发者根据设备的特性（主要是视口宽度）应用不同的样式。
- **`all`媒体类型**：适用于所有设备。如果未指定媒体类型，则使用此默认值。
- **`print`媒体类型**：这适用于在打印预览模式下在屏幕上查看的分页材料和文档。
- **`screen`媒体类型**：主要用于屏幕。
```css
@media screen and (min-width: 768px) {
  /* Styles for screens at least 768px wide */
}
```
- **`aspect-ratio`**这描述了视口的宽度和高度之间的比例。
- ```css
@media screen and (aspect-ratio: 16/9) {
  /* Styles for screens with a 16:9 aspect ratio */
}
```
- **`orientation`**这用于指示设备是横向还是纵向显示。
- ```css
@media screen and (orientation: landscape) {
  /* Styles for landscape orientation */
}
```
- **`resolution`**这用于描述输出设备的分辨率，单位为每英寸点数 (dpi) 或每厘米点数 (dpcm)。
- ```css
@media screen and (min-resolution: 300dpi) {
  /* Styles for high-resolution screens */
}
```
- **`hover`**这是用来测试主要输入机制是否可以悬停在元素上。
- ```css
@media (hover: hover) {
  /* Styles for devices that support hover */
}
```
- **`prefers-color-scheme`**：用于检测用户是否请求了浅色或深色主题。
```css
@media (prefers-color-scheme: dark) {
  /* Styles for dark mode */
}
```
媒体查询还可以使用逻辑运算符组合多个条件。`and`运算符用于组合多个媒体特征，而`not``and``only`运算符可用于否定或隔离媒体查询。以下是一个组合多个特征的示例：

```css
@media screen and (min-width: 768px) and (orientation: landscape) {
  /* Styles for landscape screens at least 768px wide */
}
```

也可以用逗号分隔的列表来指定多个查询，其作用类似于“或”运算符：

```css
@media screen and (min-width: 768px), print {
  /* Styles for screens at least 768px wide OR for print */
}
```
### 通用媒体断点

- **定义**：媒体断点是指网站设计中布局和内容会根据不同屏幕尺寸进行调整的特定点。有一些通用的断点可用于针对手机、平板电脑和台式电脑屏幕进行优化。但试图涵盖所有可能的设备屏幕尺寸是不明智的。
- **小型设备（智能手机）**：最大 640 像素
- **中等尺寸设备（平板电脑）**：641像素至1024像素
- **大型设备（台式机）**：1025像素及以上

### 移动优先方法

- **定义**：该`mobile-first`方法是一种响应式网页设计的设计理念和开发策略，优先考虑为移动设备创建网站，然后再为更大的屏幕进行设计。
## 过渡
transition
```css
a {
  transition: color 1s linear;
}
```
transition属性接受的值按顺序依次为:应用于该过渡的属性、过渡持续时间，以及定时器。
如果存在多个具有过渡的属性，你可以将每个属性的值用逗号分隔地写出来
```css
p {
  transition: property1 0.1s, property2 0.6s linear;
}
```

## 转换
它允许您在不影响其他元素布局的情况下修改网页上元素的视觉呈现方式。它使您能够对元素应用各种变换，例如在二维或三维空间中旋转、缩放、倾斜或平移（移动）它们。

该`transform`属性通过对元素的坐标系应用数学变换来实现。这意味着您可以在保持元素原始位置和文档流不变的情况下，调整其形状和位置。

Example Code

```css
p {
  transform: scale(0.9);
}
```
transform 属性还可以使用另一个值 skewX，该函数会将元素水平方向进行倾斜
```css
div {
  transform: skewX(7deg);
}
```

2D转换方法

| 函数                              | 描述                       |
| ------------------------------- | ------------------------ |
| matrix(_n_,_n_,_n_,_n_,_n_,_n_) | 定义 2D 转换，使用六个值的矩阵。       |
| translate(_x_,_y_)              | 定义 2D 转换，沿着 X 和 Y 轴移动元素。 |
| translateX(_n_)                 | 定义 2D 转换，沿着 X 轴移动元素。     |
| translateY(_n_)                 | 定义 2D 转换，沿着 Y 轴移动元素。     |
| scale(_x_,_y_)                  | 定义 2D 缩放转换，改变元素的宽度和高度。   |
| scaleX(_n_)                     | 定义 2D 缩放转换，改变元素的宽度。      |
| scaleY(_n_)                     | 定义 2D 缩放转换，改变元素的高度。      |
| rotate(_angle_)                 | 定义 2D 旋转，在参数中规定角度。       |
| skew(_x-angle_,_y-angle_)       | 定义 2D 倾斜转换，沿着 X 和 Y 轴。   |
| skewX(_angle_)                  | 定义 2D 倾斜转换，沿着 X 轴。       |
| skewY(_angle_)                  | 定义 2D 倾斜转换，沿着 Y 轴。       |
3D 转换方法

| 函数                                                                              | 描述                         |
| ------------------------------------------------------------------------------- | -------------------------- |
| matrix3d(_n_,_n_,_n_,_n_,_n_,_n_,  <br>_n_,_n_,_n_,_n_,_n_,_n_,_n_,_n_,_n_,_n_) | 定义 3D 转换，使用 16 个值的 4x4 矩阵。 |
| translate3d(_x_,_y_,_z_)                                                        | 定义 3D 转化。                  |
| translateX(_x_)                                                                 | 定义 3D 转化，仅使用用于 X 轴的值。      |
| translateY(_y_)                                                                 | 定义 3D 转化，仅使用用于 Y 轴的值。      |
| translateZ(_z_)                                                                 | 定义 3D 转化，仅使用用于 Z 轴的值。      |
| scale3d(_x_,_y_,_z_)                                                            | 定义 3D 缩放转换。                |
| scaleX(_x_)                                                                     | 定义 3D 缩放转换，通过给定一个 X 轴的值。   |
| scaleY(_y_)                                                                     | 定义 3D 缩放转换，通过给定一个 Y 轴的值。   |
| scaleZ(_z_)                                                                     | 定义 3D 缩放转换，通过给定一个 Z 轴的值。   |
| rotate3d(_x_,_y_,_z_,_angle_)                                                   | 定义 3D 旋转。                  |
| rotateX(_angle_)                                                                | 定义沿 X 轴的 3D 旋转。            |
| rotateY(_angle_)                                                                | 定义沿 Y 轴的 3D 旋转。            |
| rotateZ(_angle_)                                                                | 定义沿 Z 轴的 3D 旋转。            |
| perspective(_n_)                                                                | 定义 3D 转换元素的透视视图。           |
transform-origin
变换原点属性用于指定CSS变换操作所作用的基点。例如，当你应用旋转变换(如本项目中稍后将要进行的操作)时，变换原点就决定了元素将围绕哪个点进行旋转。


## CSS动画

- **定义**：CSS动画允许您在网页上创建动态、引人入胜的视觉效果，而无需使用JavaScript或复杂的编程。它们提供了一种在指定时间内平滑过渡不同样式元素的方法。
- **规则：此`@keyframes`规则**定义了动画的各个阶段和样式。它指定了元素在动画过程中各个阶段应具有的样式。
- **`animation`属性**：这是用于应用动画的简写属性。
- **`animation-name`**：这指定要使用的规则名称`@keyframes`。
- **`animation-duration`**：这设置动画完成所需的时间。
- **`animation-timing-function`**：这定义了动画如何随时间推移而进行（例如缓动、线性、缓入缓出）。
- **`animation-delay`**：这指定动画开始前的延迟时间。
- **`animation-iteration-count`**：此设置动画应重复播放的次数。
- **`animation-direction`**：这决定了动画应该正向播放、反向播放还是交替播放。
- **`animation-fill-mode`**：这指定了元素在动画之前和之后的样式应该如何设置。
- **`animation-play-state`**这样就可以暂停和恢复动画。

## CSS 滤镜

- **定义**：此属性可用于创建各种效果，例如模糊、颜色偏移和对比度调整。
该`filter`属性可用于创建各种效果，例如模糊、颜色偏移和对比度调整。`filter`属性的基本语法非常简单：
```css
selector {
  filter: function(amount);
}
```
- **`blur()`功能**：此函数对元素应用高斯模糊。模糊程度以像素为单位，表示模糊半径。
- **`brightness()`功能**：此函数用于调整元素的亮度。值为 0% 时，元素将完全变黑；值大于 100% 时，亮度将增加。
- **`grayscale()`功能**：此函数将元素转换为灰度图像。转换程度以百分比表示，100% 表示完全灰度，0% 表示图像保持不变。
- **`sepia()`功能**：此函数将元素应用棕褐色调。与灰度模式类似，它使用百分比值。
- **`hue-rotate()`功能**：此函数对元素应用色调旋转。该值以度为单位，表示围绕色环的旋转角度。
## 常见问题样式`datetime-local`和`color`属性

- **常见问题**：这些特殊类型的输入框依赖于复杂的伪元素来创建日期和颜色选择器等元素。这给这些输入框的样式设计带来了很大的挑战。其中一个挑战是，默认样式完全取决于浏览器，因此您编写的 CSS 代码在不同的浏览器上可能完全不同，即使您编写的代码能够使选择器呈现出您想要的效果。




## CSS重置

- **定义**：CSS 重置样式表会移除网页浏览器应用于 HTML 元素的全部或部分默认格式。第三方 CSS 重置选项包括`sanitize.css`和`normalize.css`。

用于`appearance: none`输入
- **`appearance: none`**浏览器会对很多元素应用默认样式。CSS`appearance: none`属性可以让你完全控制样式，但也有一些注意事项。为输入元素创建自定义样式时，你需要确保焦点和错误指示器仍然可见。



## 其他
### 鼠标的属性
鼠标的属性`cursor`有以下几个属性值：
- `auto`：默认值。浏览器根据当前情况自动确定鼠标光标类型。
- `pointer`：IE6.0，竖起一只手指的手形光标。就像通常用户将光标移到超链接上时那样。
- `hand`：和`pointer`的作用一样：竖起一只手指的手形光标。就像通常用户将光标移到超链接上时那样。
- all-scroll :　 IE6.0 有上下左右四个箭头，中间有一个圆点的光标。用于标示页面可以向上下左右任何方向滚动。
- col-resize :　 IE6.0 有左右两个箭头，中间由竖线分隔开的光标。用于标示项目或标题栏可以被水平改变尺寸。
- crosshair :　 简单的十字线光标。
- default :　 客户端平台的默认光标。通常是一个箭头。
- move :　 十字箭头光标。用于标示对象可被移动。
- help :　 带有问号标记的箭头。用于标示有帮助信息存在。
- no-drop :　 IE6.0 带有一个被斜线贯穿的圆圈的手形光标。用于标示被拖起的对象不允许在光标的当前位置被放下。
- not-allowed :　 IE6.0 禁止标记(一个被斜线贯穿的圆圈)光标。用于标示请求的操作不允许被执行。
- progress :　 IE6.0 带有沙漏标记的箭头光标。用于标示一个进程正在后台运行。
- row-resize :　 IE6.0 有上下两个箭头，中间由横线分隔开的光标。用于标示项目或标题栏可以被垂直改变尺寸。
- text :　 用于标示可编辑的水平文本的光标。通常是大写字母 I 的形状。
- vertical-text :　 IE6.0 用于标示可编辑的垂直文本的光标。通常是大写字母 I 旋转90度的形状。
- wait :　 用于标示程序忙用户需要等待的光标。通常是沙漏或手表的形状。
- *-resize :　 用于标示对象可被改变尺寸方向的箭头光标



object-fit cover object-fit属性，并将其设置为cover。这将告诉图片在保持宽高比的同时填充img容器，从而实现裁剪以适应尺寸。

aspect-ratio: 35 / 4; 规定目标显示区域的宽度/高度比

 `max()`功能

该`max()`函数返回一组以逗号分隔的值中的最大值：

```css
img {
  width: max(250px, 25vw);
}
```

在上面的例子中，如果视口宽度小于 1000 像素，则图像宽度为 250 像素。如果视口宽度大于 1000 像素，则图像宽度为 25vw。这是因为 25vw 等于视口宽度的 25%。
`min()`功能

role属性
为提高页面可访问性，可通过使用角色属性来向辅助技术表明页面中某个元素背后的目的。角色属性是Web可访问性倡议(WAI)的一部分，并可以接受预设值。
每个区域角色都需要一个标签，这有助于屏幕阅读器用户理解该区域的用途。添加标签的一种方法是:在区域内添加一个标题元素，然后用`aria-labelledby'属性对其进行引用。

clip: rect(1px,1px,1px,1px);

  clip-path: inset(50%);
  CSS的clip属性用于定义元素可见的部分。将`span[class~='sr-only']`选择器设置为具有rect(1px,1px,1px,1px)的clip属性。
clip-path属性决定了clip属性应呈现的形状。将clip-path属性设置为inset(50%)的值，可使clip路径在元素内部形成，一个矩形区域。




## CSS和无障碍设计的最佳实践

- **`display: none;`**使用`display: none;`此方法意味着屏幕阅读器和其他辅助技术将无法访问此内容，因为它未包含在辅助功能树中。因此，仅当您希望从视觉呈现和辅助功能中完全移除内容时，才应使用此方法。
- **`visibility: hidden;`**此属性和值会在视觉上隐藏内容，但仍将其保留在文档流中，这意味着它仍然占据页面上的空间。这些元素也将不再被屏幕阅读器读取，因为它们已从辅助功能树中移除。
- **`.sr-only`CSS 类**：这是一种常用的技术，用于在视觉上隐藏内容，同时保持屏幕阅读器可以访问该内容。

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

- **`scroll-behavior: smooth;`**此属性和值可实现平滑滚动效果。
- **`prefers-reduced-motion`功能**：这是一个媒体功能，可用于检测用户的动画偏好。

```css
@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}
```

在上面的示例中，如果用户未在其设备上设置动画首选项，则会启用平滑滚动。

## 使用 HTML 属性隐藏内容

- **`aria-hidden`属性**：用于对使用辅助技术（例如屏幕阅读器）的用户隐藏元素。例如，这可以用来隐藏不提供任何实际内容的装饰性图像。
- **`hidden`属性**：此属性受大多数现代浏览器支持，它会在视觉上和辅助功能树中隐藏内容。可以使用 JavaScript 轻松切换此属性。

```html
<p aria-hidden>This paragraph is visible for sighted users, but is hidden from assistive technology.</p>
<p hidden>This paragraph is hidden from both sighted users and assistive technology.</p>
```



## CSS 变量

### CSS 自定义属性（CSS 变量）
**定义**：CSS 自定义属性，也称为 CSS 变量，是由 CSS 作者定义的实体，其中包含可在整个文档中重复使用的特定值。它们是一项强大的功能，可以提高样式表的效率、可维护性和灵活性。自定义属性在创建可主题化的设计时尤其有用。您可以为不同的主题定义一组属性。
声明自定义属性的语法很简单。它以两个短横线 ( `--`) 开头，后跟属性名称：
```css
:root {
  --main-color: #3498db;
}
```
在这个例子中，我们声明了一个名为 `<propertyName>` 的自定义属性，`--main-color`其值为 `<value> `#3498db` `。`:root`伪类通常用于声明全局自定义属性，因为它代表 DOM 树中的最高级别父级。
要使用自定义属性，您可以使用以下`var()`函数：
```css
.button {
  background-color: var(--main-color);
}
```
自定义属性的一个关键特性是它们遵循 CSS 层叠规则。这意味着您可以针对特定元素或上下文重新定义它们：
```css
.alert {
  --main-color: #e74c3c;
  background-color: var(--main-color);
}
```
在这种情况下，具有该类的元素`alert`将使用不同的`--main-color`值，覆盖全局定义。

自定义属性也支持备用值。如果自定义属性未定义或无效，您可以提供备用值：

```html
<link rel="stylesheet" href="styles.css">
<div class="text">This is some text.</div>
```

```css
:root {
  --text-color: green;
}

.text {
  color: var(--text-color, green);
}
```

这里，如果`--text-color`未定义，则`color`默认值为`green`。
切换主题就像给`body`元素添加或删除一个类一样简单。

自定义属性还可以与媒体查询结合使用，以创建响应式设计：

```html
<link rel="stylesheet" href="styles.css">

<div class="card">
  <h2>Responsive Design</h2>
  <p>Resize the window to see the card adapt!</p>
</div>

```

```css
:root {
  --card-width: 90%;
  --card-bg: #f0f0f0;
  --card-padding: 1rem;
  --text-color: #333;
}

/* Tablet screens and up */
@media (min-width: 600px) {
  :root {
    --card-width: 70%;
    --card-bg: #e8f5e9;
    --card-padding: 1.5rem;
  }
}

/* Desktop screens and up */
@media (min-width: 1024px) {
  :root {
    --card-width: 50%;
    --card-bg: #d0f0ff;
    --card-padding: 2rem;
  }
}

body {
  font-family: system-ui, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #fafafa;
}

.card {
  width: var(--card-width);
  background-color: var(--card-bg);
  padding: var(--card-padding);
  color: var(--text-color);
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  text-align: center;
  transition: all 0.3s ease;
}
```

### 规则`@property`​

- **定义**：该`@property`规则是一项强大的 CSS 功能，允许开发人员定义自定义属性，并更好地控制其行为，包括动画效果和初始值。

```css
@property --property-name {
  syntax: '<type>';
  inherits: true | false;
  initial-value: <value>;
}
```

- **`--property-name`**这是您要定义的自定义属性的名称。与所有自定义属性一样，它必须以两个短横线开头。`--property-name`可以是类似`<color>`  `<length>` `<string> `、`<string>`  `<string>`  `<string>`     `<number><percentage>`或  更复杂的类型。
- **`syntax`**这定义了属性的类型。
- **`inherits`**：这指定该属性是否应从其父元素继承其值。
- **`initial-value`**：这将设置属性的默认值。
```css
@property --gradient-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.gradient-box {
  width: 100px;
  height: 100px;
  background: linear-gradient(var(--gradient-angle), red, blue);
  transition: --gradient-angle 0.5s;
}

.gradient-box:hover {
  --gradient-angle: 90deg;
}
```
- **备用值**：使用自定义属性时，您可以`var()`像使用标准自定义属性一样，使用函数提供备用值。
```css
.button {
  background-color: var(--main-color, #3498db);
}
```



### 辅助功能和`prefers-reduced-motion`媒体查询

- **`prefers-reduced-motion`媒体查询**：动画的主要可访问性问题之一是它们可能会给部分用户带来不适甚至身体伤害。患有前庭功能障碍或运动敏感的人在观看某些类型的屏幕动画时可能会感到头晕、恶心或头痛。**媒体**`prefers-reduced-motion`查询允许 Web 开发人员在系统层面检测用户是否请求了最小动画或运动效果。
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
查询`@media`规则检查用户是否偏好减少动态效果。如果是，则应用规则中包含的样式。

在媒体查询中，我们针对所有元素（`*`），并覆盖动画和过渡属性。

我们将`animation-duration`和设置`transition-duration`为一个极小的值（`0.01ms`）。这实际上关闭了动画，但仍然允许它们完成播放，这对于某些功能来说至关重要。

`animation-iteration-count: 1`确保所有循环动画只播放一次。

`scroll-behavior: auto`关闭平滑滚动效果。

该`!important`声明用于确保这些规则优先于其他动画样式。
需要注意的是，虽然这种方法能有效减少动画动作，但它是一种一刀切的方法。为了更精确地控制动画动作，您可能需要为动画定义特定的减少动作的替代方案。
以下是一个更有针对性的方法示例：

```css
.animated-element {
  transition: transform 0.3s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .animated-element {
    transition: none;
  }
}
```

在这种情况下，我们仅在`transition`用户希望减少动作时才禁用特定元素的动画效果。这样，您就可以为有需要的用户提供其他动作较少的体验。
# 其他
对象适配属性（object-fit）告诉浏览器如何在其容器内定位该元素。在此示例中，覆盖功能（cover）会将图像设置为填充容器，并根据需要进行裁剪，以避免改变图像的纵横比。
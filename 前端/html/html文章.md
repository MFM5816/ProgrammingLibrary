# 初识html
## HTML在Web中扮演什么角色？

HTML，即超文本标记语言，是一种用于创建网页的标记语言。当你访问一个网站并看到段落、标题、链接、图像和视频等内容时，这些就是HTML。

这里有一个使用 HTML 元素的小例子。尝试在编辑器中编辑一些文本，并在预览窗口中查看更改的更新。

```html
<h1>Main heading element</h1>

<p>I am a paragraph element.</p>
```

HTML 通过元素来表示网页的内容和结构。大多数元素都有一个开始标签和一个结束标签。有时这些标签也被称为起始标签和结束标签。在这两个标签之间是网页的内容。这些内容可以是文本，也可以是其他 HTML 元素。

以下是段落元素的另一个示例。请在编辑器中将文本更改为“say” `I love coding!`，然后在预览窗口中查看结果。

```html
<p>I am a paragraph element.</p>
```

标签的开始和结束都以左尖括号 ( ) 开头`<`，以右尖括号 ( `>`) 结尾，标签名称位于这两个尖括号之间。虽然 HTML 标签名称不区分大小写，但普遍接受的惯例和最佳实践是使用小写字母来编写标签名称。

下面我们来仔细看看段落的开头和结尾标签：

```html
<p>
```

```html
</p>
```

开始标签和结束标签的区别在于，结束标签的左尖括号后面紧跟一个斜杠（`/``\`）。有些 HTML 元素没有结束标签，这些元素被称为空元素。

以下是一个空图像元素的示例：

```html
<img>
```

请注意，此图像元素没有结束标签，也没有任何内容。空元素不能包含任何内容，只能有一个开始标签。

有时你会看到一些空元素，它们`/`在前面使用 a，`>`像这样：

```html
<img />
```

虽然许多代码格式化工具（如 Prettier）会选择在空元素中包含 <img> 标签`/`，但 HTML 规范指出，<img> 标签的存在`/`“并不会将开始标签标记为自闭合标签，而是没有必要的，并且没有任何效果”。

在实际开发过程中，你会遇到这两种形式，因此熟悉这两种形式都很重要。

如果要显示图片，需要在图片元素中添加几个属性。属性是用于调整 HTML 元素行为的特殊值。

这是一个带有属性的图像元素示例。将该属性`src`的值更新为，您将看到图像变为两只猫安然入睡的画面。`src``"https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"`

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/running-cats.jpg" />
```

该`src`属性用于指定图像的位置。对于图像元素，最佳实践是包含另一个名为 ` `alt`<image>` 的属性。`<image>``alt`属性用于为图像提供简短的描述性文本。

`src`这里有一个带有 `image` 和`text`属性的图像元素示例`alt`。尝试将 `image` 的`src`值更新为 `true` `"https://.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"`，你会看到图像消失，只剩下`alt`文本显示。

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch." />
```

所以，你可能想知道单靠HTML是否足以搭建一个网站。答案是：这要视情况而定。如果你只是做一个小型练习项目，只显示文本和图片，那么单靠HTML可能就足够了。但是，如果你要创建一个现代化的专业网站，则需要HTML、CSS和JavaScript。

HTML 用于内容和结构，CSS 用于样式，JavaScript 用于为网页添加交互功能。我们可以用一座完整的建筑物来形象地比喻 HTML、CSS 和 JavaScript 之间的关系。

HTML 代表构成墙体的砖块、混凝土和铁架，它是建筑物的地基，使建筑物坚固。CSS 代表室内外设计，使房屋外观美观。JavaScript 代表电力和供水系统，确保不间断的供水和供电。
## 什么是属性，它们是如何运作的？

属性是放置在 HTML 元素开始标签内的值。属性提供有关元素的附加信息，或指定元素的行为方式。以下是属性的基本语法：

```html
<element attribute="value"></element>
```

属性名称后跟等号 ( `=`) 和用引号括起来的值。该值可以是字符串或数字，具体取决于属性类型。

第一个示例使用了 `URL``href`和`target``打开位置` 属性。`URL``href`属性指定链接的 URL，而 ``target`打开位置` 属性指定链接的打开方式。

启用交互式编辑器并将链接更改为`href="https://www.freecodecamp.org/news/"`。`href="https://www.freecodecamp.org"`现在，当您点击交互式编辑器中的链接时，您将在新的浏览器标签页中看到 freeCodeCamp 主页。

```html
<a href="https://www.freecodecamp.org/news/" target="_blank">Visit freeCodeCamp</a>
```

如果没有这个`href`属性，链接将无法工作，因为没有目标 URL。因此，您必须添加此`href`属性才能使链接生效。该属性`target="_blank"`允许链接在新浏览器标签页中打开。您将`target`在后续课程中了解更多关于此属性的信息。

其他常见属性有 src` `、`alt`或 `<alternative>` 属性，分别用于指定图像的来源和提供图像的替代描述文本。

启用交互式编辑器并更改`src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"`。`src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/running-cats.jpg"`然后将`alt="Two tabby kittens sleeping together on a couch."`更改`alt="Two cats running in the dirt."`。

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch." />
```

与 `image` 属性类似`href`，`image``src`属性也是必需的，因为它指定了要显示的图像文件。`image``alt`属性并非必需，但为了提高可访问性，建议使用。可访问性是指确保每个人，包括残障人士，都能使用和理解网站、应用程序和物理空间等资源。您将在接下来的课程中了解更多关于可访问性的知识。

有些属性的语法比较特殊，例如`checked`属性本身。

启用交互式编辑器，然后尝试单击预览窗口中的复选框，查看它在选中和未选中状态之间切换。

```html
<input type="checkbox" checked />
```

在以下示例中，我们有一个`input`元素，其`type`属性设置为`checkbox`。输入框用于收集用户数据，`type`属性指定输入框的类型。在本例中，此输入框是一个复选框。您将在后续课程中了解更多关于输入框工作原理的信息。

该`checked`属性用于指定复选框的默认选中状态。该`checked`属性不需要值。如果存在该属性，则复选框默认选中；如果不存在该属性，则复选框默认未选中。这被称为布尔属性。您将在学习 JavaScript 部分时了解更多关于布尔值的知识。

启用交互式编辑器，然后尝试`checked`从元素中移除该属性`input`。您会发现默认情况下复选框不再被选中。

```html
<input type="checkbox" checked />
```

在 HTML 中，你会遇到几个常见的布尔属性，例如`disabled``true`、`readonly``false` 和 `false` `required`。这些属性用于指定元素的状态，例如它是禁用的、只读的还是必需的。

`input`这里有一个默认禁用的文本元素示例。启用交互式编辑器，然后`input`在预览窗口中点击该元素。现在移除`disabled`该元素的属性`input`，你会发现它`input`不再默认禁用。现在你应该可以点击它并在文本框中输入内容了。

```html
<input type="text" disabled>
```

HTML 拥有许多属性，可用于自定义网页元素的行为和外观。了解如何使用属性对于创建交互式且易于访问的网页内容至关重要。在接下来的几节课中，您将学习更多 HTML 属性以及如何在 Web 开发项目中有效地使用它们。
# 了解HTML样板
## HTML 中的 link 元素有什么作用？如何利用 link 元素链接到外部样式表？

让我们来了解一下这个`link`元素，以及如何使用它来链接到外部样式表。

该`link`元素用于链接到外部资源，例如样式表和网站图标。以下是使用该`link`元素链接到外部 CSS 文件的基本语法：

```html
<link rel="stylesheet" href="./styles.css" />
```

该`rel`属性用于指定链接资源与 HTML 文档之间的关系。在本例中，我们需要指定此链接资源为`stylesheet`.

将 HTML 和 CSS 代码分离到不同的文件中被认为是最佳实践。开发人员会使用 ` `link`<style>` 元素来存放外部 CSS 文件，而不是将所有内容都写在 HTML 文档中。

该`href`属性用于指定外部资源的 URL 位置。

示例中的斜杠`dot`表示计算机在当前文件夹或目录中查找文件`styles.css`。

该`link`元素应放置在另一个`head`元素内部，如下例所示：

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Examples of the link element</title>
  <link rel="stylesheet" href="./styles.css" />
</head>
```

在专业的代码库中，您经常会看到多个`link`元素链接到不同的样式表、字体和图标。以下示例展示了如何使用该`link`元素链接到名为_Playwright Cuba 的_外部 Google 字体：

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap"
  rel="stylesheet"
/>
```

Google Fonts 是一套免费开源的自定义字体，您可以在任何项目中使用。您可以选择想要使用的字体，Google 会提供必要的 HTML 和 CSS 代码。在本例中，` class` 属性`preconnect`的值`rel`指示浏览器尽早连接到该`href`属性指定的值。这样做是为了加快这些外部资源的加载速度。

该元素的另一个常见用途`link`是链接到图标。以下是链接到网站图标 (favicon) 的示例：

```html
<link rel="icon" href="favicon.ico" />
```

网站图标（favicon）是“favourite icon”（最喜欢的图标）的缩写，它是一个通常显示在浏览器标签页网站标题旁边的小图标。许多网站会使用网站图标来展示其品牌标识。
## 什么是 HTML 样板代码，它为什么重要？

我们来学习一下HTML样板代码。

你可能会问，什么是 HTML 样板代码？它就像一个现成的网页模板。你可以把它想象成房子的地基。样板代码包含了每个 HTML 文档所需的基本结构和必要元素。它可以节省你的时间，并确保你的网页设置正确。以下是一个示例：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
  </body>
</html>
```

让我们来分析一下这段样板代码的关键部分。首先是`DOCTYPE`声明：

```html
<!DOCTYPE html>
```

它告诉浏览器你正在使用哪个版本的 HTML。接下来是`html`标签：

```html
<!DOCTYPE html>
<html lang="en">
  <!--All other elements go inside here-->
</html>
```

这会包裹住你的所有内容，并可以指定页面的语言。在`html`标签内，你会找到两个主要部分——`<head>``head`和 `<style>` `body`：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!--Important metadata goes here-->
  </head>
  <body>
    <!--Headings, paragraphs, images, etc. go inside here-->
  </body>
</html>
```

本`head`部分包含重要的幕后信息：

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document Title Goes Here</title>
  <link rel="stylesheet" href="./styles.css" />
</head>
```

网站的元数据包含在 ` `meta`<meta>` 元素中，其中包含字符编码等详细信息，以及像 Twitter 这样的网站应该如何预览您页面的链接。网站标题位于 `<title>` 元素中，它决定了浏览器标签页或窗口中显示的文本。最后，您通常会在 `<externalstylesheet> ` 部分使用`<style>` 元素`title`链接页面的外部样式表。`head``link`

此`body`部分用于放置所有内容：

```html
<body>
  <h1>I am a main title</h1>
  <p>Example paragraph text</p>
</body>
```

那么，为什么样板代码如此重要呢？它可以确保你的页面结构正确，并且在不同的浏览器上都能良好运行。使用样板代码可以帮助你避免常见错误并遵循最佳实践。它是任何网站项目的绝佳起点。记住，你可以根据自己的需求定制样板代码。随着经验的积累，你可能会添加自己喜欢的元素或`meta`标签。不断改进你的个人样板代码，你会发现它在启动新项目时可以节省大量时间。

下次创建新的 HTML 文件时，不妨考虑使用模板。它绝对能为你打下坚实的基础。
## 什么是UTF-8字符编码？为什么需要它？

UTF-8，即 UCS 转换格式 8，是一种广泛应用于 Web 的标准化字符编码。字符编码是计算机存储字符数据的方式。本质上，网页上的所有文本都是一系列字符，这些字符以一个或多个字节的形式存储。在计算机领域，一个字节是由 8 位（二进制数字）组成的数据单元。UTF-8 支持 Unicode 字符集中的所有字符，包括所有书写系统、语言和技术符号中的字符和符号。以下示例展示了如何使用`meta`带有 `<code> `charset`` 属性的 `<code>` 元素来设置字符编码`UTF-8`：

```html
<meta charset="UTF-8" />
```

将字符编码设置为 UTF-8，可以确保带重音符号的`"e"`字符（`é`）在页面上正确显示。以下是使用 UTF-8 字符编码的完整代码示例：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Examples of the UTF-8 encoding</title>
  </head>
  <body>
    <p>Café</p>
  </body>
</html>
```

对于您创建的每个新项目，您都应该包含此`meta`元素，并将`charset`属性设置为`UTF-8`。
# 基础知识
## 什么是div元素？何时应该使用它们？

该`div`元素用作容器，将其他元素组合在一起。

这里有一个元素示例`div`。在该`div`元素内添加另一个段落元素，并在预览窗口中查看更改。要查看预览，您需要启用交互式编辑器。

```html
<div>
  <p>Example paragraph element.</p>
</div>
```

`div`当您需要将共享一组 CSS 样式的 HTML 元素分组时，主要会用到该元素。您将在后续课程和研讨会中学习更多关于 CSS 的知识。

尽管该`div`元素在实际代码库中很常用，但应注意不要过度使用。有时使用其他元素会更合适。

例如，如果您想将内容分成多个部分，那么`section`使用 `<section>` 元素比使用 `<section>` 元素更合适`div`。

`section`在第一个元素下方添加另一个元素。然后在该`section`元素内部添加 `<a>``h2`和`<a> `p`` 元素。您可以随意使用任何文本，预览窗口中会显示更改。要与示例交互，您需要启用交互式编辑器。

```html
<section>
  <h2>Mammals</h2>
  <p>
    Mammals are warm-blooded animals with fur or hair. Most give birth to live
    young.
  </p>
  <ul>
    <li>Lion</li>
    <li>Elephant</li>
    <li>Dolphin</li>
  </ul>
</section>
```

元素`section`具有语义含义，而`div`元素则不具有语义含义。语义指的是语言中词语或短语的意义。HTML 也是一种语言，其中的元素也具有自身的语义含义。这意味着，如果您使用一个`section`元素，浏览器会识别其语义含义，并将其视为一个部分——无论是在桌面端、移动端还是其他任何设备上。
## 什么是 ID 和类，以及何时应该使用它们？

该`id`属性为HTML元素添加唯一标识符。

`h1`以下是一个带有`id`of 的元素的示例`title`。

在元素下方`h1`，添加一个`h2`元素，并将 `<textarea>` `id`属性设置为 "subtitle"。您可以为 `<textarea>` 输入任何您想要的文本`h2`，并在预览窗口中查看更改。要与示例进行交互，您需要启用交互式编辑器。

```html
<h1 id="title">Movie Review Page</h1>

```

您可以在 JavaScript 或 CSS 中引用`id`该名称。以下是一个 CSS 示例，它引用该名称将文本更改为。`title``id``title``color``red`

**注意**：本交互式示例中已为您提供了一些 CSS 代码。不必担心理解这些 CSS 代码，因为您将在后续课程中学习更多相关内容。如果您想将文本颜色更改为蓝色，请启用交互式编辑器，单击选项`styles.css`卡并将值更改`color: red;`为`color: blue;`。

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

`#`前面的井号 ( #)`title`告诉计算机你要用`id`这个值来定位一个对象。`id`名称不能重复使用，而且必须始终唯一。关于值，还需要注意一点：`id`值中不能包含空格。以下示例展示了如何将单词`main`和`heading`应用于`id`属性值：

```html
<h1 id="main heading">Main heading</h1>
```

浏览器会将此空间视为元素的一部分，`id`这会导致样式和脚本方面出现不必要的问题。`id`属性值应该只包含字母、数字、下划线和短横线。

与`id`属性不同，`class`属性值不需要唯一，并且可以包含空格。

`box`以下是将名为“class”的类应用于元素的示例`div`。

```html
<div class="box"></div>
```

如果要给一个元素添加多个类名，可以用空格分隔这些类名。以下是一个更新后的示例，展示了如何给一个`div`元素添加多个类。

```html
<div class="box red-box"></div>
```

以下是对多个元素应用多个类的另一个示例`div`。

**注意**：本交互式示例中已为您提供了一些 CSS 代码。不必担心理解这些 CSS 代码，因为您将在后续课程中学习更多相关内容。如果您想更改第一个和第三个框的颜色，请启用交互式编辑器，然后单击选项`styles.css`卡并将值更改`background-color: red;`为`background-color: black;`。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>Colored boxes example</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <div class="box red-box"></div>
    <div class="box blue-box"></div>
    <div class="box red-box"></div>
    <div class="box blue-box"></div>
  </body>
</html>
```

```css
.box {
  width: 100px;
  height: 100px;
}

.red-box {
  background-color: red;
}

.blue-box {
  background-color: blue;
}
```

所以，总结一下，什么时候应该使用类，什么时候应该使用`id`样式`class`？类最适合用于将一组样式应用于多个元素。如果要针对特定​​元素，最好使用样式，`id`因为样式值必须是唯一的。

## 什么是 HTML 实体？常见的例子有哪些？

HTML实体（或字符引用）是一组用于表示HTML中保留字符的字符。

假设您想`This is an <img/> element`在屏幕上显示这段文本。如果您使用编辑器中当前的代码，则无法显示预期结果。即使您为示例添加了`src`属性`alt`，它也会在段落中间显示一张图片，而不是您想要的结果。要与示例进行交互，您需要启用交互式编辑器。

```html
<p>This is an <img /> element</p>
```

当 HTML 解析器看到小于号 ( ) 后跟 HTML 标签名称时，它会将其解释为一个 HTML 元素。这就是为什么屏幕上`<`没有显示预期结果的原因。`This is an <img/> element`

要解决这个问题，您可以使用 HTML 实体。以下是一个更新后的示例，其中使用了正确的 HTML 实体来表示小于号 ( `<`<) 和大于`>`号 (>)。现在您应该能`This is an <img/> element`在屏幕上看到结果了。

启用交互式编辑器，然后尝试`&lt;p&gt;learning is fun&lt;/p&gt;`在段落元素下方添加一个元素。你应该会`<p>learning is fun</p>`在屏幕上看到它。

```html
<p>This is an &lt;img /&gt; element</p>

```

这类字符引用被称为命名字符引用。命名引用以 & 符号开头`&`，以分号 (" `;`") 结尾。使用命名字符引用，HTML 解析器就不会将其与实际的 HTML 元素混淆。

另一种字符引用类型是十进制数字引用。这种字符引用以 & 符号和井号 ( `#`) 开头，后跟一个或多个十进制数字，最后以分号结尾。

以下是使用十进制数字表示小于号的示例。

启用交互式编辑器并修改代码以查看不同的符号。您可以使用`&#169;`表示版权符号，也`&#174;`可以使用 表示商标符号。

```html
&#60;
```

最后一种字符引用是十六进制数字引用。这种字符引用以 & 符号、# 符号和字母 开头，`x`后面跟着一个或多个 ASCII 十六进制数字，最后以分号结尾。

以下是使用十六进制数字表示小于号的示例。

启用交互式编辑器并修改代码以查看不同的符号。您可以使用`&#x20AC;`它来表示欧元符号，也`&#x03A9;`可以使用希腊字母大写Ω来表示希腊字母Ω符号。

```html
&#x3C;
```
## HTML 中的 script 元素扮演什么角色？如何利用它链接到外部 JavaScript 文件？

该`script`元素用于嵌入可执行代码。大多数开发者会使用它来执行 JavaScript 代码。JavaScript 用于为网页添加交互功能。常见的 JavaScript 应用示例包括交互式游戏、图片轮播和实时验证用户输入的动态表单。

`script`以下是在 HTML 文档中使用该元素的示例。移除`//``<div>` 前面的 ` <from>` 标签`alert("Welcome to freeCodeCamp");`，您应该会看到一个弹出提示框。要查看预览，您需要启用交互式编辑器。

```html
<body>
  <script>
    // alert("Welcome to freeCodeCamp");
  </script>
</body>
```

虽然理论上你可以将所有 JavaScript 代码都写在标签内，但最佳实践是链接到外部 JavaScript 文件。以下是使用`<script>` 元素链接到外部 JavaScript 文件`script`的示例：`script`

```html
<script src="path-to-javascript-file.js"></script>
```

这里使用`<source>``src`属性来指定外部 JavaScript 文件的位置。` `src`<source>` 代表“源”。不建议将所有 JavaScript 代码都放在 HTML 文档中的原因在于关注点分离。关注点分离是一种设计原则，它将程序分成不同的部分，每个部分负责一个不同的关注点。在本例中，我们希望将 JavaScript 代码与 HTML 代码分开。
# 搜索引擎优化
## 元描述的作用是什么？它如何影响搜索引擎优化？

SEO，即搜索引擎优化，是一种优化网页以提高其在搜索引擎中的可见度和排名的实践。提升网站 SEO 的一种方法是使用 `<meta>``meta`元素为网页添加简短描述。以下是一个使用 `<meta>` 元素为园艺网站设置页面描述的示例：

```html
<meta
  name="description"
  content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
```

通过将该`name`属性设置为 true `description`，可以确保浏览器、搜索引擎和其他网络工具正确解析此元数据。`content`您可以在该属性中放置描述。建议您保持描述简短明了。这是因为搜索引擎通常会根据搜索结果页面的布局截断描述。

与其他类型的元素类似`meta`，页面`meta`描述不会直接显示在网页上。页面描述可以在搜索引擎结果页面摘要中找到。以下是 freeCodeCamp 子版块和 GitHub 代码库的页面结果摘要示例：

```sh
r\FreeCodeCamp: This is the official subreddit for the freeCodeCamp.org community. Learn to
code for free together with millions of other people...
```

```sh
Our full-stack web development and machine learning curriculum is completely free and self-
paced. We have thousands of interactive coding challenges to help you...
```

在这些示例中，每个页面描述都位于网站链接的正下方。用户只需几秒钟即可大致了解页面内容，并决定是否点击链接获取更多信息。

虽然`meta`描述不会直接影响网站在搜索引擎上的排名，但一个好的描述可以为您的网站带来更多流量。

## Open Graph 标签的作用是什么？它们如何影响 SEO？

Open Graph 协议使您能够控制网站内容在各种社交媒体平台（例如 Facebook、LinkedIn 等）上的显示方式。通过设置这些 Open Graph 属性，您可以吸引用户点击并与您的内容互动。您可以通过`meta`HTML`head`代码中的一系列元素来设置这些属性。

首先要包含的重要 OG 属性是 `<OG>` 。以下是为 freeCodeCamp 主页`title`设置 OG 的示例：`title`

```html
<meta content="freeCodeCamp.org" property="og:title" />
```

对于该`property`属性，您需要指定其值为`og:title`。该`content`属性用于编写您希望在社交媒体网站上显示的标题。

下一个重要的 OG 属性是。以下是使用 OG 属性创建 freeCodeCamp 主页`type`的示例：`type`

```html
<meta property="og:type" content="website" />
```

该`type`属性用于表示社交媒体上分享的内容类型。此类内容的示例包括文章、网站、视频或音乐。

第三个重要的 OG 属性是。以下是设置freeCodeCamp 主页`image`OG 的示例：`image`

```html
<meta
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
  property="og:image"
/>
```

在这个例子中，Open Graph 图片指向的是 freeCodeCamp 的标志。所有这些图片都应该是高质量的，并且尺寸和比例都合适。大多数社交媒体平台都会提供图片要求标准，以帮助您确保您的内容在其网站上显示良好。例​​如，developers.facebook.com 的文档页面指出：

“为了在高分辨率设备上获得最佳显示效果，请使用至少 1200 x 630 像素的图片。对于包含较大图片的链接页面帖子，您至少应使用 600 x 315 像素的图片。”

第四个重要的 OG 属性是。以下是设置freeCodeCamp 主页`url`OG 的示例：`url`

```html
<meta property="og:url" content="https://www.freecodecamp.org" />
```

您可以设置更多 OG 属性，例如`description`、`audio`和`video`。`locale`但是，开放图`url`、`image`、`type`和`title`是最重要的属性。

那么，这些开放图谱属性是如何影响搜索引擎优化的呢？当你的内容在社交媒体上分享时，精心设计的开放图谱属性可以提升你的内容在用户信息流中的展示效果。这可以带来更高的点击率，从而向搜索引擎发出信号，表明你的内容具有相关性和吸引力。
# 音频和视频
## HTML音频和视频元素的作用是什么？它们是如何工作的？

`<audio> ` 和  `<video>` 元素允许您向 HTML 文档添加音频和视频内容。`<audio>`元素支持常见的音频格式，例如 mp3、wav 和 ogg。` <video>`元素支持 mp4、ogg 和 webm 格式。

要在网页上添加音频内容，可以使用`audio`带有属性的元素，该`src`属性指向音频文件的位置。

如预览窗口所示，页面上没有任何内容显示。要查看预览，您需要启用交互式编辑器。

```html
<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3"></audio>
```

如果你想在页面上显示音频播放器，那么你可以添加`audio`带有该`controls`属性的元素。

在预览窗口中点击播放按钮，即可收听昆西·拉尔森的一首歌曲。要收听其他歌曲，请更改该`src`值`"https://cdn.freecodecamp.org/curriculum/js-music-player/never-not-favored.mp3"`。要查看预览，您需要启用交互式编辑器。

```html
<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3" controls></audio>
```

该`controls`属性允许用户管理音频播放，包括调节音量、暂停或恢复播放。该`controls`属性是一个布尔属性，可以添加到元素中以启用内置播放控件。如果省略，则不会显示任何控件。

除了 ` `src`and``controls`属性之外，还有其他几个属性可以增强元素的功能`audio`。`replay``loop`属性是一个布尔属性，用于控制音频是否持续播放。

这里有一个使用该`loop`属性播放昆西·拉尔森歌曲《Can't Stay Down》的示例。要查看循环播放效果，请启用交互式编辑器，将播放头拖动到歌曲末尾附近，歌曲播放完毕后它将重新开始播放。

```html
<audio
  src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3"
  loop
  controls
></audio>
```

您还可以使用另一个属性`muted`。当元素中存在`audio`此布尔属性时，音频将以静音状态开始播放。以下是使用此`muted`属性的示例。

要收听音乐，请启用交互式编辑器，然后单击音频播放器中的音量图标。

```html
<audio
  src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3"
  loop
  controls
  muted
></audio>
```

对于音频文件类型，不同浏览器的支持情况有所不同。为了解决这个问题，你可以在 `<audio>` 元素`source`内使用 `<audio>` 元素，浏览器会自动选择它能够识别的第一个音频源。以下是一个使用多个 ` <audio>` 元素的`audio`示例：`source``audio`

```html
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
```

浏览器会首先尝试播放 ogg 类型的音频，如果无法播放，则会向下移动到列表中的下一个类型。

我们目前学到的所有属性在这个元素中也都受支持。以下是一个使用带有 `<style> ` 、`<style>` 和`<style>` 属性的元素`video`的示例。`video``loop``controls``muted`

将该属性添加`autoplay`到起始`video`标签中，即可使视频自动播放。要与示例进行交互，您需要启用交互式编辑器。

**注意**`width`：此处使用此属性是为了缩小视频尺寸，使其更好地适应预览窗口。您将`width`在后续课程中了解更多关于此属性的信息。

```html
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  width="400"
></video>
```

对于`src``<source>` 属性，我们使用了来自 archive.org 的名为“Big Buck Bunny”的视频。如果您想在视频下载时显示图像，可以使用 ` `poster`<image>` 属性。此属性不适用于`audio``<div>` 元素，并且是 `<div>` 元素特有的`video`。以下示例展示了如何使用 ` `poster`<image>` 属性以及 peach.blender.org 提供的内容。

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
# 处理图像和SVG
## 优化媒体资产的常用方法有哪些？

在网页上使用图片等媒体时，需要考虑三个因素：大小、格式和压缩。

我们先来谈谈图片尺寸。在构建网站时，您通常会设置图片样式，使其以特定尺寸显示。例如，您可能希望图片以 640x480 的分辨率显示。640 代表宽度，480 代表高度，单位均为像素。准备图片时，您需要将其缩放到 640x480 的尺寸，以匹配样式。如果您提供的图片分辨率为 1920x1080，但样式设置却使其小得多，那么用户就需要下载不必要的数据。分辨率越低，文件大小就越小。

接下来要考虑的是文件格式。PNG 和 JPG 是两种最常见的文件格式，但它们已不再是理想的图像格式。除非您需要兼容旧版浏览器，否则应考虑使用更优化的格式，例如 WEBP 或 AVIF。

最后，您可以对图像运行压缩算法。压缩算法用于减小文件或数据的大小。您可以使用 pngcrush 等工具在本地压缩图像，也可以使用在线压缩工具。但是，值得注意的是，某些文件格式（例如 JPG）并非无损压缩。无损压缩是指可以从压缩后的数据中完美地还原原始数据。如果您尝试压缩 JPG 图像，则会导致图像质量下降。在为网页选择图像时，您应该牢记所有这些因素。
## 图像许可有哪些类型，它们是如何运作的？

图片被视为知识产权，这意味着它们受版权法规保护，版权通常归创作者所有。默认情况下，图片以“保留所有权利”的形式发布。创作者或出版商有时拥有图片的全部版权。

这意味着，除非您采取以下三种措施之一，否则您不能在您的网页中使用这些图像：获得版权所有者的书面许可、从版权所有者处购买许可，或者以符合合理使用原则的方式将图像融入您的网页。

第三点有点棘手。合理使用要求你对图像的使用既要有限，又要具有转化性。合理使用的例子包括评论或评析艺术作品，或者创作图像的戏仿作品。

有些图片可能采用较为宽松的许可协议，例如知识共享许可协议（Creative Commons License）或freeCodeCamp使用的BSD许可协议。这些图片可用于您的网站，但您需要阅读许可协议以了解使用这些图片时需要遵守的规则。例如，您可能需要将您的网站开源，或者您可能被禁止以任何方式修改图片。

最后，部分图片可能会进入公有领域。公有领域的图片不附带任何版权，可以自由使用，不受任何限制。根据知识共享署名-相同方式共享 0 协议授权的图片也被视为公有领域图片。

大多数搜索引擎都允许你按图片许可筛选搜索结果。此外，还有像 Pixabay 和 Unsplash 这样的网站提供免费图片。在网站上使用图片时，务必注意版权和许可问题。
## 什么是 SVG，以及何时应该使用它们？

首先，你需要了解图像的工作原理。常见的图像格式，例如 PNG 和 JPG，都属于栅格格式。这意味着它们本质上是基于像素的，数据记录的是每个像素的颜色值。

栅格图像的一大缺点是放大效果不佳。如果您曾经尝试放大PNG图像，您可能会发现图像会变得像素化或模糊。

SVG 是一种不同类型的图像。SVG 代表可缩放矢量图形。矢量图形基于路径和方程式跟踪数据，从而绘制点、线和曲线。这意味着像 SVG 这样的矢量图形可以缩放到任意大小而不会影响图像质量。

SVG 的一个独特优势在于它能将数据存储在 XML 中。这意味着你可以直接在代码中使用 `<div>``svg`元素，将其作为原始 HTML 代码使用。此外，你还可以通过编程方式更改图像的颜色。

要将笑脸改为红色，请启用交互式编辑器并更改其`fill="yellow"`值`fill="red"`。

```html
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="45" stroke="black" stroke-width="4" fill="yellow" />
  <circle cx="35" cy="40" r="5" fill="black" />
  <circle cx="65" cy="40" r="5" fill="black" />
  <path d="M35 65 Q50 80 65 65" stroke="black" stroke-width="4" fill="transparent" />
</svg>
```

以下是该示例的基本要素：

- 该`svg`元素是整个图形的容器。它定义了所有形状出现的空间。所有你想用 SVG 绘制的内容，例如圆形、线条或路径，都放在该`svg`元素内。
- 该`circle`元素用于构成脸部和眼睛。一个大圆构成黄色的脸部，两个小圆构成眼睛。
- 该`path`元素用于绘制微​​笑。它能勾勒出嘴部的曲线。
- 每个 SVG 元素都有属性来控制其外观和在绘图区域中的位置。

以下是一些示例。要更改任何示例的颜色，请将属性值更新`fill`为任何已命名的颜色，例如`red`、`green`、`blue`、`yellow`等。

```html
<!-- Star Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="gold" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2L14.9 8.6L22 9.3L17 14.1L18.3 21.2L12 17.8L5.7 21.2L7 14.1L2 9.3L9.1 8.6L12 2Z"/>
</svg>

<!-- Heart Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="crimson" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 6 4 4 6.5 4C8 4 9.5 4.8 10.5 6.09C11.5 4.8 13 4 14.5 4C17 4 19 6 19 8.5C19 12.28 15.6 15.36 10.45 20.04L12 21.35Z"/>
</svg>

<!-- Checkmark Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="green" xmlns="http://www.w3.org/2000/svg">
  <path d="M20.29 5.71L9 17L3.71 11.71L5.12 10.29L9 14.17L18.88 4.29L20.29 5.71Z"/>
</svg>
```

那么，什么时候应该使用 SVG 呢？图标就是一个很好的例子。如果您想创建自定义项目符号，或者在链接中添加图标来代表社交媒体平台，使用 SVG 是最佳选择。最受欢迎的图标库之一 Font Awesome 就使用 SVG 图像来制作图标。SVG 也非常适合用于网页徽标，因为它们可以完美缩放。它们允许您将布局调整为所需的任何响应式设计。下次当您本地有 SVG 文件时，不妨尝试用文本编辑器打开它并修改代码。
# 语义化HTML
## 为什么你应该关注语义化 HTML？

语义是指语言中词语或短语的含义。HTML 也是一种语言，其中的元素也具有各自的语义。实际上，你可以把 HTML 文档想象成一个文本文档。就像文本文档一样，HTML 文档中也可能包含标题、图像、粗体文本和其他格式。

元素的语义含义指的是该元素所传达的特定信息。`p`例如，一个元素的语义含义就是一段文本：

```html
<p>
  Let me tell you about my fantastic holiday in Paris.
  I saw the impressive Eiffel Tower up close!
</p>
```

大多数元素都具有语义意义。该`div`元素是极少数没有语义意义的元素之一。但这为什么重要呢？

首先，使用规范的语义化 HTML 能确保屏幕阅读器等辅助技术用户获得最佳体验。此外，语义化 HTML 还能提升您的搜索排名。这被称为搜索引擎优化，或简称 SEO。

最后，正确使用语义元素可以提升您的开发体验。您无需在大量开发代码中费力查找导航栏，可以`nav`直接编辑元素并清楚地了解更改的内容。在本节中，您将深入了解这些主题、如何使用语义元素以及语义化 HTML 的重要性。
## 为什么拥有良好的组织结构层级很重要？

创建结构层级最重要的方面是正确使用标题元素。标题元素编号为`<h1>`、`<h2>`、`<h3>`等等。这些数字代表该元素的标题级别。

就像文本文件一样，标题的顺序也应该正确。`h1`元素就是你的顶级标题。页面上通常只会有一个顶级标题，而且它通常应该位于所有内容之前。

你的`h2`元素就是你的副标题。它应该始终位于你的标题之后`h1`，并且可以位于一些介绍性文字之后。与`h1`元素不同，你可以`h2`在页面上放置多个元素。你通常会这样做来区分不同的内容部分。

按照这个模式，你的`h3``<head>` 元素应该始终位于 ` `h2`<head>` 元素之后。也就是说，你永远不应该直接从 `<head>` 跳到 ` `h1`<head> `h3``。但是，你可以在同一层级拥有多个 `<head>` 元素。例如，以下代码是正确的：

```html
<section>
  <h1>freeCodeCamp</h1>
  <h2>Learn Front-End Development</h2>
  <h2>Learn Back-End Development</h2>
</section>
```

但这段代码不正确，因为`h3`位于 之前`h2`。

将元素移到`h2`上方，`h3`使其语义正确。要与代码交互，您需要启用交互式编辑器。

```html
<section>
  <h1>freeCodeCamp</h1>
  <h3>Introduction to HTML</h3>
  <h2>Learn Frontend Development</h2>
</section>
```

由于其样式特性，人们可能会倾向于使用特定的标题元素，例如`h1`用于大文本：

```html
<article>
  <p>
    Here is some
    <h1>Large Text</h1>
  </p>
</article>
```

相反，您应该为文档结构选择合适的元素，并使用 CSS 来实现您想要的样式。

使用正确的层级结构对于无障碍访问至关重要。屏幕阅读器等辅助技术依赖于网页结构来确定如何解析网页并将其朗读给用户。如果`h3`在 `<div>` 元素后使用 `<div>` 元素，`h1`屏幕阅读器用户可能会误以为自己不小心跳过了重要内容，因为缺少 `<div>``h2`元素。

合理的网页结构对搜索引擎优化 (SEO) 至关重要。搜索引擎会使用自动化程序解析网页内容，并确定其在搜索结果中的显示位置和时间。如果网页结构混乱，搜索引擎可能无法在相关的搜索结果中获得理想的排名。

最后，根据你的代码结构错误程度，你的 HTML 代码甚至可能在技术上无效。在这种情况下，浏览器只能猜测你的意图。而它猜测的结果可能根本不是你想要的。

正如你今天所学到的，使用正确的页面结构层次有很多好处。在构建新项目时，请牢记这一点。
## 表现型HTML和语义型HTML有什么区别？

展示型 HTML 侧重于内容的外观和样式。在 HTML 的早期，开发者会使用 `<div>` `center`、 `<span> `big`` 和`font` `<div>` 等元素。但在现代 Web 开发中，由于这些元素的局限性以及对可访问性和可维护性的负面影响，不应再使用这些元素。

许多用于展示的 HTML 元素已被弃用，这意味着它们已经过时，不再推荐使用。现在有更好的方法可以达到相同的效果。不过，了解这些方法的存在仍然很有帮助，所以我们来看一些例子。

该`font`元素已弃用，用于设置文本的字体大小和颜色。以下是一个该`font`元素的示例。

启用交互式编辑器，并将字号从 5 改为 7，即可看到字体增大。

```html
<font size="5" color="blue">This text is blue and large.</font>
```

此示例将文本颜色设置为  `bluecolor`，大小设置为 `size`。`color`属性`5`的值范围`size`为 `0``1`到 `1` `7`，其中 ` `1`0` 为最小值，` `7`1` 为最大值。`3`如果您未显式设置 `color` 值，则默认值为 `0`。

虽然这个元素仍然有效，但你不应该使用它，因为字体大小和颜色应该始终在 CSS 中设置，而不是在 HTML 中设置。

该`center`元素是另一个已弃用的元素，用于在其容器内水平居中显示内容。以下是一个包`center`​​含文本和段落元素的元素示例。

启用交互式编辑器，并`center`在其周围添加标签，`<p>`Another example text.</p>`使其在页面上居中显示。

```html
<center>
  This text is centered.
  <p>HTML is awesome.</p>
</center>

<p>Another example text.</p>
```

接下来是 `big`元素。这是另一个已弃用的 HTML 展示型元素，它会使包含的文本比周围的文本高一级。这里有一个示例，定义了一个包含两部分的段落。

启用交互式编辑器，并`big`在文本周围添加标签`Some other text`，然后在预览窗口中查看更改。

```html
<p>
  This text has a normal font size.
  <big>This text is larger.</big>
  Some other text.
</p>
```

请记住，字体大小应该始终使用 CSS 设置，因此在现代 HTML 中不应使用此元素。

以上是一些用于展示的HTML元素示例。但它们都已被弃用，不再推荐使用。那么应该使用什么替代呢？让我们来看看。

语义化HTML现在是推荐的做法。它描述了元素的内容，因此更容易阅读、理解和维护。

使用语义化的HTML可以让搜索引擎更容易理解你的网站。这也有助于提高网站的可访问性，因为屏幕阅读器需要语义信息来描述网页内容。

语义化 HTML 元素的示例包括：

- `header`用于定义文档或章节标题的元素。
- 导航部分元素，`nav`用于包含导航链接的部分。
- `section`用于对相关信息进行分组的元素。
- `figure`用于插图和图表的元素。

`header`这是一个包含导航部分元素的元素示例。

启用交互式编辑器，并`<a href="#">Products</a>`在其中添加内容`nav`，然后在预览窗口中查看更改。

```html
<header>
  <nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <!--Add the products link here-->

    <a href="#">Contact</a>
  </nav>
</header>
```

语义元素在 HTML 结构中清晰地展现了其用途。HTML 中有很多不同的语义元素，您一定能找到适合您项目需求的元素。

做得好！现在你明白表现型 HTML 和语义型 HTML 的区别了：语义型 HTML 描述内容，而表现型 HTML 则侧重于外观。
## 何时应该使用强调元素而不是习语文本元素？

这些元素与 HTML 的展示性和语义性概念密切相关。惯用文本元素 `<img> `i`` 最初用于展示效果，以斜体显示文本。但现在，它经常用于突出显示不同的语气或语气、外语习语、技术术语和想法。

以下是官方 HTML 规范中的一个示例，使用该`i`元素显示法语习语。

```html
<p>There is a certain <i lang="fr">je ne sais quoi</i> in the air.</p>
```

`lang`标签内的属性用于`<i>`指定内容的语言。在本例中，语言为法语。该`i`元素并不表示文本是否重要，它只是表明该文本与周围的文本有所不同。

如果您确实需要强调文本的重要性，可以使用类似的语义元素，称为强调元素`em`。如果您需要提供更多上下文信息，通常建议使用此元素。您应该将此元素用于需要与周围文本进行特殊强调的文本部分。它通常仅限于几个词，因为它可能会改变句子的含义。

这是段落中强调元素的一个例子。

```html
<p>
  Never give up on <em>your</em> dreams.
</p>
```

你可以看到这句话`Never give up on your dreams`。注意，这个词`your`会被强调，因为它位于这个元素内。在浏览器中，你会看到这个词`your`是斜体字，以告诉读者这是句子中的一个重要词。

即使文本位于习语文本元素内时看起来相同，语义强调元素也会在幕后传达其含义和重要性。

需要注意的是，这些元素不应仅用于装饰目的。如果您需要将文本显示为斜体，但该文本在段落中没有特殊用途、样式或含义，则应使用 CSS。
## 何时应该使用“强力”元素而不是“吸引注意力”元素？

“突出显示”元素（ `b`）通常用于突出显示摘要中的关键词或评论中的产品名称。通常，浏览器会将此文本显示为粗体。以下示例展示了如何使用该`b`元素突出显示此评论中的产品名称：

```html
<p>
  We tested several products, including the <b>SuperSound 3000</b> for audio
  quality, the <b>QuickCharge Pro</b> for fast charging, and the
  <b>EcoClean Vacuum</b> for cleaning. The first two performed well, but the
  <b>EcoClean Vacuum</b> did not meet expectations.
</p>
```

浏览器会将这些文本部分显示为粗体。这种视觉强调能够吸引读者注意产品名称。

如果您需要强调文本的重要性，则应该使用 `strong`元素而不是 `<b>`元素。

`strong` 是一个语义化的 HTML 元素，用于突出显示关键或紧急的文本。例如，该`strong`元素用于标记一条非常重要的警告，告知顾客可能对某种产品产生过敏反应：

```html
<p>
  <strong>Warning:</strong> This product may cause allergic reactions.
</p>
```

这一`strong`元素传达了紧迫感。

从视觉上看，两者非常相似，因为它们默认都是粗体显示。但它们的含义却截然不同。“强调”元素只是吸引人们对文本的注意力，并不表示其重要性，而“突出显示”`strong`元素的作用则远不止于此。它传达了一种重要性或紧迫感。这就是它们的主要区别。

要从中选择，请考虑文本的目的及其在周围内容中的重要性。
## 什么是描述列表？何时应该使用它们？

描述列表非常适合以有条理且易于阅读的格式呈现术语和定义，就像词汇表或真正的词典一样，您可以在其中找到单词及其相应的定义。

这是一个 HTML 描述列表示例，其中包含两个术语及其对应的详细信息。

启用交互式编辑器，然后尝试取消注释代码，即可在预览窗口中看到新的详细信息项。

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
  <!-- <dt>JS</dt>
  <dd>JavaScript</dd> -->
</dl>
```

在这种情况下，术语指的是 HTML 和 CSS 这两个缩写词，而详细信息则是它们的完整解释。详细信息也可以是术语的定义或其他相关信息。

你需要三个 HTML 元素来定义一个描述列表。首先是描述列表元素，即 `<description>` `dl`，它是整个列表的容器。你可以在示例中看到它包裹着描述列表的所有其他元素。

然后，每个术语对应一个描述元素`dt`。在本例中，描述列表包含两个术语：HTML 和 CSS，因此它有两个这样的元素。

最后，每个术语后面都会有一个描述详情元素，`dd`用于显示与该术语相关的描述或详细信息。在本例中，它们分别是超文本标记语言 (Hypertext Markup Language) 和层叠样式表 (Cascading Style Sheets)。

在浏览器中，您会看到每个术语及其对应的描述。默认情况下，描述会略微向右缩进，以便在视觉上加以区分。

但描述列表并不局限于术语和定义，它们的功能远不止于此。例如，这里有一个包含两种原料的食谱。

启用交互式编辑器，然后尝试取消注释代码，即可在预览窗口中看到新的详细信息项。

```html
<dl>
  <dt>Flour</dt>
  <dd>2 cups</dd>
  <dt>Sugar</dt>
  <dd>1/2 cup</dd>
  <!-- <dt>Vegetable Oil</dt>
  <dd>2 tablespoons</dd> -->
</dl>
```

整个描述列表位于一个描述列表元素内。第一个成分（`Flour`）位于一个描述术语元素内。然后，您可以查看该成分所需的用量：`2 cups`。这位于紧随其对应成分之后的描述详情元素内。

同样的结构也适用于其他情况`Sugar`。在本例中，食谱只有两种配料，但如果配料更多，则可以在整个描述列表中重复使用相同的结构。

在浏览器中，你会看到配料列在左侧，计量单位缩进以在视觉上将它们分开。

描述列表的其他用途包括产品规格、常见问题解答、联系信息和元数据。本质上，当您有两个以键值对形式呈现的相关信息时，其中一个作为标签（键），另一个作为附加相关信息（值），就可以使用描述列表。
## HTML中块级引用和行内引用是如何工作的？

在 HTML 中，使用带引号的元素来区分引用的文本和周围的内容。这使得引用的文本格式易于识别。

您应该使用块引用元素来表示从其他来源引用的内容。它主要用于较长的引用。如果引用的来源包含地址，您可以使用 `<source>``cite`属性进行引用。此属性的值必须是有效的 URL。以下是块引用元素中的引用示例：

```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
</blockquote>
```

此元素有一个`cite`属性。该属性的值`cite`是来源的 URL。虽然此属性不会改变引用块的显示方式，但它对于向屏幕阅读器和搜索引擎提供更多关于引用的信息非常有用。在浏览器中，您会看到文本略微缩进。

如果你想在引用块的开头和结尾加上引号，可能需要在文本中显式地添加引号。你可以像我刚才那样直接在引用块元素内输入文本，也可以将其包裹在一个或多个段落元素中。当文本包含多个段落，但你想将它们保留在同一个引用块内时，这种方法非常有用。以下是一个包​​含四个段落的示例：

```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  <p>Build your projects. Show them to your friends. Build projects for your friends.</p>
  <p>Build your network. Help the people you meet along the way. What goes around comes around. You'll get what's coming to you.</p>   
  <p>It is not too late. Life is long.</p>
  <p>You will look back on this moment years from now and be glad you made a move.</p>
</blockquote>
```

所有段落都包含在同一个块引用元素中，因此它们属于同一条引用。您可以看到该元素有一个`cite`属性，其中包含来源的 URL。在浏览器中，您会看到这四个段落彼此对齐，但相对于它们的容器缩进。

目前我一直使用`cite`属性来标注引文来源，但该属性实际上并不会向用户显示来源。它只是在后台运行。

如果您想以视觉方式标注来源，可以`cite`在引用块元素之外添加一个引用元素 `<citation>`。这与`cite`属性不同。引用元素是一个 HTML 元素，可用于标记引用作品的标题，例如书籍文章、歌曲、电影、网站或研究论文。以下是一个示例：

```html
<div>
  <blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?
  </blockquote>
  <p>—Quincy Larson, <cite>How to Learn to Code and Get a Developer Job [Full Book].</cite></p>
</div>
```

引用块元素包含引用的文本。在该元素下方，您可以看到一个段落元素，其中包含作者姓名，段落元素后跟一个引用元素。引用元素包含引文出处的书籍标题。

如果你打开浏览器，就能清楚地看到来源，并发现这句话出自昆西·拉森（Quincy Larson）所著的一本书。这本书的书名是`How to Learn to Code and Get a Developer Job`……

对于来自其他来源的长篇引用，您应该使用这样的块引用。但有时您可能只需要引用较长段落中的几个词。

这正是行内引用元素的作用。它用于引用其他来源的简短文本。大多数现代浏览器会在使用此元素时自动为行内引用添加引号。例如：

```html
<p>
  As Quincy Larson said,
  <q cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Momentum is everything.
  </q>
</p>
```

您可以看到一个包含文本的段落元素。部分文本是行内引用，因为它位于行内引用元素内。您还可以添加一个`cite`属性来注明文本来源。

这与使用块引用元素的方式完全相同。视觉上不会有任何变化，但会为屏幕阅读器和搜索引擎提供更多关于引用的信息。

在浏览器中，你会看到引用的文本是段落的一部分，并且被引号括起来。大多数现代浏览器会自动添加这些引号。

块引用和行内引用有什么区别？你应该对来自其他来源的较长引用使用块引用，对来自其他来源的较短引用（这些引用应该成为现有段落的一部分）使用行内引用。
## 如何在HTML中显示缩写？

缩写是单词或短语的缩短形式。例如，“Dr”后面加句点，就是“doctor”（医生）的缩写。

缩写有两种常见形式：首字母缩略词和首字母缩写词。

首字母缩略词是由一个短语的首字母组成的单词，每个字母代表该短语中某个单词的首字母。

GUI 是一个首字母缩写词的例子。它代表图形用户界面（Graphical User Interface）。取 G、U 和 I 这三个单词的首字母，就得到了 GUI 这个缩写词。

首字母缩写词是由短语的首字母组成的，每个字母代表该短语中某个单词的首字母。

例如，HTML 是一个首字母缩写词；它代表超文本标记语言，发音方式是将每个字母 H、T、M、L 拼写出来。

首字母缩略词和缩写词都是缩写的一种形式。区别在于，首字母缩略词像单词一样发音，而缩写词则像单个字母一样发音。

它们对于撰写更简洁的文本非常有帮助，尤其是在特定语境下它们是众所周知且易于理解的词汇时。

如果您需要在 HTML 中显示缩写词（例如首字母缩略词或缩写），`<abbreviation>` 元素正是您所需要的。首次使用时，您应该始终解释其完整含义。之后，您可以使用 `<abbreviation>` 元素突出显示这些缩写词并提供更多详细信息。

这里有一个示例，其中包含以下句子`HTML is the foundation of the web`：

```html
<p><abbr>HTML</abbr> is the foundation of the web.</p>
```

缩写词的 HTML 代码位于一个缩写元素内。在浏览器中，你会发现实际上并没有什么变化，它看起来仍然像普通文本。缩写元素在后台提供了有用的上下文信息，但用户看到的仍然是普通文本。

如果你想帮助用户理解这个首字母缩写词的含义，你可以使用`title`属性显示它的完整形式。

该`title`属性是可选的，但如果您决定包含它，则它必须是缩写、首字母缩略词或首字母缩写词的人类可读描述。

我们沿用之前的例子，但这次加上`title`属性。它将是`HyperText Markup Language`首字母缩写词的展开形式：

```html
<p><abbr title="HyperText Markup Language">HTML</abbr> is the foundation of the web.</p>
```

通常情况下，添加此属性后，缩写元素的样式会发生变化。具体样式取决于浏览器。某些浏览器可能会显示虚线下划线，而其他浏览器可能会将内容转换为小型大写字母。当用户将鼠标悬停在缩写上时，会以工具提示的形式显示完整形式。

虽然你不一定需要在网页上的每个缩写词中使用缩写元素，但建议对那些可能不明确或需要更多上下文的缩写词使用缩写元素。

你应该运用最佳判断力，在信息和表达方式之间找到合适的平衡点，避免文本过于冗杂，同时保持清晰简洁。
## 如何在HTML中显示地址？

联系地址元素用于表示网页上某个部分的联系信息。该`address`元素用途广泛，可用于企业页面、作者页面、个人网站等。

在构建网站的联系部分时，应该使用语义`address`元素而不是像 这样的通用元素`div`。

`address`以下是使用该元素创建公司联系页面的示例：

```html
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

在这个例子中，包含了公司名称、实际地址、电话号码和电子邮件地址等信息。对于实际地址，使用了换行符 `<br>``br`来区分街道名称、城市和国家/地区。

对于电话号码，我们使用了一个锚元素，并将`href`值设置为电话号码。`tel:+`该`href`属性的值会创建一个可点击的链接，以便在某些支持的设备上发起电话呼叫。

对于电子邮件地址，使用了另一个锚元素，其`href`值设置为`mailto`链接。HTML`mailto`文档中使用链接，使用户能够在他们首选的电子邮件客户端中打开新邮件。

使用链接的缺点之一`mailto`是用户常常将其视为垃圾邮件。不幸的是，许多垃圾邮件发送者会利用这种方式向用户发送电子邮件。因此，在使用链接时请务必注意这一点。
## 如何在HTML中显示时间和日期？

该`time`元素用于表示特定的时间点。

`time`以下是使用该元素表示两点钟，即晚上八点钟的示例。

```html
<p>The reservations are for <time datetime="20:00">20:00 </time></p>
```

该`datetime`属性用于将日期和时间转换为机器可读格式。

这很重要，因为它有助于搜索引擎结果，并帮助浏览器更有效地处理日期和时间信息。

该属性的值`datetime`必须是有效的年份、有效的月份、有效的时间、本地日期、全球日期或有效的持续时间字符串。

以下是使用时间元素表示特定日期的另一个例子：

```html
<p>
  The graduation will be on <time datetime="2024-06-15T15:00">June 15</time>
</p>
```

该`datetime`属性值采用 ISO 8601 格式。ISO 8601 是表示日期和时间的国际标准。

该值的第一部分是年、月、日。值中的大写字母 T 是日期和时间之间的分隔符。

一千五百时就是下午三点。

当您需要表示事件、发布日期或约会时，最好使用该`time`元素。
## 如何在HTML中显示数学方程式和化学式？

上标元素用于将一段文本显示为上标。上标是指显示在文本行上方的符号或字母。

以下示例使用上标元素来表示指数（要查看预览，请启用交互式编辑器）：

```html
<p>2<sup>2</sup> (2 squared) is 4.</p>
```

在这个例子中，数字 2 被包裹在标签内`sup`，以表示段落内的上标。在预览窗口中，你会看到第二个数字 2 比第一个数字 2 更小，位置也略高一些。

上标元素的常见用途包括表示指数、上标字母和序数。以下示例展示了如何使用上标元素表示上标字母（要查看预览，请启用交互式编辑器）：

```html
<p>
  Monseigneur is often written as <strong>M<sup>gr</sup></strong>.
</p>
```

上标字母是指以右上角标形式书写的字母，通常用于表示缩写。在本例中，字母“a”`g`和`r`“b”被包裹在上标标签内，以展示缩写形式。

需要注意的是，上标元素只能用于排版目的。如果您想为一段文本设置更高的基线，则应该使用 CSS 而不是上标元素。

要在 HTML 中表示化学方程式，可以使用下标元素。该元素使用下标来降低基线，从而使用更小的文本显示方程式。

以下示例展示了如何使用下标元素来显示二氧化碳的化学式（要查看预览，请启用交互式编辑器）：

```html
<p>CO<sub>2</sub></p>
```

数字 2 被包裹在`sub`标签内，是为了说明该字符应该是下标。

下标元素的常见用途包括化学式、脚注和变量下标。
## 如何在HTML中表示计算机代码？

行内代码元素用于在文本中插入简短的代码片段。该代码元素的常见应用场景包括技术文章和文档页面。

`code`以下是使用该元素显示 CSS 代码片段的示例：

```html
<p>
  To set the text color to blue in CSS, use the following code:
  <code>color: blue;</code>
</p>
```

在这个例子中，CSS`color`属性用于将文本颜色设置为`blue`。通过将此代码片段包裹在`<code>`标签内，可以告诉浏览器该文本是一段行内代码。

浏览器将对元素内的内容应用默认样式`code`。默认样式为等宽字体。

该`code`元素用于表示单行代码。如果要表示多行代码，则需要将该`code`元素放置在预格式化文本元素内。

预格式化文本元素用于表示预格式化文本。以下示例展示了如何使用预格式化文本元素来显示 CSS 声明：

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

在浏览器中，你会看到代码向右缩进了几格。如果你更改代码示例中的缩进，屏幕上的缩进也会随之改变。

当需要在 HTML 文档中包含代码示例时，应该使用 `<code>`元素来显示简短的内联示例。

如果需要显示更长的代码片段，则需要使用 `<code>``pre`和 `<code> `code`` 元素。
## U、S 和 Ruby 元素分别用于什么用途，它们是如何工作的？

未明确标注的注释元素（`u`简称元素）用于表示应用了非文本注释的行内文本。

以下是一个使用该`u`元素突出显示各种拼写错误的示例：

```html
<p>
  You can use the unarticulated annotation element to highlight
  <u>inccccort</u> <u>spling</u> <u>issses</u>.
</p>
```

示例中，单词“ `incorrect`, `spelling`, 和”`issues`拼写错误。该元素的默认样式`u`是在文本下方添加黑色下划线。

在 HTML4 中，`<textarea>``u`元素用于样式设置。但在 HTML5 中，`<textarea>``u`元素只能用于指示文本应用了非文本注释。

如果你想给一段文字添加下划线，应该使用 CSS 而不是 HTML。

删除线元素（`s`简称删除线元素）用于表示文本不再准确或相关。以下示例展示了如何使用删除线`s`元素来表示活动已取消：

```html
<p><s>Tomorrow's hike will be meeting at noon.</s></p>

<p>Due to unforeseen weather conditions, the hike has been canceled.</p>
```

在这个例子中，第一句话被划掉了，因为徒步旅行由于天气原因取消了。

该`s`元素绝不应仅用于显示文档的更改。在这种情况下，更合适的元素应该是删除文本元素和插入文本元素。

该`ruby`元素表示显示在正文上方或下方的短文本。它通常用于显示东亚字符的发音。以下是`ruby`MDN 网页文档中的元素示例：

```html
<ruby> 明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp> </ruby>
```

该`rp`元素（或 Ruby 回退括号元素）用作不支持显示 Ruby 注解的浏览器的回退方案。

该`rt`元素（或称红宝石文本元素）用于指示红宝石注释的文本。此文本通常用于东亚排版中的发音或翻译说明。

虽然该`ruby`元素也可用于其他类型的注释，但最常见的用途是东亚排版。

## HTML中的表单、标签和输入框是如何工作的？

HTML 中的 `<form>`元素`form`用于收集用户信息，例如姓名和电子邮件地址。以下是一个 ` `form`<form>` 元素的示例：

```html
<form action="url-goes-here">
  <!-- input elements go here -->
</form>
```

该`action`属性指定表单数据提交后将发送到哪里。要收集特定信息，例如姓名和电子邮件地址，您可以使用 ` `input`<form>` 元素。以下是使用 `<form>` 元素的示例`input`。

启用交互式编辑器，并`input`在预览窗口中输入您的姓名，即可与元素进行交互。

```html
<form action="">
  <input type="text" />
</form>
```

`input``<input>` 元素是空元素，没有结束标签。`type``type`属性定义了用户输入的数据类型。在本例中，数据为纯文本。要为输入框添加标签，可以使用 `<label>`元素。以下是一个使用 ` <label>` 元素并添加文本的`label`示例。`label``Full Name:`

点击`Full Name:`预览窗口中的文本，即可看到输入内容变为焦点。要与示例进行交互，您需要启用交互式编辑器。

```html
<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
```

通过将 `<a>` 元素嵌套在 `<div>` 元素`input`内，可以在 `<a> ` 和 `<div>`字段`label`之间建立隐式关联。“隐式”指的是无需显式声明或使用额外属性或元素定义即可理解或推断出的内容。要显式地将 `<a>`与 `<div>`关联起来，可以使用 `@ email` 属性。以下示例展示了如何使用`@email` 属性来表示电子邮件地址标签。`label``input``label``input``for``for`

`input`在预览窗口中输入一个虚拟邮箱地址（例如@example.com）来与元素进行交互`jane@example.com`。要与示例进行交互，您需要启用交互式编辑器。

```html
<form action="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" />
</form>
```

`for`使用显式关联时，` type` 和`type` 属性的值`id`必须相同。在本例中，它们的值都设置为 `true` `email`。`email`输入框中的 `type` 属性提供对格式正确的电子邮件地址的基本验证。如果您想向用户显示有关预期输入的额外提示，可以使用 ` `placeholder`type` 属性。以下是在电子邮件输入框中使用 `type` 属性的示例`placeholder`。

启用交互式编辑器，点击电子邮件输入框并开始输入电子邮件，您就会看到占位符文本消失。

```html
<form action="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" placeholder="example@email.com" />
</form>
```

对于占位符文本，您需要提供简短明了的文字，以说明您期望用户输入的数据格式和类型。在本例中，占位符文本“”`example@email.com`向用户表明他们必须输入格式正确的电子邮件地址。
## 按钮有哪些类型，以及何时应该使用它们？

该`button`元素用于在激活时执行特定操作。以下是一个`button`按钮文本为“”的元素示例`Start Game`。

```html
<button>Start Game</button>
```

该元素的其他用途`button`包括提交表单、显示模态框或切换侧边菜单的打开和关闭。该`button`元素有一个`type`属性，用于控制按钮激活时的行为。该`type`属性的第一个可能值是type。以下是一个使用 type为type 且 text 为 text 的元素`button`示例：`button``button``Show Alert`

```html
<button type="button">Show Alert</button>
```

默认情况下，按钮激活后不会执行任何操作。但是，您可以添加一些 JavaScript 代码，使按钮具有交互功能，例如在本例中显示一个警告框。

点击按钮`Show Alert`，屏幕上会弹出提示信息。要与示例进行交互，您需要启用交互式编辑器。

**注意**：本交互式示例使用了 JavaScript，但您无需担心理解 JavaScript 代码。您将在后续模块中学习 JavaScript。

```html
<button type="button">Show Alert</button>
<script src="index.js"></script>
```

```js
const btn = document.querySelector("button");
btn.addEventListener("click", () => alert("You clicked on the alert button"));
```

该属性的另一个可能值`type`是value。以下是使用具有该类型的元素`submit`的示例。`button``submit`

```html
<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="submit">Submit form</button>
</form>
```

在这个`form`元素内部，包含一个用于输入用户电子邮件地址的元素。当用户点击提交按钮时，他们的数据将被发送到服务器进行处理。该属性的第三个可能值是“已重置”和“已提交”按钮`label`。以下是一个包​​含重置按钮和提交按钮的元素示例。`input``type``reset``form`

启用交互式编辑器，并在预览窗口中输入一个虚假的电子邮件地址，然后点击重置按钮，即可看到该电子邮件地址从输入框中消失。

```html
<form action="">
  <label for="email">Email address:</label>
  <input type="email" id="email" name="email" />
  <button type="reset">Reset form</button>
  <button type="submit">Submit form</button>
</form>
```

在这个修改后的示例中，我们使用 `<a>``label`和`input``<input>` 元素来收集用户的电子邮件地址。当用户点击重置按钮时，所有输入的数据都会被清除。需要注意的是，重置按钮通常不是最佳选择，因为它们可能导致用户意外重置数据。此外，表单中过多的按钮也会使用户界面显得杂乱。

在 HTML 中创建按钮的另一种方法是使用 `<button> `input`` 元素。`<button> `input`` 元素还有一个 ` `type`value` 属性，其值可以是`submit``<button>` `reset`、`<button>` 和 ` <button>`。以下是一个将 ` value` 设置为`<button>` 的`button`示例：`input``type``button`

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

该`value`属性用于显示按钮文本。那么，`<button>``input`和` `button`<a>` 元素之间有什么区别呢？`input``<button>` 元素是空元素，这意味着它们不能包含子节点（例如文本），只能包含一个开始标签。另一方面，`<a>``button`元素提供了更大的灵活性，因为您可以在其中嵌套文本、图像和图标。
## HTML 表单中的客户端表单验证是什么？有哪些示例？

当用户在您的网站上填写表单时，务必确保他们以正确的格式填写所有必要信息。HTML 表单控件（例如输入框）内置了许多验证功能，您可以利用这些功能来检查无效数据。这将有助于确保用户在信息提交并被服务器处理之前修正这些错误。

“客户端”一词指的是在用户计算机或设备上发生的一切，例如用户直接交互的网站或应用程序部分。这包括布局、设计和任何交互功能。

“服务器端”一词指的是在托管网站或应用程序的服务器、计算机或系统上发生的一切活动。这包括处理数据、运行应用程序以及处理来自用户设备的请求。

虽然客户端验证很重要，但为了增强安全性，您还需要服务器端验证。恶意用户可以绕过客户端检查，因此强大的服务器端措施至关重要。您将在后续模块中了解更多相关内容。现在，让我们来看一些客户端表单验证的示例。

内置表单验证的一个常见例子是`required`在输入框中使用属性。该`required`属性指定用户需要填写表单的相应部分才能提交。以下是`required`在电子邮件输入框中使用该属性的示例。

点击按钮`Submit Form`而不提供电子邮件地址，您将看到一条消息弹出，提示您填写该字段。

```html
<form action="">
  <label for="email">Email Address (Required field):</label>
  <input required type="email" name="email" id="email" />
  <button type="submit">Submit Form</button>
</form>
```

每个浏览器都有自己显示此警告信息的样式。

使用电子邮件输入框的另一个优点是，电子邮件输入框具有一些基本的验证功能，以确保电子邮件地址格式正确。例如，如果您输入一些随机词语并点击提交，浏览器会弹出提示，指出`@`缺少某个标识。

在邮箱地址栏中输入地址`abc`，然后点击提交按钮。此时应该会弹出一条消息，提示该邮箱地址无效。

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

`min``minlength`和 ` `maxlength`max` 属性用于设置电子邮件输入框的最小和最大字符长度。如果未设置最小长度或超过最大字符长度，浏览器将显示警告信息。
## 不同的形态状态有哪些？它们为什么重要？

在 HTML 中，表单控件（如输入框）可以处于不同的阶段或状态，例如`focused`状态 1、`readonly`状态 2 或`disabled`状态 3。

第一种状态将被视为初始`default`状态。电子邮件地址输入框的默认状态是空白输入框。这是电子邮件输入框首次在页面上呈现时的样子。

```html
<input type="email" name="email" id="email" />
```

当用户点击表单控件或使用键盘上的 Tab 键选中它时，该控件就处于选中状态`focused`。在选中状态下`focused`，大多数浏览器会在输入框周围显示蓝色高亮边框。您也可以在 CSS 中添加其他样式。

点击预览窗口的任意空白区域，然后按下快捷`tab`键即可查看焦点状态。要查看预览，您需要启用交互式编辑器。

```html
<input type="email" name="email" id="email" />
```

表单的另一种状态是“`disabled`无法聚焦或激活”状态。此状态会向用户显示某个输入框无法获得焦点或激活。

启用交互式编辑器，然后尝试点击电子邮件输入框，你会发现它将不再获得焦点。

```html
<input disabled type="email" name="email" id="email" />
```

与状态类似`focused`，您可以使用 CSS 为状态添加其他样式`disabled`。

表单的另一种状态是只读`readonly`状态。在这种状态下，表单控件（例如输入框）对用户不可编辑。以下示例演示如何将电子邮件输入框设置为只读。该`value`属性用于设置输入框内显示的值。

`example@email.com`启用交互式编辑器，尝试在预览窗口中编辑当前值，您会发现这是不可能的。

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
# 表格
## HTML表格有哪些用途，以及不应该用于哪些用途？

如今HTML表格的使用频率远不如以前了。但是，作为前端开发人员，你仍然应该熟悉它们。早在20世纪90年代，表格就是开发人员在浏览器中展示数据的最早方式之一。

以下是一个用于从美国劳工统计局生成表格的代码示例：

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

如您所见，有一个主`table`元素，其`id`值为`quickfacts`。在该主元素内部，表格包含一个桌头元素、`thead`一个桌身元素`tbody`和一个桌尾元素`tfoot`。

表格的头部、主体和尾部元素都可以包含若干行表格数据`tr`。每一行表格数据都可以包含一个表头，`th`用于标记该行中的数据。此外，每一行表格数据还可以包含若干个单独的数据单元格，称为表格数据`td`。

现在，HTML元素确实很多。但别被吓到——它们遵循简单的层级结构。

以下是我们能够创建的包含所有这些元素的最简单的表格：

```html
<table>
  <thead>
    <tr>
      <th>The title of this table</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First Row</th>
      <td>
        First Data Cell
      </td>
    </tr>
    <tr>
      <th>Second Row</th>
      <td>
        Second Data Cell
      </td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th>The footer of this table, which might contain date of publication, author credits, or other meta information.</th>
    </tr>
  </tfoot>
</table>
```

所以正如你所看到的，数据本身总是位于一个元素内`tr`——而该`tr`元素内又包含一个`th`带有标题的元素和一个`td`带有数据的元素。

有些网站会选择使用`div`s 来构建自己的表格，而不是使用更合适的`table`元素。

虽然可以使用通用`div`元素显示表格数据，但最好还是使用`table`元素。

很多年前，开发者可能会使用 ` `table`<div>` 标签来定位网页上的非数据元素。这从来都不是最佳实践。但你可能仍然会遇到一些代码库，其中仍然像这样使用表格。

如今，开发者们使用 CSS 的 Flexbox 和 Grid 布局来设计页面。freeCodeCamp 将在后续文章中深入讲解这些工具。

目前，只需将 HTML 表格用于其最初的预期用途：显示表格数据。
# 使用HTML工具
## 什么是 HTML 验证器？它如何帮助你调试代码？

HTML 是一种非常宽容的语言——即使你犯了错误，比如忘记添加结束标签，元素仍然会渲染出来。

假设你有一个`h2`缺少结束标签的元素：

```html
<h1>Article Topic</h1>
<h2>Subheading 1 </h2>
<h2>Subheading 2 </h2>

<!-- This h2 does not have a closing tag -->
<h2>Subheading 3
```

即使`h2`没有结束标签，HTML 也能正常渲染。这是因为浏览器使用了一种解析算法，该算法可以处理常见错误，并尽可能按照作者的意图渲染 HTML。

但这有时可能会适得其反。让我们在代码中现有的标题 2 标签下添加几个段落：

```html
<h1>Article Topic</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores, nisi.</p>

<h2>Subheading 1 </h2>
<p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. At, doloremque.</p>

<h2>Subheading 2 </h2>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, placeat.</p>

<!-- This h2 does not have a closing tag -->
<h2>Subheading 3
<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempore, illum.</p>
```

因此，`h2`缺少结束`h2`标签的段落元素会被渲染成标题 2。这就是为什么你需要一个 HTML 验证器。

HTML验证器是一种工具，用于检查您的HTML代码是否符合标准HTML规范。它可以帮助您识别HTML代码中的错误和警告，确保您的网页结构正确并符合Web标准。

使用 HTML 验证器不仅对你和你未来的代码审查有益，而且对任何查看你的代码的人也有益，例如你的队友和开源贡献者。

市面上有很多HTML验证器可供使用。其中最广泛接受的是`w3.org`标记验证服务（Markup Validation Service）。

访问该网站后[`validator.w3.org`](https://validator.w3.org/)，您可以点击按钮`Validate by Direct Input`并粘贴您的 HTML 代码。

点击按钮后`Check`，将显示需要修复的错误列表。

您还可以使用另一个 HTML 验证器[`jsonformatter.org`](https://jsonformatter.org/)。

您可以将 HTML 代码复制粘贴到第一个编辑器中，单击按钮后`Validate`，它会显示代码中的任何错误。
## 如何使用 DOM 检查器和开发者工具调试和构建项目

在开发项目的过程中，您经常会遇到程序无法按预期运行的问题。

程序员通常将问题称为 bug。查找并修复这些 bug 的过程称为调试。

要调试代码，您需要使用浏览器提供的一些工具。

两个重要的工具是 DOM 检查器和开发者工具。

DOM 检查器允许您检查当前页面的 HTML 结构。

DOM 代表文档对象模型。它是一个树状结构，用于表示页面上的元素。您将在后续模块中学习更多关于 DOM 的知识。

开发者工具允许您检查当前页面的 HTML、CSS 和 JavaScript。

我们来看一个 HTML 示例，其中锚元素存在一个小错误：

```html
<a href="https://www.freecodecamp.org/larn/">freeCodeCamp curriculum</a>
```

点击该链接后，将跳转到 404 页面。404 页面是用户尝试访问服务器上不存在的网页时出现的错误页面。

此链接旨在指向 freeCodeCamp 课程。

要查看问题可能出在哪里，您可以使用开发者工具。

要在浏览器中打开开发者工具，您可以右键单击页面并选择`Inspect`。

您也可以`Control Shift I`在PC键盘或`Command Option I`Mac上使用。

在谷歌浏览器中打开开发者工具后，你会看到多个标签页。第一个标签页是页面结构标签`Elements`页。该标签页会显示你当前浏览页面的 HTML 结构。

第二个标签页称为错误显示`Console`标签页。此标签页会显示页面上可能出现的任何错误。

如果遇到失效链接，您可以查看控制台以获取该失效链接的错误信息。失效链接通常会持续显示 404 错误。404 错误表示页面未找到。

这说明问题出在锚元素中的 URL 上。检查该`href`值时，你会发现其中存在拼写错误。

目前控制台显示`/larn`404 错误信息，但正确的 URL 应该是 [`/learn`此处应填写正确的 URL]。链接更正后，即可正常工作。

在整个认证过程中，您将学习更多关于使用开发者工具的知识，但这只是一个简单的示例，说明它如何帮助您调试代码。
# 无障碍
## 什么是无障碍设计？

无障碍设计是指创造所有人都能使用的产品和服务。在网页开发领域，它指的是创建所有人都能理解和使用的网站，包括有视觉、听觉、运动和认知障碍的人士。

可能影响用户在线体验的一些残疾示例包括：

- 失明。
- 低视力。
- 色盲。
- 耳聋。
- 使用键盘、鼠标或触摸屏有困难。
- 注意力障碍
- 内存问题。
- 口语表达或理解能力存在困难。
- 对闪光灯敏感。

以上仅列举了可能影响全球用户的众多情况中的几种。

为了帮助您创建无障碍网站，万维网联盟（W3C）制定了一套国际标准，您可以遵循这些标准，使您的网站对残疾人士更易于访问和使用。

这些标准被称为“Web 内容无障碍指南”（WCAG）。

这些指导原则的设计以四个核心原则为指导，称为**POUR**。

- `P`代表可感知性。用户必须能够感知您呈现的信息。例如，您可以为图像提供替代文本，以便使用屏幕阅读器访问您网站的用户能够理解图像内容。
- `O`代表可操作性。用户必须能够与用户界面进行交互。例如，您可以确保所有功能都可以通过键盘访问，而不仅仅是鼠标。
- `U`“Understandable”代表“易于理解”。用户必须能够理解信息。例如，您可以避免使用复杂的句子，并尽可能使用简单的语言。
- `R`代表稳健性。各种浏览器和其他工具（包括辅助技术）必须能够解读内容。

使用语义化的HTML对于使您的网站与不同的浏览器和辅助技术兼容非常有帮助。

如果你的内容不遵循这些核心原则中的任何一条，那么并非所有人都能使用你的网站。

为了检查您是否正确遵循了这些指南，您可以访问万维网联盟的快速参考手册。手册中提供了全面的标准和技术列表。

无障碍设计对于网站开发至关重要。通过秉持包容性理念进行开发，您可以确保每个人都能访问和使用您的内容，促进平等，并为世界各地的用户创造更好的体验。

## 什么是屏幕阅读器？哪些人使用屏幕阅读器？

屏幕阅读器是一种辅助技术程序，可以帮助盲人和视力障碍者使用电脑和移动设备。

屏幕阅读器不仅仅是盲人和视障人士访问电脑和移动设备的工具。

他们帮助这些人获得教育、工作机会和社交媒体资源。这确保了数字包容性，并增强了他们充分参与社会的能力。

人们普遍误以为屏幕阅读器是文本转语音设备。

然而，文本转语音只是屏幕阅读器的功能之一。有些屏幕阅读器甚至会将文本渲染成盲文输出，而不是语音。

除了文本转语音和盲文输出之外，屏幕阅读器的其他显著功能还包括导航辅助和网页浏览辅助。

屏幕阅读器程序并非仅为盲人和视障人士设计。阅读障碍者和认知障碍人士也使用屏幕阅读器。目前所有主流操作系统都内置了屏幕阅读器。

macOS 和 iOS 都内置了 VoiceOver 功能。在电脑上，您可以按下 键启用它`CMD + F5`。在 iPhone 上，您可以通过“设置”访问它。

Windows 电脑内置了“讲述人”功能。您可以按 键启用它`WIN + CTRL + ENTER`。此外，Windows 电脑还提供了非视觉桌面访问 (NVDA) 和语音作业访问 (JAWS) 服务。NVDA 是免费开源软件，而 JAWS 是付费软件。

Linux 系统有_Orca_用于桌面环境，_Speakup_用于 Linux 终端。

安卓手机内置了 TalkBack 功能。您可以通过依次进入_“设置”>“特殊功能”>“辅助功能”>“TalkBack”来开启它。_

部分安卓设备还内置了Ella和Select to Speak语音助手。

屏幕阅读器用户面临的一大挑战是，许多软件开发人员在设计产品时并没有考虑到屏幕阅读器的友好性和可访问性。

尽管无障碍设计是一个广泛的话题，但每个开发者都需要学习如何让他们的网页软件对盲人和视障人士以及其他残疾人群体无障碍。

这体现了同理心和对包容性的承诺，确保所有用户都能从他们的作品中受益。
## 什么是大字键盘或盲文键盘？哪些人使用它们？

大字键盘和盲文键盘专为视力障碍人士设计。大字键盘（也称大字体键盘）的字母、数字和符号比标准键盘上的更大。这种设计有助于那些难以看清按键上小字的用户。大多数大字键盘还具有更高的对比度和亮度。

MaxiAids品牌生产的大字键盘，按键为黄色，字母、数字和符号均为黑色，字体大而粗体。这对于视力障碍人士来说非常实用。

另一款键盘是黑色大字键盘，按键上印有白色字样。这款键盘也带有背光，用户可以根据不同的光线条件调节亮度。

大字键盘为视力障碍用户提供视觉提示，而盲文键盘则为视力障碍更严重的人（包括盲人）提供完全的触觉体验。

盲文是一种触觉读写系统。它由凸起的点组成，这些点按照特定的图案排列，用来表示字母、数字和标点符号。

盲文键盘利用这种系统，通过手指触摸按键上的图案，帮助用户找到正确的按键。按键上有凸起的圆点，排列成各种图案，代表字母、数字和符号。

有些键盘结合了这两种方法——既有大字体，按键上也印有盲文图案。这对于视力障碍人士和正在学习盲文的人来说都很有帮助。

大字键盘和盲文键盘是帮助视障人士的工具。通过提供替代输入方式，这些辅助技术确保每个人都能融入数字世界。
## 轨迹球、操纵杆和触摸板等替代指点设备是用来做什么的？

替代指点设备是能够有效替代传统鼠标的输入设备。对于残疾人士、前肢残疾人士和行动不便人士而言，这些设备对于提高计算机的易用性至关重要。

常见的替代指点设备包括轨迹球、操纵杆和触摸板。

轨迹球是一种固定式指向设备，它由一个位于球窝内的可移动大球组成。它还包括用于点击和执行其他功能的附加按钮。

与需要移动才能控制光标的传统鼠标不同，轨迹球无需移动。用户可以直接用手指、拇指或手掌操控轨迹球，从而在屏幕上移动光标。

有些传统鼠标顶部或侧面也带有轨迹球。如果您想逐步过渡到轨迹球鼠标，这些鼠标或许是不错的入门选择。

轨迹球减少了用户导航所需的物理移动，因此非常适合行动不便的用户。此外，如果您需要高精度操作且桌面空间有限，轨迹球也比传统鼠标更理想。

操纵杆是一种指向设备，主要用于游戏和某些工业应用，例如机械控制。它由一个可以上下左右旋转的操纵杆组成，通常还包括用于执行各种操作的附加按钮。

操纵杆能够对数字环境中的移动和动作进行精确控制。这使得它们在飞行模拟器、起重机、驾驶游戏以及其他需要精确方向输入的应用中广受欢迎。

由于操纵杆可以进行更大幅度、更精准的动作，因此对手部颤抖和不稳的人很有帮助。

它们还能减轻重复性动作带来的压力和疼痛，因此非常适合关节炎和腕管综合征患者。

触控板是一种扁平的、触控式的设备，内置于笔记本电脑和一些键盘中。用户可以通过在其表面滑动手指来控制屏幕上的光标。

除了用于光标控制的表面外，触摸板还具有模拟传统鼠标操作的按钮，例如右键单击和左键单击。

大多数人认为触控板比鼠标更好，因为它支持多点触控手势，如捏合缩放、双指滚动、点击和三指滑动，从而显著增强了导航体验。

触控板非常适合手臂或手部活动受限的人士，因为使用时前肢几乎始终保持静止。它也适合关节炎和关节疼痛患者，因为他们的手臂活动量不大。
## 屏幕放大镜有什么用途？

屏幕放大镜是一种可以帮助视力低下或其他视力障碍人士更好地访问数字内容和网络的工具。

让我们深入了解这些工具是什么，以及它们在数字内容可访问性方面发挥的作用。

屏幕放大镜的工作原理是放大电脑或移动设备屏幕上的文本、图形和其他元素。许多屏幕放大镜允许用户将显示内容放大 200% 以上。用户随后可以使用鼠标或键盘浏览页面。此外，大多数放大镜还在设置中提供可自定义的缩放比例和其他功能。

屏幕放大镜主要帮助视力障碍人士阅读文本，因为文档或应用程序中的小字体对他们来说可能难以辨认。通过放大文本，他们可以阅读电子邮件、文章和其他内容，而无需费力地用眼。屏幕放大镜还能辅助网页浏览。它们可以帮助用户找到并点击按钮、链接和其他可能难以看清的交互元素。这种可视性的提升确保用户能够轻松浏览网站、填写表格并参与在线活动。

因此，软件开发人员需要确保他们的数字产品能够被视力障碍人士使用。需要考虑的一些因素包括：

- 使用可缩放字体，以便用户可以调整页面大小而不会破坏布局。
- 通过响应式设计，确保用户界面能够适应不同的屏幕尺寸。
- 采用高对比度配色方案和可自定义颜色。
- 实现非粘性且小巧的导航栏，以便用户在使用放大镜时仍然可以看到内容。
- 使用普通的HTML文本，而不是文本图像。
- 在触发该问题的元素旁边直接提供反馈，以及更多功能。

所有主流操作系统都至少内置了一个放大镜：

- macOS 和 iOS 都支持缩放功能。在 macOS 中，您可以依次进入“设置”、“辅助功能”，然后点击“缩放”。启用“使用键盘快捷键缩放”选项即可。
    - _您可以在 iPhone 上通过“设置”>“辅助功能”>“缩放”_来开启此功能。
- 安卓设备有放大功能。要开启此功能，请前往_“设置”>“特殊功能”>“辅助功能”>“放大_”。由于不同设备的设置可能略有不同，您也可以在设置主页搜索“放大”来找到它。
- Windows系统自带放大镜功能。您可以通过依次点击_“设置”>“轻松使用”>“放大镜”_来使用它。
- Linux操作系统中的放大镜名称各不相同，有时是Zoom，有时是Magnifier。

除了操作系统内置的屏幕放大镜之外，一些实用的第三方屏幕放大镜包括：

- 适用于 Windows 的 ZoomText。
- ClaroView 适用于 macOS 和 Windows 系统。
- 适用于 Windows 的 iZoom。
- Zoomify - macOS 屏幕放大镜。
- 适用于 Windows 的 LunarPlus。
- 适用于 macOS 的 Loupe。

## 语音识别软件有哪些用途？

语音识别软件帮助残障人士与电脑和其他数字设备进行交互。让我们来探讨一下什么是语音识别软件，以及它在数字包容中发挥的作用。

在无障碍领域，语音识别工具可以让残障人士通过语音发出指令来执行各种任务，而无需使用键盘和鼠标等传统输入设备。这些任务包括撰写电子邮件和其他文档、上网以及控制智能家居设备。

由于语音识别软件工具消除了人为交互的需要，因此赋予了残疾人士极大的独立性和对自身环境的控制权。

以下人群可能会发现语音识别软件非常有用：

- 视力障碍人士，包括低视力或失明人士。
- 行动不便的人士，例如手部和手臂活动受限，或患有关节炎和腕管综合征等疾病的人士。
- 手部或手臂受伤的康复者。
- 患有认知障碍的人，例如记忆力问题或注意力缺陷障碍。
- 老年人可能觉得使用语音命令更容易。

值得注意的是，语音识别技术的使用者并非只有残障人士。执法机构、游戏玩家、司机和繁忙的专业人士也都在使用语音识别工具。

一些允许用户与计算机交互的语音识别软件包括 macOS/iOS 的 Voice Control、Android 的 Voice Access 以及 Windows 的 Windows Speech Recognition（在最新版本的 Windows 系统中称为 Voice Access）。Nuance 的 Dragon 是一款流行的 Windows 第三方语音识别软件。
## 有哪些常用的无障碍审核工具？

无障碍设计是数字内容中至关重要却又常常被忽视的一个方面。在制作无障碍数字内容时，务必确保其符合无障碍标准。

无障碍审核工具是一款应用程序，它通过报告可通过自动化测试轻松发现的无障碍问题，帮助您提升数字内容的无障碍性。这些内容包括网站、Web 应用程序和移动应用程序。

值得注意的是，虽然自动化辅助功能工具在提升辅助功能方面发挥着一定作用，但它们通常只能发现大约三分之一的潜在辅助功能问题。因此，切勿完全依赖这些工具来评估内容的辅助功能。始终需要进行人工测试，最好由残障人士进行测试，以确保内容尽可能地易于访问。

我们来看看一些可以帮助您提高数字内容可访问性的免费工具。

Google Lighthouse 是一款流行的网站指标检测工具，您可以直接在 Chrome 开发者工具中使用，也可以在线使用。这意味着您不仅可以检测在线网站，还可以检测本地开发的网站。

您可以查看的指标包括可访问性、SEO、最佳实践和性能。

要使用 Lighthouse，请按快捷键打开开发者工具`F12`，并切换到 Lighthouse 选项卡。选择要检查的指标，选择要测试的设备，然后单击“分析页面加载”按钮。

检查完成后，将显示无障碍评分，以及需要修复的任何问题列表。

如果您需要更可靠的指标，请考虑使用网页版。缺点是它不支持测试本地网站。您可以通过以下网址访问网页版`pagespeed.web.dev`： [此处应填写网址]。

WAVE 是另一款可靠的辅助功能检测工具，您可以将其作为 Chrome 扩展程序或网页版使用。您只需输入网站的 URL，即可生成一份全面的辅助功能报告。该报告包含已实现的辅助功能、ARIA 标识和对比度对比等信息。

IBM Equal Accessibility Checker 是另一款强大的工具，可用于提升数字内容的可访问性。借助它，您可以扫描网站是否存在可访问性问题，并生成详细报告。

您可以将其用作 Chrome 扩展程序或 Firefox 插件。

要将 IBM Accessibility Checker 作为 Chrome 扩展程序使用，请从 Chrome 网上应用商店下载。打开开发者工具，方法是按下快捷键`F12`并选择“元素”面板中的“辅助功能检查器”选项卡。点击扫描按钮开始检查，系统将生成一份报告。您可以点击“导出 XLS”按钮，将报告导出为电子表格和 HTML 文件。

请记住，虽然这些自动化工具可以帮助您提升内容的可访问性，但即使其中任何一项工具获得了满分，也不意味着您的内容就完全无障碍。这些工具的测试范围有限，始终需要进行人工测试，以确保所有人都能获得更佳的访问体验。

## 合理的标题级别结构如何影响可访问性？

您之前学习了正确的标题级别结构。现在，您将学习良好的标题结构如何影响可访问性。

合理使用标题能够为用户构建视觉层级，帮助他们浏览和理解网页内容。逻辑清晰的标题层级结构能够帮助屏幕阅读器用户理解内容结构，并快速浏览网页。创建恰当的标题文本，准确描述后续内容，有助于所有用户在您的网站上找到所需信息。此外，精心设计的标题还有助于提升网站的搜索引擎优化 (SEO)。

把标题看作是网站的地基。如果没有良好的地基，内容的易用性就会受到影响。

让我们来看看如何通过正确使用标题，使您的网页项目对使用辅助技术的人更加友好。

从“标题”到“分类”的各种标题，`h1`为`h6`屏幕阅读器用户创建了一个导航结构。屏幕阅读器可以列出页面上的所有标题，使用户能够直接跳转到所需的部分。因此，正确排列标题对于帮助这些用户避免不必要的内容并快速找到所需信息至关重要。

视力障碍或认知障碍人士需要快速便捷地处理信息，以减轻认知负荷。

标题的正确排列固然重要，但标题文字清晰明了、描述性强也同样重要。

以下是一些正确使用标题的关键做法：

- 使用层级分明的标题，以体现清晰的组织结构。例如，页面标题应为“`<title>” `h1`，主要章节应使用`h2` “<section>”，子章节应使用“<sub>d</sub>” `h3`，依此类推，直至“<section> `h6`”。
- 不要从`h1`跳到`h3`，或者从`h2`跳到`h4`，依此类推。
- 使用清晰、描述性的文字概括每个标题后面的内容。
- 不要孤立地使用标题——标题后面必须跟一些内容。
- 必要时请使用合适的标题，而不是通过格式化文本使其看起来像标题。
- 每个页面都应该只有一个`h1`元素来代表主要主题或标题。

以下是一个基本的标记示例，展示了如何在页面上使用标题：

示例代码

```html
<!-- Page title -->
<h1>What is HTML</h1>

<!-- First section -->
<section>
  <h2>Introduction to HTML</h2>
  <p>
    HTML stands for HyperText Markup Language. It is the standard language for
    creating web pages.
  </p>
</section>
<!-- Second section -->
<section>
  <h2>History of HTML</h2>
  <p>HTML began to take shape in the early 90s</p>
  <h3>Origins</h3>
  <p>
    HTML was created by Tim Berners-Lee in 1991. It has evolved significantly
    over the years.
  </p>
</section>
```
## 表格和无障碍设计的最佳实践是什么？

当我们看到表格时，我们会立即开始在数据和标题之间建立视觉联系。

例如，假设我们有一个表格来记录宠物信息。我们有两只狗和两只猫，表格显示了它们的名字和年龄。视力正常的人或许能够理解表格中的信息关系，但对于使用屏幕阅读器浏览表格的人来说，理解表格中的值和表头之间的联系就困难得多。

作为一名网页开发人员，您负责创建这些关联，并以屏幕阅读器用户易于理解的方式构建 HTML 标记。

那么，让我们来看看如何创建所有人都能理解的无障碍表格。我们要介绍的第一个最佳实践是使用表格标题。通过 `<table>``caption`元素，您可以编写表格的标题（或说明文字），这样用户，尤其是使用辅助技术的用户，就能快速了解表格的用途和内容。您应该将 `<table>``caption`元素紧跟在 `<table>` 元素的开始标签之后`table`。这样，屏幕阅读器和其他辅助技术可以在朗读内容之前朗读标题，从而提供更多上下文信息。

```html
<table>
  <caption>Our Pets</caption>
  <!-- Table Rows and Columns -->
</table>
```

现在我们来谈谈行标题和列标题。标题是特殊的单元格，通常位于行或列的开头，用于描述该行或列中存储的数据类型。您可以使用表头元素定义行标题或列标题`th`。

例如，下面的代码创建了一个包含两只宠物的表格。每一行都有一个行标题（宠物的名称），每一列都有一个列标题，用于描述该列中的数据代表的内容（年龄和类型）。

```html
<table>
  <caption>Our Pets</caption>
  <thead>
    <tr>
      <!-- Column Headers -->
      <th>Name</th>
      <th>Age</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Nora</th> <!-- Row Header -->
      <td>5</td>
      <td>Dog</td>
    </tr>
    <tr>
      <th>Gino</th> <!-- Row Header -->
      <td>2</td>
      <td>Cat</td>
    </tr>
  </tbody>
</table>
```

请注意，上面的代码`caption`在起始`table`元素之后紧接着有一个元素。然后，在表头`thead`元素（）内部，包含了列标题（`Name`、、`Age`和`Type`）。在第二行和第三行，在表体`tbody`元素（）内部，我们找到了每只宠物的数据。宠物的名字是行标题，因为它们位于表头元素（`th`）内部。

将数据单元格与其对应的标题关联起来对屏幕阅读器来说也至关重要。该`scope`属性决定标题是行标题还是列标题。屏幕阅读器可以根据表格结构正确判断，但通常建议明确指定，`scope`以确保清晰易懂。

该`scope`属性有四个可能的值。最常用的两个值分别用于`col`列和`row`行。在下面的代码中，可以看到我们已将该`scope`属性添加到列标题和行标题。三个列标题（`Name``<title> `、`<title>`、`<title>``Age`和`<title>`）的 `<title>`属性`Type`值为`<column>`。`scope``col`

两个行标题（`Nora`和）`Gino`具有`scope`。`row`

```html
<table>
  <caption>Our Pets</caption>
  <thead>
    <tr>
      <!-- Now they have scope -->
      <th scope="col">Name</th>
      <th scope="col">Age</th>
      <th scope="col">Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Nora</th>
      <td>5</td>
      <td>Dog</td>
    </tr>
    <tr>
      <th scope="row">Gino</th>
      <td>2</td>
      <td>Cat</td>
    </tr>
  </tbody>
</table>
```

如果列标题或行标题跨越多个单元格，则该设置`scope`也会分别应用于每个单元格。以下是一个示例：

```html
<table>
  <tbody>
    <tr>
      <td></td>
      <th scope="col">Name</th>
      <th scope="col">Age</th>
    </tr>
    <tr>
      <th rowspan="2" scope="row">Dogs</th>
      <th scope="row">Nora</th>
      <td>5</td>
    </tr>
    <tr>
      <th scope="row">Gino</th>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" scope="row">Cats</th>
      <th scope="row">Lulu</th>
      <td>10</td>
    </tr>
    <tr>
      <th scope="row">Elizabeth</th>
      <td>6</td>
    </tr>
  </tbody>
</table>
```

`Nora`在此表中，包含“'s age ( )”的单元格`5`将有一个列标题（`Age`）和两个行标题（`Dogs`和`Nora`）。`Gino`“'s age ( `2`)”也将有一个列标题（`Age`）和两个行标题（`Dogs`和`Gino`）。

但是，有些屏幕阅读器可能无法解析结构复杂的表格，因此您还应该尽可能地将表格展平，以避免行标题和列标题跨越多个单元格。

你的目标始终应该是确保用户能够访问这些信息，即使他们的屏幕阅读器可以处理复杂的表格结构。

对于单元格宽度，建议避免使用固定值，而应使用相对值，例如百分比。此外，尽量避免定义单元格高度，这样用户可以根据需要调整文本大小。

最后，应尽可能让浏览器决定表格宽度，以减少水平滚动的需要。

HTML 表格对于以易于访问和理解的格式呈现结构化数据至关重要。遵循这些无障碍指南，您可以创建所有人都能轻松理解的表格。
## 为什么输入数据需要有关联的标签？

输入字段上的标签看似是小细节，但它们在使表单更易于所有人使用方面起着至关重要的作用。

标签可以帮助残障人士，使表单对所有人更加友好，并最终提高表单转化率。

让我们深入探讨一下为什么给输入元素添加标签对于可访问性和可用性至关重要。

屏幕阅读器通常依赖标签来描述输入字段的用途。为了使其正常工作，标签必须以编程方式与输入字段关联`input`。虽然有多种方法可以实现这一点，但最常用的方法是使用 HTML`label`元素。

以下是如何将 a`label`与 an关联起来的方法`input`：

示例代码

```html
<form>
   <label for="name">Your Name</label>
   <input type="text" id="name" />
</form>
```

在这个例子中，元素`for`的属性与元素的`label`关联。这种关联使得屏幕阅读器能够在元素处于聚焦状态时播报元素，从而使屏幕阅读器用户能够理解元素的用途。`id``input``label``input``input`

为所有输入字段添加标签也有利于搜索引擎优化 (SEO)。有了合适的标签，搜索引擎就能更好地理解页面内容，从而对页面搜索排名产生积极影响。

但重要的是要明白，你创作的内容是给人类看的，而不是给搜索引擎看的。因此，你应该确保标签尽可能清晰明了、描述详尽。
## ARIA 角色
### WAI-ARIA 的目的是什么？它是如何运作的？

使静态内容易于访问相对简单，但动态内容则更具挑战性。而这正是 WAI-ARIA 的用武之地。

让我们来看看 WAI-ARIA 是什么，它的目的是什么，它是如何工作的，以及一些例子。

WAI-ARIA 代表 Web 无障碍倡议 - 无障碍富互联网应用。它是一项旨在增强动态内容和用户界面 (UI) 组件无障碍性的规范。

请注意，WCAG 和 WAI-ARIA 并不相同。WCAG 提供网页无障碍访问的通用指南，而 WAI-ARIA 则提供使动态和交互式内容对辅助技术用户无障碍访问的具体规则。

因此，WAI-ARIA 的主要目的是提高动态内容和 UI 组件（这些组件没有原生 HTML 等效项）的可访问性。

WAI-ARIA 的工作原理是引入一组可添加到 HTML 元素的属性，以提供额外的语义信息。这些属性分为角色、状态和属性三类。

ARIA 角色定义了网站或 Web 应用程序中元素的用途。以下示例展示了如何为`button`元素设置角色`div`。

```html
<div role="button">Click Me</div>
```

这样做是告诉辅助技术该元素是一个按钮。但是，角色本身并不提供任何功能。仅仅赋予它`div`一个`role`属性`button`并不会让它像按钮一样工作。要让它看起来像按钮并且行为也像按钮，你需要使用 CSS 和 JavaScript 来实现所需的效果。

以下是使用 HTML、CSS 和 JavaScript 创建自定义`button`元素的示例。

**注意**：不必担心理解 CSS 和 JavaScript 代码。你将在后续模块中学习这些语言。

```html
<link href="styles.css" rel="stylesheet">
<div id="custom-btn" role="button">Click Me</div>
<script src="index.js"></script>
```

```css
#custom-btn {
  display: inline-block;
  padding: 0.4em 1em;
  font-size: 1rem;
  font-family: sans-serif;
  color: buttontext;
  background-color: buttonface;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
  text-align: center;
}

#custom-btn:focus {
  outline: 2px solid Highlight;
  outline-offset: 2px;
}

#custom-btn:active {
  background-color: #ddd;
}
```

```js
const button = document.getElementById("custom-btn");

button.addEventListener("click", () => {
  alert("Button clicked!");
});

button.addEventListener("keydown", (e) => {
  if (e.key === "Enter" || e.key === " ") {
    e.preventDefault(); 
    button.click();
  }
});
```

最好始终使用原生元素`button`或`input`带有元素的元素`type="button"`。

ARIA 属性提供有关元素的更多详细信息。例如，该`aria-labelledby`属性允许您将元素连接到特定标签：

```html
<h2 id="header-id">About freeCodeCamp</h2>
<button id="button-id" aria-labelledby="header-id button-id">Learn More</button>
```

这将使辅助技术用户能够理解和使用其中的元素。

为了充分发挥 WAI-ARIA 的优势，请尽可能坚持使用原生 HTML，因为它通常能提供更好的可访问性。

仅当 HTML 无法满足需求时才使用 WAI-ARIA，并且不要忘记使用屏幕阅读器等辅助技术进行测试，或者请残障人士测试您的作品。此外，请确保 WAI-ARIA 的状态和属性能够随内容实时更新。避免过度使用 ARIA，因为它常常会造成混淆。
### ARIA角色有哪些？

ARIA 代表 Accessible Rich Internet Applications（可访问富互联网应用）。

ARIA角色定义了HTML元素的语义含义。它们对于确保使用辅助技术（例如屏幕阅读器）的用户能够访问网页内容至关重要。

HTML 根据其内容是否传达含义，分为语义元素和非语义元素。

许多语义化的 HTML 元素默认都已分配了 ARIA 角色。例如，`button`元素的默认 ARIA 角色为`button`。

`div`但非语义元素没有作用。例如，如果您不明确指定某个元素的作用，屏幕阅读器将无法理解该元素的用途。

要指定元素的 ARIA 角色，只需添加`role`属性，像这样`role="ARIA role"`，其中 value 是 ARIA 规范中角色的名称。

需要注意的是，为元素指定角色（role）只会起到一个作用：告知辅助技术该元素的用途。它不会为元素添加任何功能或行为。如果用户期望某个角色以某种方式运行，则需要开发者自行添加该预期行为。例如，为 `<a>` 元素添加 `role`并`role`不会自动使其可由鼠标点击或键盘操作。开发者有责任添加使 `<a>` 元素能够像按钮一样运行的预期行为，而且在大多数情况下，直接使用 `<a>`元素是更好的选择。`button``div``div``button`

ARIA角色主要分为六大类：

- 文档结构角色
- 小部件角色
- 里程碑式角色
- 实时区域角色
- 窗口角色
- 以及抽象角色

让我们更详细地了解一下它们。

文档结构角色定义了网页的整体结构。借助这些角色，辅助技术可以理解不同部分之间的关​​系，并帮助用户浏览内容。

然而，大多数文档结构角色在现代 Web 开发中并未得到应用，因​​为浏览器已经支持等效的语义 HTML 元素，应尽可能优先使用这些元素。

您应该指定那些没有等效语义元素的角色。例如：`toolbar`，，，，，，和。`tooltip``feed``math``presentation``none``note`

还有其他类似的角色，但这些是最常用的。这是一个`div`使用`math`ARIA 角色的示例。该示例`div`包含一个数学公式。

```html
<div role="math" aria-label="x squared + y squared = 3">
  x<sup>2</sup> + y<sup>2</sup> = 3
</div>
```

您还会注意到它`div`有一个`aria-label`属性。此属性的值应该是一个表示表达式的字符串。

小部件角色定义了交互元素（例如滚动条）的用途和功能。

小部件角色示例包括`scrollbar`，，（当可聚焦时`searchbox`），，，，，，和。`separator``slider``spinbutton``switch``tab``tabpanel``treeitem`

有些角色具有等效的语义元素。如果存在语义元素，则应优先考虑语义元素而非角色。例如，应优先使用 HTML元素，而不是在元素中`button`添加 `<div>``role`标签。`button``div`

地标角色用于对网页的主要部分进行分类和标记。屏幕阅读器利用它们为用户提供便捷的导航，帮助他们快速找到页面的重要部分。为了保持整体布局简洁易懂，应谨慎使用地标角色。地标角色的示例包括`banner`` `complementary`<div> ` `contentinfo`、`<span> ` 、 `form`` <span>`、`<span>`、`<span>`和`<span> `。每个地标角色都有对应的 HTML 元素，例如`<div> `、`<span> `main`` 、 `<span>`、 ` <span>`、`<span> ` 和`<span>`。如果您使用正确的 HTML 元素来定义页面的各个部分，则无需显式地为这些元素添加 `<div>` 属性。`navigation``region``search``header``footer``aside``form``main``nav``section``search``role`

实时区域角色定义了内容会动态变化的元素。这样，屏幕阅读器和其他辅助技术就可以向视障用户播报内容变化。这些角色包括：`alert`，，，，和。`log``marquee``status``timer`

窗口角色定义了子窗口，例如弹出式模态对话框。这些角色包括 `<window>``alertdialog`和 ` <div> `dialog``。请注意，现在最佳实践是使用 HTML`dialog`元素及其关联的 JavaScript 方法，而不是手动创建对话框。

最后，我们来看抽象角色。这些角色有助于组织文档。它们仅供浏览器内部使用，开发者不应使用，因此您应该了解它们的存在，但不应该在您的网站或 Web 应用程序中使用它们。

借助 ARIA 角色，您可以创建易于访问且包容性强的网站和 Web 应用程序。它们提供有关 HTML 元素用途和功能的语义信息。

屏幕阅读器和其他辅助技术利用这些信息来帮助用户理解页面内容并设定使用方法，从而确保每个人都能获得良好的用户体验。

### aria-label 和 aria-labelledby 属性的作用是什么？

确保所有用户，包括残疾人士，都能顺利访问网站至关重要。

对于使用屏幕阅读器的人来说，` `aria-label`and``aria-labelledby`属性提供了有关页面元素的关键信息，这些信息可能不清楚或不可见。

让我们来看看什么是`aria-label`和`aria-labelledby`属性，以及它们在使网络对有视觉障碍和相关残疾人士无障碍访问方面所起的作用。

你会注意到 `<a>``aria-label`和`<b> `aria-labelledby`` 都以 `aria` 为前缀。这是什么意思呢？ARIA 代表 Accessible Rich Internet Applications（无障碍富互联网应用）。它是一组以 `aria` 为前缀的属性`aria-`，允许开发者向辅助技术传达元素的用途。` `aria-label`<label>` 属性是交互式元素的不可见标签。它会为元素添加一个文本标签，屏幕阅读器可以读取该标签的内容。

`aria-label`对于那些没有可见文本但仍需要屏幕阅读器描述的元素来说，这种方法尤其有用。例如，只有图标的按钮通常需要`aria-label`传达其功能。

以下是一个例子：

```html
<button aria-label="Search">
  <i class="fas fa-search"></i>
</button>
```

`Search, button`在这种情况下，即使按钮仅包含一个图标，屏幕阅读器也可能将其朗读为“” 。该`aria-label`属性告诉屏幕阅读器应该使用什么文本来代替图标。

如果按钮包含文本“搜索”而不是图标，则无需该`aria-label`属性，因为文本将作为按钮的标签。

对于输入元素，`aria-label`如果没有与输入关联的可见标签，则该属性会直接提供一个标签。

该`aria-labelledby`属性的功能与另一个属性完全相同`aria-label`，但它不是直接在属性中定义文本，而是引用页面上已存在的文本。现有文本必须具有一个`id`属性，该属性将用作该`aria-labelledby`属性的引用值。

举个例子：

```html
<input type="text" aria-labelledby="search-btn">
<button type="button" id="search-btn">Search</button>
```

在这种情况下，按钮的文本被用作搜索输入框的标签。屏幕阅读器会将输入框的内容朗读为类似“输入框” `Search, edit`。如果您之后决定将按钮文本更改为“输入框” `Find`，由于标签引用了按钮文本，因此会自动更新为新文本。也可以将多个`id`值合并到一个`aria-labelledby`属性值中。以下是具体操作方法：

```html
<div>
  <span id="volume-label">Volume</span>
  <span id="volume-details">Adjust the volume level</span>
  <input
    type="range"
    min="0"
    max="100"
    value="30"
    aria-labelledby="volume-label volume-details">
</div>
```

对于滑块，屏幕阅读器将查找 `<div>``volume-label`和`<span> `volume-details`` 元素的内容并播报`Volume Adjust the volume level`。

您已经看到 `<style>``aria-label`和`<style>` 属性都能帮助屏幕阅读器理解元素的功能。那么，应该使用哪一个呢？由于它们提供相同的功能，因此两者都可以使用，但使用 `<style>` 可能比使用`<style>``aria-labelledby`有一些优势：`aria-labelledby``aria-label`

- 如果有人使用翻译服务来翻译您页面上的内容，则`aria-label`属性中的文本可能不会总是被翻译。
- 使用此功能`aria-labelledby`还可以帮助防止屏幕阅读器用户看到的可见标签文本和不可见标签不匹配，因为更新可见文本会自动更新不可见标签。
- `aria-labelledby`可以更轻松地以编程方式创建由多个文本源组成的复杂不可见标签。

最后一点，不要同时在同一个元素上使用 `<img>``aria-label`和`aria-labelledby``<img>` 标签。否则，屏幕阅读器始终会根据 `<img>` 标签判断不可见的标签`aria-labelledby`，而`<img>` 标签`aria-label`则会被完全忽略。

### 什么是 aria-hidden 属性，它是如何工作的？

如果您需要显示内容，同时又希望对使用辅助技术（如屏幕阅读器）的用户隐藏该内容，则可以使用该`aria-hidden`属性。

你只需要将其添加到你想隐藏的 HTML 元素中，并将其值设置为`true`，就像你在这里看到的那样：`aria-hidden="true"`。

此属性会将该元素及其所有子元素从辅助功能树中隐藏，但保持它们在页面上可见。常见用例包括：

- 仅具有装饰用途的图标和图像。
- 内容重复。

需要注意的是，`display: `aria-hidden`none` 只会对屏幕阅读器等辅助技术隐藏内容。如果内容需要对所有人隐藏，则不应使用 ` `aria-hidden`display: none` 来隐藏它。例如，当前处于折叠状态的汉堡菜单必须对所有键盘用户隐藏，而不仅仅是屏幕阅读器用户。在这种情况下，您可以将菜单的 CSS`display`属性设置为` `none`display: none`，以便在菜单折叠时将其从 DOM 中移除。

永远不要使用 ` `aria-hidden`display: none` 属性来隐藏可通过键盘聚焦的元素。该`aria-hidden`属性只会将元素从辅助功能树中移除，而不会将其从 DOM 中移除。因此，屏幕阅读器用户仍然可以使用 Tab 键切换到该元素，但屏幕阅读器不会播报该元素，导致他们实际上聚焦在“空无一物”的地方。

`aria-hidden`这里有一个示例，我们通过添加值为 的属性来隐藏辅助功能树中的图标`true`。

我们只保留辅助技术可识别的文本，以避免因同一目的同时使用图标和文本而造成的任何混淆。

**注意**：此交互式示例包含 Font Awesome CDN，因此您可以在预览窗口中看到齿轮图标。

```html
<head>
  <!-- Font Awesome CDN -->
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.0/css/all.min.css"
  />
</head>

<button>
  <i class="fa-solid fa-gear" aria-hidden="true"></i>
  <span class="label">Settings</span>
</button>
```

您无需使用`aria-hidden`when：

- HTML元素已经有一个`hidden`属性了。
- 该元素或其祖先元素已被隐藏`display: none`。
- 该元素或其祖先元素已被隐藏`visibility: hidden`。

在这三种情况下，元素已经从 DOM 中移除，因此从可访问性树中隐藏，所以该`aria-hidden`属性是不必要的。

与使用任何 ARIA 属性一样，您应该始终使用辅助技术进行测试，最好让残疾人士测试您的作品，以确保即使包含这些隐藏元素，作品也易于理解。

您还应该知道，如果该元素的任何父元素将此属性设置为 true，则将其设置为 true 将不会使该元素对辅助技术`aria-hidden`公开。`false``true`

该`aria-hidden`属性用于对使用辅助技术（例如屏幕阅读器）的用户隐藏元素。

虽然它可以用于隐藏纯粹的装饰元素和重复内容，但应谨慎使用，以免妨碍可访问性。

一般来说，页面上的所有内容和功能都应该对使用辅助技术的用户开放。此功能的使用场景`aria-hidden`非常有限，主要用于通过移除纯粹的装饰性或重复信息来简化屏幕阅读器的用户体验。请勿使用此功能`aria-hidden`隐藏您认为屏幕阅读器用户不感兴趣的内容。屏幕阅读器用户理应能够访问页面上的所有信息。

通过遵循这些最佳实践并测试用户体验，您可以为所有人创造包容性的在线体验。

### 什么是 aria-describedby 属性，它是如何工作的？

该`aria-describedby`属性通过引用页面上的现有内容，向屏幕阅读器用户提供有关元素的附加信息。它在元素和内容之间建立起程序化的关联（技术上称为可访问描述），屏幕阅读器可以利用这种关联，在用户与元素交互时告知他们这些附加信息。

最常见的用途`aria-describedby`是将说明和错误信息与表单输入关联起来。由于屏幕阅读器用户浏览页面的方式多种多样，他们在切换输入框时可能会错过这些信息。使用此功能`aria-describedby`可以确保他们能够听到这些信息。

我们来看几个例子来了解它是如何工作的。在第一个例子中，我们有一个`form`接受密码的元素。

在密码输入框中输入几个字符，您会看到预览窗口中的密码被遮盖了。您还会看到，`password-help`在您输入 8 个或更多字符之前，文本会一直保持红色。

注意：此交互式示例使用 CSS 和 JavaScript 动态更新文本颜色`password-help`。不必担心理解 JavaScript 代码，因为您将在后续模块中学习 JavaScript。

```html
<link rel="stylesheet" href="styles.css">

<form>
  <label for="password">Password:</label>
  <input type="password" id="password" aria-describedby="password-help" />
  <p id="password-help">Your password must be at least 8 characters long.</p>
</form>

<script src="index.js"></script>
```

```css
#password-help {
  color: red;
}
```

```js
const passwordEl = document.getElementById("password");
const passwordHelpText = document.getElementById("password-help");

passwordEl.addEventListener("input", (e) => { 
  const userInput = e.target.value;
  passwordHelpText.style.color = userInput.length >= 8 ? "green" : "red";
});
```

我们使用一个`label`元素来显示`Password`文本，并将其与密码`input`字段关联起来。

我们还有一个段落元素，用于描述密码要求。我们使用 `<password>``aria-describedby`属性将密码`input`字段与段落元素中的密码要求关联起来。当屏幕阅读器用户与此元素交互时，屏幕阅读器会朗读该段落`input`元素的名称，并可能随后朗读密码要求。但这并非绝对保证，因为某些屏幕阅读器可能不会自动朗读附加内容，或者仅在特定情况下才会朗读。这种情况并不少见。每个屏幕阅读器都不同，处理 ARIA 属性的方式也各不相同。但这并不影响 `<password>` 属性的使用，因为它通常对屏幕阅读器用户有益。`input``Password``aria-describedby`

该属性的另一个典型应用场景`aria-describedby`是删除操作`button`。以下示例展示了一个删除操作，`button`并在其后附上一条消息，描述点击按钮后将发生的情况：

```html
<button aria-describedby="delete-message">Delete</button>

<p id="delete-message">Warning! All deletions are permanent.</p>
```

与之前的示例一样，我们使用`aria-describedby`属性将删除按钮与消息关联起来。属性`id`的值必须与删除按钮的值`aria-describedby`匹配。

该`aria-describedby`属性功能强大，可用于确保在屏幕阅读器用户与元素交互时，能够向其提供有关该元素的附加信息。它最常用于将说明和错误消息与表单输入关联起来，以降低屏幕阅读器用户在浏览表单时错过这些信息的可能性。

## 使用无障碍媒体元素
### 何时需要 alt 属性？好的 alt 文本示例有哪些？

替代文本（通常缩写为`alt`文本）是对图像的简短文字描述。它为无法看到图像的用户（例如使用屏幕阅读器和其他辅助技术的用户）提供有关图像的基本信息。

这对于确保网站对视障人士无障碍访问至关重要。

搜索引擎也会使用替代文本来理解图像。某些浏览器在图像加载不正确时也会显示替代文本。这种情况可能发生在图像文件缺失或用户网络连接出现问题时。因此，替代文本在许多方面都很有用。

视力障碍人士如果图片没有替代文字描述，就无法了解图片内容。例如，一张小狗图片的替代文字“一只可爱的小狗”就是一个糟糕的例子。

![[一只可爱的小狗.png]]

这段文字不够具体，无法传达图片的重要细节，例如小狗长什么样？小狗在哪里？小狗周围有什么重要的物品吗？

让我们改进一下。一个好的替代文本示例是：“一只戴着橙色项圈的黑白相间的小狗趴在沙滩上，侧着头看向一边。一个亮橙色的球放在它前爪附近。”

这里你可以看到 HTML 中的图像元素、`alt`属性以及更详细的描述：

示例代码

```html
<img src="puppy.png" alt="A black and white puppy with an orange collar lies on its belly in the sand, looking off to the side. A bright orange ball rests near its front paws." />
```

需要注意的是，图片替代文字的编写方式并非千篇一律。描述内容取决于图片的使用场景。例如，如果这张小狗图片出现在一个介绍犬种的网站上，你可能需要更详细地描述小狗的外貌特征，而忽略小狗在海滩上玩橙色球这一事实。总之，图片`alt`的替代文字应该体现图片在页面上的主要用途，并且提供的信息应该能够让无法看到图片的人理解图片的用途。

这里是另一个美丽的度假胜地。让我们来描述一下。

![[Pasted image 20251109170027.png]]

这张图片的糟糕配文示例`alt`是“度假村”。

这段描述太短，没有提供足够的图片信息。为了改进这段描述，您可以添加图片最重要的元素：

“热带度假村，设有被棕榈树环绕的游泳池和别墅。”

您可以在 HTML 中使用 alt 属性，如下所示：

示例代码

```html
<img src="resort.png" alt="Tropical resort featuring a swimming pool surrounded by palm trees and bungalows." />
```

既然你已经了解了好`alt`文章和坏文章的区别，让我们来看看一些最佳实践。

- 尽量保持`alt`文字简洁。文字内容应足以理解图片含义，但又不宜过长以免造成混乱。
- 你不应该试图描述每一个细节，而应该专注于图像最重要的方面。
- 通常情况下，你不需要以“图片”或“照片”开头，可以直接开始描述。
- 另外，如果图片周围已经有类似的文字，就不需要再写一遍了。
- 为了保持一致性，通常建议在替代文本末尾添加句号。
- 如果图片是指向另一个页面的链接，则文本`alt`应该描述用户点击该链接后会发生什么，而不是描述图片本身。

例如，如果你的网站有一个向右的箭头图标，点击后会跳转到下一页，那么与其像本例中那样只写“向右箭头”的替代文本，不如使用带有以下描述的 alt 属性：

示例代码

```html
<a href="about.html">
  <img src="arrow-right.png" alt="Right arrow." />
</a>
```

你应该这样写，`alt`描述用户点击图片后会发生什么。他们会进入下一页。

示例代码

```html
<a href="about.html">
  <img src="arrow-right.png" alt="Go to next page." />
</a>
```

只有传达重要信息的图片才应该配有`alt`文字。如果图片仅用于装饰目的，则应配以`null`（空白）`alt`文字，以便屏幕阅读器和其他辅助技术可以忽略它。

`alt`以下是一个空属性的示例：

示例代码

```html
<img src="decorative_image.jpg" alt="" />
```

网站上的每张图片都应该有一个`alt`属性，即使该属性为空。如果`alt`完全省略该属性，一些屏幕阅读器会朗读文件名，这可能会分散使用辅助技术用户的注意力，因此不建议这样做。

最后，在网站上线之前，您应该仔细测试屏幕阅读器是否能够`alt`正确朗读文本。

撰写有效的`alt`文本对于创建易于访问的网页内容至关重要。作为网页开发者，通过提供清晰的图片描述，您可以确保每个人都能获得包容性的在线体验。
### 好的链接文本有哪些无障碍功能优势？好的链接文本有哪些示例？

让我们从可访问性的角度来探讨编写好的链接文本的好处，并举一些好的链接文本的例子。

优质链接文本最显而易见的优势在于，它能让所有人更轻松地快速找到所需信息。描述性链接能帮助用户了解链接指向的位置和内容，避免用户迷失方向，从而提升整体用户体验。

对于使用屏幕阅读器的用户来说，清晰明了的链接文本至关重要。屏幕阅读器会朗读链接文本，因此像“阅读我们的无障碍指南”这样的文本远比“点击这里”要好得多。

清晰明了的链接文字不仅对视力障碍人士有益，对认知障碍人士也能提供清晰的上下文信息。

以下是一些编写链接文本时需要牢记的最佳实践：

- 使用下划线和其他视觉提示，确保链接在视觉上清晰可辨，以便用户能够轻松识别和浏览它们。
- 避免使用“这里”、“点击这里”和“更多信息”等通用链接文本，因为它们无法提供任何有用的信息。
- 链接文本应简洁明了，最好在 2-5 个字之间，以传达链接的目的。
- 避免使用用户可能不理解的术语和缩写。
- 关注结果，而不是行动本身。例如，“用户行为结果”，而不是“点击此处阅读更多”。
- 不要对不同的目的地重复使用相同的链接文本。
- 链接的放置应使其与周围文本逻辑相符。例如，使用“了解更多详情，请访问我们的活动页面”，而不是“点击此处了解更多”。

以下是一些针对特定使用场景的优秀链接文本示例，并与一些不太有用的链接文本进行了比较。假设您想链接到一个提供活动详情的页面，例如：

示例代码

```html
<a href="webinar-details-link">Details</a>
```

`Details`内容含糊不清，没有提供用户点击链接后会看到什么的具体信息。如果没有更多上下文，用户可能不知道该链接指向的是网络研讨会、产品、政策还是其他内容的详情。

以下是一个好的链接文本示例：

示例代码

```html
<a href="webinar-details-link">
  Get details about our upcoming webinar
</a>
```

这段链接文本为用户提供了有关即将看到的内容的背景信息，使他们更容易决定是否点击。它明确指出该链接与网络研讨会相关，从而减少了歧义。

以下是链接到博客文章的另一个示例：

示例代码

```html
<a href="/blog-post-link">Read more</a>
```

链接文本`Read more`缺乏上下文，因此在可访问性方面并不理想。

以下是一个更好的链接文本示例：

示例代码

```html
<a href="/blog-post-link">
   Read our latest blog post on web accessibility
</a>
```

更新后的链接文本让用户更清楚地了解点击链接后会看到什么以及为什么要点击该链接，这对于使用屏幕阅读器的用户来说尤其重要。

我们再来看一个例子。假设你想提供关于某个主题的更多信息：

示例代码

```html
<a href="/link-to-topic">More info</a>
```

`More info`此外，该链接内容含糊不清，可能影响用户访问。它没有提供链接指向的具体目标位置，这可能会让依赖屏幕阅读器的用户或以非线性方式浏览网站的用户感到困惑。

以下是一个更好的链接文本示例：

示例代码

```html
<a href="/link-to-topic">
   Learn more about our accessibility efforts
</a>
```

更新后的链接文本更好，因为它清晰地描述了用户点击链接后会看到的内容。用户可以立即明白该链接指向的是关于您无障碍设计工作的信息。
### 让音频和视频内容更易于访问的好方法有哪些？

多媒体，尤其是视频，已成为在线分享信息的首选格式。

随着内容的激增，越来越需要确保每个人都能在线访问和享受视频和音频内容，无论他们的能力或环境如何。

让你的音频和视频内容更易于访问并非锦上添花，而是触达更广泛受众的必要条件。让我们来看看一些经济实惠的方法，让你的音频和视频内容更易于访问。

视频不仅包含视觉效果，还包含音频，因此您首先应该考虑的是为您的视频内容添加字幕。

字幕提供口语词汇和重要非语言声音（如音乐或笑声）的文字版本，并与视频同步。

另一方面，字幕对于听不懂你所讲语言的人来说至关重要。这不仅有助于聋人或听力障碍人士，也有助于在嘈杂或安静的环境中观看视频的人。

要为视频或音频内容添加字幕，您可以使用 `<video>`或`<audio>``track`元素：`video``audio`

```html
<video
  width="400"
  height="300"
  controls
  src="https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4"
>
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</video>

<audio controls src="sample.mp3">
  <track
    src="captions.vtt"
    kind="captions"
    srclang="en"
    label="English"
  />
</audio>
```

该`kind`属性用于告知轨道元素应如何使用。该`kind`属性的有效值包括`captions`、`subtitles`、`chapters`和`metadata`。

该`srclang`属性表示内容的语言`track`。该`label`属性是文本轨道的描述性标题，浏览器使用该标题来识别文本轨道并将其显示在可用文本轨道列表中。

另一个需要考虑的重要事项是为您的音频和视频内容提供文字稿。文字稿是音频或视频中所有语音的文本版本。与字幕不同，文字稿无需与媒体同步。文字稿对聋人和听力障碍人士非常有用。对于喜欢阅读而非观看或聆听的人来说，文字稿也很有帮助。此外，文字稿还能让您的内容可搜索，方便用户快速找到音频或视频的特定部分。如果您在网站上发布了视频或音频，只需将文字稿添加到音频或视频下方即可：

```html
<audio controls>
  <source src="audio.mp3" />
  Your browser does not support the audio element.
</audio>

<!-- Transcript -->
<h3>Transcript</h3>
<p>
  [Speaker 1]: Welcome to the tutorial on making accessible content
</p>
<p>
  [Speaker 2]: Today, we'll cover captions, transcripts, and more.
</p>

<!-- Rest of transcript -->
```

如果你在 YouTube 或 Vimeo 等视频分享平台上发布视频，它们都提供视频自动字幕和文字稿功能。但如果你不满意，还可以使用 veed.io、Rev、Amara 和 Descript 等服务。

其他使您的视频和音频内容更易于访问的方法包括：

- 为聋人和听力障碍人士的视频添加手语叠加层。
- 提供音量和速度控制。
- 确保屏幕文字具有良好的对比度。
- 提供多种格式。

### 有哪些方法可以让 Web 应用程序支持键盘操作？

许多用户由于身体残疾、重复性劳损或个人偏好而依赖键盘而非鼠标。这包括屏幕阅读器用户和鼠标无法使用的用户。键盘辅助功能确保这些用户能够无障碍地高效浏览网页应用程序。

让我们来看一些可以用来使 Web 应用程序支持键盘操作的实用技巧。

许多用户依赖 Tab`Tab`键在网页上的交互元素之间切换。默认情况下，浏览器允许用户按照 HTML 代码中出现的顺序使用 Tab 键在链接、按钮和表单字段等元素之间切换。这被称为自然 Tab 键顺序。

有时，您可能需要调整哪些元素可以获得焦点，或者更改它们的焦点顺序。该`tabindex`属性允许您执行此操作。

以下是基本语法：

```html
<element tabindex="number">Element Text</element>
```

该值`tabindex`决定了元素在键盘导航中的行为方式：

`tabindex="0"`将该元素添加到自然制表顺序中。

使用 Tab 键会将焦点从 <div> 移动`button`到 <div> `div`，然后再移动到 <link>，顺序与它们在 HTML 中的顺序一致。

点击预览窗口空白处的任意位置。然后使用快捷`Tab`键查看焦点在不同元素之间的移动。

```html
<button>First</button>
<div tabindex="0">Second</div>
<a href="#">Third</a>
```

`tabindex="-1"`通过编程方式使元素可获得焦点。这对于管理通常不可获得焦点的元素（例如标题、容器、对话框或错误消息）的焦点非常有用：

```html
<p tabindex="-1">Sorry, there was an error with your submission.</p>
```

在这个例子中，段落不在正常的 Tab 键顺序中，因此用户无法通过按`Tab`Tab 键访问它。但是，如果通过脚本将焦点设置到该元素上，则该消息将会引起用户的注意。您将在 JavaScript 课程中学习更多关于此技巧的内容。

当该值`tabindex`大于某个阈值时`0`，它会设置自定义的 Tab 键顺序。因此，值较小的元素会优先获得焦点。

在这个例子中，无论 HTML 中的顺序如何，按 Tab 键都会依次聚焦于`<div>`、`<span>` 和 `<span>`元素`input`。`tabindex="1"``2``3`

```html
<input tabindex="2">
<input tabindex="1">
<input tabindex="3">
```

自定义正值有时会用于复杂的组件，例如工具栏，以便设置特定的导航顺序。然而，这种做法并不推荐，因为它会使导航变得混乱且难以维护，尤其是在页面规模扩大或发生变化时。

`accesskey`这是另一个可用于使您的 Web 项目支持键盘操作的属性。它允许您定义一个按键，该按键可以聚焦或激活特定元素。

以下是一个您可以按照以下建议尝试的交互式示例：

- `accesskey="s"`将按键分配`S`给该`Save`按钮。在大多数浏览器中，按下`ALT + S`（Windows 系统）或`CTRL + Option + S`（Mac 系统）即可激活此按钮。
- `accesskey="c"`将密钥设置`C`为按钮，允许用户使用（Windows）和（Mac）`Cancel`激活它。`ALT + C``CTRL + Option + C`
- `accesskey="h"`将密钥分配`H`给链接，允许用户使用（Windows）和（Mac）`Home`导航到主页。`ALT + H``CTRL + Option + H`

`ALT + Specified Key`请注意，激活访问密钥的具体组合键可能因浏览器和操作系统而异。通常在 Windows 和Mac 系统上是相同的`CTRL + Option + Specified Key`。

```html
<button accesskey="s">Save</button>
<button accesskey="c">Cancel</button>
<a href="index.html" accesskey="h">Home</a>
```

另一种让键盘在应用中易于使用的方法是确保提供清晰的焦点指示器。如果您觉得浏览器默认的焦点指示器不够清晰，可以通过设置元素的焦点状态来覆盖它。

这里展示了如何设置元素的焦点状态样式`button`。点击预览窗口空白处的任意位置，然后按下快捷`Tab`键即可将焦点移至按钮。

```html
<link href="styles.css" rel="stylesheet">

<button>Example button</button>
```

```css
button:focus {
  outline: 2px solid #005fcc;
}
```

该`outline`属性用于定义元素周围的轮廓。此示例将轮廓设置为粗细为 2 像素的蓝色实线。焦点指示器的样式应清晰地显示当前哪个元素获得焦点。为了确保可访问性，指示器与其覆盖的背景色之间的最小颜色对比度必须至少为 3:1。

你还应该避免键盘陷阱，当用户无法将焦点从模态框和弹出窗口等组件中的某个元素移开时，就会发生这种情况。
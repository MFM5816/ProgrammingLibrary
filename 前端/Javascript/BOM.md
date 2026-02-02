## 常见的 BOM 对象

BOM可以让我们通过JS来操作浏览器。BOM中为我们提供了一些对象，来完成对浏览器相关的操作。

常见的 BOM对象有：

- Window：代表整个浏览器的窗口，同时 window 也是网页中的全局对象。
    
- Navigator：代表当前浏览器的信息，通过该对象可以识别不同的浏览器。
    
- Location：代表当前浏览器的地址栏信息，通过 Location 可以获取地址栏信息，或者操作浏览器跳转页面。
    
- History：代表浏览器的历史记录，通过该对象可以操作浏览器的历史记录。由于隐私原因，该对象不能获取到具体的历史记录，只能操作浏览器向前或向后翻页，而且该操作只在当次访问时有效。
    
- Screen：代表用户的屏幕信息，通过该对象可以获取用户的显示器的相关信息。
    

备注：这些 BOM 对象都是作为 window 对象的属性保存的，可以通过window对象来使用，也可以直接使用。比如说，我可以使用 `window.location.href`，也可以直接使用 `location.href`，二者是等价的。

## Navigator 和 `navigator.userAgent`

`Navigator`代表当前浏览器的信息，通过该对象可以识别不同的浏览器。

由于历史原因，Navigator对象中的大部分属性都已经不能帮助我们识别浏览器了。

**一般我们只会使用`navigator.userAgent`来获取浏览器的信息**。

userAgent 的值是一个字符串，简称 **UA**，这个字符串中包含了用来描述浏览器信息的内容，不同的浏览器会有不同的userAgent。

**代码举例**：（获取当前浏览器的UA）

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <script>
            var ua = navigator.userAgent; // 获取当前浏览器的 userAgent

            console.log('qianguyihao 当前浏览器的UA是：' + ua);

            if (/firefox/i.test(ua)) {
                alert('是火狐浏览器');
            } else if (/chrome/i.test(ua)) {
                alert('是Chrome浏览器');
            } else if (/msie/i.test(ua)) {
                alert('是IE浏览器');
            } else if ('ActiveXObject' in window) {
                alert('是 IE11 浏览器');
            }
        </script>
    </body>
</html>
```
## History 对象

History对象：可以用来操作浏览器的向前或向后翻页。

### History对象的属性

```
history.length
```

解释：获取浏览器历史列表中的 url 数量。注意，只是统计当次的数量，如果浏览器关了，数量会重置为1。

### History对象的方法

**方法1**：

```
history.back();
```

解释：用来回退到上一个页面，作用和浏览器的「回退按钮」一样。

**方法2**：

```
history.forward();
```

解释：用来跳转下一个页面，作用和浏览器的「前进按钮」一样。

**方法3**：

```
history.go( int n);  // 需要整数作为参数

// 代码举例：
history.go( 1 ); // 向前跳转一个页面，相当于 history.forward()

history.go( 2 ); // 表示向前跳转两个页面

history.go( 0 ); // 刷新当前页面

history.go( -1 ); // 向后跳转一个页面，相当于 history.back()

history.go( -2 ); // 向后跳转两个页面

```

解释：向前/向后跳转 n 个页面。
## Location 对象

Location 对象：封装了浏览器地址栏的 URL 信息。

下面介绍一些常见的属性和方法。

### Location 对象的属性：location.href

```
location.href

location.href = 'https://xxx';
```

解释：获取当前页面的 url 路径（或者设置 url 路径）；或者跳转到指定路径。

举例1：

```
console.log(location.href); // 获取当前页面的url 路径

```

举例2：

```
    location.href = 'www.baidu.com'; // 跳转到指定的页面链接。通俗理解就是：跳转到其他的页面
```

从上方的**举例2**中可以看出：如果直接将`location.href`属性修改为一个绝对路径（或相对路径），则页面会自动跳转到该路径，并生成相应的历史记录。

**window.location.href 是异步代码：**

需要特别注意的是：window.location.href的赋值，并不会中断Javascript的执行立即进行页面跳转。因为 LocationChange 行为在浏览器内核中是起定时器异步执行的。异步执行的好处是为了防止代码调用过深，导致栈溢出，另外也是为了防止递归进入加载逻辑，导致状态紊乱，保证导航请求是顺序执行的。

解决办法：在 location.href 的下一行，加上 return 即可。意思是，执行了 location.href 之后，就不要再继续往下执行了。



### Location 对象的方法

**方法1**：

```
    location.assign(str);
```

解释：用来跳转到其他的页面，作用和直接修改`location.href`一样。

**方法2**：

```
    location.reload();
```

解释：用于重新加载当前页面，作用和刷新按钮一样。

代码举例：

```
    location.reload(); // 重新加载当前页面。
    location.reload(true); // 在方法的参数中传递一个true，则会强制清空缓存刷新页面。

```

**方法3**：

```

    location.replace();
```

解释：使用一个新的页面替换当前页面，调用完毕也会跳转页面。但不会生成历史记录，不能使用「后退按钮」后退。
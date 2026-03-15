# DrissionPage

![](img\DrissionPage\logo.png)

## 一、介绍

DrissionPage 是一个基于 python 的网页自动化工具。

它既能控制浏览器，也能收发数据包，还能把两者合而为一。

可兼顾浏览器自动化的便利性和 requests 的高效率。

它功能强大，内置无数人性化设计和便捷功能。

它的语法简洁而优雅，代码量少，对新手友好。

DrissionPage的优点：

> 无 webdriver 特征，不会被网站识别
> 无需为不同版本的浏览器下载不同的驱动
> 运行速度更快
> 可以跨 iframe 查找元素，无需切入切出
> 把 iframe 看作普通元素，获取后可直接在其中查找元素，逻辑更清晰
> 可以同时操作浏览器中的多个标签页，即使标签页为非激活状态，无需切换
> 可以直接读取浏览器缓存来保存图片，无需用 GUI 点击另存
> 可以对整个网页截图，包括视口外的部分（90以上版本浏览器支持）
> 可处理非open状态的 shadow-root

详细内容见于http://drissionpage.cn/

## 二、安装

### 1.运行环境

> 最新版本：4.0.4.21
>
> 支持系统：Windows、Linux、Mac
>
> python 版本：3.6 及以上
>
> 支持应用：Chromium 内核浏览器（如 Chrome、Edge），electron 应用

### 2.安装

```
pip install DrissionPage
```

### 3.尝试启动浏览器

默认状态下，程序会自动在系统内查找 Chrome 路径。

执行以下代码，浏览器启动并且访问了项目文档，说明可直接使用，跳过后面的步骤即可。

```
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://g1879.gitee.io/DrissionPageDocs')
```

如果上面的步骤提示出错，说明程序没在系统里找到 Chrome 浏览器。

可用以下其中一种方法设置，设置会持久化记录到默认配置文件，之后程序会使用该设置启动。

**获取浏览器路径的方法**

打开浏览器，在地址栏输入`chrome://version`（Edge 输入`edge://version`），回车

![](img\DrissionPage\获取浏览器路径.png)

如图所示，红框中就是要获取的路径。

**方法一：**

新建一个临时 py 文件，并输入以下代码，填入您电脑里的 Chrome 浏览器可执行文件路径，然后运行。

```
from DrissionPage import ChromiumOptions

path = r'D:\Chrome\Chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
ChromiumOptions().set_browser_path(path).save()
```

**方法二：**

在命令行输入以下命令

```
dp -p D:\Chrome\chrome.exe
```



## 三、sessionPage

顾名思义，`SessionPage`是一个使用使用`Session`（requests 库）对象的页面，它使用 POM 模式封装了网络连接和 html 解析功能，使收发数据包也可以像操作页面一样便利。

并且，由于加入了本库独创的查找元素方法，使数据的采集便利性远超 requests + beautifulsoup 等组合。

### 1.创建页面对象

#### `SessionPage`初始化参数

| 初始化参数           | 类型                       | 默认值 | 说明                                                         |
| -------------------- | -------------------------- | ------ | ------------------------------------------------------------ |
| `session_or_options` | `Session` `SessionOptions` | `None` | 传入`Session`对象时使用该对象收发数据包；传入`SessionOptions`对象时用该配置创建`Session`对象；为`None`则从 ini 文件读取 |
| `timeout`            | `float`                    | `None` | 连接超时时间，为`None`则从配置文件中读取                     |

#### 创建对象

```
from DrissionPage import SessionPage

page = SessionPage()
```

`SessionPage`无需控制浏览器，无需做任何配置即可使用。

直接创建时，程序默认读取 ini 文件配置，如 ini 文件不存在，会使用内置配置。

#### 配置信息

`SessionOptions`是专门用于设置`Session`对象初始状态的类，内置了常用的配置。

| 初始化参数  | 类型   | 默认值 | 说明                                  |
| ----------- | ------ | ------ | ------------------------------------- |
| `read_file` | `bool` | `True` | 是否从 ini 文件中读取配置信息         |
| `ini_path`  | `str`  | `None` | 文件路径，为`None`则读取默认 ini 文件 |

```
# 导入 SessionOptions
from DrissionPage import SessionPage, SessionOptions

# 创建配置对象，并设置代理信息
so = SessionOptions().set_proxies(http='127.0.0.1:1080')
# 用该配置创建页面对象
page = SessionPage(session_or_options=so)
```

#### 获取网页

##### get请求

`get()`方法语法与 requests 的`get()`方法一致，在此基础上增加了连接失败重试功能。与 requests 不一样的是，它不返回`Response`对象。

| 参数名称      | 类型    | 默认值  | 说明                                           |
| ------------- | ------- | ------- | ---------------------------------------------- |
| `url`         | `str`   | 必填    | 目标 url                                       |
| `show_errmsg` | `bool`  | `False` | 连接出错时是否显示和抛出异常                   |
| `retry`       | `int`   | `None`  | 重试次数，为`None`时使用页面参数，默认 3       |
| `interval`    | `float` | `None`  | 重试间隔（秒），为`None`时使用页面参数，默认 2 |
| `timeout`     | `float` | `None`  | 加载超时时间（秒）                             |
| `**kwargs`    | -       | `None`  | 连接所需其它参数，具体见 requests 用法         |

返回

| 返回类型 | 说明         |
| -------- | ------------ |
| `bool`   | 是否连接成功 |

`**kwargs`参数与 requests 中该参数使用方法一致，但有一个特点，如果该参数中设置了某一项（如`headers`），该项中的每个项会覆盖从配置中读取的同名项，而不会整个覆盖。
就是说，如果想继续使用配置中的`headers`信息，而只想修改其中一项，只需要传入该项的值即可。

- 程序会根据要访问的网址自动在`headers`中加入`Host`和`Referer`项
- 程序会自动从返回内容中确定编码，一般情况无需手动设置

```
#普通网页
from DrissionPage import SessionPage

page = SessionPage()
page.get('http://g1879.gitee.io/drissionpage')
#带参数
from DrissionPage import SessionPage

page = SessionPage()

url = 'https://www.baidu.com'
headers = {'referer': 'gitee.com'}
cookies = {'name': 'value'}
proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
page.get(url, headers=headers, cookies=cookies, proxies=proxies)
```

##### post请求

用法与`get()`一致。

| 参数名称      | 类型    | 默认值  | 说明                                           |
| ------------- | ------- | ------- | ---------------------------------------------- |
| `url`         | `str`   | 必填    | 目标 url                                       |
| `show_errmsg` | `bool`  | `False` | 连接出错时是否显示和抛出异常                   |
| `retry`       | `int`   | `None`  | 重试次数，为`None`时使用页面参数，默认 3       |
| `interval`    | `float` | `None`  | 重试间隔（秒），为`None`时使用页面参数，默认 2 |
| `timeout`     | `float` | `None`  | 加载超时时间（秒）                             |
| `**kwargs`    | -       | `None`  | 连接所需其它参数，具体见 requests 用法         |

返回

| 返回类型 | 说明         |
| -------- | ------------ |
| `bool`   | 是否连接成功 |

```
from DrissionPage import SessionPage

page = SessionPage()
data = {'username': 'xxxxx', 'pwd': 'xxxxx'}

page.post('http://example.com', data=data)
# 或
page.post('http://example.com', json=data)
```

`data`参数和`json`参数都可接收`str`和`dict`格式数据，即有以下 4 种传递数据的方式：

```
# 向 data 参数传入字符串
page.post(url, data='abc=123')

# 向 data 参数传入字典
page.post(url, data={'abc': '123'})

# 向 json 参数传入字符串
page.post(url, json='abc=123')

# 向 json 参数传入字典
page.post(url, json={'abc': '123'})
```

#### 获取页面信息

成功访问网页后，可使用`SessionPage`自身属性和方法获取页面信息。



* url

  此属性返回当前访问的 url。

  **类型：**`str`

* `url_available`

  此属性以布尔值返回当前链接是否可用。

  **类型：**`bool`

* title

  此属性返回当前页面`title`文本。

  **类型：**`str`

* raw_data

  此属性返回访问到的元素数据，即`Response`对象的`content`属性。

  **类型：**`bytes`

* html

  此属性返回当前页面 html 文本。

  **类型：**`str`

* json

  此属性把返回内容解析成 json。
  比如请求接口时，若返回内容是 json 格式，用`html`属性获取的话会得到一个字符串，用此属性获取可将其解析成`dict`。 支持访问 `*.json` 文件，也支持 API 返回的json字符串。

  **类型：**`dict`

* 

  

语法：

WebPage是功能最全面的页面类，既可控制浏览器，也可收发数据包：

```handlebars
from DrissionPage import WebPage
```

如果只要控制浏览器，导入`ChromiumPage`：

```python
from DrissionPage import ChromiumPage
```

如果只要收发数据包，导入`SessionPage`：

```python
from DrissionPage import SessionPage
```

* 配置

  ChromiumOptions类用于设置浏览器启动参数：

  ```
  from DrissionPage import ChromiumOptions
  ```

  SessionOptions类用于设置Session对象启动参数：

  ```
  from DrissionPage import SessionOptions
  ```

  动作链，用于模拟一系列键盘和鼠标的操作：

  ```
  from DrissionPage import ActionChains
  ```

  键盘按键类，用于键入 ctrl、alt 等按键：

  ```
  from DrissionPage import Keys
  ```

  easy_set里保存了一些便捷的 ini 文件设置方法，可选择使用：

  ```
  from DrissionPage.easy_set import *
  ```

* 定位元素

  ```
  from DrissionPage import ChromiumPage
   
  # 创建页面对象，并启动或接管浏览器
  page = ChromiumPage()
  # 跳转到登录页面
  page.get('https://gitee.com/login')    # get()方法用于访问参数中的网址。它会等待页面完全加载，再继续执行后面的代码。
   
  # 定位到账号文本框，获取文本框元素
  ele = page.ele('#user_login')    # ele()方法用于查找元素，它返回一个ChromiumElement对象，用于操作元素。'#user_login'是定位符文本，#意思是按id属性查找元素。ele()内置了等待，如果元素未加载，它会执行等待，直到元素出现或到达时限。默认超时时间 10 秒。
   
  # 输入对文本框输入账号
  ele.input('您的账号')
  # 定位到密码文本框并输入密码
  page.ele('#user_password').input('您的密码')
  # 点击登录按钮
  page.ele('@value=登 录').click()    # @表示按属性名查找
  ```

* 爬取网页

  ```
  from DrissionPage import SessionPage
   
  # 创建页面对象
  page = SessionPage()
   
  # 爬取3页
  for i in range(1, 4):
      # 访问某一页的网页
      page.get(f'https://gitee.com/explore/all?page={i}')
      # 获取所有开源库<a>元素列表
      links = page.eles('.title project-namespace-path')    # 页面对象的eles()获取页面中所有class属性为'title project-namespace-path'的元素对象，eles()方法用于查找多个符合条件的元素，返回由它们组成的list
      # 遍历所有<a>元素
      for link in links:
          # 打印链接信息
          print(link.text, link.link)    # .text获取元素的文本，.link获取元素的href或src属性
  ```

* 下载网页

  ```
  from DrissionPage import SessionPage 
   
  url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
  save_path = r'C:\download'    # 保存的路径
   
  page = SessionPage()
  page.download(url, save_path, 'img')  # 支持重命名，处理文件名冲突
  ```

  

* 元素查找

  ```
  # 根据属性查找，@ 后面可跟任意属性
  page.ele('@id:ele_id', timeout=2)  # 查找 id 为 ele_id 的元素，设置等待时间2秒  
  page.eles('@class')  # 查找所有拥有 class 属性的元素
  page.eles('@class:class_name')  # 查找所有 class 含有 ele_class 的元素 
  page.eles('@class=class_name')  # 查找所有 class 等于 ele_class 的元素 
   
  # 根据 class 或 id 查找
  page.ele('#ele_id')  # 等价于 page.ele('@id=ele_id')
  page.ele('#:ele_id')  # 等价于 page.ele('@id:ele_id')
  page.ele('.ele_class')  # 等价于 page.ele('@class=ele_class')
  page.ele('.:ele_class')  # 等价于 page.ele('@class:ele_class')
   
  # 根据 tag name 查找
  page.ele('tag:li')  # 查找第一个 li 元素  
  page.eles('tag:li')  # 查找所有 li 元素  
   
  # 根据 tag name 及属性查找
  page.ele('tag:div@class=div_class')  # 查找 class 为 div_class 的 div 元素
  page.ele('tag:div@class:ele_class') # 查找 class 含有 ele_class 的 div 元素
  page.ele('tag:div@class=ele_class') # 查找 class 等于 ele_class 的 div 元素
  page.ele('tag:div@text():search_text') # 查找文本含有 search_text 的 div 元素
  page.ele('tag:div@text()=search_text') # 查找文本等于 search_text 的 div 元素
   
  # 根据文本内容查找
  page.ele('search text')  # 查找包含传入文本的元素  
  page.eles('text:search text')  # 如文本以 @、tag:、css:、xpath:、text: 开头，则应在前加上 text: 避免冲突  
  page.eles('text=search text')  # 文本等于 search_text 的元素
   
  # 根据 xpath 或 css selector 查找
  page.eles('xpath://div[@class="ele_class"]')  
  page.eles('css:div.ele_class')  
   
  # 根据 loc 查找
  loc1 = By.ID, 'ele_id'
  loc2 = By.XPATH, '//div[@class="ele_class"]'
  page.ele(loc1)
  page.ele(loc2)
   
  # 查找下级元素
  element = page.ele('@id:ele_id')
  element.ele('@class:class_name')  # 在 element 下级查找第一个 class 为 ele_class 的元素
  element.eles('tag:li')  # 在 ele_id 下级查找所有li元素
   
  # 根据位置查找
  element.parent  # 父元素  
  element.next  # 下一个兄弟元素  
  element.prev  # 上一个兄弟元素  
   
  # 获取 shadow-root，把它作为元素对待。只支持 open 的 shadow-root
  ele1 = element.shadow_root.ele('tag:div')
   
  # 串连查找
  page.ele('@id:ele_id').ele('tag:div').next.ele('some text').eles('tag:a')
   
  # 简化写法
  eles = page('@id:ele_id')('tag:div').next('some text').eles('tag:a')
  ele2 = ele1('tag:li').next('some text')
  ```

* 元素操作

  ```
  element.click(by_js)  # 点击元素，可选择是否用 js 方式点击
  element.input(value)  # 输入文本
  element.run_script(js)  # 对元素运行 JavaScript 脚本
  element.submit()  # 提交
  element.clear()  # 清空元素
  element.screenshot(path, filename)  # 对元素截图
  element.select(text)  # 根据文本选择下拉列表
  element.set_attr(attr, value)  # 设置元素属性值
  element.remove_attr(attr)  # 删除属性
  element.drag(x, y, speed, shake)  # 拖动元素相对距离，可设置速度和是否随机抖动
  element.drag_to(ele_or_loc, speed, shake)  # 拖动元素到另一个元素或某个坐标，可设置速度和是否随机抖动
  element.hover()  # 在元素上悬停鼠标+
  ```

* 元素属性

  ```
  element.html  # 返回元素 outerHTML
  element.inner_html  # 返回元素 innerHTML
  element.tag  # 返回元素 tag name
  element.text  # 返回元素 innerText 值
  element.comments  # 返回元素内注释列表
  element.link  # 返回元素 href 或 src 绝对 url
  element.texts()  # 返回元素内所有直接子节点的文本，包括元素和文本节点，可指定只返回文本节点
  element.attrs  # 返回元素所有属性的字典
  element.attr(attr)  # 返回元素指定属性的值
  element.css_path  # 返回元素绝对 css 路径
  element.xpath  # 返回元素绝对 xpath 路径
  element.parent  # 返回元素父元素
  element.next  # 返回元素后一个兄弟元素
  element.prev  # 返回元素前一个兄弟元素
  element.parents(num)  # 返回第 num 级父元素
  element.nexts(num, mode)  # 返回后面第几个元素或节点
  element.prevs(num, mode)  # 返回前面第几个元素或节点
  element.ele(loc_or_str, timeout)  # 返回当前元素下级第一个符合条件的子元素、属性或节点文本
  element.eles(loc_or_str, timeout)  # 返回当前元素下级所有符合条件的子元素、属性或节点文本
  ```

* 浏览器和数据包模式切换

  ```
  from DrissionPage import WebPage
  
  # 创建页面对象
  page = WebPage()
  # 访问网址
  page.get('https://www.baidu.com')
  # 查找文本框元素并输入关键词
  page('#kw').input('DrissionPage')
  # 点击搜索按钮
  page('#su').click(wait_loading=True)
  # 切换到收发数据包模式
  page.change_mode()
  # 获取所有<h3>元素
  links = page.eles('tag:h3')
  # 遍历获取到的元素
  for link in links:
      # 打印元素文本
      print(link.text)
  
  ```

## 
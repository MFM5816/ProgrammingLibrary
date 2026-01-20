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
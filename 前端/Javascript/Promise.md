Promise 是 JavaScript 中特有的语法。可以毫不夸张得说，Promise 是ES6中最重要的语法，没有之一。初学者可能对 Promise 的概念有些陌生，但是不用担心。大多数情况下，使用 Promise 的语法是比较固定的。
## Promise 的介绍和优点（为什么需要 Promise？）

Promise 是异步编程的一种**新的解决方案和规范**。ES6将其写进了语言标准，统一了用法，原生提供了 Promise 对象。

Promise 对象, 可以**用同步的表现形式来书写异步代码**（也就是说，代码看起来是同步的，但本质上的运行过程是异步的）。使用 Promise 主要有以下优点：

- 1、可以很好地解决ES5中的**回调地狱**的问题（避免了层层嵌套的回调函数）。
- 2、统一规范、语法简洁、可读性和和可维护性强。
- 3、Promise 对象提供了简洁的 API，使得管理异步任务更方便、更灵活。

从语法上讲，Promise 是一个构造函数。从功能上来说，Promise 对象用于封装一个异步操作，并获取其成功/ 失败的结果值。

从写法规范上讲，**Promise 本质上是处理异步任务的一种编写规范**，要求每个人都按照这种规范来写。异步任务成功了该怎么写、异步任务失败了该怎么写、成功或者失败之后怎么通知调用者，这些都有规定的写法。Promise 的目的就是要让每个使用ES6的人都遵守这种写法规范。

Promise 的伪代码结构，大概是这样的：

```
// 伪代码1
myPromise()
    .then(
        function () {},
        function () {}
    )
    .then(
        function () {},
        function () {}
    )
    .then(
        function () {},
        function () {}
    );

// 伪代码2
是时候展现真正的厨艺了().然后(买菜).然后(做饭).然后(洗碗);
```

上面的伪代码可以看出，业务逻辑上层层递进，但是代码写法上却十分优雅，没有过多的嵌套。
## Promise 的基本使用

ES5中，使用传统的回调函数处理异步任务时，其基本模型的写法已在上一篇内容“回调函数”里讲过。

ES6中，有了 Promise之后，我们可以对那段代码进行改进（基本模型不变）。你会发现，代码简洁规范了许多。

使用 Promise 处理异步任务的**基本代码结构**如下，我们先来认识一下：

```
// 使用 Promise 处理异步任务的基本模型

// 封装异步任务
function requestData(url) {
  // resolve 和 reject 这两个单词是形参，可以自由命名。大家的习惯写法是写成 resolve 和 reject
  const promise = new Promise((resolve, reject) => {
    const res = {
      retCode: 0,
      data: 'qiangu yihao`s data',
      errMsg: 'not login',
    };
    setTimeout(() => {
      if (res.retCode == 0) {
        // 网络请求成功
        resolve(res.data);
      } else {
        // 网络请求失败
        reject(res.errMsg);
      }
    }, 1000);
  });
  return promise;
}


// 调用异步任务
requestData('www.qianguyihao.com/index1').then(data => {
  console.log('异步任务执行成功:', data);
}).catch(err=> {
  console.log('异步任务执行失败:', err);
})

// 再次调用异步任务
requestData('www.qianguyihao.com/index2').then(data => {
  console.log('异步任务再次执行成功:', data);
}).catch(err=> {
  console.log('异步任务再次执行失败:', err);
})


// 调用异步任务（写法2）
/* 这段代码的写法比较啰嗦。一般推荐上面的写法。
const myPromise = requestData('www.qianguyihao.com/index1');
myPromise.then(data => {
  console.log('异步任务执行成功:', data);
});
myPromise.catch(err => {
  console.log('异步任务执行失败:', err);
});

const myPromise2 = requestData('www.qianguyihao.com/index2');
myPromise2.then(data => {
  console.log('异步任务执行成功:', data);
});
myPromise2.catch(err => {
  console.log('异步任务执行失败:', err);
});
*/
```
## Promise 的状态和回调函数
### Promise 对象的 3 种状态

在使用 Promise 时，我们可以将它划分为三种状态：

- `pending`：等待中。属于初始状态，既没有被兑现，也没有被拒绝。
    
- `fulfilled`：已兑现/已解决/成功。执行了`resolve()` 时，立即处于该状态，表示 Promise已经被**解决**，任务**执行成功**。
    
- `rejected`：已拒绝/失败。执行了 `reject()`时，立即处于该状态，表示 Promise已经被**拒绝**，任务**执行失败**。
    

具体解释：

1、Promise 的中文名翻译为“承诺”（一般不称呼中文名）。resolve 的中文翻译为“解决”，reject 的中文翻译为“拒绝”。

2、当 new Promise()执行之后，promise 对象的状态会被初始化为`pending`，这个是初始状态。`new Promise()`这行代码，括号里的内容是同步执行的。括号里可以再定义一 异步任务的 function，function 有两个参数：resolve 和 reject。如下：

- 如果异步任务成功了，请执行 resolve()，此时，promise 的状态会自动变为 fulfilled。
    
- 如果异步任务失败了，请执行 reject()，此时，promise 的状态会自动变为 rejected。
    

3、什么时候算成功，什么时候算失败呢？这是**你自己定**的，需要结合具体需求和业务逻辑灵活决定。

关于 promise 的状态改变，以及如何处理状态改变，伪代码及详细注释如下：

```
// 创建 promise 实例
const promise = new Promise((resolve, reject) => {
  //进来之后，promise 的状态为 pending
  console.log('同步代码'); //这行代码是同步的
  //开始执行异步操作（这里开始，根据具体需求写异步的代码，比如ajax请求 or 开启定时器）
  if (异步的ajax请求成功) {
    console.log('233');
    // 如果请求成功了，请写resolve()，此时，promise的状态会自动变为fulfilled（成功状态）
    resolve('请求成功，并传参');
  } else {
    // 如果请求失败了，请写reject()，此时，promise的状态会被自动变为rejected（失败状态）
    reject('请求失败，并传参');
  }
});
console.log('qianguyihao');

//调用promise的then()：开始处理成功和失败
promise.then(
  successValue => {
    // 处理 promise 的成功状态：如果promise的状态为fulfilled，则执行这里的代码
    console.log(successValue, '回调成功了'); // 这里的 successMsg 是前面的 resolve('请求成功，并传参')  传过来的参数
  },
  errorMsg => {
    //处理 promise 的失败状态：如果promise的状态为rejected，则执行这里的代码
    console.log(errorMsg, '回调失败了'); // 这里的 errorMsg 是前面的 reject('请求失败，并传参') 传过来的参数
  }
);
```
### Promise 的回调函数

Promise的回调函数，伪代码如下：

```
const promise = new Promise(executor);

// 【划重点】下面这两行代码是等价的，选其中一种写法即可。这两种写法没有区别，只是写法形式上的区别
promise.then(onFulfilled, onRejected);

promise.then(onFulfilled).catch(onRejected);
```

Promise是一个类，通过 `new Promise()` 进行**实例化**，构造出一个 Promise 实例对象。

1、Promise 的构造函数中需要传入一个参数，这个参数是一个回调函数，常用于处理异步任务。这个回调函数有一个专有名词叫 **executor**（执行器），因为在 `new Promise()` 时，这个函数会**立即执行**。

可以在该回调函数中传入两个参数：resolve 和 reject。我们可以在适当的时机执行 resolve()、reject()，用于改变当前 Promise 实例的状态到**成功**或**失败**。

（2）当Promise状态变为成功时，会触发 then() 方法里的回调函数的执行，对成功的返回结果进行处理。

（3）当Promise状态变为失败时，会触发 catch() 方法里的回调函数的执行，，对失败的返回结果进行处理。

2、`then()`方法的括号里面有两个参数，分别代表两个回调函数 **onFulfilled** 和 **onRejected**，这两个函数一直处于**监听状态**：

- 参数1：**成功的回调函数**。如果 Promise 的状态为 fulfilled（意思是：任务执行成功），则触发 onFulfilled 函数的执行。
    
- 参数2：**失败的回调函数**。如果 Promise 的状态为 rejected（意思是，任务执行失败），则触发 onRejected 函数的执行。
    

3、**只有 Promise 的状态被改变之后，才会走到 then() 或者 catch()**。也就是说，在 new Promise() 时，如果没有写 resolve()，则 promise.then() 不执行；如果没有写 reject()，则 promise.catch() 不执行。

4、resolve()和 reject()这两个方法，可以给 promise.then()、promise.catch()传递参数。

5、then() 可以被多次调用，会按照顺序执行。比如：

```
const promise = new Promise(executor);

// then() 可以被多次调用
promise.then(onFulfilled, onRejected);
promise.then(onFulfilled, onRejected);
```
### Promise的状态图
![[Promise的状态图.png]]
### Promise 的状态一旦改变，就不能再变

Promise 的状态一旦改变，就确定下来了，不能再变。也不能再次执行 resolve()或者 reject()来改变状态。Promise 的状态改变，是不可逆的。

代码举例：

```
const p = new Promise((resolve, reject) => {
    resolve(1); // 代码执行到这里时， promise状态是 fulfilled
   resolve(111); // 这行重复代码写了没用，等于没写
    reject(2); // 尝试修改状态为 rejected，是不行的。因为状态执行到上面的 resolve(1)时，已经被改变了。
});

p.then((res) => {
    console.log(res);
}).catch((err) => {
    console.log(err);
});
```

### new Promise() 是同步代码

`new Promise()`这行代码本身是同步的。promise 如果没有使用 resolve 或 reject 更改状态时，状态为 pending，里面的代码是同步代码。

**举例 1**：（重要）

```
// 会立即创建 Promise 实例
const promise1 = new Promise((resolve, reject) => {
  // 这行代码会立即执行
  console.log('qianguyihao1');
})

console.log(promise1); // 此时 promise1 的状态为 pending（准备阶段）

// 需要调用 promise2函数，才会创建 Promise 实例
function promise2() {
  return new Promise((resolve, reject) => {
    // 这行代码不会立即执行
    console.log('qianguyihao2');
  })
}
```

上面的代码中，我既没有写 reslove()，也没有写 reject()。那么，Promise 一直处于准备阶段。

此外，需要特别注意的是，promise1 中的 console.log() 会**立即执行**，因为**Promise的执行器函数在创建 Promise 实例时就会被调用，并立即开始执行其中的代码逻辑**。

**举例 2**：

```
new Promise((resolve, reject) => {
    console.log('promise1'); // 这行代码是同步代码，会立即执行
}).then((res) => {
    console.log('promise then:' + res); // 这行代码不会执行，因为前面没有写 resolve()，所以走不到 .then
});
```

打印结果：

```
promise1
```

上方代码，仔细看注释：如果前面没有写 `resolve()`，那么后面的 `.then`是不会执行的。

**举例 3**：

```
new Promise((resolve, reject) => {
    resolve();
    console.log('promise1'); // 代码1：同步任务，会立即执行
}).then(res => {
    console.log('promise  then'); // 代码2：异步任务中的微任务
});

console.log('千古壹号'); // 代码3：同步任务
```

打印结果：

```
promise1
千古壹号
promise  then
```

代码解释：

当完成异步任务之后，状态分为成功或失败，此时我们就可以用 reslove() 和 reject() 来修改 promise 的状态。

代码 1 是同步代码，所以最先执行。代码 2 是**微任务**里面的代码，所以要先等同步任务（代码 3）先执行完。当写完`resolve();`之后，就会立刻把 `.then()`里面的代码加入到微任务队列当中。
## Promise 封装定时器
### 传统写法

写法 1：

```
// 定义一个异步的延迟函数：异步函数结束1秒之后，再执行cb回调函数
function fun1(cb) {
    setTimeout(function () {
        console.log('即将执行cb回调函数');
        cb();
    }, 1000);
}

// 先执行异步函数 fun1，再执行回调函数 myCallback
fun1(myCallback);

// 定义回调函数
function myCallback() {
    console.log('我是延迟执行的cb回调函数');
}
```

写法 2：（精简版，更常见）

```
// 定义一个异步的延迟函数：异步函数结束1秒之后，再执行cb回调函数
function fun1(cb) {
    setTimeout(cb, 1000);
}

// 先执行异步函数fun1，再执行回调函数
fun1(function () {
    console.log('我是延迟执行的cb回调函数');
});
```

上⾯的例⼦就是最传统的写法，在异步结束后通过传入回调函数的方式执⾏函数。
### Promise 写法

```
function myPromise() {
    return new Promise((resolve) => {
        setTimeout(resolve, 1000);
    });
}

/* 【重要】上面的 myPromise 也可以写成：
function myPromise() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve();
        }, 1000);
    });
}
*/

// 先执行异步函数 myPromise，再执行回调函数
myPromise().then(() => {
    console.log('我是延迟执行的回调函数');
});
```
## Promise 封装 Ajax 请求
### 传统写法

```
// 封装 ajax 请求：传入回调函数 success 和 fail
function ajax(url, success, fail) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url);
    xmlhttp.send();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            success && success(xmlhttp.responseText);
        } else {
            // 这里的 && 符号，意思是：如果传了 fail 参数，就调用后面的 fail()；如果没传 fail 参数，就不调用后面的内容。因为 fail 参数不一定会传。
            fail && fail(new Error('接口请求失败'));
        }
    };
}

// 执行 ajax 请求
ajax(
    '/a.json',
    (res) => {
        console.log('qianguyihao 第一个接口请求成功:' + JSON.stringify(res));
    },
    (err) => {
        console.log('qianguyihao 请求失败:' + JSON.stringify(err));
    }
);
```

上面的传统写法里，定义和执行 ajax 时需要传⼊ success 和 fail 这两个回调函数，进而执行回调函数。

注意看注释，`callback && callback()`这种格式的写法，很常见。
### Promise 写法

有了 Promise 之后，我们不需要传入回调函数，而是：

- 先将 promise 实例化；
    
- 然后在原来执行回调函数的地方，改为执行对应的改变 promise 状态的函数；
    
- 并通过 then ... catch 或者 then ...then 等写法，实现链式调用，提高代码可读性。
    

和传统写法相比，promise 在写法上的大致区别是：定义异步函数的时候，将 callback 改为 resolve 和 reject，待状态改变之后，我们在外面控制具体执行哪些函数。

写法 1：

```
// 封装 ajax 请求：传入回调函数 success 和 fail
function ajax(url, success, fail) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url);
    xmlhttp.send();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            success && success(xmlhttp.responseText);
        } else {
            // 这里的 && 符号，意思是：如果传了 fail 参数，就调用后面的 fail()；如果没传 fail 参数，就不调用后面的内容。因为 fail 参数不一定会传。
            fail && fail(new Error('接口请求失败'));
        }
    };
}

// 第一步：model层的接口封装
function promiseA() {
    return new Promise((resolve, reject) => {
        ajax('xxx_a.json', (res) => {
            // 这里的 res 是接口的返回结果。返回码 retCode 是动态数据。
            if (res.retCode == 0) {
                // 接口请求成功时调用
                resolve('request success' + res);
            } else {
                // 接口请求失败时调用
                reject({ retCode: -1, msg: 'network error' });
            }
        });
    });
}

// 第二步：业务层的接口调用。这里的 data 就是 从 resolve 和 reject 传过来的，也就是从接口拿到的数据
promiseA()
    .then((res) => {
        // 从 resolve 获取正常结果：接口请求成功后，打印接口的返回结果
        console.log(res);
    })
    .catch((err) => {
        // 从 reject 获取异常结果
        console.log(err);
    });
```

上方代码中，当从接口返回的数据`data.retCode`的值（接口返回码）不同时，可能会走 resolve，也可能会走 reject，这个由你自己的业务决定。

接口返回的数据，一般是`{ retCode: 0, msg: 'qianguyihao' }` 这种 json 格式， retCode 为 0 代表请求接口成功，所以前端对应会写`if (res.retCode == 0)`这样的逻辑。

另外，上面的写法中，是将 promise 实例定义成了一个**函数** `promiseA`。我们也可以将 promise 实例定义成一个**变量** `promiseB`，达到的效果和上面的代码是一模一样的。写法如下：（写法上略有区别）

写法 2：

```
// 第一步：model层的接口封装
const promiseB = new Promise((resolve, reject) => {
    ajax('xxx_a.json', (res) => {
        // 这里的 res 是接口的返回结果。返回码 retCode 是动态数据。
        if (res.retCode == 0) {
            // 接口请求成功时调用
            resolve('request success' + res);
        } else {
            // 接口请求失败时调用
            reject({ retCode: -1, msg: 'network error' });
        }
    });
});

// 第二步：业务层的接口调用。这里的 data 就是 从 resolve 和 reject 传过来的，也就是从接口拿到的数据
promiseB
    .then((res) => {
        // 从 resolve 获取正常结果
        console.log(res);
    })
    .catch((err) => {
        // 从 reject 获取异常结果
        console.log(err);
    });
```

注意，如果你用的是写法 1（将 promise 实例定义为函数），则调用 promise 的时候是`promiseA().then()`，如果你用的是写法 2（将 promise 实例定位为函数），则调用的时候用的是`promiseB.then()`。写法 1 多了个括号，不要搞混了。
## resolve() 传入的参数（重要）
执行 resolve()之后，Promise 的状态一定会变成 fulfilled 吗？这是不一定的。

严格来说，在我们调用 resolve 时，如果 resolve()的参数中传入的值**本身不是一个Promise**，那么会将该 promise 的状态变成 fulfilled。

resolve()的参数中，可以传入哪些值，Promise会进入哪种状态呢？具体情况如下：

- 情况1：如果resolve()中传入**普通的值或者普通对象**（包括 undefined），那么Promise 的状态为fulfilled。这个值会作为then()回调的参数。这是最常见的情况。
- 情况2：如果resolve()中传入的是**另外一个新的 Promise**，那么原 Promise 的状态将**交给新的 Promise 决定**。
- 情况3：如果resolve()中传入的是一个对象，并且这个对象里有实现then()方法（这种对象称为 **thenable** 对象），那就会执行该then()方法，并且根据**then()方法的结果来决定Promise的状态**。

情况3中，我们通常称这个对象为 thenable 对象。thenable 的意思是，在某个对象或者函数中定义了一个 then() 方法，我们就称其为 thenable 对象/thenable函数。注意，thenable对象里面的那个单词只能写 then，不能写其他的单词；如果写其他的单词，就不是 thenable 对象了，就不符合情况3，而是符合情况1。

扩展一下：reject()的参数中可以传入什么值呢？无论传入什么值，Promise 都会直接进入 rejected 状态，并触发 catch() 方法的执行。
### resolve() 中传入新的 Promise

代码举例：

```
const promise1 = new Promise((resolve, reject) => {
  resolve(promise2);
});

const promise2 = new Promise((resolve, reject) => {
  reject('promise2 的 reject');
});

promise1
  .then(res => {
    console.log('qianguyihao then');
    console.log(res);
  })
  .catch(err => {
    console.log('qianguyihao catch');
    console.log(err);
  });
```

打印结果：

```
qianguyihao catch
promise2 的 reject
```

代码解释：

promise1 在执行resolve时，传入的是 promise2。那么，promise1接下来的状态将交给 promise2 处理。因为 promise2 执行的是 reject()，所以 promise1 的状态进入 rejected，执行 catch() 方法。

上方代码中，如果把 promise1 和 promise2 的顺序换一下的话， 代码会报错：

```
const promise1 = new Promise((resolve, reject) => {
  resolve(promise2);
});

const promise2 = new Promise((resolve, reject) => {
  reject('promise2 的 reject');
});

promise1
  .then(res => {
    console.log('qianguyihao then');
  })
  .catch(err => {
    console.log('qianguyihao catch');
    console.log(err);
  });
```
### resolve()中传入 thenable 对象

代码举例：

```
const promise1 = new Promise((resolve, reject) => {
  // resolve 里传入了一个 thenable 对象，里面有一个 then()方法，then()方法里执行的是 reject()
  resolve({
    name: 'qianguyihao',
    then: (resolve, reject) => {
      // 可以执行 resolve，也可以执行 reject，这里以 reject 为例
      reject('thenable reject');
    },
  });
});

promise1
  .then(res => {
    console.log('qianguyihao then');
    console.log(res);
  })
  .catch(err => {
    console.log('qianguyihao catch');
    console.log(err);
  });
```

打印结果：

```
qianguyihao catch
thenable reject
```

代码解释：

promise1 在执行resolve时，传入的是一个 thenable 对象。thenable 对象里有一个 then()方法。那么，promise1接下来的状态将由 thenable 对象 里的 then() 方法决定。当前的代码中， then() 里执行的是 reject()，所以 promise1 的状态进入 rejected，执行 catch() 方法。

上方代码中，如果把 thenable 对象里的单词`then`改成`then1`会怎么样呢？那它就不是 thenable 对象，只是一个普通的对象，代码如下：

```
const promise1 = new Promise((resolve, reject) => {
  // resolve 里传入了一个 thenable 对象，里面有一个 then()方法，then()方法里执行的是 reject()
  resolve({
    name: 'qianguyihao',
    // 把 单词 then 改成 then1，就不符合 thenable 对象 的特征了
    then1: (resolve, reject) => {
      reject('thenable resolve');
    },
  });
});

promise1
  .then(res => {
    console.log('qianguyihao then');
    console.log(JSON.stringify(res));
  })
  .catch(err => {
    console.log('qianguyihao catch');
    console.log(err);
  });
```

## Promise实例的方法
### Promise 实例的方法简介

Promise 的 API 分为两种：

- Promise 实例的方法（也称为：Promis的实例方法）
- Promise 类的方法（也称为：Promise的静态方法）

Promise **实例**的方法：我们需要实例化 Promise，也就是先 new 一个 Promise 实例对象，然后通过 Promise 实例去调用 `then`、`catch`、`finally`等方法。这几个方法就是 Promise 的实例方法。

Promise 实例提供了如下方法：

- promise.then()：异步任务成功的回调函数。
    
- promise.catch()：异步任务失败的回调函数。
    
- promise.finaly()：异步任务无论成功与否，都会执行的回调函数。
### Promise 实例的 then()方法

then()方法是 Promise实例上的一个方法。它其实是放在Promise的原型上的 `Promise.prototype.then`。
#### then()方法的参数

then()方法可以接收一个参数，也可以接收两个参数。两个参数时，分别代表两个回调函数，这两个函数一直处于**监听状态**：

- 参数1：当 Promise 的状态变为 fulfilled（意思是：任务执行成功）时会立即执行的回调函数。
    
- 参数2：当 Promise 的状态为 rejected（任务执行失败）时会立即执行的回调函数。
    

下面这两种写法是等价的。处理 rejected 失败状态的回调函数，既可以放在 then() 方法的第二个参数里，也可以单独放在 catch() 方法的参数里。

写法1：

```
const promise = new Promise((resolve, reject) => {
  reject('qianguyihao');
});

promise.then(
  res => {
    console.log('res:', res);
  },
  err => {
    console.log('err:', err);
  }
);
```

写法2：

```
const promise = new Promise((resolve, reject) => {
  reject('qianguyihao');
});

promise
  .then(res => {
    console.log('res:', res);
  })
  .catch(err => {
    console.log('err:', err);
  });
```

#### then()方法可以被多次调用

一个 Promise 的 then() 方法可以被多次调用。每次调用时我们都可以传入对应fulfilled状态的回调函数。当 Promise 的状态变为 fulfilled 时，这些回调函数都会被执行。

then被调用多次的伪代码：

```
const myPromise = new Promise();

myPromise.then();
myPromise.then();
myPromise.then();
```

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('qianguyihao');
});

myPromise.then(res => {
  console.log('成功回调1');
  console.log('res1:', res);
});

myPromise.then(res => {
  console.log('成功回调2');
  console.log('res2:', res);
});

myPromise.then(res => {
  console.log('成功回调3');
  console.log('res3', res);
});
```
当 myPromise 状态为 fulfilled 时，下面的四个 then() 方法**都在监听**，所以这四个 then() 方法都会收到状态确定的通知，进而都会执行。
### then() 方法的返回值
then()方法本身是有返回值的，它会返回一个**新的Promise对象**。因为 then()方法的返回值永远是一个 Promise 对象，所以我们才可以对它进行**链式调用**。

Promise 链式调用的伪代码：

```
// 伪代码
myPromise.then().then().catch()
```

上方代码中，因为 myPromise.then() 的返回值本身就是一个 Promise，所以才可以继续调用 then()、继续调用 catch()。

那么，**then()方法返回的 Promise 对象处于什么状态呢**？then()方法的参数里，是一个回调函数。这取决于回调函数的返回值是什么。情况如下：

1、当then()方法中的回调函数在执行时，那么Promise 处于pending状态。

2、当 then()方法中的回调函数中，手动 return 一个返回值时，那么 Promise 的状态取决于返回值的类型。当返回值这行代码执行完毕后， Promise 会立即决议，进入确定状态（成功 or 失败）。具体情况如下：

- 情况1：如果没有返回值（相当于 return undefined），或者返回值是**普通值/普通对象**，那么 Promise 的状态为fulfilled。这个值会作为fulfilled 状态的回调函数的参数值。
- 情况2：如果返回值是**另外一个新的 Promise**，那么原 Promise 的状态将**交给新的 Promise 决定**，这两个Promise 的状态一致。
- 情况3：如果返回值是一个对象，并且这个对象里有实现then()方法（这种对象称为 **thenable** 对象），那就会执行该then()方法，并且根据**then()方法的结果来决定Promise的状态**。

还有一种特殊情况：

- 情况4：当then()方法传入的回调函数遇到异常或者手动抛出异常时，那么， Promise 处于rejected 状态，并将抛出的错误作为 rejected 状态的回调函数的参数值。

**小结**：then()方法里，我们可以通过 return **传递结果和状态**给下一个新的Promise。

#### 默认返回值

如果then()方法的回调函数里没写返回值（相当于 return undefined），那么then()方法的返回值是一个新的Promise。新 Promise 的状态为fulfilled，其then()方法里，res的值为 undefined。

then() 链式调用的代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('qianguyihao');
});

myPromise
  .then(res => {
    console.log('成功回调1');
    console.log('res1:', res);
    /*
    这里虽然什么都没写，底层默认写了如下代码：
    return new Promise((resolve, reject) => {
  		resolve(); // resolve() 的参数是空，相当于 resolve(undefined)
    })
    */
  })
  .then(res => {
    console.log('成功回调2');
    console.log('res2:', res);
  })
  .then(res => {
    console.log('成功回调3');
    console.log('res3', res);
  });
```

打印结果：

```
成功回调1
res1: qianguyihao

成功回调2
res2: undefined

成功回调3
res3：undefined
```

代码解释：

第一个 then()里的回调，是由 myPromise 进行决议。第二个then()、第三个then() 也在**等待决议**。

但是，**第二个 then() 的回调是由第一个 then()传入的回调函数，返回的 Promise 进行决议**；第三个 then() 的回调是由第二个 then()传入的回调函数，返回的 Promise 进行决议，以此类推。所以，这两个then()里面的打印参数的结果是 undefined，并没有打印 myPromise 的决议结果。

换句话说，第一个 then() 在等待 myPromise 的决议结果，有决议结果后执行；第二个 then() 在等待第一个 then()参数里返回的新 Promise的决议结果，有决议结果后执行；第三个 then() 在等待第二个 then()参数里返回的新 Promise的决议结果，有决议结果后执行。
#### 返回普通值：通过 return 传递数据结果

我们也可以在 then()方法的回调函数里，手动 return 自己想要的数据，比如一个普通值 value1。这个普通值就可以传递给下一个新的Promise。新 Promise 的状态为fulfilled，其then()方法里，res的值为 value1。

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('1号');
});

myPromise
  .then(res => {
    console.log('res1:', res);
    // return一个普通值，把这个值传递给下一个Promise
    return '2号';
  	/*
  	上面这行 return，相当于：
  	return new Promise((resolve, reject)=> {
  		resolve('2号');
  	})
  	*/
  })
  .then(res => {
  	// res可以接收到上一个 Promise 传递的值
    console.log('res2:', res);
  })
  .then(res => {
    console.log('res3:', res);
  });
```
#### 返回新的 Promise

情况1、在 then() 方法的回调函数中 return 一个成功的新 Promise，那么，then()返回的Promise 也是成功状态。相当于把新Promise的成功结果传递出去。代码举例：

```
const promise1 = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled 1');
});

const promise2 = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled 2');
});

promise1
  .then(res => {
    console.log('res1:', res);
    return promise2;
  })
  .then(res => {
    // 监听 promise2 的成功状态
    console.log('res2:', res);
  })
  .then(res => {
    console.log('res3', res);
  });
```

打印结果：

```
res1: qianguyihao fulfilled 1
res2: qianguyihao fulfilled 2
res3 undefined
```

情况2、在 then() 方法的回调函数中 return 一个失败的新 Promise，那么，then()返回的Promise 也是失败状态。再继续往下走，会怎么样？相当于把新Promise 的失败原因传递出去。代码举例：

```
const promise1 = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled 1');
});

const promise2 = new Promise((resolve, reject) => {
  reject('qianguyihao rejected 2');
});

promise1
  .then(res => {
    console.log('res1:', res);
    // return 一个 失败的 Promise
    return promise2;
  })
  .then(res => {
    console.log('res2:', res);
  }, err => {
    // 如果 promise2 为失败状态，可以通过 then() 的第二个参数（即失败的回调函数）捕获异常，然后就可以继续往下执行其他的代码
    console.log('err2:', err);
   // 这里相当于 return undefined
  })
  .then(res => {
    console.log('res3', res);
  }, err => {
    console.log('err3:', err);
  });
```

打印结果：

```
res1: qianguyihao fulfilled 1
err2: qianguyihao rejected 2
res3: undefined
```

上方代码可以看到，第二个Promise走的是失败回调，这很容易理解。重点是，最后一个 Promise 走的是成功回调，这很出人意料。我们稍后学习 catch()方法的返回值后，就能看懂。**这例子很经典，一定要记住**。

情况3：在 then() 方法的回调函数中 return 一个 pending 状态的新 Promise，那么 then() 返回的Promise状态也是 pending。
#### 返回 thenable 对象

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled 1');
});

myPromise
  .then(res => {
    console.log('res1:', res);
    return {
      then: (resolve, reject) => {
        resolve('thenable fulfilled');
      },
    };
  })
  .then(res => {
    console.log('res2:', res);
  })
  .then(res => {
    console.log('res3', res);
  });
```

打印结果：

```
res1: qianguyihao fulfilled 1
res2: thenable fulfilled
res3 undefined
```
#### then() 中抛出异常

当then()方法传入的回调函数遇到异常或者手动抛出异常时，那么，then()所返回的**新的 Promise 会进入rejected 状态**，进而触发新Promise 的 catch() 方法的执行，做异常捕获。

#### 特殊情况：then() 中传入非函数时，会发生值穿透

在Promise的`then()`方法中，如果传入一个非函数作为参数，JS 会将其忽略，并且将前一个 Promise 的结果值传递给下一个`then()`方法。这意味着如果你在`then()`中传入非函数参数，它将被视为一个空操作，而不会对Promise链产生任何影响。

“值穿透”的意思是，传入的非函数值会被忽略。

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('Hello');
});

myPromise
  .then('Invalid Argument')
  .then(res1 => {
    console.log('res1:', res1);
    return 'World';
  })
  .then(res2 => {
    console.log('res2:', res2);
  });
```

打印结果：

```
res1: Hello
res2: World
```
### Promise 实例的 catch() 方法
catch()方法是 Promise实例上的一个方法。它其实是放在Promise的原型上的 `Promise.prototype.catch`。
#### catch() 方法的参数

catch()方法可以接收一个参数。这个参数是一直处于**监听状态**的回调函数。当 Promise 的状态为 rejected（任务执行失败）时会立即执行这个回调函数。

代码举例：

```
const promise = new Promise((resolve, reject) => {
  reject('qianguyihao reject');
});

promise
  .then(res => {
    console.log('res:', res);
  })
  .catch(err => {
    console.log('err:', err);
  });
```

打印结果：

```
err: qianguyihao reject
```
#### catch() 方法可以被多次调用

一个 Promise 的 catch() 方法可以被多次调用。每次调用时我们都可以传入对应 rejected 状态的回调函数。当 Promise 的状态变为 rejected 时，这些回调函数都会被执行。

catch() 被调用多次的伪代码：

```
const myPromise = new Promise();

myPromise.catch();
myPromise.catch();
myPromise.catch();
```

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  reject('qianguyihao rejected');
});

myPromise.catch(err => {
  console.log('失败回调1');
  console.log('err1:', err);
});

myPromise.catch(err => {
  console.log('失败回调2');
  console.log('err2:', err);
});

myPromise.catch(err => {
  console.log('失败回调3');
  console.log('err3:', err);
});
```

打印结果：

```
失败回调1
err1: qianguyihao rejected

失败回调2
err2: qianguyihao rejected

失败回调3
err3: qianguyihao rejected
```

代码解释：

当 myPromise 状态为 rejected 时，下面的四个 catch() 方法**都在监听**，所以这四个 catch() 方法都会收到状态确定的通知，进而都会执行。
### catch() 方法的返回值（重要）

与 then() 方法类似，catch()方法默认也是有返回值的，它会返回一个**新的Promise对象**。因为 catch()方法的返回值永远是一个 Promise 对象，所以我们才可以对它进行**链式调用**。

Promise 链式调用的伪代码：

```
// 伪代码
myPromise.then().then().catch().then()
```

上方代码中，因为 myPromise.catch() 的返回值本身就是一个 Promise，所以才可以继续调用 then()、继续调用 catch()。

与 then() 方法类似，**catch()方法返回的 Promise 对象处于什么状态呢**？catch()方法的参数里，是一个回调函数。这取决于回调函数的返回值是什么。情况如下：

1、当catch()方法中的回调函数在执行时，那么Promise 处于 pending 状态。

2、当 catch方法中的回调函数中，手动 return 一个返回值时，那么 Promise 的状态取决于返回值的类型。当返回值这行代码执行完毕后， Promise 会立即决议，进入确定状态（成功 or 失败），进而触发下一个then/catch 函数的执行。同时可以给下一个 then/catch 传递参数。具体情况如下：

- 情况1：如果没有返回值（相当于 return undefined），或者返回值是**普通值/普通对象**，那么 Promise 的状态为fulfilled。这个值会作为then()回调的参数。
- 情况2：如果返回值是**另外一个新的 Promise**，那么原 Promise 的状态将**交给新的 Promise 决定**。这两个Promise 的状态一致。
- 情况3：如果返回值是一个对象，并且这个对象里有实现then()方法（这种对象称为 **thenable** 对象），那就会执行该then()方法，并且根据**then()方法的结果来决定Promise的状态**。

还有一种特殊情况：

- 情况4：当catch()方法传入的回调函数遇到异常或者手动抛出异常时，那么， Promise 处于rejected 状态。

**小结**：catch()方法里，我们可以通过 return **传递结果**给下一个新的Promise。

#### 默认返回值

如果catch()方法的回调函数里没写返回值（相当于 return undefined），那么catch()方法的返回值是一个新的Promise。新 Promise 的状态为fulfilled，其then()方法里，res的值为 undefined。

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  reject('qianguyihao rejected');
});

myPromise
  .catch(err => {
    console.log('err:', err);
    /*
    这里虽然什么都没写，底层默认写了如下代码：
    return new Promise((resolve, reject) => {
      resolve(undefined); // resolve() 的参数是空
    })
    */
  })
  .then(res => {
    console.log('res:', res);
  });
```

打印结果：

```
err: qianguyihao rejected
res: undefined
```

#### 返回普通值

我们也可以在 catch()方法的回调函数里，手动 return 自己想要的数据，比如一个普通值 value1。这个普通值就可以传递给下一个新的Promise。新 Promise 的状态为fulfilled，其then()方法里，res的值为 value1。

代码举例：

```
const myPromise = new Promise((resolve, reject) => {
  reject('1号');
});

myPromise
  .catch(err => {
    console.log('err1:', err);
    return '2号';
    /*
    上面这行 return，相当于：
    return new Promise((resolve, reject)=> {
      resolve('2号');
    })
    */
  })
  .then(res => {
    console.log('res2:', res);
  })
  .then(res => {
    console.log('res3:', res);
  });
```

返回结果：

```
err1: 1号
res2: 2号
res3: undefined
```
### catch() 方法的执行时机
#### Promise 抛出 rejected 异常时，一定要捕获并处理

当 Promise 状态为 rejected 时，表示抛出异常，如果不处理失败的回调，行不行呢？不行，会报错。代码举例：

```
      const promise = new Promise((resolve, reject) => {
        // 在这里抛出异常
        reject('qianguyihao reject');
      });

      promise.then(res => {
        console.log('res:', res);
      });
```
报错的意思是：未捕获 rejected 失败状态的 Promise 异常。必须要加一个 catch() 进行捕获。

书写 Promise 时，比较好的习惯是，无论如何都要在末尾写一个 catch() 方法。
#### 可在 then() 中通过 throw 抛出异常

先来看一段代码：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('aaa');
});

myPromise
  .then(res => {
    console.log('res1:', res);
   // 如果我想在这里 return 一个失败状态的promise，该怎么做？
  })
  .then(res => {
    console.log('res2:', res);
  })
  .catch(err => {
    console.log('err:', err);
  });
```

注意看注释，如果在那个位置return 一个失败状态的Promise，该怎么做？

做法1：

```
return new Promise((resolve, reject)=> {
  reject('第二个 promise 执行失败');
})
```

做法2：

```
throw new Error('第二个 Promise 执行失败');
```

做法2比做法1更为常用，完整代码如下：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('aaa');
});

myPromise
  .then(res => {
    console.log('res1:', res);
    // 抛出异常：相当于 return 一个失败状态的 Promise
    throw new Error('第二个 Promise 执行失败');
  })
  .then(res => {
    console.log('res2:', res);
  })
  .catch(err => {
    console.log('err:', err);
  });
```

打印结果：

```
res1: aaa
err: Error: 第二个 Promise 执行失败
```

当通过 throw 抛出异常后，当前 then() 里的后续代码会暂停执行，后续的 then() 也会暂停执行，直接往后走到最近的 catch()。

throw 这种写法在实战开发中很常用，需要理解并记住。
#### 找到最近的 catch() 去执行

我们先来看一段代码：

```
const myPromise = new Promise((resolve, reject) => {
  reject('qianguyihao rejected');
});

myPromise
  .then(res => {
    console.log('res1:', res);
  })
  .then(res => {
    console.log('res2:', res);
  })
  .catch(err => {
    console.log('err:', err);
  });
```

打印结果：

```
err: qianguyihao rejected
```

上方代码中的 catch() 是属于哪个 Promise 实例的方法呢？其实没有严格的界限。它既可以捕获 myPromise的异常，也可以捕获那两个 then()的异常，就是这么灵活。

再来看一段代码：

```
const myPromise = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled');
});

myPromise
  .then(res => {
    console.log('res1:', res);
    // 遇到异常（或者任务失败）后，会找到最近的 catch() 去执行
    throw new Error('not login')
  })
  .then(res => {
    console.log('res2:', res);
  }, err => {
    console.log('err2:', err);
  })
  .catch(err => {
    console.log('err3:', err);
  });
```

打印结果：

```
res1: qianguyihao fulfilled
err2: Error: not login
```

请记住，myPromise 的状态变为失败时，它会找到**最近的**那个**失败回调函数**并执行。这是 Promise的内部机制。
### 处理失败状态的两种写法
我们有两种写法可以捕获 Promise的失败/异常状态：

- 写法 1：单独写 catch() 方法作为失败的回调函数。
    
- 写法 2：then()方法里可以传两个参数，第⼀个参数是成功时的回调函数，第⼆个参数是失败时的回调函数。
#### 代码格式

这两种写法的**代码格式**如下：

```
// 第一步：model层的接口封装
const myPromise = new Promise((resolve, reject) => {
  // 这里做异步任务（比如 ajax 请求接口，或者定时器），然后执行 resolve 或者 reject。
	...
  ...
});

const onFulfilled = (res) => {
  console.log(res);
};

const onRejected = function (err) {
  console.log(err);
};

// 写法1：通过 catch 方法捕获失败状态的Promise
myPromise.then(onFulfilled).catch(onRejected);

// 写法2：then()方法里可以传两个参数，第⼀个参数是成功时的回调函数，第⼆个参数是失败时的回调函数。
myPromise.then(onFulfilled, onRejected);
```

注意事项：

1、上面这两种写法是等价的，选其中一种写法即可。这两种写法几乎没有区别。

2、有一点点区别：

- `myPromise.then(onFulfilled).catch(onRejected)`：既可以捕获到 myPromise 的异常，**也可以捕获到 then() 里面的异常**（划重点）。
- `myPromise.then(onFulfilled, onRejected)`：只能捕获到 promise的异常，无法捕获then()里面的异常。

知识拓展：`myPromise.catch().then()`这种写法，只能捕获到 myPromise 里面的异常。
#### 代码举例

这两种写法在实战开发中的**代码举例**如下：

```
function myPromise() {
    return new Promise((resolve, reject) => {
        // 这里做异步任务（比如 ajax 请求接口，或者定时器）
            ...
            ...
    });
}

// 写法1
myPromise()
    .then((res) => {
        // 从 resolve 获取正常结果
        console.log('接口请求成功时，走这里');
        console.log(res);
    })
    .catch((err) => {
        // 从 reject 获取异常结果
        console.log('接口请求失败时，走这里');
        console.log(err);
    })
    .finally(() => {
        console.log('无论接口请求成功与否，都会走这里');
    });


// 写法 2：（和写法 1 等价）
myPromise()
    .then(
        (res) => {
            // 从 resolve 获取正常结果
            console.log('接口请求成功时，走这里');
            console.log(res);
        },
        (err) => {
            // 从 reject 获取异常结果
            console.log('接口请求失败时，走这里');
            console.log(err);
        }
    )
    .finally(() => {
        console.log('无论接口请求成功与否，都会走这里');
    });
```

**代码解释**：写法 1 和写法 2 的作用是等价的。只不过，写法 2 是把 catch 里面的代码作为 then 里面的第二个参数而已。
### Promise 实例的 finally() 方法

finally() 方法是在ES9（ES 2018）中新增的一个特性，表示 Promise 对象无论变成 fulfilled 状态 还是 rejected 状态，finally() 里传入的回调函数都会被执行。

finally() 里可传入一个参数，这个参数是一个回调函数。回调函数不传参数，因为前面无论是 fulfilled 状态，还是 rejected状态，这个回调函数都会执行。

finally() 方法很实用，可以避免我们写很多重复代码，它的执行时机也有很重要的应用场景。

代码举例：

```
const promise1 = new Promise((resolve, reject) => {
  resolve('promise1 fulfilled');
});

const promise2 = new Promise((resolve, reject) => {
  reject('promise2 rejected');
});

promise1
  .then(res => {
    console.log('res1:', res);
  })
  .catch(err => {
    console.log('err1:', err);
  })
  .finally(() => {
    console.log('promise1 决议后都会执行的代码');
  });

promise2
  .then(res => {
    console.log('res2:', res);
  })
  .catch(err => {
    console.log('err2:', err);
  })
  .finally(() => {
    console.log('promise2 决议后都会执行的代码');
  });
```

打印结果：

```
res1: promise1 fulfilled
err2: promise2 rejected
promise1 决议后都会执行的代码
promise2 决议后都会执行的代码
```
## Promise的链式调用
实际开发中，我们经常需要先后请求多个接口：发送第一次网络请求后，等待请求结果；有结果后，然后发送第二次网络请求，等待请求结果；有结果后，然后发送第三次网络请求。以此类推。

比如说：在请求完接口 1 的数据`data1`之后，需要根据`data1`的数据，继续请求接口 2，获取`data2`；然后根据`data2`的数据，继续请求接口 3。换而言之，现在有三个网络请求，请求 2 必须依赖请求 1 的结果，请求 3 必须依赖请求 2 的结果。

如果按照往常的写法，会有三层回调，陷入“回调地狱”的麻烦。

这种场景其实就是接口的多层嵌套调用，在前端的异步编程开发中，经常遇到。有了 Promise 以及更高级的写法之后，我们可以把多层嵌套调用按照**线性**的方式进行书写，非常优雅。也就是说：Promise 等ES6的写法可以把原本的**多层嵌套写法**改进为**链式写法**。
### Promise 链式调用：封装多次网络请求
#### ES5 中的传统嵌套写法

伪代码举例：

```
// 封装 ajax 请求：传入请求地址、请求参数，以及回调函数 success 和 fail。
function requestAjax(url, params, success, fail) {
  var xhr = new xhrRequest();
  // 设置请求方法、请求地址。请求地址的格式一般是：'https://api.example.com/data?' + 'key1=value1&key2=value2'
  xhr.open('GET', url);
  // 设置请求头（如果需要）
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      success && success(xhr.responseText);
    } else {
      fail && fail(new Error('接口请求失败'));
    }
  };
}

// ES5的传统写法，执行 ajax 请求，层层嵌套
requestAjax(
  'https://api.qianguyihao.com/url_1', params_1,
  res1 => {
    console.log('第一个接口请求成功:' + JSON.stringify(res1));
    // ajax嵌套调用
    requestAjax('https://api.qianguyihao.com/url_2', params_2, res2 => {
      console.log('第二个接口请求成功:' + JSON.stringify(res2));
      // ajax嵌套调用
      requestAjax('https://api.qianguyihao.com/url_3', params_3, res3 => {
        console.log('第三个接口请求成功:' + JSON.stringify(res3));
      });
    });
  },
  (err1) => {
    console.log('qianguyihao 请求失败:' + JSON.stringify(err1));
  }
);
```

上面的代码层层嵌套，可读性很差，而且出现了我们常说的回调地狱问题。
#### Promise 的嵌套写法

改用 ES6 的 Promise 之后，写法上会稍微改进一些。代码举例如下：

```
// 【公共方法层】封装 ajax 请求的伪代码。传入请求地址、请求参数，以及回调函数 success 和 fail。
function requestAjax(url, params, success, fail) {
  var xhr = new xhrRequest();
  // 设置请求方法、请求地址。请求地址的格式一般是：'https://api.example.com/data?' + 'key1=value1&key2=value2'
  xhr.open('GET', url);
  // 设置请求头（如果需要）
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      success && success(xhr.responseText);
    } else {
      fail && fail(new Error('接口请求失败'));
    }
  };
}

// 【model层】将接口请求封装为 Promise
function requestData1(params_1) {
  return new Promise((resolve, reject) => {
    requestAjax('https://api.qianguyihao.com/url_1', params_1, res => {
      // 这里的 res 是接口返回的数据。返回码 retCode 为 0 代表接口请求成功。
      if (res.retCode == 0) {
        // 接口请求成功时调用
        resolve('request success' + res);
      } else {
        // 接口请求异常时调用
        reject({ retCode: -1, msg: 'network error' });
      }
    });
  });
}


// requestData2、requestData3的写法与 requestData1类似。他们的请求地址、请求参数、接口返回结果不同，所以需要挨个单独封装 Promise。
function requestData2(params_2) {
  return new Promise((resolve, reject) => {
    requestAjax('https://api.qianguyihao.com/url_2', params_2, res => {
      if (res.retCode == 0) {
        resolve('request success' + res);
      } else {
        reject({ retCode: -1, msg: 'network error' });
      }
    });
  });
}

function requestData3(params_3) {
  return new Promise((resolve, reject) => {
    requestAjax('https://api.qianguyihao.com/url_3', params_3, res => {
      if (res.retCode == 0) {
        resolve('request success' + res);
      } else {
        reject({ retCode: -1, msg: 'network error' });
      }
    });
  });
}

// 【业务层】Promise 调接口的嵌套写法。温馨提示：这段代码在接下来的学习中，会被改进无数次。
// 发送第一次网络请求
requestData1(params_1).then(res1 => {
  console.log('第一个接口请求成功:' + JSON.stringify(res1));

  // 发送第二次网络请求
  requestData1(params_2).then(res2 => {
    console.log('第二个接口请求成功:' + JSON.stringify(res2));

    // 发送第三次网络请求
    requestData1(params_3).then(res3 => {
      console.log('第三个接口请求成功:' + JSON.stringify(res3));
    })
  })
})
```

上方代码非常经典。在真正的实战中，我们往往需要嵌套请求**多个不同的接口**，它们的接口请求地址、要处理的 resolve 和 reject 的时机、业务逻辑往往是不同的，所以需要分开封装不同的 Promise 实例。也就是说，如果要调三个不同的接口，建议单独封装三个不同的 Promise 实例：requestData1、requestData2、requestData3。

这三个 Promise 实例，最终都需要调用底层的公共方法 requestAjax()。每个公司都有这样的底层方法，里面的代码会做一些公共逻辑，比如：封装原生的 ajax请求，用户登录态的校验等等；如果没有这种公共方法，你就自己写一个，为组织做点贡献。

但是，细心的你可能会发现：上面的最后10行代码仍然不够优雅，因为 Promise 在调接口时出现了嵌套的情况，实际开发中如果真这么写的话，是比较挫的，阅读性非常差，我不建议这么写。要怎么改进呢？这就需要用到 Promise 的**链式调用**。
#### Promise 的链式调用写法（重要）

针对多个不同接口的嵌套调用，采用 Promise 的**链式调用**写法如下：（将上方代码的最后10行，改进如下）

```
requestData1(params_1).then(res1 => {
  console.log('第一个接口请求成功:' + JSON.stringify(res1));
  // 【关键代码】继续请求第二个接口。如果有需要，也可以把 res1 的数据传给 requestData2()的参数
  return requestData2(res1);
}).then(res2 => {
  console.log('第二个接口请求成功:' + JSON.stringify(res2));
  // 【关键代码】继续请求第三个接口。如果有需要，也可以把 res2 的数据传给 requestData3()的参数
  return requestData3(res2);
}).then(res3 => {
  console.log('第三个接口请求成功:' + JSON.stringify(res3));
}).catch(err => {
  console.log(err);
})
```

上面代码中，then 是可以链式调用的，一旦 return 一个新的 Promise 实例之后，后面的 then() 就可以作为这个新 Promise 在成功后的回调函数。这种**扁平化**的写法，更方便维护，可读性更好；并且可以更好的**管理**请求成功和失败的状态。

这段代码很经典，你一定要多看几遍，多默写几遍，倒背如流也不过分。如果你平时的异步编程代码能写到这个水平，说明你对 Promise 已经入门了，因为绝大多数人都是用的这个写法。

其实还有更高级、更有水平的写法，那就是用生成器、用 async ... await 来写Promise的链式调用，也就是改进上面的十几行代码。你把它掌握了，编程水平才能更上一层楼。

#### Promise 链式调用举例：封装 Node.js 的回调方法

代码结构与上面的类似，这里仅做代码举例，不再赘述。

传统写法：

```
fs.readFile(A, 'utf-8', function (err, data) {
    fs.readFile(B, 'utf-8', function (err, data) {
        fs.readFile(C, 'utf-8', function (err, data) {
          console.log('qianguyihao:' + data);
        });
    });
});
```

上方代码多层嵌套，存在回调地狱的问题。

Promise 写法：

```
function read(url) {
    return new Promise((resolve, reject) => {
        fs.readFile(url, 'utf8', (err, data) => {
            if (err) reject(err);
            resolve(data);
        });
    });
}

read(A)
    .then((data) => {
        return read(B);
    })
    .then((data) => {
        return read(C);
    })
    .then((data) => {
        console.log('qianguyihao:' + data);
    })
    .catch((err) => {
        console.log(err);
    });
```
### 用 async ... await 封装链式调用
前面讲的 Promise 链式调用是用 `then().then().then()` 这种写法。其实我们还可以用更高级的写法，也就是用生成器、用 async ... await 改写那段代码。改进之后，代码写起来非常简洁。
#### 用生成器封装链式调用

代码举例：

```
// 封装 Promise 链式请求
function* getData(params_1) {
  // 【关键代码】
  const res1 = yield requestData1(params_1);
  const res2 = yield requestData2(res1);
  const res3 = yield requestData3(res2);
}

// 调用 Promise 链式请求
const generator = getData(params_1);

generator.next().value.then(res1 => {
  generator.next(res1).value.then(res2 => {
    generator.next(res2).value.then(res3 => {
      generator.next(res3);
    })
  })
})
```

生成器在执行时，是分阶段执行的，每次遇到 next()方法后就会执行一个阶段，遇到 yield 就会结束当前阶段的执行并暂停。 上方代码中，yield 后面的内容是当前阶段产生的 Promise 对象；yield 前面的内容是要传递给下一个阶段的参数。
#### 用 async ... await 封装链式调用（重要）

上面的生成器代码有些晦涩难懂，实际开发中，通常不会这么写。我们更喜欢用 async ... await 语法封装 Promise 的链式调用。async ... await 是属于生成器的语法糖，写起来更简洁直观、更容易理解。

代码举例：

```
// 封装：用 async ... await 调用 Promise 链式请求
async function getData() {
  const res1 = await requestData1(params_1);
  const res2 = await requestData2(res1);
  const res3 = await requestData3(res2);
}

getData();
```

代码解释：requestData1()、requestData2()、requestData3() 这三个函数都是一个Promise对象，其内部封装的代码写法已经在前面
### 链式调用，如何处理任务失败的情况
在链式调用多个异步任务的Promise时，如果中间有一个任务失败或者异常，要怎么处理呢？是继续往下执行？还是停止执行，直接抛出异常？这取决于你的业务逻辑是怎样的。

常见的处理方案有以下几种，你可以根据具体情况**按需**选择。
#### 统一处理失败的情况，不继续往下走

针对 a、b、c 这三个请求，不管哪个请求失败，我都希望做统一处理。这种代码要怎么写呢?我们可以在最后面写一个 catch。

由于是统一处理多个请求的异常，所以**只要有一个请求失败了，就会马上走到 catch**，剩下的请求就不会继续执行。比如说：

- a 请求失败：然后会走到 catch，不执行 b 和 c
    
- a 请求成功，b 请求失败：然后会走到 catch，不执行 c。
    

代码举例如下：

```
getPromise('a.json')
  .then((res) => {
    console.log(res);
    return getPromise('b.json'); // 继续请求 b
  })
  .then((res) => {
    // b 请求成功
    console.log(res);
    return getPromise('c.json'); // 继续请求 c
  })
  .then((res) => {
    // c 请求成功
    console.log('c：success');
  })
  .catch((err) => {
    // 统一处理请求失败
    console.log(err);
  });
```
#### 中间的任务失败后，如何继续往下走？

在多个Promise的链式调用中，**如果中间的某个Promise 执行失败，还想让剩下的其他 Promise 顺利执行**的话，那就请在中间**那个失败的Promise里加一个失败的回调函数**（可以写到then函数的第二个参数里，也可以写到catch函数里）。捕获异常后，便可继续往下执行其他的Promise。

代码举例：

```
const promise1 = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled 1');
});

const promise2 = new Promise((resolve, reject) => {
  reject('qianguyihao rejected 2');
});

const promise3 = new Promise((resolve, reject) => {
  resolve('qianguyihao fulfilled 3');
});


promise1
  .then(res => {
    console.log('res1:', res);
    // return 一个 失败的 Promise
    return promise2;
  })
  .then(res => {
    console.log('res2:', res);
    return promise3;
  }, err => {
    // 如果 promise2 为失败状态，可以通过 then() 的第二个参数（即失败的回调函数）捕获异常，然后就可以继续往下执行其他 Promise
    console.log('err2:', err);
    // 关键代码：即便 promise2 失败了，也要继续执行 Promise3
    return promise3;
  })
  .then(res => {
    console.log('res3', res);
  }, err => {
    console.log('err3:', err);
  });
```

打印结果：

```
res1: qianguyihao fulfilled 1
err2: qianguyihao rejected 2
res3 qianguyihao fulfilled 3
```

上方代码中，我们单独处理了 promise2 失败的情况。不管promise2 成功还是失败，我们都想让后续的 promise3 正常执行。

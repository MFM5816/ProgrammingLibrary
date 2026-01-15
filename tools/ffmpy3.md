# ffmpy3

[ffmpy3 是FFmpeg](https://ffmpeg.org/)的 Python 包装器，最初是从[ffmpy](https://github.com/Ch00k/ffmpy)项目派生的。它根据提供的参数及其各自的选项编译 FFmpeg 命令行，并使用 Python 的[`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess).

ffmpy3 类似于 FFmpeg 使用的命令行方法。它可以读取任意数量的输入“文件”（常规文件、管道、网络流、抓取设备等）并写入任意数量的输出“文件”。有关 FFmpeg 命令行选项和参数如何工作的更多详细信息，请参阅 FFmpeg[文档。](https://ffmpeg.org/ffmpeg.html#Synopsis)

ffmpy3支持FFmpeg的[管道](https://ffmpeg.org/ffmpeg-protocols.html#pipe)协议。这意味着可以将输入数据传递到`stdin`并从中获取输出数据`stdout`。

目前 ffmpy3 有`ffmpeg`和`ffprobe`命令的包装器，但应该可以用它运行其他 FFmpeg 工具（例如`ffserver`）

## 安装

```
pip install ffmpy3
```

## 快速开始

```
>>> import ffmpy3
>>> ff = ffmpy3.FFmpeg(
...     inputs={'input.mp4': None},
...     outputs={'output.avi': None}
... )
>>> ff.run()
```

这将`input.mp4`当前目录中的文件作为输入，将视频容器从 MP4 更改为 AVI，而不更改任何其他视频参数，并`output.avi`在当前目录中创建一个新的输出文件。

## 语法

```
ffmpy3.FFmpeg（executable='ffmpeg'， global_options=None，inputs=None，outputs=None ）
```

从传递的参数（可执行路径、选项、输入和输出）编译 FFmpeg 命令行。

`inputs`和`outputs`是包含输入/输出作为键以及它们各自的选项作为值的字典。

一个字典值（选项集）必须是单个空格分隔的字符串，或者是不带空格的列表或字符串（即选项的每个部分都是列表的单独项目，是调用选项`split()`字符串的结果）。

如果该值是一个列表，则不能混合，即不能包含带空格的项目。 包含引用的复杂 FFmpeg 命令行是一个例外：引用部分必须是一个字符串，即使它包含空格（请参见*示例*以获取更多）信息）。

| 参数： | **Executable** （[*str*](https://docs.python.org/3/library/stdtypes.html#str)） – FFMPEG 可执行文件的路径;默认情况下，将在 `PATH` 中搜索 ffmpeg 命令，但可以使用 `ffmpeg` 可执行文件的绝对路径覆盖<br />**global_options** （*iterable*） – 传递给 `ffmpeg` 可执行文件的全局选项（例如 `-y`、`-v` 等）;可以指定为列表/元组/字符串集，也可以指定为一个空格分隔的字符串;默认情况下，不会传递任何全局选项<br />**inputs** （[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)） – 将一个或多个输入参数指定为键的字典，其相应的选项（作为字符串列表或单个空格分隔的字符串）作为值<br />**outputs** （[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)） – 将一个或多个输出参数指定为键的字典，其相应的选项（作为字符串列表或单个空格分隔的字符串）作为值 |
| :----- | ------------------------------------------------------------ |



```
run(input_data=无， stdout=无， stderr=无)
```

执行 FFmpeg 命令行。

`input_data`可以包含 FFmpeg 的输入，以防[管道](https://ffmpeg.org/ffmpeg-protocols.html#pipe)协议用于输入。

`stdout` 和 stderr 指定将进程的 `stdout` 和 `stderr` 重定向到何处。`stderr`默认情况下，不执行重定向，这意味着所有输出都将转到正在运行的 shell（此模式通常仅用于调试目的）。

如果使用 FFmpeg 管道协议进行输出，则必须通过传递子进程将 `stdout` 重定向到`pipe`。PIPE 作为 `stdout` 参数。

返回包含进程的 `stdout` 和 `stderr` 的 2 元组。如果没有重定向，或者如果输出被重定向到例如 os.devnull，则返回的值将是两个 None 值的元组，否则它将包含 ffmpeg 进程返回的实际 `stdout` 和 `stderr` 数据。

| 参数：      | **input_data** （[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)） – FFmpeg 以字节形式处理（音频、视频等）的输入数据（例如，以二进制模式读取文件的结果）**stdout** – 将 FFmpeg `stdout` 重定向到何处。默认值为 None，表示不重定向。**stderr** – 将 FFmpeg `stderr` 重定向到何处。默认值为 None，表示不重定向。 |
| :---------- | ------------------------------------------------------------ |
| **Raises:** | [`FFExecutableNotFoundError`](https://ffmpy3.readthedocs.io/en/latest/ffmpy3.html#ffmpy3.FFExecutableNotFoundError) – 传递的可执行路径无效。[`FFRuntimeError`](https://ffmpy3.readthedocs.io/en/latest/ffmpy3.html#ffmpy3.FFRuntimeError) – 进程退出并出现错误。 |
| 返回：      | 包含进程中的 `stdout` 和 `stderr` 的 2 元组。                |
| 返回类型：  | 元                                                           |



```
run_async(input_data=无，stdout=无，stderr=无)
```

异步执行 FFmpeg 命令行。

`input_data`可以包含 FFmpeg 的输入

`stdout` 和 stderr 指定将进程的 `stdout` 和 `stderr` 重定向到何处。`stderr`默认情况下，不执行重定向，这意味着所有输出都将转到正在运行的 shell（此模式通常仅用于调试目的）。

如果使用 FFmpeg 管道协议进行输出，则必须通过传递子进程将 `stdout` 重定向到`pipe`。PIPE 作为 `stdout` 参数。

请注意，父进程负责从 stdout/stderr 读取任何输出。即使不使用输出，也应执行此操作，因为否则该过程可能会死锁。这可以通过在返回的 `asyncio.subprocess.Process.communicate()` 或根据需要手动读取流来完成。`asyncio.subprocess.Process`

返回对创建的供父程序使用的子进程的引用。

| 参数：      | **input_data** （[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)） – FFmpeg 以字节形式处理（音频、视频等）的输入数据（例如，以二进制模式读取文件的结果）**stdout** – 将 FFmpeg `stdout` 重定向到何处。默认值为 None，表示不重定向。**stderr** – 将 FFmpeg `stderr` 重定向到何处。默认值为 None，表示不重定向。 |
| :---------- | ------------------------------------------------------------ |
| **Raises:** | [`FFExecutableNotFoundError`](https://ffmpy3.readthedocs.io/en/latest/ffmpy3.html#ffmpy3.FFExecutableNotFoundError) – 传递的可执行路径无效。 |
| 返回：      | 已创建的子进程。                                             |
| 返回类型：  | `asyncio.subprocess.Process`                                 |



```
wait()
```

异步等待进程完成执行。

| **Raises:** | [`FFRuntimeError`](https://ffmpy3.readthedocs.io/en/latest/ffmpy3.html#ffmpy3.FFRuntimeError) – 进程退出并出现错误。 |
| :---------- | ------------------------------------------------------------ |
| 返回：      | 如果进程成功完成，则为 0，如果进程尚未启动，则为 None（无）  |
| 返回类型：  | [int](https://docs.python.org/3/library/functions.html#int) 或 [None |



```
class ffmpy3.FFprobe(executable='ffprobe', global_options='', inputs=None)
```

[ffprobe](https://www.ffmpeg.org/ffprobe.html) 的包装器.

从传递的参数（可执行路径、选项、输入）编译 FFprobe 命令行。默认情况下，FFprobe 可执行文件取自 `PATH`，但可以使用绝对路径覆盖。

| 参数： | executable （[*str*](https://docs.python.org/3/library/stdtypes.html#str)） – FFProbe 可执行文件的绝对路径**global_options** （*iterable*） – 传递给 ffprobe 可执行文件的全局选项;可以指定为字符串的列表/元组或空格分隔的字符串**inputs** （[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)） – 将一个或多个输入指定为键的字典，其相应的选项作为值 |
| :----- | ------------------------------------------------------------ |

## 使用

### 格式转换

最简单的使用示例是将媒体从一种格式转换为另一种格式（在本例中为从 MPEG 传输流到 MP4），同时保留所有其他属性：

```
>>> from ffmpy3 import FFmpeg
... ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.mp4': None}
... )
>>> ff.cmd
'ffmpeg -i input.ts output.mp4'
>>> ff.run()
```

### 转码

如果同时我们想使用不同的编解码器重新编码视频和音频，则必须指定其他输出选项：

```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.mp4': '-c:a mp2 -c:v mpeg2video'}
... )
>>> ff.cmd
'ffmpeg -i input.ts -c:a mp2 -c:v mpeg2video output.mp4'
>>> ff.run()
```

### 解复用

一个更复杂的使用示例是将 MPEG 传输流解复用为单独的基本（音频和视频）流，并将它们保存在 MP4 容器中，同时保留编解码器（请注意此处的选项如何使用列表）：

```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={
...         'video.mp4': ['-map', '0:0', '-c:a', 'copy', '-f', 'mp4'],
...         'audio.mp4': ['-map', '0:1', '-c:a', 'copy', '-f', 'mp4']
...     }
... )
>>> ff.cmd
'ffmpeg -i input.ts -map 0:1 -c:a copy -f mp4 audio.mp4 -map 0:0 -c:a copy -f mp4 video.mp4'
>>> ff.run()
警告
```

> 注意
>
> 请注意，不能混合选项的表达式格式，即不可能有一个包含带空格的字符串的列表（一个例外是[复杂命令行](https://ffmpy3.readthedocs.io/en/latest/examples.html#complex-cmds)）。例如，此命令行不适用于 `FFmpeg`:
>
> ```
> >>> from subprocess import PIPE
> >>> ff = FFmpeg(
> ...     inputs={'input.ts': None},
> ...     outputs={
> ...         'video.mp4': ['-map 0:0', '-c:a copy', '-f mp4'],
> ...         'audio.mp4': ['-map 0:1', '-c:a copy', '-f mp4']
> ...     }
> ... )
> >>> ff.cmd
> 'ffmpeg -hide_banner -i input.ts "-map 0:1" "-c:a copy" "-f mp4" audio.mp4 "-map 0:0" "-c:a copy" "-f mp4" video.mp4'
> >>>
> >>> ff.run(stderr=PIPE)
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/Users/ay/projects/personal/ffmpy3/ffmpy3.py", line 104, in run
>     raise FFRuntimeError(self.cmd, ff_command.returncode, out[0], out[1])
> ffmpy3.FFRuntimeError: `ffmpeg -hide_banner -i input.ts "-map 0:1" "-c:a copy" "-f mp4" audio.mp4 "-map 0:0" "-c:a copy" "-f mp4" video.mp4` exited with status 1
> 
> STDOUT:
> 
> 
> STDERR:
> Unrecognized option 'map 0:1'.
> Error splitting the argument list: Option not found
> 
> ```

### 多路复用

要通过重新编码将视频和音频多路复用回 MPEG 传输流，请执行以下操作：

```
>>> ff = FFmpeg(
...     inputs={'video.mp4': None, 'audio.mp3': None},
...     outputs={'output.ts': '-c:v h264 -c:a ac3'}
... )
>>> ff.cmd
'ffmpeg -i audio.mp4 -i video.mp4 -c:v h264 -c:a ac3 output.ts'
>>> ff.run()
```

在某些情况下，必须保留输入和输出的顺序（例如，使用 FFmpeg [-map](https://trac.ffmpeg.org/wiki/How to use -map option) 选项时）。在这些情况下，使用常规的 Python 字典将不起作用，因为它不保留顺序。请改用 [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)。例如，我们希望将一个视频和两个音频流多路复用到 MPEG 传输流中，使用不同的编解码器对两个音频流进行重新编码。在这里，我们使用 OrderedDict 来保留输入的顺序，以便它们与输出选项中的流顺序相匹配：

```
>>> from collections import OrderedDict
>>> inputs = OrderedDict([('video.mp4', None), ('audio_1.mp3', None), ('audio_2.mp3', None)])
>>> outputs = {'output.ts', '-map 0 -c:v h264 -map 1 -c:a:0 ac3 -map 2 -c:a:1 mp2'}
>>> ff = FFmpeg(inputs=inputs, outputs=outputs)
>>> ff.cmd
'ffmpeg -i video.mp4 -i audio_1.mp3 -i audio_2.mp3 -map 0 -c:v h264 -map 1 -c:a:0 ac3 -map 2 -c:a:1 mp2 output.ts'
>>> ff.run()
```

### 使用`pipe`协议

`ffmpy3` 可以从 `STDIN` 读取输入并将输出写入 `STDOUT`。这可以通过使用 FFmpeg [管道](https://www.ffmpeg.org/ffmpeg-protocols.html#pipe)协议来实现。以下示例从包含 RGB 格式的原始视频帧的文件中读取数据，并将其传递给 `STDIN` 上的 `ffmpy3`;`ffmpy3` 将使用 H.264 对原始帧数据进行编码，并将其打包到 MP4 容器中，将输出传递给 STDOUT（请注意，您必须使用子进程将进程的 `STDOUT` 重定向到管道`STDOUT``subprocess.PIPE` 作为 `stdout` 值，否则输出将丢失）：

```
>>> import subprocess
>>> ff = FFmpeg(
...     inputs={'pipe:0': '-f rawvideo -pix_fmt rgb24 -s:v 640x480'},
...     outputs={'pipe:1': '-c:v h264 -f mp4'}
... )
>>> ff.cmd
'ffmpeg -f rawvideo -pix_fmt rgb24 -s:v 640x480 -i pipe:0 -c:v h264 -f mp4 pipe:1'
>>> stdout, stderr = ff.run(input_data=open('rawvideo', 'rb').read(), stdout=subprocess.PIPE)
```

### 异步执行

在某些情况下，人们可能不希望运行 `FFmpeg` 并阻止等待结果或将多线程引入应用程序。在这种情况下，可以使用 [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio) 进行异步执行。

```
>>> ff = ffmpy3.FFmpeg(
...     inputs={'input.mp4': None},
...     outputs={'output.avi': None}
... )
>>> ff.run_async()
>>> await ff.wait()
```

也可以在没有多线程或阻塞的情况下处理 `FFmpeg` 输出。以下代码片段将 FFmpeg 进度输出中的 `CR` 替换为 `LF`，并在 `FFmpeg` 处理输入视频时将其回显到 `STDERR`。

```
>>> import asyncio
>>> import sys
>>> ff = ffmpy3.FFmpeg(
...     inputs={'input.mp4': None},
...     outputs={'output.avi': None},
... )
>>> _ffmpeg_process = await ff.run_async(stderr=asyncio.subprocess.PIPE)
>>> line_buf = bytearray()
>>> my_stderr =_ffmpeg_process.stderr
>>> while True:
>>>     in_buf = (await my_stderr.read(128)).replace(b'\r', b'\n')
>>>     if not in_buf:
>>>         break
>>>     line_buf.extend(in_buf)
>>>     while b'\n' in line_buf:
>>>         line, _, line_buf = line_buf.partition(b'\n')
>>>         print(str(line), file=sys.stderr)
>>> await ff.wait()
```



## ErrorInfor

* ```
  ffmpy3.``FFExecutableNotFoundError
  ```

当未找到 FFmpeg/FFprobe 可执行文件时引发。

* ```
  ffmpy3.FFRuntimeError( cmd、exit_code、stdout='b'、stderr='b' )
  ```

  当 FFmpeg/FFprobe 命令行执行返回非零退出代码时引发。

  - `cmd`

    用于启动可执行文件的命令，包含所有命令行选项。类型：[斯特](https://docs.python.org/3/library/stdtypes.html#str)

  - `exit_code`

    可执行文件的结果退出代码。类型：[整数](https://docs.python.org/3/library/functions.html#int)

  - `stdout`

    stdout 的内容（仅当同步执行时）。类型：[字节](https://docs.python.org/3/library/stdtypes.html#bytes)

  - `stderr`

    stderr 的内容（仅当同步执行时）。类型：[字节](https://docs.python.org/3/library/stdtypes.html#bytes)




# ffmpeg



## 引言

### 什么是FFmpeg？为什么要选FFmpeg？

[FFmpeg官网](https://ffmpeg.org/)介绍说：“一个完整的跨平台解决方案，用于录制、转换和流式传输音频和视频。”

即“一套完整的跨平台解决方案，用于录制、转换和流式传输音频和视频。”

通俗来说，FFmpeg能够录制、转码和推流音视频，支持几乎所有主流的音视频格式和编解码器。虽然录制和推流通常会选择OBS等专业工具，但FFmpeg的核心优势在于其强大的转码功能。

为什么选择FFmpeg？因为它功能强大、灵活免费、开源且使用方便！

### 由来和发展

FFmpeg起源于2000年，由法国程序员Fabrice Bellard发起开发，最初的目的是打造一个免费的多媒体处理工具。随着时间的推移，FFmpeg逐渐发展成为一个功能强大且开源的多媒体框架，支持多媒体视频格式的编解码、转换、录制和流式传输。而且其活跃的开源社区不断贡献代码和新功能，使FFmpeg在多媒体处理领域保持领先地位，广泛评价视频播放器、直播平台、视频编辑软件等各个场景。其实，格式工厂、暴风影音和QQ影音的转码工具等，都是在FFmpeg上套了一层图形化界面，其本质还是靠FFmpeg来进行转码。

## 下载与安装配置（以WINDOWS为例）

[![FFmpeg入门指南](https://camo.githubusercontent.com/61fe7b119d188095971f572680c9a405d1350beef545bcaca26a3ad14dca4e1f/68747470733a2f2f63646e2e61756861696a70616e2e746f702f77702d636f6e74656e742f75706c6f6164732f2f323032352f30372f66666d7065672d67657474696e672d737461727465642d315f636f6d707265737365642e706e67)](https://camo.githubusercontent.com/61fe7b119d188095971f572680c9a405d1350beef545bcaca26a3ad14dca4e1f/68747470733a2f2f63646e2e61756861696a70616e2e746f702f77702d636f6e74656e742f75706c6f6164732f2f323032352f30372f66666d7065672d67657474696e672d737461727465642d315f636f6d707265737365642e706e67)

### 下载解压

1. 打开[FFmpeg官网](https://ffmpeg.org/)，点击“ `Download`”。
2. 注意不要点击中间的“ `Download Source Code`”，那是来源代码。
3. 在页面左下角找到“ `Get packages & executable files`”，点击进入。
4. 选择Windows版本，推荐下载第一个版本`Windows builds from gyan.dev`。
5. 下载完成后，将压缩包解压到任意目录（例如D盘）。

### 配置环境变量

1. 找到FFmpeg解压后的 `bin` 文件夹路径（如 `D:\ffmpeg-2025-07-01-git-11d1b71c31-full_build\bin`）。
2. 右键“ `此电脑`”→“ `属性`”→“ `高级系统设置`”→“ `环境变量`”。
3. 在“ `系统变量`”中找到 `Path`，点击“ `编辑`” → “ `新建`”，添加FFmpeg的 `bin` 路径。
4. 点击确定保存。

### 验证安装

按 `Win + R`，输入 `cmd` 或 `powershell`，回车，输入：

```shell
ffmpeg -version
```

如果显示版本信息，则说明安装成功。

### 基础操作

命令行看起来复杂，但掌握基础命令后其实非常简单。小技巧：可以将文件直接拖入命令行窗口，自动输入文件路径，避免手动输入或复制粘贴。

FFmpeg基本命令格式：

```shell
ffmpeg [全局选项] -i 输入文件 [输入选项] [输出选项] 输出文件
```

1. 全局选项：控制 FFmpeg 整体行为（如日志级别、线程数等）。
2. -i 输入文件：指定输入源（文件、设备或流）。
3. 输入选项：针对输入文件的特殊处理（如截取片段）。
4. 输出选项：指定转码参数、过滤器、编码器等。
5. 输出文件：目标文件路径及格式。

默认情况下，如果你是在 Win + R 里打开的命令行，输出文件会保存到当前用户主目录（如 C:\Users\用户名）。

## 常用的例子

下面举了几个常用的例子：

### 查看文件信息

```shell
ffmpeg -i input.mp4
```

### 简单转码（直接复制视频和音频流，不重新编码）

```shell
ffmpeg -i input.mp4 -c:v copy -c:a copy output.mkv
```

> **注意**：如果输入视频和编码格式与目标格式不兼容，或者是需要调整画质、码率以及添加过滤器等，则需要重新编码。

### 转换音频格式（WAV 转 AAC）

```shell
ffmpeg -i input.wav output.aac
```

### 调整分辨率（转换为1280x720）

```shell
ffmpeg -i input.mp4 -vf "scale=1280:720" output_720p.mp4
```

### 压缩视频（调整码率为1000kbps）

```shell
ffmpeg -i input.mp4 -b:v 1000k output_compressed.mp4
```

### 音频输出（高质量 MP3）

```shell
ffmpeg -i input.mp4 -q:a 0 -map a output.mp3
```

### 使用更高效的编码格式 H.265

```shell
ffmpeg -i input.mts -c:v libx265 -crf 28 -preset fast -c:a aac -b:a 192k output.mp4
```

**参数说明**：

- `-c:v libx265`：视频编码为H.265
- `-crf 28`：质量控制参数，范围18-28，数值越小质量越好
- `-preset fast`：编码速度，速度越快压缩率可能越低
- `-c:a aac -b:a 192k`：音频编码为AAC，码率192kbps

### 视频转GIF（前5秒，10fps，宽度320像素，自动等比缩放）

```shell
ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" -t 5 output.gif
```


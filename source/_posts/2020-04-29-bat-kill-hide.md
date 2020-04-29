---
layout: post
title:  "批处理kill隐藏的cmd窗口"
date: 2020-04-29 09:40:04 +0800
categories: [bat]
tags: [bat, windows]
excerpt_separator: <!--more-->
---
批处理kill隐藏的cmd窗口
<!--more-->

## 1 概述

当我们把bat隐藏之后，进程会多一个批处理进程并且不同程序的批处理是相同的，我们无法判断需要kill哪个。

思路:
我们可以通过使用自己的cmd.exe的方式，然后只kill掉服务自己的cmd.exe。

## 2 实现

```bat
if "%1"=="r" goto start
if "%1"=="h" goto begin
if not exist nvrcmd.exe (
    copy C:\windows\system32\cmd.exe nvrcmd.exe /y
)

start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin

tasklist | find /C "nvrcmd.exe"
if %errorlevel%==0 (
    echo nvrcmd.exe has started, will kill it
    taskkill /f /im "nvrcmd.exe"
)

start mshta vbscript:CreateObject("WScript.Shell").Run("nvrcmd.exe /c %~nx0 r",0)(window.close)&&exit
:start
```

1. 是否在本地存在nvrcmd.exe,如果没有则从C盘下面复制
2. 使用隐藏的方式运行此脚本
3. 隐藏脚本已经启动，会运行到`begin`之后
4. 判断`nvrcmd.exe`是否运行，如果正在运行则kill掉
5. 使用`nvrcmd.exe`运行此脚本
6. `r`入参成立，会运行到`start`
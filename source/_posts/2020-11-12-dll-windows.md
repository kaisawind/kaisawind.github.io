---
layout: post
title: "windows查看dll依赖"
date: 2020-11-13 10:55:14 +0800
categories: [编程语言,cpp]
tags: [C#, cpp, C]
excerpt_separator: <!--more-->
---
windows查看dll依赖
<!--more-->

开始菜单打开`Developer Command Prompt for VS 2019`
在cmd中定位要查看的dll

```bash
dumpbin /dependents ice_ipcsdk.dll
```
执行结果
![](/images/深度截图_选择区域_20201113101454.png)
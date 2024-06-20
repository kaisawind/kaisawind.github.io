---
layout: post
title:  "linux查找所有深度文件夹中文件并删除"
date: 2024-06-20 23:47:42
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
linux查找所有深度文件夹中文件并删除
<!--more-->

* 查找所有深度文件夹并删除
```bash
find . -type d -name \.@__thumb -prune -exec rm -rf {} \;
```
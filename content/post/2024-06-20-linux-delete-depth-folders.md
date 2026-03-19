---
layout: post
title:  "linux查找所有深度文件夹中文件并删除"
date: 2024-06-20 23:47:42
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
linux查找所有深度文件夹中文件并删除
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


* 查找所有深度文件夹并删除
```bash
find . -type d -name \.@__thumb -prune -exec rm -rf {} \;
```
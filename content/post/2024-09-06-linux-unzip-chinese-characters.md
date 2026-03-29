---
layout: post
title:  "linux下unzip解压中文乱码"
date: 2024-09-06 18:28:54
lastmod: 2026-03-19
categories: [编程语言,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "linux下unzip解压中文乱码"
---
linux下unzip解压中文乱码
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


命令
```bash
unzip -O gbk xxxx.zip -d xxxx
```
---
layout: post
title:  "查找两个txt中其中一个没有另一个的行"
date: 2025-04-25 10:55:00
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
---
查找两个txt中其中一个没有另一个的行
<!--more-->


```bash
# b.txt中没有a.txt的内容
grep -vFxf a.txt b.txt > unique.txt
```

-F: 固定匹配 (避免正则表达式)
-x：匹配整行（避免部分匹配）
-v：反向选择（排除匹配行）
-f：从B.txt中读取匹配模式
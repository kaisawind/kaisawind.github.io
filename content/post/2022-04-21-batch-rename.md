---
layout: post
title:  "linux批量重命名文件"
date: 2022-04-21 20:00:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
linux批量重命名文件
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


```bash
ls | cat -n | while read n f; do mv "$f" `printf "%012d.jpg" $n`; done
```
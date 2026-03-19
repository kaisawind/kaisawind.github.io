---
layout: post
title: 'Linux Mv Files to Folder'
date: 2024-06-21T16:38:55Z
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
linux通过find查找文件并移动到指定文件夹
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


```bash
find path_a -type f -name "some_name" ! -path "**/.@__thumb/*" -print0 | xargs -0 -I {} mv {} path_b
```

`! -path "**/.@__thumb/*"` -> 排除某个文件夹下文件
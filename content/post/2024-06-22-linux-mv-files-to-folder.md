---
layout: post
title: 'Linux Mv Files to Folder'
date: 2024-06-21T16:38:55Z
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
linux通过find查找文件并移动到指定文件夹
<!--more-->

```bash
find path_a -type f -name "some_name" ! -path "**/.@__thumb/*" -print0 | xargs -0 -I {} mv {} path_b
```

`! -path "**/.@__thumb/*"` -> 排除某个文件夹下文件
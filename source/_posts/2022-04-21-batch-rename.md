---
layout: post
title:  "linux批量重命名文件"
date: 2022-04-21 20:00:16
categories: [linux]
tags: [linux， kernel]
excerpt_separator: <!--more-->
---
linux批量重命名文件
<!--more-->

```bash
ls | cat -n | while read n f; do mv "$f" `printf "%012d.jpg" $n`; done
```
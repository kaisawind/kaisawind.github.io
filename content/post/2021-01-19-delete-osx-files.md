---
layout: post
title:  "删除Mac OSX生成的缩略图文件"
date: 2021-01-19 13:35:16
categories: [linux,manjaro]
tags: [linux]
excerpt_separator: <!--more-->
---
删除Mac OSX生成的缩略图文件
<!--more-->

## 1. 概述
Mac OSx会生成`._xxxx`的缩略图文件，导致整个文件系统出问题。需要删除

## 2. 命令

查找所有以`._`开头的文件
```bash
find . -type f -name '._*'
```

确认之后，追加删除
```bash
find . -type f -name '._*' -delete
```
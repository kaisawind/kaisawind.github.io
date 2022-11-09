---
layout: post
title:  "ModuleNotFoundError: No module named 'distutils.cmd'"
date: 2022-11-09 14:08:54
categories: [编程语言,python]
tags: [python, linux]
excerpt_separator: <!--more-->
---
ModuleNotFoundError: No module named 'distutils.cmd'
<!--more-->

virtualenv 安装非host版本的python环境时，找不到包distutils。
在主机环境中安装python版本的distutils包

```bash
sudo apt-get install python3.8-distutils
```
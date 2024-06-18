---
layout: post
title:  "Mount Windows Network Drives in WSL"
date: 2024-06-17 23:22:42
categories: [windows,wsl]
tags: [windows]
excerpt_separator: <!--more-->
---
在WSL2中挂载网络盘
<!--more-->

```bash
mkdir /mnt/m
sudo mount -t drvfs M: /mnt/m
```
---
layout: post
title:  "Mount Windows Network Drives in WSL"
date: 2024-06-17 23:22:42
categories: [windows,wsl]
excerpt_separator: <!--more-->
---
Mount Windows Network Drives in WSL
<!--more-->

```bash
mkdir /mnt/m
sudo mount -t drvfs M: /mnt/m
```
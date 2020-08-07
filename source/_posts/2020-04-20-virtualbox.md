---
layout: post
title:  "virtualbox使用物理磁盘"
date: 2020-04-20 21:31:16 +0800
categories: [虚拟化,virtualbox]
tags: [linux,windows,virtualbox]
excerpt_separator: <!--more-->
---
virtualbox使用物理磁盘
<!--more-->

首先需要取得磁盘的所有权限
```bash
sudo chmod 666 /dev/sda1
```

关键命令
```bash
sudo vboxmanage internalcommands createrawvmdk -filename /home/pana/win10.vmdk -rawdisk /dev/sda1 -relative
```

然后在GUI中将创建的磁盘链接进行注册


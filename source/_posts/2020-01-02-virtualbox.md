---
layout: post
title: "virtualbox虚拟机命令行安装增强功能"
date: 2020-01-02 10:18:00
categories: [虚拟化,virtualbox]
tags: [linux,virtualbox,centos]
excerpt_separator: <!--more-->
---
virtualbox虚拟机命令行安装增强功能
<!--more-->

* 添加增强功能镜像
虚拟机菜单→设备→安装增强功能

* 虚拟系统挂载镜像
```bash
sudo /dev/cdrom /mnt/
```

* 安装增强功能
```bash
cd /mnt/
sudo ./VBoxLinuxAdditions.run
```

注意: 安装增强功能会重新编译内核,所以需要编译工具
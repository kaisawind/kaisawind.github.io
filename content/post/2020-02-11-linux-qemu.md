---
layout: post
title:  "linux使用qemu安装arm64开发环境"
date: 2020-02-11 10:01:04
categories: [虚拟化,qemu]
tags: [linux]
excerpt_separator: <!--more-->
---
linux使用qemu安装arm64开发环境
<!--more-->

## 1. 概述

linux下搭建qemu开发环境要比windows简单,通过命令行就可以简单的进行安装。

## 2. 安装

默认安装方式i386
```bash
sudo apt-get install qemu
```

默认安装方式是不支持arm架构，需要单独安装arm的qemu
```bash
sudo apt-get install qemu-arm
```

或者完全安装qemu
```bash
sudo apt-get install qemu
sudo apt-get install qemu-system
sudo apt-get install qemu-user
```

## 3. 虚拟系统管理器

qemu图形管理界面软件https://virt-manager.org/

![](/images/深度截图_选择区域_20200211102843.png)

### 3.1 安装

```bash
sudo apt-get install virt-manager
```

### 3.2 创建虚拟机

[文件]-[新建虚拟机]

![](/images/20200211103233.png)

选择系统盘
![](/images/深度截图_选择区域_20200211103353.png)

配置CPU和内存
![](/images/20200211103433.png)

配置磁盘
![](/images/20200211103533.png)

最后确认
![](/images/深度截图_选择区域_20200211103541.png)

### 3.3 管理虚拟机

![](/images/深度截图_virt-manager_20200211103959.png)
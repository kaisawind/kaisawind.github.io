---
layout: post
title: "virtualbox虚拟机共享文件夹权限"
date: 2020-01-02 10:18:00 +0800
categories: [linux]
tags: [linux,virtualbox,centos]
excerpt_separator: <!--more-->
---
virtualbox虚拟机共享文件夹权限
<!--more-->

virtualbox共享文件夹之后,本地用户无法访问,所以需要添加当前用户到vboxsf

```bash
sudo usermod -aG vboxsf $(whoami)
```
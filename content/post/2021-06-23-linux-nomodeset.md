---
layout: post
title:  "ubuntu配置nomodeset"
date: 2021-06-23 18:15:16
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
ubuntu配置nomodeset.
<!--more-->

## 1. 概述
当ubuntu安装在没有独立显卡的机器上时，或者核显的版本太高，就会导致安装之后无法进入桌面。此时需要设置nomodeset.

## 2. 方法1(重启失效)

在`/boot/grub/grub.cfg`的`linux /boot/vmlinuz***`开头，`quiet splash`后面添加`nomodeset`.
因为grub.cfg每次开机时会重新启动，所以开机失效。

## 3. 方法2

`/etc/default/grub`的`quiet splash`后面添加`nomodeset`.
开机不会失效。
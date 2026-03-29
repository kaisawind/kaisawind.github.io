---
layout: post
title:  "ubuntu删除娱乐软件"
date: 2024-09-30 16:31:54
lastmod: 2026-03-19
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "ubuntu删除娱乐软件"
---
ubuntu删除娱乐软件
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


命令
```bash
sudo apt-get purge thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines cheese gnome-sudoku transmission-common gnome-orca deja-dup
sudo apt-get remove --purge "libreoffice*"
sudo apt-get clean
sudo apt-get autoremove
```
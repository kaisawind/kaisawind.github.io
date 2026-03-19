---
layout: post
title:  "linux can't read superblock on"
date: 2022-04-22 10:02:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
意外停电后，重启系统，不能自动挂载
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


```bash
sudo fsck /dev/xxxxx

Inode 525737 seems to contain garbage.  Clear? yes
```
`a`为全部yes
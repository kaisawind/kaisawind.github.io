---
layout: post
title:  "linux的ssh策略"
date: 2021-02-03 16:26:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "linux的ssh策略"
---
linux的ssh策略
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


策略文件位置
* `/etc/ssh/sshd_config`

```conf
#LoginGraceTime 2m
#PermitRootLogin yes
#StrictModes yes
MaxAuthTries 6
MaxSessions 10
```

1. PermitRootLogin: 是否允许root登录
2. MaxAuthTries: 登录多少次之后禁止登录
3. MaxSessions: 最多开机多少句柄
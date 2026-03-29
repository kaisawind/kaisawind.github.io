---
layout: post
title: "linux单网卡设置多IP"
date: 2021-11-27 12:00:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "linux 单网卡设置多 IP"
---
linux 单网卡设置多 IP
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


`/lib/systemd/network/10-eth0.network`IP 配置路径

```bash
[Match]
Name=eth0
[Network]
Address=192.168.1.104/24
Address=192.168.2.104/24
Gateway=192.168.1.1
Gateway=192.168.2.1
```

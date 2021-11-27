---
layout: post
title: "NXP iMax系统修改静态IP"
date: 2021-11-27 11:46:16
categories: [linux]
tags: [linux， kernel]
excerpt_separator: <!--more-->
---

NXP iMax 系统修改静态 IP

<!--more-->

`/lib/systemd/network/10-eth0.network`IP 配置路径

```bash
[Match]
Name=eth0
[Network]
Address=192.168.1.104/24
Gateway=192.168.1.1
```

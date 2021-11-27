---
layout: post
title: "linux单网卡设置多IP"
date: 2021-11-27 12:00:16
categories: [linux]
tags: [linux， kernel]
excerpt_separator: <!--more-->
---

linux 单网卡设置多 IP

<!--more-->

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

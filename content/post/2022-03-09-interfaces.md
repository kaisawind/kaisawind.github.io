---
layout: post
title:  "linux的interfaces网络配置"
date: 2022-03-09 13:03:16
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
linux的interfaces网络配置
<!--more-->

/etc/network/interfaces
```bash
# cat /etc/network/interfaces 
# interface file auto-generated by buildroot

auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
  address 192.168.1.100
  netmask 255.255.255.0
  gateway 192.168.1.1
```
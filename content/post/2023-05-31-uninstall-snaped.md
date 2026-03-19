---
layout: post
title:  "ubuntu卸载snaped"
date: 2023-05-31 20:44:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
ubuntu卸载snaped
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。


```bash
snap list
sudo snap remove chromium snap-store 
sudo systemctl stop snapd
sudo apt remove --purge --assume-yes snapd gnome-software-plugin-snap
rm -rf ~/snap/
sudo rm -rf /var/cache/snapd/ 
```
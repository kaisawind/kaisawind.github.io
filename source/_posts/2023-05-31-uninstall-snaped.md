---
layout: post
title:  "ubuntu卸载snaped"
date: 2023-05-31 20:44:16
categories: [k8s]
tags: [k8s, linux]
excerpt_separator: <!--more-->
---
ubuntu卸载snaped
<!--more-->

```bash
snap list
sudo snap remove chromium snap-store 
sudo systemctl stop snapd
sudo apt remove --purge --assume-yes snapd gnome-software-plugin-snap
rm -rf ~/snap/
sudo rm -rf /var/cache/snapd/ 
```
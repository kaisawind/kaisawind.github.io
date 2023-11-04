---
layout: post
title:  "Ubuntu 修改内核"
date: 2023-11-04 23:22:55
categories: [linux,ubuntu]
excerpt_separator: <!--more-->
---
Ubuntu 修改内核

### 脚本

```bash
wget https://raw.githubusercontent.com/pimlie/ubuntu-mainline-kernel.sh/master/ubuntu-mainline-kernel.sh
chmod +x ubuntu-mainline-kernel.sh

# search and find your wanted version
ubuntu-mainline-kernel.sh -r | grep 5.13

# install that version kernel
ubuntu-mainline-kernel.sh -i v5.13.19

# get all menuentries
grep 'menuentry \|submenu ' /boot/grub/grub.cfg | cut -f2 -d "'"

# change the grub configuration
vi /etc/default/grub
from: GRUB_DEFAULT=0
to: GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.13.19-051319-generic"

# update grub
update-grub

# reboot
reboot now

# verify
uname -r
```

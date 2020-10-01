---
layout: post
title:  "linux使用wine运行游戏"
date: 2020-09-30 09:40:16 +0800
categories: [linux,manjaro]
tags: [linux]
excerpt_separator: <!--more-->
---
linux使用wine运行游戏
<!--more-->

## 1. 概述
wine是linux系统中运行windows软件的程序。

## 2. 运行SC2

### 2.1 SC2简介
SC2是暴雪的一块游戏，全程星际争霸2,在wine的支持列表中，是史诗级支持度。所以测试SC2的运行是最简单的。

### 2.2 wine安装
```bash
sudo pacman -S wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader
```

### 2.3 lutris简介
lutris是使用wine支持linux运行游戏的平台，由于为每个游戏进行了特殊配置，所以会使使用wine更简单。

```bash
sudo pacman -S lutris
```

### 2.4 nvidia显卡支持
```bash
sudo pacman -S nvidia-dkms nvidia-utils lib32-nvidia-utils nvidia-settings vulkan-icd-loader lib32-vulkan-icd-loader
```

**独立显卡切换**
```bash
prime-offload
optimus-manager --switch nvidia
```
之后会有一个重新登录

### 2.5 暴雪客户端
暴雪客户端是暴雪游戏的平台。
在lutris中搜索`Battle.net`,点击右侧的安装
![](/images/深度截图_选择区域_20201001101318.png)
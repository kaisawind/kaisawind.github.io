---
layout: post
title:  "ffmpeg在linux上编译windows版本"
date: 2021-03-18 16:51:37
categories: [FFmpeg]
tags: [linux]
excerpt_separator: <!--more-->
---
ffmpeg在linux上编译windows版本
<!--more-->

## 1. 概要

编译机系统是manjaro

## 2. 必要软件

```bash
sudo pacman -Syu mingw-w64-gcc mingw-w64-pkg-config
```

## 3. 编译

```bash
./configure --disable-static --enable-shared --enable-decoder=h264 --arch=x86_64 --target-os=mingw64  --cross-prefix=x86_64-w64-mingw32- --prefix=./ffmpeg-4.3.git-mingw64-dev
make
```
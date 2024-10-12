---
layout: post
title:  "alpine镜像编译libmodbus"
date: 2024-10-12 10:02:54
categories: [linux,alpine]
tags: [alpine]
draft: false
excerpt_separator: <!--more-->
---
alpine镜像编译libmodbus
<!--more-->

命令
```bash
docker run --rm --platform linux/arm/v7 -it -v $PWD:/mnt alpine sh

sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
apk update && apk add linux-headers libtool autoconf automake git bash build-base

cd /mnt/ && git config --global --add safe.directory /mnt && git clean -d -x -f

./autogen.sh && mkdir build && ./configure --prefix=/mnt/build --enable-static && make install
```
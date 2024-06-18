---
layout: post
title:  "golang跨平台编译"
date: 2022-04-08 10:31:54
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang跨平台编译
<!--more-->

列出go支持的所有平台和架构
```bash
go tool dist list
```

CGO跨平台编译
```bash
CC=arm-linux-gnueabihf-gcc GOOS=linux GOARCH=arm GOARM=6 CGO_ENABLED=1 go build -v -o myprogram -ldflags="-extld=$CC"
```

```bash
CC=i586-mingw32-gcc GOOS=windows GOARCH=386 CGO_ENABLED=1 go build -v -o myprogram.exe -ldflags="-extld=$CC"
```

链接库跨平台编译
```bash
CC=arm-linux-gnueabihf-gcc GOARCH=arm GOOS=linux GOARM=7 CGO_ENABLED=1 go build -buildmode=c-shared -o example/libi2c.so .
```
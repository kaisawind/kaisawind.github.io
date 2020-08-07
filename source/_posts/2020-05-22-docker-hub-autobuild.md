---
layout: post
title:  "docker hub自动构建多平台镜像(aarch64/arm64)"
date: 2020-05-22 15:08:42 +0800
categories: [docker, docker]
tags: [docker, linux, arm]
excerpt_separator: <!--more-->
---
docker hub自动编译多平台镜像
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 用到的技术](#2-用到的技术)
- [3. 基础信息](#3-基础信息)
- [4. 多平台(多CPU)支持方法](#4-多平台多cpu支持方法)
  - [4.1 multiarch/qemu-user-static](#41-multiarchqemu-user-static)
  - [4.2 docker hub hooks](#42-docker-hub-hooks)
  - [4.3 Dockerfile添加qemu-user-static](#43-dockerfile添加qemu-user-static)
- [5. build日志](#5-build日志)
- [6. 一些坑](#6-一些坑)

<!-- /code_chunk_output -->


## 1. 概述

docker hub能够很方便的根据git hub的代码提交自动构建镜像，但是默认方法不能自动构建非amd64的镜像。

## 2. 用到的技术

* qemu
能够模拟CPU的虚拟机
https://www.qemu.org/

* binfmt-misc
二进制执行文件切换不同CPU执行
https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html

* docker18.03 ee
docker hub使用的docker版本，文档需要参照旧文档
https://docs.docker.com/v18.03/engine/reference/builder/

* docker hub
docker hub自动构建镜像高级篇
https://docs.docker.com/docker-hub/builds/advanced/

* Support automated ARM builds #1261
https://github.com/docker/hub-feedback/issues/1261

## 3. 基础信息

docker hub的machine也是一台linux机器(可能是虚拟机)，用户可以更改machine的一些配置，甚至可以安装软件。
以下是docker hub的machine基础信息，注意docker的版本，书写Dockerfile时需要注意
```bash
KernelVersion: 4.4.0-1060-aws
Components: [{u'Version': u'18.03.1-ee-3', u'Name': u'Engine', u'Details': {u'KernelVersion': u'4.4.0-1060-aws', u'Os': u'linux', u'BuildTime': u'2018-08-30T18:42:30.000000000+00:00', u'ApiVersion': u'1.37', u'MinAPIVersion': u'1.12', u'GitCommit': u'b9a5c95', u'Arch': u'amd64', u'Experimental': u'false', u'GoVersion': u'go1.10.2'}}]
Arch: amd64
BuildTime: 2018-08-30T18:42:30.000000000+00:00
ApiVersion: 1.37
Platform: {u'Name': u''}
Version: 18.03.1-ee-3
MinAPIVersion: 1.12
GitCommit: b9a5c95
Os: linux
GoVersion: go1.10.2
```

## 4. 多平台(多CPU)支持方法

qemu和binfmt能够支持跨平台可执行文件运行。
当docker hub自动构建时，我们需要考虑以下两点：
1. 在host上运行其它平台的镜像
2. 在容器内运行其它平台的可执行文件

为了实现这两点，我们需要在host和容器中安装qemu-user-static。

### 4.1 multiarch/qemu-user-static
https://github.com/multiarch/qemu-user-static

`multiarch/qemu-user-static`是一个docker镜像有以下几种镜像

1. `multiarch/qemu-user-static` image
2. `multiarch/qemu-user-static:$version` images
3. `multiarch/qemu-user-static:$from_arch-$to_arch` images
4. `multiarch/qemu-user-static:$from_arch-$to_arch-$version` images
5. `multiarch/qemu-user-static:$to_arch` images
6. `multiarch/qemu-user-static:$to_arch-$version` images
7. `multiarch/qemu-user-static:register` image

有两种主要用法

```bash
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```
或
```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

`-p yes`参数需要内核支持，最小的支持内核是kernel 4.10，但是docker hub的内核是4.4，所以我们使用`multiarch/qemu-user-static:register`
https://github.com/multiarch/qemu-user-static/issues/100#issuecomment-566030523

### 4.2 docker hub hooks

我们需要在build之前，也就是pre_build,先执行
```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

amd64不需要hooks,只有arm64需要，所以只在arm64下建立hooks文件夹
docker hub hooks目录结构
```bash
.
├── amd64
│   └── Dockerfile
└── arm64
    ├── Dockerfile
    └── hooks
        └── pre_build
```

### 4.3 Dockerfile添加qemu-user-static

```Dockerfile
FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/golang:alpine AS builder
COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
RUN apk add upx make git
RUN make
```

## 5. build日志

```bash
Cloning into '.'...
Warning: Permanently added the RSA host key for IP address '140.82.114.4' to the list of known hosts.
Reset branch 'master'
Your branch is up-to-date with 'origin/master'.
Executing pre_build hook...
Unable to find image 'multiarch/qemu-user-static:register' locally
register: Pulling from multiarch/qemu-user-static
e2334dd9fee4: Pulling fs layer
9af49f645bc8: Pulling fs layer
ed8a5179ae11: Pulling fs layer
1ec39da9c97d: Pulling fs layer
1ec39da9c97d: Waiting
9af49f645bc8: Verifying Checksum
9af49f645bc8: Download complete
ed8a5179ae11: Verifying Checksum
ed8a5179ae11: Download complete
e2334dd9fee4: Verifying Checksum
e2334dd9fee4: Download complete
1ec39da9c97d: Verifying Checksum
1ec39da9c97d: Download complete
e2334dd9fee4: Pull complete
9af49f645bc8: Pull complete
ed8a5179ae11: Pull complete
1ec39da9c97d: Pull complete
Digest: sha256:0b29354dc736460c0076b0b1b150605511dd48e2d7df51f749f0825e948479c0
Status: Downloaded newer image for multiarch/qemu-user-static:register
Setting /usr/bin/qemu-alpha-static as binfmt interpreter for alpha
Setting /usr/bin/qemu-arm-static as binfmt interpreter for arm
Setting /usr/bin/qemu-armeb-static as binfmt interpreter for armeb
Setting /usr/bin/qemu-sparc-static as binfmt interpreter for sparc
Setting /usr/bin/qemu-sparc32plus-static as binfmt interpreter for sparc32plus
Setting /usr/bin/qemu-sparc64-static as binfmt interpreter for sparc64
Setting /usr/bin/qemu-ppc-static as binfmt interpreter for ppc
Setting /usr/bin/qemu-ppc64-static as binfmt interpreter for ppc64
Setting /usr/bin/qemu-ppc64le-static as binfmt interpreter for ppc64le
Setting /usr/bin/qemu-m68k-static as binfmt interpreter for m68k
Setting /usr/bin/qemu-mips-static as binfmt interpreter for mips
Setting /usr/bin/qemu-mipsel-static as binfmt interpreter for mipsel
Setting /usr/bin/qemu-mipsn32-static as binfmt interpreter for mipsn32
Setting /usr/bin/qemu-mipsn32el-static as binfmt interpreter for mipsn32el
Setting /usr/bin/qemu-mips64-static as binfmt interpreter for mips64
Setting /usr/bin/qemu-mips64el-static as binfmt interpreter for mips64el
Setting /usr/bin/qemu-sh4-static as binfmt interpreter for sh4
Setting /usr/bin/qemu-sh4eb-static as binfmt interpreter for sh4eb
Setting /usr/bin/qemu-s390x-static as binfmt interpreter for s390x
Setting /usr/bin/qemu-aarch64-static as binfmt interpreter for aarch64
Setting /usr/bin/qemu-aarch64_be-static as binfmt interpreter for aarch64_be
Setting /usr/bin/qemu-hppa-static as binfmt interpreter for hppa
Setting /usr/bin/qemu-riscv32-static as binfmt interpreter for riscv32
Setting /usr/bin/qemu-riscv64-static as binfmt interpreter for riscv64
Setting /usr/bin/qemu-xtensa-static as binfmt interpreter for xtensa
Setting /usr/bin/qemu-xtensaeb-static as binfmt interpreter for xtensaeb
Setting /usr/bin/qemu-microblaze-static as binfmt interpreter for microblaze
Setting /usr/bin/qemu-microblazeel-static as binfmt interpreter for microblazeel
Setting /usr/bin/qemu-or1k-static as binfmt interpreter for or1k
KernelVersion: 4.4.0-1060-aws
Components: [{u'Version': u'18.03.1-ee-3', u'Name': u'Engine', u'Details': {u'KernelVersion': u'4.4.0-1060-aws', u'Os': u'linux', u'BuildTime': u'2018-08-30T18:42:30.000000000+00:00', u'ApiVersion': u'1.37', u'MinAPIVersion': u'1.12', u'GitCommit': u'b9a5c95', u'Arch': u'amd64', u'Experimental': u'false', u'GoVersion': u'go1.10.2'}}]
Arch: amd64
BuildTime: 2018-08-30T18:42:30.000000000+00:00
ApiVersion: 1.37
Platform: {u'Name': u''}
Version: 18.03.1-ee-3
MinAPIVersion: 1.12
GitCommit: b9a5c95
Os: linux
GoVersion: go1.10.2
Starting build of index.docker.io/kaisawind/broker.mqtt:arm64...
Step 1/19 : FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
---> f61b879dd4f3
Step 2/19 : FROM arm64v8/golang:alpine AS builder
---> 6bf3dc21cd79
Step 3/19 : COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
---> 734e735c89dc
Step 4/19 : ENV GO111MODULE=on
---> Running in a46917d52cc4
Removing intermediate container a46917d52cc4
---> 8e1be59b8c58
Step 5/19 : RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
---> Running in 76d4165a28a0
Removing intermediate container 76d4165a28a0
---> 35eb38c32562
Step 6/19 : RUN apk add upx make git
---> Running in 84b75cf0ce90
```

## 6. 一些坑

* kenel版本为4.4不支持`docker run --rm --privileged multiarch/qemu-user-static --reset -p yes`
* docker版本为18.03不支持`--platform=<>`,例如：
`FROM --platform=linux/arm64 golang:alpine AS builder`
* 容器内如果想运行二进制文件，容器内也需要有`qemu-user-static`
* docker hub的hook的文件夹名是`hooks`,不是`hook`
---
layout: post
title:  "docker仓库间多架构镜像同步"
date: 2025-10-22 19:24:54
lastmod: 2026-03-19
categories: [linux,ubuntu,docker]
tags: [ubuntu, docker]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "docker仓库间多架构镜像同步"
---
docker仓库间多架构镜像同步
<!--more-->

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。


使用skopeo工具进行镜像同步
```bash
sudo apt-get install -y skopeo
```

同步命令
```bash
skopeo copy --multi-arch=all --dest-tls-verify=false --retry-delay=3s docker://quay.io/skopeo/stable:latest docker://192.168.1.118:5000/skopeo/stable:latest
```

使用容器
```bash
podman run --rm docker://quay.io/skopeo/stable:latest copy --multi-arch=all --dest-tls-verify=false --retry-delay=3s docker://quay.io/skopeo/stable:latest docker://192.168.1.118:5000/skopeo/stable:latest
```

* --dest-tls-verify: 目标使用http
* --retry-delay: 超时检测间隔时间
* --multi-arch=all: 多平台架构

多平台架构镜像保存到本地镜像文件
```bash
skopeo copy --multi-arch=all docker://quay.io/skopeo/stable:latest oci-archive:skopeo.img
```

本地镜像文件推送到仓库
```bash
skopeo copy --multi-arch=all --dest-tls-verify=false --retry-delay=3s oci-archive:skopeo.img docker://192.168.1.118:5000/skopeo/stable:latest
```

本地镜像仓库保存本地镜像文件
```bash
skopeo copy --multi-arch=all --src-tls-verify=false docker://192.168.1.118:5000/skopeo/stable:latest oci-archive:skopeo.img 
```
---
layout: post
title:  "docker buildx构建多平台镜像"
date: 2020-05-22 17:55:42 +0800
categories: [docker, buildx]
tags: [docker, linux, arm]
excerpt_separator: <!--more-->
---
docker buildx构建多平台镜像
<!--more-->

## 1. 概述
Docker Buildx是docker19.03的`experimental feature`，使用时需要打开`experimental`

`~/.docker/config.json`
```json
{
    "experimental": "enabled",
    "debug": true
}
```

## 2. 使用

创建buildx句柄
```bash
docker buildx create --use --name mybuild
```
查看支持的平台
```bash
#$ docker buildx ls
NAME/NODE    DRIVER/ENDPOINT             STATUS  PLATFORMS
mybuilder *  docker-container                    
  mybuilder0 unix:///var/run/docker.sock running linux/amd64, linux/386
default      docker                              
  default    default                     running linux/amd64, linux/386
```

启用binfmt转换
```bash
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

再次查看
```bash
#$ docker buildx ls
NAME/NODE    DRIVER/ENDPOINT             STATUS  PLATFORMS
mybuilder *  docker-container                    
  mybuilder0 unix:///var/run/docker.sock running linux/amd64, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
default      docker                              
  default    default                     running linux/amd64, linux/386
```

使用docker buildx创建镜像
```bash
docker buildx build --platform linux/amd64,linux/arm64 .
```


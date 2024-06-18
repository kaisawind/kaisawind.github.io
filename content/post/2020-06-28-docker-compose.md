---
layout: post
title:  "docker buildx构建多平台compose镜像"
date: 2020-06-28 17:55:42
categories: [docker, compose]
tags: [docker]
excerpt_separator: <!--more-->
---
docker buildx构建多平台compose镜像
<!--more-->

## 1. 概述
由于单片机使用的是arm架构，但是官方的compose镜像不支持arm,所以需要自己构建compose镜像

## 2. 使用镜像安装docker-compose

### 2.1. 导入镜像

```bash
docker load -i csedge-compose-v1.25.0.tar
```

### 2.2. 复制脚本

```bash
cp docker-compose /usr/local/bin/
chmod +x /usr/local/bin/docker-compose
```

### 2.3. 测试

```bash
docker-compose -v
```

```bash
docker-compose version 1.25.0
```

## 3. 构建compose镜像

compose官方代码库
`https://github.com/docker/compose`

修改Dockerfile.
主要修改几点:
1. alpine镜像源
```Dockerfile
RUN sed -e 's/dl-cdn[.]alpinelinux.org/mirrors.aliyun.com/g' -i~ /etc/apk/repositories
```
2. debian镜像源
```Dockerfile
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
```
3. pip镜像源
```Dockerfile
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
4. tox镜像源
```ini
[tox]
envlist = py37,pre-commit
indexserver =
    default = https://pypi.tuna.tsinghua.edu.cn/simple
```

生成镜像
```bash
docker buildx build --platform=linux/arm64,linux/amd64,linux/arm --push -t csedge/compose:1.26.0 .
```

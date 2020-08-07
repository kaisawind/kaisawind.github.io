---
layout: post
title:  "Docker Registry服务部署"
date: 2019-04-24 17:19:43 +0800
categories: [docker,docker]
excerpt_separator: <!--more-->
---

Registry是一个无状态，高度可扩展的服务端应用程序，可存储并允许您分发Docker镜像。
从docker官方镜像库拉去镜像太慢，所以需要本地的Registry进行镜像的本地化管理。

<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [Docker Registry服务部署](#docker-registry服务部署)
	* [1. 概述](#1-概述)
	* [2. 部署](#2-部署)
		* [2.1 创建Registry文件夹](#21-创建registry文件夹)
		* [2.2 下载registry镜像到本地](#22-下载registry镜像到本地)
		* [2.3 启动registry镜像](#23-启动registry镜像)
		* [2.4 配置docker私有镜像库](#24-配置docker私有镜像库)
		* [2.5 上传镜像到私有镜像库](#25-上传镜像到私有镜像库)
		* [2.6 从私有镜像库下载镜像](#26-从私有镜像库下载镜像)

<!-- /code_chunk_output -->

## 1. 概述

Registry是一个无状态，高度可扩展的服务端应用程序，可存储并允许您分发Docker镜像。
从docker官方镜像库拉去镜像太慢，所以需要本地的Registry进行服务的本地话管理。

## 2. 部署

### 2.1 创建Registry文件夹

应为镜像会占用比较大的磁盘空间，所以Registry文件夹需要放到大磁盘分区中。

```shell
mkdir ~/DockerRegistry
```

### 2.2 下载registry镜像到本地

```shell
docker pull registry
```

### 2.3 启动registry镜像

```shell
docker run -d -p 5000:5000 \
  --restart=always \
  --name registry \
  -v /home/user/registry-conf/config.yml:/etc/docker/registry/config.yml \
  -v /home/user/DockerRegistry:/var/lib/registry
```

* -p 5000:5000 指定registry映射到主机的端口为5000
* --restart=always 如果镜像异常关闭将会重启
* -d 后台运行
* -v /home/user/registry-conf/config.yml:/etc/docker/registry/config.yml
    挂载本地的配置文件替换容器内部默认的配置文件
* /home/user/DockerRegistry:/var/lib/registry
    将容器内部的存储文件映射到本地进行存储

### 2.4 配置docker私有镜像库

如果需要向私有镜像库上传镜像，需要修改docker的daemon.json文件。

文件位置：/etc/docker/daemon.json

将私有镜像库的ip地址追加到daemon.json中，假设私有镜像库地址为`192.168.1.192:5000`

```json
{
    "insecure-registries": [
        "192.168.1.192:5000","dev.teamx.work"
    ]
}

```

重启docker

```shell
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### 2.5 上传镜像到私有镜像库

重命名镜像

```shell
docker 127.0.0.1:5000/adax/adax-webui 192.168.1.192:5000/adax/adax-webui
```

上传镜像到私有镜像库

```shell
docker push 192.168.1.192:5000/adax/adax-webui
```

### 2.6 从私有镜像库下载镜像

```shell
docker pull 192.168.1.192:5000/adax/adax-webui
```
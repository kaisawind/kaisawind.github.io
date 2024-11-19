---
layout: post
title:  "docker本地创建多平台镜像"
date: 2024-11-19 12:49:54
categories: [linux,ubuntu,docker]
tags: [ubuntu, docker]
draft: false
excerpt_separator: <!--more-->
---
docker本地创建多平台镜像-ce
<!--more-->


```bash
#!/bin/bash
set -e

#!/bin/bash

set -e

# 镜像版本
version=$2
# 镜像名称
image=$1
# 本地仓库地址
registry=192.168.1.118:5000

docker pull --platform=linux/arm64 ${image}:${version} && \
docker tag ${image}:${version} ${registry}/${image}:${version}-arm64 && \
docker push ${registry}/${image}:${version}-arm64

docker pull --platform=linux/amd64 ${image}:${version} && \
docker tag ${image}:${version} ${registry}/${image}:${version}-amd64 && \
docker push ${registry}/${image}:${version}-amd64

docker manifest create --insecure ${registry}/${image}:${version} ${registry}/${image}:${version}-arm64 ${registry}/${image}:${version}-amd64
docker manifest annotate --insecure ${registry}/${image}:${version} ${registry}/${image}:${version}-arm64 --os linux --arch arm64
docker manifest annotate --insecure ${registry}/${image}:${version} ${registry}/${image}:${version}-amd64 --os linux --arch amd64

docker manifest --insecure push -p ${registry}/${image}:${version} 
```
---
layout: post
title:  "Docker 本地创建多平台镜像"
date: 2024-11-19 12:49:54
lastmod: 2026-03-19
categories: [linux,ubuntu,docker]
tags: [ubuntu, docker]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "Docker 本地创建多平台镜像，支持同时构建和部署适用于不同架构（如 amd64、arm64）的镜像。本文介绍如何使用 Docker manifest 创建多平台镜像。"
---
Docker 本地创建多平台镜像，支持同时构建和部署适用于不同架构（如 amd64、arm64）的镜像。本文介绍如何使用 Docker manifest 创建多平台镜像。
<!--more-->

> **提示**: Docker 已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。

## 概述

多平台镜像允许一个镜像标签支持多个 CPU 架构，Docker 会根据运行环境自动选择合适架构的镜像。常见架构包括：

- **amd64**: x86_64 架构（PC、服务器）
- **arm64**: ARM 64位架构（Apple Silicon、ARM 服务器）
- **arm/v7**: ARM 32位架构（树莓派等）

## 前置要求

```bash
# 启用 experimental 特性
export DOCKER_CLI_EXPERIMENTAL=enabled

# 验证 buildx 是否可用
docker buildx version
```

## 方法一：使用 Manifest（推荐）

### 基本步骤

```bash
# 1. 拉取不同架构的镜像
docker pull --platform=linux/amd64 nginx:latest
docker pull --platform=linux/arm64 nginx:latest

# 2. 为镜像打标签
docker tag nginx:latest registry.example.com/nginx:latest-amd64
docker tag nginx:latest registry.example.com/nginx:latest-arm64

# 3. 创建 manifest
docker manifest create registry.example.com/nginx:latest \
  registry.example.com/nginx:latest-amd64 \
  registry.example.com/nginx:latest-arm64

# 4. 标注架构信息
docker manifest annotate registry.example.com/nginx:latest \
  registry.example.com/nginx:latest-amd64 --os linux --arch amd64
docker manifest annotate registry.example.com/nginx:latest \
  registry.example.com/nginx:latest-arm64 --os linux --arch arm64

# 5. 推送 manifest
docker manifest push registry.example.com/nginx:latest
```

### 完整脚本

```bash
#!/bin/bash

set -e

# 镜像版本
version=$2
# 镜像名称
image=$1
# 本地仓库地址
registry=192.168.1.118:5000

echo "开始处理镜像: ${image}:${version}"

# 拉取 ARM64 架构镜像
echo "拉取 ARM64 镜像..."
docker pull --platform=linux/arm64 ${image}:${version} && \
docker tag ${image}:${version} ${registry}/${image}:${version}-arm64 && \
docker push ${registry}/${image}:${version}-arm64

# 拉取 AMD64 架构镜像
echo "拉取 AMD64 镜像..."
docker pull --platform=linux/amd64 ${image}:${version} && \
docker tag ${image}:${version} ${registry}/${image}:${version}-amd64 && \
docker push ${registry}/${image}:${version}-amd64

# 创建多平台 manifest
echo "创建 manifest..."
docker manifest create --insecure -a ${registry}/${image}:${version} \
  ${registry}/${image}:${version}-arm64 \
  ${registry}/${image}:${version}-amd64

# 标注架构信息
echo "标注架构信息..."
docker manifest annotate ${registry}/${image}:${version} \
  ${registry}/${image}:${version}-arm64 --os linux --arch arm64
docker manifest annotate ${registry}/${image}:${version} \
  ${registry}/${image}:${version}-amd64 --os linux --arch amd64

# 推送 manifest
echo "推送 manifest..."
docker manifest push --insecure -p ${registry}/${image}:${version}

echo "完成!"
```

### 使用方法

```bash
# 赋予执行权限
chmod +x build_multiarch.sh

# 执行脚本
./build_multiarch.sh nginx 1.24
```

## 方法二：使用 Docker Buildx

### 初始化构建器

```bash
# 创建新的构建器实例
docker buildx create --name multiarch-builder --use

# 启动构建器
docker buildx inspect --bootstrap
```

### 构建多平台镜像

```bash
# 构建并推送到本地仓库
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t registry.example.com/myapp:latest \
  --push \
  .

# 构建并加载到本地（仅支持当前架构）
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:latest \
  --load \
  .
```

### 使用 Dockerfile 示例

```dockerfile
FROM alpine:latest
RUN apk add --no-cache python3
COPY app.py /app/
CMD ["python3", "/app/app.py"]
```

## 验证多平台镜像

```bash
# 查看 manifest 信息
docker manifest inspect registry.example.com/nginx:latest

# 测试不同架构
docker run --rm --platform linux/amd64 nginx:latest uname -m
docker run --rm --platform linux/arm64 nginx:latest uname -m
```

## 常见问题

### manifest create 失败

```bash
# 清理旧的 manifest
docker manifest rm registry.example.com/nginx:latest

# 重新创建
docker manifest create registry.example.com/nginx:latest \
  registry.example.com/nginx:latest-amd64
```

### 平台架构不支持

```bash
# 查看支持的平台
docker buildx ls

# 添加模拟平台
docker run --privileged --rm tonistiigi/binfmt --install all
```

### 推送失败

```bash
# 配置 insecure registry
echo '{"insecure-registries":["192.168.1.118:5000"]}' | \
  sudo tee -a /etc/docker/daemon.json

# 重启 Docker 服务
sudo systemctl restart docker
```

## 最佳实践

1. **命名规范**: 使用 `-amd64`、`-arm64` 等后缀区分架构
2. **版本管理**: 明确版本号，避免使用 `latest`
3. **自动化**: 使用 CI/CD 管道自动化多平台构建
4. **测试验证**: 在不同架构上测试镜像功能
5. **文档记录**: 记录构建和部署流程

## 相关命令速查

```bash
# 查看镜像架构
docker image inspect nginx:latest | grep Architecture

# 查看 manifest 信息
docker manifest inspect registry.example.com/nginx:latest

# 删除 manifest
docker manifest rm registry.example.com/nginx:latest

# 查看构建器状态
docker buildx ls

# 切换构建器
docker buildx use multiarch-builder
```
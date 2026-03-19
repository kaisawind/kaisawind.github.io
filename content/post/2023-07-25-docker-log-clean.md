---
layout: post
title:  "Docker容器日志清理"
date: 2023-07-25 14:33:46
lastmod: 2026-03-19
categories: [docker,linux]
tags: [docker]
excerpt_separator: <!--more-->
---
Docker容器日志清理
<!--more-->

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。

## 问题背景

Docker容器日志会不断增长，占用大量磁盘空间。需要定期清理或限制日志大小。

## 查看日志大小

```bash
# 查看所有容器日志大小
docker ps -aq | xargs docker inspect --format='{{.LogPath}}' | xargs ls -lh

# 查看特定容器日志
docker inspect --format='{{.LogPath}}' <container_id>
ls -lh $(docker inspect --format='{{.LogPath}}' <container_id>)
```

## 清理日志

### 方法1：truncate清空日志

```bash
# 清空特定容器日志
truncate -s 0 $(docker inspect --format='{{.LogPath}}' <container_id>)

# 清空所有容器日志
docker ps -aq | xargs -I {} sh -c "truncate -s 0 $(docker inspect --format='{{.LogPath}}' {})"
```

### 方法2：手动删除日志文件

```bash
# 停止容器
docker stop <container_id>

# 删除日志文件
rm $(docker inspect --format='{{.LogPath}}' <container_id>)

# 重启容器
docker start <container_id>
```

## 限制日志大小

### 配置daemon.json

编辑 `/etc/docker/daemon.json`：

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

参数说明：
- `max-size`: 单个日志文件最大大小
- `max-file`: 保留的日志文件数量

重启Docker服务：
```bash
sudo systemctl restart docker
```

### 单个容器配置

```bash
# 运行时指定日志配置
docker run --log-driver json-file --log-opt max-size=10m --log-opt max-file=3 nginx

# docker-compose.yml
services:
  nginx:
    image: nginx
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## 日志驱动选择

```bash
# none: 禁用日志
docker run --log-driver none nginx

# json-file: 默认驱动
docker run --log-driver json-file nginx

# syslog: 发送到syslog
docker run --log-driver syslog nginx

# journald: 发送到journald
docker run --log-driver journald nginx

# local: 本地日志，带轮转
docker run --log-driver local --log-opt max-size=10m nginx
```

## 定时清理脚本

```bash
#!/bin/bash
# docker-log-clean.sh

# 清理所有容器日志
docker ps -aq | xargs -I {} sh -c "truncate -s 0 $(docker inspect --format='{{.LogPath}}' {})"

# 删除悬空镜像
docker image prune -f

# 删除停止的容器
docker container prune -f

# 删除未使用的网络
docker network prune -f

# 清理所有未使用资源
docker system prune -f
```

## 设置定时任务

```bash
# 编辑crontab
crontab -e

# 每周日凌晨2点清理
0 2 * * 0 /path/to/docker-log-clean.sh >> /var/log/docker-clean.log 2>&1
```

## 最佳实践

1. **设置日志限制**：在daemon.json中配置全局日志限制
2. **定期清理**：设置定时任务定期清理
3. **使用日志驱动**：生产环境使用syslog或ELK收集日志
4. **监控磁盘**：监控/var/lib/docker目录磁盘使用
5. **应用日志分离**：应用日志挂载到宿主机单独管理
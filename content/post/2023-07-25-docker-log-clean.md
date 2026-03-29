---
layout: post
title:  "Docker容器日志清理"
date: 2023-07-25 14:33:46
lastmod: 2026-03-19
categories: [docker,linux]
tags: [docker]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "Docker容器日志清理"
---
Docker容器日志清理
<!--more-->

> **提示**: Docker已推出新的命令结构，, 建议使用 `docker image` 和 `docker container` 子命令。

## 方法1：限制日志大小

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

## 方法2：手动清理日志

### 查看日志大小

```bash
# 查看Docker日志目录
sudo du -sh /var/lib/docker/containers/*/*.log

# 查看总大小
sudo du -sh /var/lib/docker/containers
```

### 清理特定容器日志

```bash
# 清空日志文件
sudo truncate -s 0 /var/lib/docker/containers/*/*.log

# 或删除后重建
sudo rm /var/lib/docker/containers/*/*.log
sudo systemctl restart docker
```

### 一键清理脚本

```bash
#!/bin/bash
# docker-log-clean.sh

echo "Cleaning Docker logs..."

for log in /var/lib/docker/containers/*/*.log; do
    echo "Truncating: $log"
    sudo truncate -s 0 "$log"
done

echo "Done!"
```

## 方法3：使用日志驱动

### 使用journald驱动

```bash
# 修改daemon.json
{
  "log-driver": "journald"
}

# 或运行时指定
docker run --log-driver journald nginx
```

### 使用syslog驱动

```bash
{
  "log-driver": "syslog",
  "log-opts": {
    "syslog-address": "tcp://192.168.0.42:123"
  }
}
```

### 使用none驱动

```bash
# 完全禁用日志
docker run --log-driver none nginx
```

## 方法4：Docker Compose配置

```yaml
services:
  app:
    image: nginx
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## 定时清理

### 使用CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: log-cleaner
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: cleaner
            image: alpine
            command:
            - sh
            - -c
            - find /var/lib/docker/containers -name "*.log" -exec truncate -s 0 {} \;
            volumeMounts:
            - name: docker-containers
              mountPath: /var/lib/docker/containers
          volumes:
          - name: docker-containers
            hostPath:
              path: /var/lib/docker/containers
          restartPolicy: OnFailure
```

## 监控日志大小

```bash
#!/bin/bash
# monitor_logs.sh

THRESHOLD=5G
LOG_DIR="/var/lib/docker/containers"

size=$(du -sb $LOG_DIR | cut -f1)
size_human=$(du -sh $LOG_DIR | cut -f1)

if [ $size -gt $((5*1024*1024*1024)) ]; then
    echo "Warning: Docker logs exceed ${THRESHOLD}. Current size: ${size_human}"
    # 发送警报
fi
```

## 最佳实践

1. **提前配置**：在部署前设置日志限制
2. **统一管理**：使用日志驱动集中管理
3. **定期监控**：监控日志文件大小
4. **日志轮转**：使用logrotate自动清理
5. **避免truncate**：生产环境优先使用配置限制

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
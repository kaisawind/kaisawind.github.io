---
layout: post
title:  "docker gui(portainer)"
date: 2020-08-21 13:24:42
lastmod: 2026-03-19
categories: [docker]
tags: [docker]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "docker gui(portainer)"
---
docker gui(portainer)
<!--more-->

Portainer 是一个轻量级的 Docker 管理界面，提供了直观的 Web UI 来管理 Docker 容器、镜像、网络、卷等资源。它支持单机和 Swarm 集群，是 Docker 管理的必备工具之一。

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。

## Portainer 简介

### 什么是 Portainer

Portainer 是一个开源的 Docker 管理工具，具有以下特点：
- 基于 Web 的图形界面
- 轻量级，资源占用低
- 支持 Docker Standalone 和 Swarm 模式
- 提供 REST API
- 支持多用户和权限管理
- 完全开源（MIT 许可证）

### 功能特性

- **容器管理**: 启动、停止、删除、查看日志
- **镜像管理**: 拉取、删除、构建镜像
- **网络管理**: 创建、删除、配置网络
- **卷管理**: 管理 Docker 数据卷
- **服务栈**: 管理 Docker Compose 文件
- **用户管理**: 多用户访问和权限控制
- **集群管理**: 管理 Docker Swarm 集群
- **模板库**: 快速部署常用应用

## 安装方法

### 方法一：Docker Standalone（推荐）

```bash
# 1. 创建数据卷
docker volume create portainer_data

# 2. 运行 Portainer 容器
docker run -d \
  -p 9000:9000 \
  -p 9443:9443 \
  --name=portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# 3. 访问 Portainer
# 浏览器打开: http://localhost:9000
# 或: https://localhost:9443
```

### 方法二：Docker Compose 安装

创建 `docker-compose.yml`:

```yaml
version: '3.8'

services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: always
    ports:
      - "9000:9000"
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    networks:
      - portainer_network

networks:
  portainer_network:
    driver: bridge

volumes:
  portainer_data:
    driver: local
```

启动：

```bash
docker-compose up -d
```

### 方法三：Docker Swarm 集群安装

```bash
# 1. 创建服务栈
docker stack deploy -c portainer-stack.yml portainer
```

创建 `portainer-stack.yml`:

```yaml
version: '3.8'

services:
  portainer:
    image: portainer/portainer-ce:latest
    command: -H unix:///var/run/docker.sock
    ports:
      - target: 9000
        published: 9000
        protocol: tcp
        mode: host
      - target: 9443
        published: 9443
        protocol: tcp
        mode: host
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.role == manager
    networks:
      - portainer_network

networks:
  portainer_network:
    driver: overlay

volumes:
  portainer_data:
    driver: local
```

### 方法四：Kubernetes 安装

使用 Helm 安装：

```bash
# 添加 Portainer Helm 仓库
helm repo add portainer https://portainer.github.io/k8s/
helm repo update

# 安装 Portainer
helm install portainer portainer/portainer --namespace portainer --create-namespace

# 或使用自定义配置
helm install portainer portainer/portainer \
  --namespace portainer \
  --create-namespace \
  --set service.type=LoadBalancer \
  --set tls.enabled=true
```

## 初始配置

### 首次登录

1. 打开浏览器访问 `http://localhost:9000`
2. 创建管理员账户：
   - Username: `admin`
   - Password: 设置强密码（至少 12 个字符）
3. 点击 "Create User"

### 添加 Docker 环境

首次登录后，需要添加 Docker 环境：

1. 选择 "Get Started"
2. 选择环境类型：
   - Docker Standalone
   - Docker Swarm
   - Kubernetes
3. 配置环境详情
4. 点击 "Connect"

### 环境管理

添加多个 Docker 环境：

1. 点击左侧菜单 "Environments"
2. 点击 "Add environment"
3. 选择环境类型
4. 填写环境详情：
   - Name: 环境名称
   - Endpoint: Docker API 地址
5. 点击 "Add environment"

## 主要功能使用

### 1. 容器管理

#### 查看容器列表

```
左侧菜单 → Containers
```

查看所有运行中的容器，包括：
- 容器名称
- 镜像名称
- 状态
- 端口映射
- 资源使用情况

#### 容器操作

```bash
# 在 UI 中可以执行以下操作：

# 启动容器
点击容器的 "Start" 按钮

# 停止容器
点击容器的 "Stop" 按钮

# 重启容器
点击容器的 "Restart" 按钮

# 删除容器
点击容器的 "Remove" 按钮

# 查看日志
点击容器的 "Logs" 按钮

# 进入容器终端
点击容器的 "Console" 按钮

# 查看容器详情
点击容器名称

# 查看容器统计
点击容器的 "Stats" 按钮
```

#### 控制台操作

1. 选择容器
2. 点击 "Console"
3. 选择模式：
   - `/bin/bash` 或 `/bin/sh`
   - `/bin/ash`（Alpine）
4. 点击 "Connect"

### 2. 镜像管理

#### 拉取镜像

```
左侧菜单 → Images → Pull image
```

输入镜像名称：
```
nginx:latest
mysql:5.7
redis:alpine
```

#### 构建镜像

```
左侧菜单 → Images → Build image
```

1. 选择 Dockerfile 路径
2. 设置镜像名称和标签
3. 点击 "Build"

#### 镜像操作

```bash
# 删除镜像
选择镜像 → 点击 "Remove"

# 查看镜像详情
点击镜像名称

# 查看镜像层
点击镜像 → Layers

# 推送镜像到注册表
选择镜像 → Push
```

### 3. 网络管理

#### 创建网络

```
左侧菜单 → Networks → Add network
```

配置网络：
```yaml
Name: my_network
Driver: bridge
Subnet: 172.20.0.0/16
Gateway: 172.20.0.1
```

#### 网络操作

```bash
# 查看网络详情
点击网络名称

# 查看网络中的容器
点击网络 → Containers

# 删除网络
选择网络 → Remove
```

### 4. 卷管理

#### 创建卷

```
左侧菜单 → Volumes → Add volume
```

配置卷：
```yaml
Name: my_volume
Driver: local
```

#### 卷操作

```bash
# 查看卷详情
点击卷名称

# 查看卷内容
点击卷 → Browse

# 删除卷
选择卷 → Remove
```

### 5. 服务栈管理

#### 部署服务栈

```
左侧菜单 → Stacks → Add stack
```

配置栈：
```yaml
Name: my_stack
Editor type: Web editor
Compose file:
  version: '3.8'
  services:
    nginx:
      image: nginx:latest
      ports:
        - "80:80"
    redis:
      image: redis:alpine
```

点击 "Deploy the stack"

#### 更新服务栈

```
左侧菜单 → Stacks → 选择栈 → Editor
```

修改配置后点击 "Update the stack"

#### 删除服务栈

```
左侧菜单 → Stacks → 选择栈 → Remove
```

### 6. 用户管理

#### 创建用户

```
左侧菜单 → Users → Add user
```

配置用户：
```yaml
Username: newuser
Password: securepassword
Role: User
```

#### 权限管理

```
左侧菜单 → Users → 选择用户 → Access control
```

配置用户权限：
- 完全访问
- 只读访问
- 限制访问

## 高级配置

### 1. 配置反向代理（Nginx）

创建 Nginx 配置 `/etc/nginx/conf.d/portainer.conf`:

```nginx
server {
    listen 80;
    server_name portainer.example.com;

    location / {
        proxy_pass http://localhost:9000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # WebSocket 支持
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

重启 Nginx：

```bash
sudo nginx -t
sudo systemctl restart nginx
```

### 2. 配置 SSL/HTTPS

使用 Let's Encrypt：

```bash
# 安装 certbot
sudo apt-get install certbot

# 获取证书
sudo certbot certonly --standalone -d portainer.example.com

# 配置 Nginx SSL
server {
    listen 443 ssl http2;
    server_name portainer.example.com;

    ssl_certificate /etc/letsencrypt/live/portainer.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/portainer.example.com/privkey.pem;

    location / {
        proxy_pass http://localhost:9000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

### 3. 配置备份和恢复

#### 备份 Portainer 数据

```bash
#!/bin/bash
# backup_portainer.sh

BACKUP_DIR="/backup/portainer"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BACKUP_DIR"

# 停止容器
docker stop portainer

# 备份数据卷
docker run --rm \
  -v portainer_data:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/portainer_$DATE.tar.gz /data

# 启动容器
docker start portainer

echo "备份完成: $BACKUP_DIR/portainer_$DATE.tar.gz"
```

#### 恢复 Portainer 数据

```bash
#!/bin/bash
# restore_portainer.sh

BACKUP_FILE=$1

if [ -z "$BACKUP_FILE" ]; then
    echo "用法: $0 <备份文件>"
    exit 1
fi

# 停止容器
docker stop portainer

# 恢复数据卷
docker run --rm \
  -v portainer_data:/data \
  -v $(dirname "$BACKUP_FILE"):/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/$(basename $BACKUP_FILE) -C /data --strip-components=1"

# 启动容器
docker start portainer

echo "恢复完成"
```

### 4. 配置监控和告警

#### 使用 Prometheus 监控

```bash
# Portainer 内置了 Prometheus 端点
# 访问: http://localhost:9000/api/prometheus/metrics

# 配置 Prometheus 抓取
scrape_configs:
  - job_name: 'portainer'
    metrics_path: '/api/prometheus/metrics'
    static_configs:
      - targets: ['localhost:9000']
```

#### 配置告警规则

```yaml
groups:
  - name: portainer_alerts
    rules:
      - alert: PortainerDown
        expr: up{job="portainer"} == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Portainer is down"
          description: "Portainer has been down for more than 5 minutes."
```

## 常见问题和解决方案

### 1. 无法访问 Web 界面

**问题**: 浏览器无法连接到 Portainer

**解决方案**:

```bash
# 1. 检查容器状态
docker ps -a | grep portainer

# 2. 查看容器日志
docker logs portainer

# 3. 检查端口占用
sudo netstat -tlnp | grep 9000

# 4. 重启容器
docker restart portainer

# 5. 检查防火墙
sudo ufw status
sudo ufw allow 9000/tcp
```

### 2. 数据丢失

**问题**: Portainer 重启后数据丢失

**解决方案**:

```bash
# 检查数据卷是否正确挂载
docker inspect portainer | grep -A 10 Mounts

# 确保使用了命名卷
docker volume ls | grep portainer

# 检查数据卷内容
docker run --rm -v portainer_data:/data alpine ls -la /data
```

### 3. 性能问题

**问题**: Portainer 响应缓慢

**解决方案**:

```bash
# 1. 增加容器资源限制
docker run -d \
  --name=portainer \
  --restart=always \
  --memory="512m" \
  --cpus="1.0" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# 2. 清理旧的日志
docker logs portainer --tail 100

# 3. 定期重启
docker restart portainer
```

### 4. 权限问题

**问题**: 无法执行某些操作

**解决方案**:

```bash
# 1. 检查 Docker 套接字权限
sudo ls -la /var/run/docker.sock

# 2. 将用户添加到 docker 组
sudo usermod -aG docker $USER

# 3. 重新登录
newgrp docker

# 4. 重启 Portainer
docker restart portainer
```

### 5. 升级问题

**问题**: 升级后无法启动

**解决方案**:

```bash
# 1. 备份数据
# （参考上面的备份脚本）

# 2. 停止并删除旧容器
docker stop portainer
docker rm portainer

# 3. 拉取新镜像
docker pull portainer/portainer-ce:latest

# 4. 启动新容器
docker run -d \
  --name=portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# 5. 查看日志
docker logs portainer
```

## 最佳实践

### 1. 安全配置

```yaml
# 使用 HTTPS
# 配置 SSL 证书

# 设置强密码
# 至少 12 个字符，包含大小写字母、数字和特殊字符

# 限制用户访问
# 为不同用户分配不同的权限级别

# 定期更新
# 跟踪 Portainer 版本更新

# 启用日志审计
# 记录所有重要操作
```

### 2. 备份策略

```bash
# 定期备份
0 2 * * * /path/to/backup_portainer.sh

# 保留多个备份
find /backup/portainer -type f -mtime +7 -delete

# 验证备份
定期测试恢复流程
```

### 3. 监控和维护

```bash
# 监控资源使用
docker stats portainer

# 检查日志
docker logs -f portainer

# 定期清理
docker system prune -f

# 更新镜像
docker pull portainer/portainer-ce:latest
```

### 4. 集群管理

```bash
# 在 Swarm 集群中部署
docker stack deploy -c portainer-stack.yml portainer

# 使用负载均衡
# 配置多个 Portainer 实例

# 高可用配置
# 使用共享存储和负载均衡器
```

## 自动化脚本

### 一键安装脚本

```bash
#!/bin/bash
# install_portainer.sh

set -e

echo "开始安装 Portainer..."

# 检查 Docker 是否安装
if ! command -v docker &> /dev/null; then
    echo "错误: Docker 未安装"
    exit 1
fi

# 创建数据卷
echo "创建数据卷..."
docker volume create portainer_data

# 停止旧容器（如果存在）
if docker ps -a | grep -q portainer; then
    echo "停止旧容器..."
    docker stop portainer
    docker rm portainer
fi

# 拉取最新镜像
echo "拉取镜像..."
docker pull portainer/portainer-ce:latest

# 启动新容器
echo "启动容器..."
docker run -d \
  -p 9000:9000 \
  -p 9443:9443 \
  --name=portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# 等待容器启动
echo "等待容器启动..."
sleep 10

# 检查容器状态
if docker ps | grep -q portainer; then
    echo "Portainer 安装成功！"
    echo "访问地址: http://localhost:9000"
    echo "或: https://localhost:9443"
else
    echo "Portainer 启动失败，查看日志:"
    docker logs portainer
    exit 1
fi
```

### 更新脚本

```bash
#!/bin/bash
# update_portainer.sh

set -e

echo "开始更新 Portainer..."

# 备份数据
echo "备份数据..."
docker run --rm \
  -v portainer_data:/data \
  -v /backup:/backup \
  alpine tar czf /backup/portainer_$(date +%Y%m%d_%H%M%S).tar.gz /data

# 停止旧容器
echo "停止旧容器..."
docker stop portainer

# 备份容器配置
docker inspect portainer > /tmp/portainer_config.json

# 删除旧容器
docker rm portainer

# 拉取新镜像
echo "拉取新镜像..."
docker pull portainer/portainer-ce:latest

# 启动新容器
echo "启动新容器..."
docker run -d \
  -p 9000:9000 \
  -p 9443:9443 \
  --name=portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# 等待容器启动
echo "等待容器启动..."
sleep 10

# 检查容器状态
if docker ps | grep -q portainer; then
    echo "Portainer 更新成功！"
else
    echo "Portainer 更新失败，正在回滚..."
    # 回滚逻辑...
    exit 1
fi
```

## 相关资源

- Portainer 官网: https://www.portainer.io/
- Portainer 文档: https://docs.portainer.io/
- Portainer GitHub: https://github.com/portainer/portainer
- 安装指南: https://docs.portainer.io/start/install
- 用户指南: https://docs.portainer.io/user/quick-start

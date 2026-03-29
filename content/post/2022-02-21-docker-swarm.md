---
layout: post
title:  "Docker Stack删除无用的服务"
date: 2022-02-21 14:31:46
lastmod: 2026-03-19
categories: [docker,swarm]
tags: [docker]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "Docker Stack删除无用的服务"
---
Docker Stack删除无用的服务
<!--more-->

在 Docker Swarm 集群中使用 Docker Stack 部署应用时，经常会遇到从 docker-compose.yml 文件中删除某些服务后，但这些服务仍然在集群中运行的情况。这是因为 Docker Stack 默认不会自动删除已经部署但不再在配置文件中的服务。本文详细介绍如何正确管理和清理 Docker Stack 中的服务。

## Docker Stack 基础概念

### 什么是 Docker Stack

Docker Stack 是 Docker Swarm 模式下用于部署和管理分布式应用的工具。它基于 docker-compose.yml 文件定义服务栈，可以一键部署多个相关联的服务。

### Stack 部署原理

当执行 `docker stack deploy` 时：
1. 读取 docker-compose.yml 文件
2. 解析服务定义
3. 创建或更新服务
4. **默认保留已存在的服务**

这就是为什么从配置文件中删除服务后，服务仍然存在。

## 问题场景

### 常见问题

```yaml
# docker-compose.yml - 初始版本
version: '3.8'
services:
  mysql:
    image: mysql:5.7
    deploy:
      replicas: 1
  redis:
    image: redis:alpine
    deploy:
      replicas: 1
  nginx:
    image: nginx:alpine
    deploy:
      replicas: 2
```

部署后，运行三个服务：mysql、redis、nginx。

```yaml
# docker-compose.yml - 更新版本（删除了 redis）
version: '3.8'
services:
  mysql:
    image: mysql:5.7
    deploy:
      replicas: 1
  nginx:
    image: nginx:alpine
    deploy:
      replicas: 2
```

重新部署后，redis 服务仍然在运行！

### 问题原因

Docker Stack 采用"声明式"管理：
- 只保证配置文件中的服务存在
- 不保证配置文件中没有的服务被删除
- 这是设计上的保守策略，防止意外删除

## 解决方案：使用 --prune 参数

### 基本用法

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。

```bash
docker stack deploy -c docker-compose.yml iotx --prune
```

### 参数说明

- `-c` 或 `--compose-file`: 指定 compose 文件
- `iotx`: Stack 名称
- `--prune`: 删除不再在配置文件中的服务

### 完整示例

```bash
# 1. 部署 Stack
docker stack deploy -c docker-compose.yml iotx

# 2. 查看当前服务
docker stack services iotx

# ID   NAME             MODE        REPLICAS   IMAGE
# abc  iotx_mysql       replicated  1/1        mysql:5.7
# def  iotx_redis       replicated  1/1        redis:alpine
# ghi  iotx_nginx       replicated  2/2        nginx:alpine

# 3. 修改 docker-compose.yml（删除 redis）

# 4. 重新部署（不使用 --prune）
docker stack deploy -c docker-compose.yml iotx

# 5. 再次查看服务（redis 仍然存在）
docker stack services iotx

# ID   NAME             MODE        REPLICAS   IMAGE
# abc  iotx_mysql       replicated  1/1        mysql:5.7
# def  iotx_redis       replicated  1/1        redis:alpine
# ghi  iotx_nginx       replicated  2/2        nginx:alpine

# 6. 使用 --prune 重新部署
docker stack deploy -c docker-compose.yml iotx --prune

# 7. 查看服务（redis 已删除）
docker stack services iotx

# ID   NAME             MODE        REPLICAS   IMAGE
# abc  iotx_mysql       replicated  1/1        mysql:5.7
# ghi  iotx_nginx       replicated  2/2        nginx:alpine
```

## 详细操作指南

### 1. 检查当前 Stack 状态

```bash
# 列出所有 Stack
docker stack ls

# 查看特定 Stack 的服务
docker stack services iotx

# 查看服务详情
docker service ps iotx_mysql

# 查看 Stack 的网络
docker network ls | grep iotx

# 查看 Stack 的配置
docker stack config iotx
```

### 2. 安全清理流程

```bash
#!/bin/bash
# 安全清理 Docker Stack 中无用的服务

STACK_NAME="iotx"
COMPOSE_FILE="docker-compose.yml"

echo "=== 清理 Stack: $STACK_NAME ==="

# 1. 查看当前服务
echo "当前服务:"
docker stack services $STACK_NAME

# 2. 验证 compose 文件
echo "验证 compose 文件..."
docker-compose -f $COMPOSE_FILE config > /dev/null
if [ $? -ne 0 ]; then
    echo "错误: compose 文件无效"
    exit 1
fi

# 3. 备份当前配置
echo "备份当前配置..."
docker stack config $STACK_NAME > $STACK_NAME-backup.yml

# 4. 使用 --prune 部署
echo "部署并清理..."
docker stack deploy -c $COMPOSE_FILE $STACK_NAME --prune

# 5. 等待服务稳定
echo "等待服务稳定..."
sleep 10

# 6. 验证服务状态
echo "验证服务状态:"
docker stack services $STACK_NAME

# 7. 检查是否有失败的任务
FAILED=$(docker stack services $STACK_NAME --format "{{.Replicas}}" | grep -c "0/")
if [ $FAILED -gt 0 ]; then
    echo "警告: 有服务任务失败"
fi

echo "=== 清理完成 ==="
```

### 3. 批量清理多个 Stack

```bash
#!/bin/bash
# 批量清理多个 Stack

STACKS=("iotx" "app1" "app2")

for stack in "${STACKS[@]}"; do
    echo "处理 Stack: $stack"
    
    # 检查 Stack 是否存在
    docker stack ls --format "{{.Name}}" | grep -q "^$stack$"
    if [ $? -ne 0 ]; then
        echo "Stack $stack 不存在，跳过"
        continue
    fi
    
    # 获取 compose 文件
    COMPOSE_FILE="${stack}-compose.yml"
    
    if [ ! -f "$COMPOSE_FILE" ]; then
        echo "未找到 compose 文件: $COMPOSE_FILE，跳过"
        continue
    fi
    
    # 部署并清理
    docker stack deploy -c $COMPOSE_FILE $stack --prune
    
    echo "Stack $stack 处理完成"
    echo "---"
done
```

## 高级场景

### 1. 多个 compose 文件

```bash
# 使用多个 compose 文件部署
docker stack deploy -c docker-compose.yml -c docker-compose.override.yml iotx --prune

# 合并多个文件后清理
docker-compose -f docker-compose.yml -f docker-compose.override.yml config > merged.yml
docker stack deploy -c merged.yml iotx --prune
```

### 2. 命名空间管理

```bash
# 部署到不同的命名空间（Stack 名称）
docker stack deploy -c dev.yml iotx-dev --prune
docker stack deploy -c prod.yml iotx-prod --prune

# 清理特定命名空间
docker stack rm iotx-dev
```

### 3. 滚动更新和清理

```bash
#!/bin/bash
# 滚动更新并清理

STACK_NAME="iotx"
COMPOSE_FILE="docker-compose.yml"
SERVICE_NAME="app"

echo "滚动更新服务: $SERVICE_NAME"

# 1. 更新镜像版本
docker service update --image myapp:v2.0 iotx_app

# 2. 等待更新完成
while true; do
    replicas=$(docker service ls --filter name=iotx_app --format "{{.Replicas}}")
    if [[ $replicas == *"/"* ]]; then
        running=${replicas%%/*}
        total=${repairs##*/}
        if [ $running -eq $total ]; then
            echo "更新完成"
            break
        fi
    fi
    echo "等待中: $replicas"
    sleep 5
done

# 3. 清理旧配置
docker stack deploy -c $COMPOSE_FILE $STACK_NAME --prune
```

## 常见问题和解决方案

### 1. --prune 参数无效

**问题**: 使用 --prune 后服务仍然存在

**原因**: 
- 服务在 compose 文件中但被禁用
- 服务名称不匹配
- 缓存问题

**解决方案**:

```bash
# 1. 清理 Docker 缓存
docker system prune -f

# 2. 强制重新拉取镜像
docker stack deploy -c docker-compose.yml iotx --prune --with-registry-auth

# 3. 手动删除服务
docker service rm iotx_redis

# 4. 检查服务名称
docker stack services iotx --format "{{.Name}}"
```

### 2. 服务依赖关系

**问题**: 删除某个服务后，其他服务无法启动

**原因**: 服务间存在依赖关系

**解决方案**:

```yaml
# 在 compose 文件中定义依赖
version: '3.8'
services:
  web:
    image: myweb:latest
    depends_on:
      - db
      - cache
  db:
    image: mysql:5.7
  cache:
    image: redis:alpine
```

```bash
# 安全删除顺序
# 1. 先删除依赖方
docker service rm iotx_web

# 2. 再删除被依赖方
docker service rm iotx_db

# 3. 最后使用 --prune 部署
docker stack deploy -c docker-compose.yml iotx --prune
```

### 3. 数据丢失风险

**问题**: 清理服务时误删数据

**解决方案**:

```yaml
# 使用命名卷持久化数据
version: '3.8'
services:
  mysql:
    image: mysql:5.7
    volumes:
      - mysql_data:/var/lib/mysql
volumes:
  mysql_data:
    driver: local
```

```bash
# 备份数据卷
docker run --rm -v iotx_mysql_data:/data -v $(pwd):/backup \
    ubuntu tar czf /backup/mysql-backup.tar.gz /data

# 清理前确认数据已备份
docker volume ls
```

### 4. 网络资源泄漏

**问题**: 重复部署后网络资源累积

**解决方案**:

```bash
# 查看网络
docker network ls | grep iotx

# 清理未使用的网络
docker network prune -f

# 清理特定 Stack 的网络
docker network rm iotx_default
```

## 最佳实践

### 1. 部署流程

```bash
#!/bin/bash
# 标准部署流程

set -e

# 1. 验证配置文件
echo "验证配置文件..."
docker-compose config > /dev/null

# 2. 拉取最新镜像
echo "拉取镜像..."
docker-compose pull

# 3. 部署并清理
echo "部署服务..."
docker stack deploy -c docker-compose.yml iotx --prune

# 4. 等待服务就绪
echo "等待服务就绪..."
timeout 300 bash -c 'until docker stack services iotx --format "{{.Replicas}}" | grep -v "0/"; do sleep 5; done'

echo "部署完成"
```

### 2. 版本管理

```bash
#!/bin/bash
# 版本化部署

VERSION=$(date +%Y%m%d-%H%M%S)
COMPOSE_FILE="docker-compose.yml"
BACKUP_DIR="backups/$VERSION"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 备份当前配置
cp $COMPOSE_FILE $BACKUP_DIR/

# 备份当前服务列表
docker stack services iotx > $BACKUP_DIR/services.txt

# 部署新版本
docker stack deploy -c $COMPOSE_FILE iotx --prune

# 记录部署日志
echo "Deployment $VERSION: $(date)" >> deploy.log
```

### 3. 监控和告警

```bash
#!/bin/bash
# 监控 Stack 状态

STACK_NAME="iotx"
ALERT_EMAIL="admin@example.com"

# 检查服务状态
check_services() {
    docker stack services $STACK_NAME --format "{{.Name}}: {{.Replicas}}" | while read line; do
        service=$(echo $line | cut -d: -f1)
        replicas=$(echo $line | cut -d: -f2 | xargs)
        
        if [[ $replicas == *"0/"* ]]; then
            echo "警告: 服务 $replicas 停止运行"
            # 发送告警
            echo "服务停止: $line" | mail -s "Stack Alert" $ALERT_EMAIL
        fi
    done
}

# 定期检查
while true; do
    check_services
    sleep 60
done
```

### 4. 灾难恢复

```bash
#!/bin/bash
# Stack 恢复脚本

STACK_NAME="iotx"
BACKUP_DIR="backups/latest"

# 1. 删除现有 Stack
echo "删除现有 Stack..."
docker stack rm $STACK_NAME

# 2. 等待删除完成
echo "等待删除完成..."
while docker stack ls --format "{{.Name}}" | grep -q "^$STACK_NAME$"; do
    sleep 2
done

# 3. 恢复配置
echo "恢复配置..."
cp $BACKUP_DIR/docker-compose.yml .

# 4. 重新部署
echo "重新部署..."
docker stack deploy -c docker-compose.yml $STACK_NAME --prune

# 5. 验证服务
echo "验证服务..."
docker stack services $STACK_NAME

echo "恢复完成"
```

## 完整示例项目

### docker-compose.yml

```yaml
version: '3.8'

services:
  # 数据库服务
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: mydb
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - backend
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == manager
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3

  # 缓存服务
  redis:
    image: redis:alpine
    networks:
      - backend
    deploy:
      replicas: 1
      restart_policy:
        condition: on-failure

  # 应用服务
  app:
    image: myapp:latest
    depends_on:
      - mysql
      - redis
    environment:
      DB_HOST: mysql
      REDIS_HOST: redis
    networks:
      - frontend
      - backend
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure

  # Web 服务
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    networks:
      - frontend
    deploy:
      replicas: 2
      placement:
        constraints:
          - node.labels.web == true

  # 监控服务
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - prometheus_data:/prometheus
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - backend
    deploy:
      replicas: 1

networks:
  frontend:
    driver: overlay
  backend:
    driver: overlay

volumes:
  mysql_data:
    driver: local
  prometheus_data:
    driver: local
```

### 部署脚本 deploy.sh

```bash
#!/bin/bash
set -e

STACK_NAME="iotx"
COMPOSE_FILE="docker-compose.yml"
VERSION=$(date +%Y%m%d-%H%M%S)

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 1. 前置检查
log_info "前置检查..."
if [ ! -f "$COMPOSE_FILE" ]; then
    log_error "配置文件不存在: $COMPOSE_FILE"
    exit 1
fi

# 2. 验证配置
log_info "验证配置..."
docker-compose -f $COMPOSE_FILE config > /dev/null || exit 1

# 3. 备份
log_info "备份配置..."
mkdir -p backups/$VERSION
cp $COMPOSE_FILE backups/$VERSION/
docker stack ls --format "{{.Name}} {{.Services}}" | grep $STACK_NAME > backups/$VERSION/stack.txt 2>/dev/null || true

# 4. 拉取镜像
log_info "拉取镜像..."
docker-compose -f $COMPOSE_FILE pull

# 5. 部署
log_info "部署服务..."
docker stack deploy -c $COMPOSE_FILE $STACK_NAME --prune

# 6. 等待服务就绪
log_info "等待服务就绪..."
timeout 300 bash -c '
while true; do
    replicas=$(docker stack services iotx --format "{{.Replicas}}" | grep -v "0/")
    if [ -n "$replicas" ]; then
        echo "所有服务已就绪"
        break
    fi
    echo "等待中..."
    sleep 5
done' || {
    log_error "部署超时"
    exit 1
}

# 7. 验证
log_info "验证服务状态..."
docker stack services $STACK_NAME

# 8. 健康检查
log_info "健康检查..."
docker stack services $STACK_NAME --format "{{.Name}}: {{.Replicas}}" | while read line; do
    if [[ $line == *"0/"* ]]; then
        log_warn "部分服务未就绪: $line"
    fi
done

log_info "部署完成！"
log_info "版本: $VERSION"
log_info "备份目录: backups/$VERSION"
```

### 清理脚本 cleanup.sh

```bash
#!/bin/bash
set -e

STACK_NAME="iotx"

# 1. 列出当前服务
echo "当前服务:"
docker stack services $STACK_NAME

# 2. 确认
read -p "确认删除 Stack? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "取消删除"
    exit 0
fi

# 3. 删除 Stack
echo "删除 Stack..."
docker stack rm $STACK_NAME

# 4. 等待删除完成
echo "等待删除完成..."
while docker stack ls --format "{{.Name}}" | grep -q "^$STACK_NAME$"; do
    sleep 2
done

# 5. 清理网络
echo "清理网络..."
docker network prune -f

# 6. 清理卷（可选）
read -p "删除数据卷? (yes/no): " confirm_vols
if [ "$confirm_vols" = "yes" ]; then
    echo "删除数据卷..."
    docker volume rm $(docker volume ls -q | grep $STACK_NAME)
fi

echo "清理完成"
```

## 相关资源

- Docker Stack 文档: https://docs.docker.com/engine/reference/commandline/stack_deploy/
- Docker Compose 文档: https://docs.docker.com/compose/
- Docker Swarm 文档: https://docs.docker.com/engine/swarm/

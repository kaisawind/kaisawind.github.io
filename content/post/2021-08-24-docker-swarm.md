---
layout: post
title:  "Docker Swarm部署服务"
date: 2021-08-24 11:31:46
categories: [docker,swarm]
tags: [docker]
excerpt_separator: <!--more-->
---
Docker Swarm部署服务
<!--more-->

## 1. 概述
Docker Swarm使用docker stack部署服务， 配置文件使用的是docker compose的配置文件，但是又不能完全使用compose文件。

## 2. 配置文件修改

* 环境变量的处理
因为docker stack不支持环境变量文件`.env`，所以需要先将compose.yml转换为完全体文件
```bash
docker-compose -f docker-compose.yml -p test config
```
复制输出内容到新的文件中。


* 修改网络类型
```yml
networks:
  iotx-network:
    driver: overlay # 网络类型需要是overlay
```

* 服务间依赖的处理
去掉所有的`depends_on`

* 本地挂在的处理
由于docker swarm是分布式集群，所以不能进行本地数据挂载。
当使用docker volume时，docker stack能正常运行，但是服务数据只会存储在指定的node上，当服务迁移，数据会变为其他node上的数据。
简而言之，node间数据是不共享的。

使用NFS进行数据共享
```yml
volumes:
  redis-data:
    driver: local
    driver_opts:
      type: nfs
      o: nfsvers=4,addr=192.168.1.118,rw
      device: ":/home/storage/redis-data"
```

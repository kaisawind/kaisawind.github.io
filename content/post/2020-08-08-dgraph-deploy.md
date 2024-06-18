---
layout: post
title:  "使用docker部署dgraph"
date: 2020-08-08 00:57:04
categories: [数据库, dgraph]
tags: [dgraph]
excerpt_separator: <!--more-->
---
dgraph部署
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 单`Alpha`](#2-单alpha)
- [3. 多`Alpha`](#3-多alpha)
- [4. 多`Zero`](#4-多zero)
- [5. 多`Zero`多节点](#5-多zero多节点)

<!-- /code_chunk_output -->


## 1. 概述
dgraph主要有三个服务:

Zero: 是集群的核心, 负责调度集群服务器和平衡服务器组之间的数据。本身不保存数据。
Alpha: 保存数据的`谓词`和`索引`. 谓词包括数据的`属性`和`数据`之间的关系; `索引`是为了更快的进行数据的过滤和查找。
Ratel: dgraph 的 UI 接口, 可以在此界面上进行数据的 CURD, 也可以修改数据的 schema。

## 2. 单`Alpha`

```yaml
version: '3.8'

volumes:
  zero1-data:
  alpha1-data:

services:
  # dgraph cluster core
  zero1:
    image: dgraph/dgraph:latest
    container_name: iotx-zero1
    hostname: iotx-zero1
    restart: on-failure
    networks:
      - iotx-network
    ports:
      - 6080:6080
    volumes:
      - zero1-data:/dgraph
    command: dgraph zero --my=iotx-zero1:5080 --replicas=1  --idx 1
  alpha1:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha1
    hostname: iotx-alpha1
    networks:
      - iotx-network
    ports:
      - 9080:9080
      - 8080:8080
    volumes:
      - alpha1-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha1:7080 --lru_mb=2048 --zero=iotx-zero1:5080 --idx=1
    depends_on:
      - zero1
  ratel:
    image: dgraph/dgraph:latest
    container_name: iotx-ratel
    hostname: iotx-ratel
    networks:
      - iotx-network
    ports:
      - 7000:8000
    restart: always
    command: dgraph-ratel
networks:
  iotx-network:
    driver: "bridge"
```

## 3. 多`Alpha`

```yaml
version: '3.8'

volumes:
  zero1-data:
  alpha1-data:
  alpha2-data:
  alpha3-data:

services:
  # dgraph cluster core
  zero1:
    image: dgraph/dgraph:latest
    container_name: iotx-zero1
    hostname: iotx-zero1
    restart: on-failure
    networks:
      - iotx-network
    ports:
      - 6080:6080
    volumes:
      - zero1-data:/dgraph
    command: dgraph zero --my=iotx-zero1:5080 --replicas=1  --idx 1
  alpha1:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha1
    hostname: iotx-alpha1
    networks:
      - iotx-network
    ports:
      - 9080:9080
      - 8080:8080
    volumes:
      - alpha1-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha1:7080 --lru_mb=2048 --zero=iotx-zero1:5080 --idx=1
    depends_on:
      - zero1
  alpha2:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha2
    hostname: iotx-alpha2
    networks:
      - iotx-network
    ports:
      - 9081:9080
      - 8081:8080
    volumes:
      - alpha2-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha2:7080 --lru_mb=2048 --zero=iotx-zero1:5080 --idx=2
    depends_on:
      - zero1
  alpha3:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha3
    hostname: iotx-alpha3
    networks:
      - iotx-network
    ports:
      - 9082:9080
      - 8082:8080
    volumes:
      - alpha3-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha3:7080 --lru_mb=2048 --zero=iotx-zero1:5080 --idx=3
    depends_on:
      - zero1
  ratel:
    image: dgraph/dgraph:latest
    container_name: iotx-ratel
    hostname: iotx-ratel
    networks:
      - iotx-network
    ports:
      - 7000:8000
    restart: always
    command: dgraph-ratel
networks:
  iotx-network:
    driver: "bridge"
```

## 4. 多`Zero`

```yaml
version: '3.8'

volumes:
  zero1-data:
  zero2-data:
  zero3-data:
  alpha1-data:
  alpha2-data:
  alpha3-data:

services:
  # dgraph cluster core
  zero1:
    image: dgraph/dgraph:latest
    container_name: iotx-zero1
    hostname: iotx-zero1
    restart: on-failure
    networks:
      - iotx-network
    ports:
      - 6080:6080
    volumes:
      - zero1-data:/dgraph
    command: dgraph zero --my=iotx-zero1:5080 --replicas=1  --idx 1
  zero2:
    image: dgraph/dgraph:latest
    container_name: iotx-zero2
    hostname: iotx-zero2
    restart: on-failure
    networks:
      - iotx-network
    volumes:
      - zero2-data:/dgraph
    command: dgraph zero --my=iotx-zero2:5080 --peer=iotx-zero1:5080 --replicas=1 --idx 2
  zero3:
    image: dgraph/dgraph:latest
    container_name: iotx-zero3
    hostname: iotx-zero3
    restart: on-failure
    networks:
      - iotx-network
    volumes:
      - zero3-data:/dgraph
    command: dgraph zero --my=iotx-zero3:5080 --peer=iotx-zero1:5080 --replicas=1 --idx 3
  alpha1:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha1
    hostname: iotx-alpha1
    networks:
      - iotx-network
    ports:
      - 9080:9080
      - 8080:8080
    volumes:
      - alpha1-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha1:7080 --lru_mb=2048 --zero=iotx-zero1:5080,iotx-zero2:5080,iotx-zero3:5080 --idx=1
    depends_on:
      - zero1
  alpha2:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha2
    hostname: iotx-alpha2
    networks:
      - iotx-network
    ports:
      - 9081:9080
      - 8081:8080
    volumes:
      - alpha2-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha2:7080 --lru_mb=2048 --zero=iotx-zero1:5080,iotx-zero2:5080,iotx-zero3:5080 --idx=2
    depends_on:
      - zero1
  alpha3:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha3
    hostname: iotx-alpha3
    networks:
      - iotx-network
    ports:
      - 9082:9080
      - 8082:8080
    volumes:
      - alpha3-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha3:7080 --lru_mb=2048 --zero=iotx-zero1:5080,iotx-zero2:5080,iotx-zero3:5080 --idx=3
    depends_on:
      - zero1
  ratel:
    image: dgraph/dgraph:latest
    container_name: iotx-ratel
    hostname: iotx-ratel
    networks:
      - iotx-network
    ports:
      - 7000:8000
    restart: always
    command: dgraph-ratel
networks:
  iotx-network:
    driver: "bridge"
```

## 5. 多`Zero`多节点

`replicas=3`意味着每个group包含三个`alpine`

```yaml
version: '3.8'

volumes:
  zero1-data:
  zero2-data:
  zero3-data:
  alpha1-data:
  alpha2-data:
  alpha3-data:

services:
  # dgraph cluster core
  zero1:
    image: dgraph/dgraph:latest
    container_name: iotx-zero1
    hostname: iotx-zero1
    restart: on-failure
    networks:
      - iotx-network
    ports:
      - 6080:6080
    volumes:
      - zero1-data:/dgraph
    command: dgraph zero --my=iotx-zero1:5080 --replicas=3  --idx 1
  zero2:
    image: dgraph/dgraph:latest
    container_name: iotx-zero2
    hostname: iotx-zero2
    restart: on-failure
    networks:
      - iotx-network
    volumes:
      - zero2-data:/dgraph
    command: dgraph zero --my=iotx-zero2:5080 --peer=iotx-zero1:5080 --replicas=3 --idx 2
  zero3:
    image: dgraph/dgraph:latest
    container_name: iotx-zero3
    hostname: iotx-zero3
    restart: on-failure
    networks:
      - iotx-network
    volumes:
      - zero3-data:/dgraph
    command: dgraph zero --my=iotx-zero3:5080 --peer=iotx-zero1:5080 --replicas=3 --idx 3
  alpha1:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha1
    hostname: iotx-alpha1
    networks:
      - iotx-network
    ports:
      - 9080:9080
      - 8080:8080
    volumes:
      - alpha1-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha1:7080 --lru_mb=2048 --zero=iotx-zero1:5080,iotx-zero2:5080,iotx-zero3:5080 --idx=1
    depends_on:
      - zero1
  alpha2:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha2
    hostname: iotx-alpha2
    networks:
      - iotx-network
    ports:
      - 9081:9080
      - 8081:8080
    volumes:
      - alpha2-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha2:7080 --lru_mb=2048 --zero=iotx-zero1:5080,iotx-zero2:5080,iotx-zero3:5080 --idx=2
    depends_on:
      - zero1
  alpha3:
    image: dgraph/dgraph:latest
    container_name: iotx-alpha3
    hostname: iotx-alpha3
    networks:
      - iotx-network
    ports:
      - 9082:9080
      - 8082:8080
    volumes:
      - alpha3-data:/dgraph
    restart: on-failure
    command: dgraph alpha --my=iotx-alpha3:7080 --lru_mb=2048 --zero=iotx-zero1:5080,iotx-zero2:5080,iotx-zero3:5080 --idx=3
    depends_on:
      - zero1
  ratel:
    image: dgraph/dgraph:latest
    container_name: iotx-ratel
    hostname: iotx-ratel
    networks:
      - iotx-network
    ports:
      - 7000:8000
    restart: always
    command: dgraph-ratel
networks:
  iotx-network:
    driver: "bridge"
```
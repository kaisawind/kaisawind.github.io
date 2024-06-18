---
layout: post
title: "docker运行geoserver服务"
date: 2020-01-08 10:59:00
categories: [map]
tags: [tools]
excerpt_separator: <!--more-->
---
docker运行geoserver服务
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 服务文件存放位置](#2-服务文件存放位置)
- [3. 服务启动](#3-服务启动)

<!-- /code_chunk_output -->


## 1. 概述

geoserver是 OpenGIS Web 服务器规范的 J2EE 实现，利用 GeoServer 可以方便的发布地图数据，允许用户对特征数据进行更新、删除、插入操作，通过 GeoServer 可以比较容易的在用户之间迅速共享空间地理信息。

## 2. 服务文件存放位置

docker hub镜像:
https://hub.docker.com/r/geonode/geoserver

git hub路径:
https://github.com/geonode/geoserver-docker

server config文件:
https://build.geo-solutions.it/geonode/geoserver/latest/

## 3. 服务启动

* 解压配置文件
```bash
sudo mkdir ~/geoserver/
sudo unzip ~/Dowmload/data-2.15.x.zip -d ~/geoserver/
```

* 修改配置文件
proxyBaseUrl地址为client端访问的地址,也可以在web上进行配置
```conf
<global>
  <settings>
...
    <proxyBaseUrl>http://192.168.99.102:8080/geoserver</proxyBaseUrl>
  </settings>
</global>
```

* 启动服务
```bash
docker run --name "geoserver" -v /var/run/docker.sock:/var/run/docker.sock -v ~/geoserver/data:/geoserver_data/data -d -p 8080:8080 geonode/geoserve
```

* 用户名密码
Username: admin
Password: geoserver
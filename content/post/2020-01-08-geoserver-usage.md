---
layout: post
title: "geoserver基本使用方法介绍"
date: 2020-01-08 11:44:00
categories: [map]
tags: [tools]
excerpt_separator: <!--more-->
---
geoserver基本介绍
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 使用流程](#2-使用流程)

<!-- /code_chunk_output -->


## 1. 概述

geoserver是 OpenGIS Web 服务器规范的 J2EE 实现，利用 GeoServer 可以方便的发布地图数据，允许用户对特征数据进行更新、删除、插入操作，通过 GeoServer 可以比较容易的在用户之间迅速共享空间地理信息。

geoserver启动方法参照
https://www.kaisawind.com/2020/01/08/2020-01-08-geoserver/

## 2. 使用流程

* 1. 创建单独的工作区
![pic](/images/geoserver_web_workspaces.png)

* 2. 导入数据或者创建数据
根据数据源的类型进行数据导入或者创建
![pic](/images/geoserver_web_NewDataPage.png)
![pic](/images/geoserver_web_StorePage.png)

* 3. 发布地图数据
导入数据时,点击发布按钮,会跳转图层创建页面
添加图层名和标题名
![pic](/images/geoserver_web_layout.png)

* 4. 地图瓦片缓存
图层创建成功后,可以在`Tile Cache`的`Tile Layers`配置瓦片数据缓存.
可以在`Tile Layers`的`Preview`进行地图展示.
![pic](/images/geoserver_web_CachedLayersPage.png)

* 5. 地图显示
![pic](/images/geoserver_gwc_map.png)
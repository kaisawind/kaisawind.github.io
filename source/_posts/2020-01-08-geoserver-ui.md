---
layout: post
title: "geoserver基本UI界面介绍"
date: 2020-01-08 11:25:00
categories: [map]
tags: [linux,map,docker]
excerpt_separator: <!--more-->
---
geoserver基本介绍
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. geoserver界面](#2-geoserver界面)
- [3. 界面介绍](#3-界面介绍)

<!-- /code_chunk_output -->


## 1. 概述

geoserver是 OpenGIS Web 服务器规范的 J2EE 实现，利用 GeoServer 可以方便的发布地图数据，允许用户对特征数据进行更新、删除、插入操作，通过 GeoServer 可以比较容易的在用户之间迅速共享空间地理信息。

geoserver启动方法参照
https://www.kaisawind.com/2020/01/08/2020-01-08-geoserver/

## 2. geoserver界面

![pic](/images/geoserver_web.png)

## 3. 界面介绍

* 关于和状态
geoserver和其中各种插件的版本
![pic](/images/geoserver_web_about.png)

* 数据
最重要的配置项,地图数据存储和配置位置
    * Layer Preview
    * Import DataImport Data
    * 工作区工作区
    * 数据存储数据存储
    * 图层图层
    * 图层组图层组
    * StylesStyles
    * Backup & RestoreBackup & Restore

* 服务
geoserver支持的各种服务的默认配置
    * WMTS
    * WCSWCS
    * WFSWFS
    * WMSWMS
    * WPSWPS

* 设置
geoserver的全局设置

* TileCaching
瓦片数据相关的配置

* Security
安全配置,包括用户名,角色,密码修改等

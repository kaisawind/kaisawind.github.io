---
layout: post
title: "geoserver多级别显示解决方法"
date: 2020-01-08 12:09:00
categories: [map]
tags: [linux,map,docker]
excerpt_separator: <!--more-->
---
geoserver多级别显示解决方法
<!--more-->

## 1. 概述

geoserver是 OpenGIS Web 服务器规范的 J2EE 实现，利用 GeoServer 可以方便的发布地图数据，允许用户对特征数据进行更新、删除、插入操作，通过 GeoServer 可以比较容易的在用户之间迅速共享空间地理信息。

geoserver启动方法参照
https://www.kaisawind.com/2020/01/08/2020-01-08-geoserver/

## 2. 图层组

geoserver的图层只能显示单级别的地图.
图层组的本意是多个图层同时叠加.比如街道名称叠加基本影像图层.

## 3. 解决思路

创建图层时,为图层固定zoom.
例如:L16的图层
![pic](/images/geoserver_web_layout16.png)

然后创建图层组,将所有固定级别的图层都添加进去.
![pic](/images/geoserver_web_layout_group.png)

## 4. 效果展示

<video class="video-player-thumbnail-image" loop="" playsinline="" autoplay=""><source src="https://cdn.loom.com/sessions/thumbnails/4775ce50e0e940e494abab32102e5b8d-00001.mp4" type="video/mp4"></video>
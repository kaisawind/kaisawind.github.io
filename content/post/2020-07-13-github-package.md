---
layout: post
title:  "github docker packages使用"
date: 2020-07-13 11:35:42
categories: [git]
tags: [git]
excerpt_separator: <!--more-->
---
github docker packages使用
<!--more-->

## 1. 概述
github推出了packages管理，到目前为止包含以下几种：
docker,Maven,NuGet,npm,RubyGems

## 2. 包管理

### 2.1 申请私有权限(token)

https://github.com/settings/tokens

* [ ] delete:packages
* [ ] read:packages
* [ ] write:packages
* [ ] repo

注意 repo权限只有是私有项目时才需要

### 2.2 登录docker

其中.github是写有申请token的文件
```bash
cat ~/.github | docker login docker.pkg.github.com -u kaisawind --password-stdin
```

### 2.3 tag镜像

对镜像的命名有严格的要求
```bash
docker tag IMAGE_ID docker.pkg.github.com/{username}/{repository-name}/IMAGE_NAME:VERSION
```

### 2.4 push镜像
```bash
docker push docker.pkg.github.com/{username}/{repository-name}/IMAGE_NAME:VERSION
```

## 3. 其他

在首页包列表中能找到docker镜像
![](/images/top-packages.png)

发布页面中能够找到docker镜像
![](/images/release-image.png)

对docker镜像进行管理
![](/images/manager-image.png)

删除docker镜像比较深，比较难找
![](/images/delete-image.png)
---
layout: post
title:  "docker compose删除孤立的服务"
date: 2020-05-11 09:15:42
lastmod: 2026-03-19
categories: [docker,compose]
tags: [docker]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "docker compose删除孤立的服务"
---
docker compose删除孤立的服务
<!--more-->

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。


```bash
WARNING: Found orphan containers (xxxx) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
```

```bash
docker-compose -f xxxx.yaml -p xxxx up -d --remove-orphans
```

```bash
Removing orphan container "xxxx"
```
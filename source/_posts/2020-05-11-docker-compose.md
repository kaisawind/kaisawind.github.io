---
layout: post
title:  "docker compose删除孤立的服务"
date: 2020-05-11 09:15:42 +0800
categories: [docker,compose]
tags: [docker, linux]
excerpt_separator: <!--more-->
---
docker compose删除孤立的服务
<!--more-->

```bash
WARNING: Found orphan containers (xxxx) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
```

```bash
docker-compose -f xxxx.yaml -p xxxx up -d --remove-orphans
```

```bash
Removing orphan container "xxxx"
```
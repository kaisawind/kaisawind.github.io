---
layout: post
title:  "Docker容器日志清理"
date: 2023-07-25 14:33:46
lastmod: 2026-03-19
categories: [docker,linux]
tags: [docker]
excerpt_separator: <!--more-->
---
Docker容器日志清理
<!--more-->

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。


/etc/docker/daemon.json
```bash
{
  "log-opts": {"max-size": "500m", "max-file": "3"}
}
```
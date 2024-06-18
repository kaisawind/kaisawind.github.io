---
layout: post
title:  "Docker容器日志清理"
date: 2023-07-25 14:33:46
categories: [docker,linux]
tags: [docker]
excerpt_separator: <!--more-->
---
Docker容器日志清理
<!--more-->

/etc/docker/daemon.json
```bash
{
  "log-opts": {"max-size": "500m", "max-file": "3"}
}
```
---
layout: post
title:  "Docker registry清理"
date: 2023-02-15 16:46:46
lastmod: 2026-03-19
categories: [docker,registry]
tags: [docker]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "Docker registry清理"
---
Docker registry清理
<!--more-->

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。


v1和v2版本
```bash
bin/registry garbage-collect --delete-untagged /etc/docker/registry/config.yml
```

v3版本
```bash
bin/registry garbage-collect --delete-untagged /etc/distribution/config.yml
```
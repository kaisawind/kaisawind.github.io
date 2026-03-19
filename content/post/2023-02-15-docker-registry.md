---
layout: post
title:  "Docker registry清理"
date: 2023-02-15 16:46:46
lastmod: 2026-03-19
categories: [docker,registry]
tags: [docker]
excerpt_separator: <!--more-->
---
Docker registry清理
<!--more-->

v1和v2版本
```bash
bin/registry garbage-collect --delete-untagged /etc/docker/registry/config.yml
```

v3版本
```bash
bin/registry garbage-collect --delete-untagged /etc/distribution/config.yml
```
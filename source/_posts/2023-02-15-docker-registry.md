---
layout: post
title:  "Docker registry清理"
date: 2023-02-15 16:46:46
categories: [docker,registry]
excerpt_separator: <!--more-->
---
Docker registry清理
<!--more-->

```bash
bin/registry garbage-collect --delete-untagged /etc/docker/registry/config.yml
```
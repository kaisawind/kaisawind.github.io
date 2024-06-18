---
layout: post
title:  "Docker Stack删除无用的服务"
date: 2022-02-21 14:31:46
categories: [docker,swarm]
tags: [docker]
excerpt_separator: <!--more-->
---
Docker Stack删除无用的服务
<!--more-->

当某个服务从yaml文件中删除之后，更新stack时并不会删除无用的服务，需要加`--prune`参数进行删除

```bash
docker stack deploy -c docker-swarm-pubsub-mysql.yml iotx --prune
```
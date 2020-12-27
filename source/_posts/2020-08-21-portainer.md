---
layout: post
title:  "docker gui(portainer)"
date: 2020-08-21 13:24:42
categories: [docker]
tags: [docker, linux, arm]
excerpt_separator: <!--more-->
---
docker gui(portainer)
<!--more-->

官网安装链接:
https://www.portainer.io/installation/

安装方法:

```bash
docker volume create portainer_data
docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```
---
layout: post
title:  "Docker Swarm UI配置"
date: 2021-08-22 19:31:46
categories: [docker,swarm]
excerpt_separator: <!--more-->
---
Docker Swarm UI配置
<!--more-->

```bash
docker volume create portainer_data
docker service create \
  --name portainer \
  --publish 9000:9000 \
  --replicas=1 \
  --constraint 'node.role == manager' \
  --mount src=portainer_data,dst=/data \
  --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  portainer/portainer \
  -H unix:///var/run/docker.sock
```

服务列表:
![services.png](/images/深度截图_选择区域_20210822194356.png)

节点列表
![nodes.png](/images/深度截图_选择区域_20210822194346.png)
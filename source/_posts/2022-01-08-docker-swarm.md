---
layout: post
title:  "Docker Swarm Replicas模式下区分Task"
date: 2022-01-08 19:03:46
categories: [docker,docker]
excerpt_separator: <!--more-->
---
Docker Swarm Replicas模式下区分Task
<!--more-->

docker swarm 可以通过go模板配置服务参数，通过这些参数区分服务。

|变量|描述|示例|
|---|---|---|
|.Service.ID|服务ID|vy91rc6fk2xihy56hp9sweuzo|
|.Service.Name|服务名称|iotx_ui|
|.Service.Labels|服务标签| |
|.Node.ID|NodeID|q7t3ol2l5a14svirnw79v3kv1|
|.Node.Hostname|Node主机名|master|
|.Task.ID|任务ID|kjxgbg2ff9cb55y9ai90hdbgy|
|.Task.Name|任务名称|iotx_ui.1.kjxgbg2ff9cb55y9ai90hdbgy|
|.Task.Slot|任务插槽|1|

![](/images/Screenshot_20220108_190535.png)

![](/images/Screenshot_20220108_191235.png)
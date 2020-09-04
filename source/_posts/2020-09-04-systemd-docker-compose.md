---
layout: post
title:  "systemd配置docker-compose命令"
date: 2020-09-04 10:46:04 +0800
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
systemd配置docker-compose命令
<!--more-->

## 1. 概述
docker compose能够有效的管理容器之间的依赖启动关系，如果全部服务使用systemd进行管理会很麻烦。
所以使用docker compose管理服务，使用systemd管理docker compose就能有效解决这个问题

## 2. 配置

edgex.service文件位置`/lib/systemd/system/`

WorkingDirectory是compose文件所在的位置，包括`.env`，否则会报错找不到文件
`After=docker.service`compose依赖docker,所以必须在docker启动之后运行
`Type=oneshot`因为是一次性的指令，所以只需要运行一次
`RemainAfterExit=yes`退出之后仍然保留状态，而不会被认为失败
```conf
[Unit]
Description=edgex docker compose services
Documentation=https://github.com/kaisawind
After=docker.service
Wants=network-online.target
Requires=docker.socket

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/root/data/edgex/
ExecStart=/usr/bin/docker-compose -f /home/root/data/edgex/docker-compose.yml -p edgex up -d --remove-orphans
ExecStop=/usr/bin/docker-compose -f /home/root/data/edgex/docker-compose.yml -p edgex stop

[Install]
WantedBy=multi-user.target
```

`systemctl status edgex`输出结果
```bash
● edgex.service - edgex docker compose services
   Loaded: loaded (/lib/systemd/system/edgex.service; enabled; vendor preset: enabled)
   Active: active (exited) since Tue 2020-09-01 09:52:21 UTC; 2 days ago
     Docs: https://github.com/kaisawind
  Process: 7397 ExecStart=/usr/bin/docker-compose -f /home/root/data/edgex/docker-compose.yml -p edgex up -d --remove-orphans (code=exited, status=0/SUCCES>
 Main PID: 7397 (code=exited, status=0/SUCCESS)

Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-core-command is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-core-data is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-dga-go is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-app-service-pdiot is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-device-serial is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-app-service-configurable-rules is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-sys-mgmt-agent is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-alarm-go is up-to-date
Sep 01 09:52:18 okmx8mm docker-compose[7397]: edgex-kuiper is up-to-date
Sep 01 09:52:21 okmx8mm systemd[1]: Started edgex docker compose services.
```
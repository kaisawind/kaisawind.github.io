---
layout: post
title:  "systemd配置timer(定时)"
date: 2020-09-04 10:55:04
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
systemd配置timer命令
<!--more-->

## 1. 概述
systemd也支持定时处理timer,但必须跟已有的systemd服务关联

## 2. 配置

edgex.timer文件位置`/lib/systemd/system/`,同时目录中需要有`edgex.service`

配置的内容是，每天凌晨启动edgex.service
`Persistent=true`定时器到时没有启动，也会自动执行相应的单元

```conf
[Unit]
Description=edgex services up

[Timer]
#OnCalendar=*-*-* 00:00:00
OnCalendar=daily
Unit=edgex.service
Persistent=true

[Install]
WantedBy=timers.target
```

## 3. 查看命令

```bash
systemctl list-timers # 列出所有定时器
systemctl is-enabled edgex.timer # 查看定时器是否启用
systemctl is-active edgex.timer # 查看定时器是否激活
```


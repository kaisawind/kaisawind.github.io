---
layout: post
title:  "root用户登陆sshd失败"
date: 2022-02-23 10:42:16
categories: [linux]
tags: [linux， kernel]
excerpt_separator: <!--more-->
---
root用户登陆sshd失败
<!--more-->

修改sshd配置，允许root用户登陆
/etc/ssh/sshd_config
```bash
PermitRootLogin yes
```
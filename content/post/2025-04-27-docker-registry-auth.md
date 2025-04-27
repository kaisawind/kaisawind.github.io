---
layout: post
title:  "docker仓库添加认证"
date: 2025-04-27 16:49:54
categories: [linux,ubuntu,docker]
tags: [ubuntu, docker]
draft: false
excerpt_separator: <!--more-->
---
docker仓库添加认证
<!--more-->

命令
```bash
sudo apt-get install apache2-utils # htpasswd
mkdir auth
htpasswd -bcB auth/htpasswd pana pana@123.com # 为用户 pana 创建密码文件
```

htpasswd
* -B：使用 bcrypt 加密方式。
* -c：创建新的密码文件。
* -b: 在命令行中输入密码

启动registry, 注意仓库路径
```bash
docker run -d -p 5000:5000 --restart=always --name registry \
-v <仓库路径>:/var/lib/registry \
-v $PWD/auth:/auth \
-e "REGISTRY_AUTH=htpasswd" \
-e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
-e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
registry
```

所有用到仓库的服务器执行以下命令
```bash
docker login <ip>:5000 -u pana -p pana@123.com
```
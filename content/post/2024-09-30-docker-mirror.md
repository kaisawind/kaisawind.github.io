---
layout: post
title:  "ubuntu镜像源安装docker-ce"
date: 2024-09-30 16:41:54
categories: [linux,ubuntu,docker]
tags: [ubuntu, docker]
draft: false
excerpt_separator: <!--more-->
---
ubuntu镜像源安装docker-ce
<!--more-->

命令
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

安装docker-ce
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
---
layout: post
title:  "linux防火墙开放端口"
date: 2020-1-18 10:53:48
categories: [linux]
excerpt_separator: <!--more-->
---
linux防火墙开放端口
<!--more-->

## 1. 概述
linux防火墙默认是开启的，但是大部分情况下都会手动关闭。
使用云服务器，由于有外网IP,所以关闭防火墙相当不安全。(经历过几次端口探测，修改服务器配置的情况)

## 2. 防火墙命令

### 2.1. 查看防火墙是否开启

```bash
systemctl status firewalld
```

### 2.2. 开启防火墙

```bash
systemctl start firewalld
```

### 2.3. 常用命令

```bash
firewall-cmd --state                          ##查看防火墙状态，是否是running
firewall-cmd --reload                         ##重新载入配置，比如添加规则之后，需要执行此命令
firewall-cmd --get-zones                      ##列出支持的zone
firewall-cmd --get-services                   ##列出支持的服务，在列表中的服务是放行的
firewall-cmd --query-service ftp              ##查看ftp服务是否支持，返回yes或者no
firewall-cmd --add-service=ftp                ##临时开放ftp服务
firewall-cmd --add-service=ftp --permanent    ##永久开放ftp服务
firewall-cmd --remove-service=ftp --permanent ##永久移除ftp服务
firewall-cmd --add-port=80/tcp --permanent    ##永久添加80端口 
firewall-cmd --remove-port=80/tcp --permanent ##永久移除80端口 
firewall-cmd --zone=public --list-ports       ##查看已开放的端口
```

### 2.4. 开放关闭端口

```bash
firewall-cmd --zone=public --add-port=5672/tcp --permanent   # 开放5672端口
firewall-cmd --zone=public --remove-port=5672/tcp --permanent  #关闭5672端口
firewall-cmd --reload   # 配置立即生效
```

### 2.5. 查看防火墙生效规则

```bash
firewall-cmd --list-all
```
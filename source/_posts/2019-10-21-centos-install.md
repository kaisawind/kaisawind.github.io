---
layout: post
title:  "CentOS系统初期配置"
date: 2019-10-21 15:02:04 +0800
categories: [linux,centos]
tags: [linux, centos]
excerpt_separator: <!--more-->
---

## 1. 安装系统

U盘安装盘制作工具

https://github.com/FedoraQt/MediaWriter

## 2. `net-tools`

* 启用网卡

    ```shell
    cd /etc/sysconfig/network-scripts/ifcfg-enp1s0
    ```

    修改

    `ONBOOT=no` - `ONBOOT=yes`

* 安装网络工具包

    ```shell
    sudo yum install net-tools
    ```

* 查看IP地址，远程shell连接

    ```shell
    ifconfig -a
    ```

## 3. `wget`

```shell
sudo yum install wget
```

## 4. 切换阿里云镜像

https://www.kaisawind.com/2019/02/21/2019-02-22-linux/

```shell
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

## 5. 更新软件

```shell
sudo yum update
```
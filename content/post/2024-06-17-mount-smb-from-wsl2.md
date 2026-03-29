---
layout: post
title:  "Mount Windows Network Drives in WSL"
date: 2024-06-17 23:22:42
lastmod: 2026-03-19
categories: [windows,wsl]
tags: [windows]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "在WSL2中挂载网络盘"
---
在WSL2中挂载网络盘
<!--more-->

## 基本用法

```bash
# 创建挂载点
mkdir /mnt/m

# 挂载Windows网络驱动器
sudo mount -t drvfs M: /mnt/m
```

## 挂载本地驱动器

```bash
# 挂载C盘
sudo mkdir -p /mnt/c
sudo mount -t drvfs C: /mnt/c

# 挂载D盘
sudo mkdir -p /mnt/d
sudo mount -t drvfs D: /mnt/d
```

## 挂载网络共享

### 方法1：先在Windows中映射网络驱动器

1. Windows资源管理器 -> 此电脑 -> 映射网络驱动器
2. 映射网络路径到盘符（如 Z:）
3. 在WSL中挂载：
   ```bash
   sudo mkdir -p /mnt/z
   sudo mount -t drvfs Z: /mnt/z
   ```

### 方法2：使用CIFS直接挂载

```bash
# 安装CIFS工具
sudo apt update
sudo apt install cifs-utils

# 创建挂载点
sudo mkdir -p /mnt/share

# 挂载网络共享
sudo mount -t cifs //server/share /mnt/share -o username=user,password=pass,uid=1000,gid=1000

# 或使用credentials文件
echo "username=user" > ~/.smbcreds
echo "password=pass" >> ~/.smbcreds
chmod 600 ~/.smbcreds
sudo mount -t cifs //server/share /mnt/share -o credentials=/home/user/.smbcreds,uid=1000,gid=1000
```

## 开机自动挂载

编辑 `/etc/fstab`：

```bash
# Windows本地驱动器
C: /mnt/c drvfs defaults 0 0

# 网络共享（使用CIFS）
//server/share /mnt/share cifs credentials=/home/user/.smbcreds,uid=1000,gid=1000 0 0
```

## 常用操作

```bash
# 查看已挂载的驱动器
mount | grep drvfs

# 卸载驱动器
sudo umount /mnt/m

# 强制卸载
sudo umount -l /mnt/m
```

## 权限问题

```bash
# 设置挂载选项（解决权限问题）
sudo mount -t drvfs C: /mnt/c -o metadata,uid=1000,gid=1000,umask=22,fmask=11

# metadata: 启用Linux权限支持
# uid/gid: 设置所有者
# umask/fmask: 设置权限掩码
```

## 最佳实践

1. **使用metadata选项**：正确处理Linux文件权限
2. **设置正确的uid/gid**：避免权限问题
3. **使用credentials文件**：安全存储密码
4. **软链接方便访问**：`ln -s /mnt/c ~/windows`
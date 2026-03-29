---
layout: post
title:  "扩展 Ubuntu Root 分区"
date: 2023-05-31 20:05:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more>-->
---
扩展 Ubuntu Root 分区是云服务器和虚拟机管理的常见需求。本文介绍如何在在线状态下扩展 root 分区。
<!--more-->

> **提示**: Linux 发行版更新较快，命令可能因版本不同而有差异。操作前务必备份数据。

## 前提条件

- 磁盘空间已在虚拟化平台扩容（如 AWS、Azure、VMware 等）
- 使用 cloud-growpart 或 growpart 工具
- 根分区使用 LVM 或标准分区

## 快速扩展

### 方法一：使用 growpart（推荐）

适用于使用 growpart 工具的云服务器：

```bash
# 扩展分区表
growpart /dev/vda 2

# 扩展文件系统
resize2fs /dev/vda2
```

### 方法二：使用 LVM

如果使用 LVM，流程如下：

```bash
# 扫描新磁盘空间
pvresize /dev/vda2

# 扩展逻辑卷
lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv

# 扩展文件系统
resize2fs /dev/ubuntu-vg/ubuntu-lv
```

## 详细步骤

### 1. 检查当前磁盘状态

```bash
# 查看磁盘分区
lsblk

# 查看文件系统信息
df -h

# 查看块设备信息
blkid
```

### 2. 扩展分区表

```bash
# 扩展指定分区
growpart /dev/vda 2

# 如果失败，尝试使用 parted
parted /dev/vda print
parted /dev/vda resizepart 2 100%
```

### 3. 扩展文件系统

```bash
# 对于 ext2/ext3/ext4 文件系统
resize2fs /dev/vda2

# 对于 XFS 文件系统
xfs_growfs /

# 对于 Btrfs 文件系统
btrfs filesystem resize max /
```

## 常见场景

### 场景一：扩展云服务器磁盘

```bash
# 扫描新磁盘
echo 1 > /sys/class/scsi_host/host0/scan

# 扩展分区
growpart /dev/sda 1

# 扩展文件系统
resize2fs /dev/sda1
```

### 场景二：扩容 LVM 逻辑卷

```bash
# 创建物理卷
pvcreate /dev/sdb

# 扩展卷组
vgextend ubuntu-vg /dev/sdb

# 扩展逻辑卷
lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv

# 扩展文件系统
resize2fs /dev/ubuntu-vg/ubuntu-lv
```

## 验证扩展结果

```bash
# 查看磁盘空间
df -h

# 查看分区大小
lsblk

# 查看文件系统信息
dumpe2fs -h /dev/vda2 | grep "Block count"
```

## 注意事项

1. **数据备份**：扩展分区前务必备份重要数据
2. **在线扩展**：大多数情况可以在线扩展，无需重启
3. **文件系统类型**：不同文件系统扩展命令不同
4. **快照备份**：在云平台上创建快照后再操作
5. **权限检查**：确保有 root 权限执行命令
6. **空间确认**：确认虚拟化平台已扩容磁盘空间

## 故障排除

### growpart 命令未找到

```bash
# 安装 cloud-guest-utils
apt update
apt install cloud-guest-utils -y
```

### 分区表锁定

```bash
# 检查是否有进程占用磁盘
lsof /dev/vda

# 停止相关服务
systemctl stop [service_name]
```

### 文件系统检查

```bash
# 强制检查文件系统
fsck -f /dev/vda2

# 扩展前检查
e2fsck -f /dev/vda2
```
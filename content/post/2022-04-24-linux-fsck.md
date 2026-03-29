---
layout: post
title:  "linux can't read superblock on"
date: 2022-04-22 10:02:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "意外停电后，重启系统，不能自动挂载"
---
意外停电后，重启系统，不能自动挂载
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。

## 问题背景

意外断电后，文件系统可能出现损坏，导致无法正常挂载。这时需要使用fsck工具修复。

## fsck基本用法

### 检查并修复文件系统

```bash
# 基本语法
sudo fsck /dev/xxxxx

# 示例
sudo fsck /dev/sdb1
```

### 交互模式

```bash
sudo fsck /dev/sdb1

fsck from util-linux 2.34
e2fsck 1.45.5 (07-Jan-2020)
/dev/sdb1 contains a file system with errors, check forced.
Pass 1: Checking inodes, blocks, and sizes
Inode 525737 seems to contain garbage.  Clear? 
```

常用选项：
- `yes` 或 `y`：清除/修复
- `no` 或 `n`：跳过
- `a`：自动修复所有问题

## 常用参数

```bash
# 自动修复（对所有问题回答yes）
sudo fsck -y /dev/sdb1

# 检查指定文件系统类型
sudo fsck -t ext4 /dev/sdb1

# 强制检查
sudo fsck -f /dev/sdb1

# 显示进度
sudo fsck -C /dev/sdb1
```

## 修复步骤

### 1. 卸载文件系统

```bash
# 卸载
sudo umount /dev/sdb1

# 如果无法卸载，查找占用进程
lsof /dev/sdb1
# 或
fuser -v /dev/sdb1
```

### 2. 运行fsck

```bash
# 自动修复
sudo fsck -y /dev/sdb1
```

### 3. 重新挂载

```bash
# 挂载
sudo mount /dev/sdb1 /mnt/data
```

## 常见错误及解决

### superblock损坏

```bash
# 查找备用superblock
sudo mke2fs -n /dev/sdb1

# 使用备用superblock修复
sudo fsck -b 32768 /dev/sdb1
```

### Inode错误

```bash
# 清除损坏的inode
sudo fsck -y /dev/sdb1
# 输出: Inode 525737 seems to contain garbage.  Clear? yes
```

### 根分区损坏

```bash
# 需要进入救援模式或Live CD
# 在启动时按住Shift键进入GRUB菜单
# 选择recovery mode
# 或使用Live CD启动
```

## 检查所有文件系统

```bash
# 检查fstab中所有文件系统
sudo fsck -A

# 只检查需要检查的文件系统
sudo fsck -R -A
```

## 开机自动检查

在`/etc/fstab`中设置：

```bash
# <device> <mount> <type> <options> <dump> <pass>
/dev/sdb1   /data    ext4   defaults   0      2
#                                    dump   pass
# pass=0: 不检查
# pass=1: 根分区
# pass=2: 其他分区
```

## 最佳实践

1. **定期检查**：定期运行fsck检查文件系统健康
2. **安全关机**：避免强制断电
3. **UPS电源**：重要服务器配备UPS
4. **备份重要数据**：修复前先备份数据
5. **使用日志文件系统**：优先使用ext4、xfs等有日志的文件系统
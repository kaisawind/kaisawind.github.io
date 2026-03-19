---
layout: post
title: "virtualbox虚拟机共享文件夹权限"
date: 2020-01-02 10:18:00
lastmod: 2026-03-19
categories: [虚拟化,virtualbox]
tags: [linux]
excerpt_separator: <!--more-->
---
virtualbox虚拟机共享文件夹权限

virtualbox共享文件夹之后,本地用户无法访问,所以需要添加当前用户到vboxsf
<!--more-->

## 问题现象

VirtualBox虚拟机共享文件夹后，访问时提示权限不足：

```bash
ls /media/sf_shared
ls: cannot access '/media/sf_shared': Permission denied
```

## 解决方法

### 方法1：添加用户到vboxsf组（推荐）

```bash
# 添加当前用户到vboxsf组
sudo usermod -aG vboxsf $(whoami)

# 注销并重新登录使更改生效
logout
# 或重启虚拟机
sudo reboot
```

### 方法2：修改文件夹权限（不推荐）

```bash
# 修改共享文件夹权限
sudo chmod 777 /media/sf_shared
```

> **警告**: chmod 777会降低安全性，不推荐在生产环境使用。

### 方法3：使用sudo访问

```bash
# 使用sudo访问共享文件夹
sudo ls /media/sf_shared

# 使用sudo编辑文件
sudo vi /media/sf_shared/file.txt
```

## 自动挂载配置

### 配置自动挂载

1. 关闭虚拟机
2. 在VirtualBox管理器中选择虚拟机
3. 设置 -> 共享文件夹
4. 添加共享文件夹：
   - 共享文件夹路径：宿主机路径
   - 共享文件夹名称：shared
   - 勾选"自动挂载"
   - 挂载点：/media/sf_shared

### 手动挂载

```bash
# 创建挂载点
sudo mkdir -p /mnt/shared

# 手动挂载
sudo mount -t vboxsf shared /mnt/shared

# 开机自动挂载（编辑/etc/fstab）
echo "shared /mnt/shared vboxsf defaults 0 0" | sudo tee -a /etc/fstab
```

## 验证配置

```bash
# 查看用户组
groups $(whoami)

# 检查vboxsf组
grep vboxsf /etc/group

# 测试访问
ls -la /media/sf_shared
```

## 常见问题

### Q: 添加用户组后仍无法访问？

重新登录或重启虚拟机使更改生效。

### Q: 共享文件夹不显示？

检查VirtualBox增强功能是否安装：

```bash
lsmod | grep vbox
# 或
ls /opt/VBoxGuestAdditions-*/
```

如果没有安装，需要先安装增强功能：

1. 虚拟机菜单 -> 设备 -> 安装增强功能
2. 在虚拟机中运行安装程序

### Q: 如何查看共享文件夹列表？

```bash
# 方法1
mount | grep vboxsf

# 方法2
df -h | grep vboxsf

# 方法3（在VirtualBox中）
VBoxManage showvminfo "VM_NAME" | grep "Shared folders"
```

## 最佳实践

1. **使用vboxsf组**：将用户添加到vboxsf组而不是修改权限
2. **自动挂载**：配置自动挂载避免手动操作
3. **符号链接**：在用户目录创建符号链接方便访问
   ```bash
   ln -s /media/sf_shared ~/shared
   ```
4. **增强功能**：确保VirtualBox增强功能已安装
5. **文件权限**：注意宿主机和虚拟机的文件权限差异
---
layout: post
title:  "python中的pip镜像源设置"
date: 2024-09-30 16:44:54
lastmod: 2026-03-19
categories: [linux,ubuntu,python]
tags: [ubuntu,python]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "python中的pip镜像源设置"
---
python中的pip镜像源设置
<!--more-->

> **提示**: Python 3.12已发布，建议使用Python 3.8+版本。

## 快速配置

```bash
# 使用清华镜像
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# 或使用阿里云镜像
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

## 常用镜像源

| 镜像源 | URL |
|--------|-----|
| 清华 | https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple |
| 阿里云 | https://mirrors.aliyun.com/pypi/simple/ |
| 中科大 | https://pypi.mirrors.ustc.edu.cn/simple/ |
| 豆瓣 | https://pypi.douban.com/simple/ |
| 华为云 | https://mirrors.huaweicloud.com/repository/pypi/simple |

## 配置方式

### 方法1：命令行配置

```bash
# 设置全局镜像源
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# 设置信任主机
pip config set install.trusted-host mirrors.tuna.tsinghua.edu.cn
```

### 方法2：配置文件

创建或编辑 `~/.pip/pip.conf`（Linux/macOS）或 `%APPDATA%\pip\pip.ini`（Windows）：

```ini
[global]
index-url = https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
trusted-host = mirrors.tuna.tsinghua.edu.cn

[install]
trusted-host = mirrors.tuna.tsinghua.edu.cn
```

### 方法3：临时使用

```bash
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple package-name
```

## 验证配置

```bash
# 查看当前配置
pip config list

# 查看镜像源
pip config get global.index-url

# 测试下载速度
pip install --dry-run numpy
```

## 常用命令

```bash
# 升级pip
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple --upgrade pip

# 安装包
pip install package-name

# 安装指定版本
pip install package-name==1.0.0

# 查看已安装的包
pip list

# 导出依赖
pip freeze > requirements.txt

# 安装依赖
pip install -r requirements.txt
```

## 最佳实践

1. **使用配置文件**：优先使用配置文件而不是每次指定镜像
2. **设置信任主机**：避免HTTPS警告
3. **定期更新pip**：`pip install --upgrade pip`
4. **使用虚拟环境**：建议使用venv或conda管理环境
5. **锁定版本**：生产环境使用requirements.txt锁定版本
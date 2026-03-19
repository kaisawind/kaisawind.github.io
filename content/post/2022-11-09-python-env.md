---
layout: post
title:  "ModuleNotFoundError: No module named 'distutils.cmd'"
date: 2022-11-09 14:08:54
lastmod: 2026-03-19
categories: [编程语言,python]
tags: [python]
excerpt_separator: <!--more-->
---
ModuleNotFoundError: No module named 'distutils.cmd'
<!--more-->

> **提示**: Python 3.12已发布，建议使用Python 3.8+版本。

## 问题背景

virtualenv 安装非host版本的python环境时，找不到包distutils。

## 解决方法

### 方法1：安装distutils包

```bash
# Ubuntu/Debian
sudo apt-get install python3.8-distutils
# 或
sudo apt-get install python3.9-distutils
sudo apt-get install python3.10-distutils

# CentOS/RHEL
sudo yum install python38-distutils
```

### 方法2：使用ensurepip

```bash
# Python 3.6+自带ensurepip
python3 -m ensurepip --upgrade

# 或
python3 -m pip install --upgrade pip
```

### 方法3：手动安装setuptools

```bash
# 下载get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# 使用指定Python版本安装
python3.8 get-pip.py
```

## 完整示例

```bash
# 1. 安装Python 3.8
sudo apt update
sudo apt install python3.8 python3.8-venv python3.8-dev

# 2. 安装distutils
sudo apt install python3.8-distutils

# 3. 创建虚拟环境
python3.8 -m venv myenv

# 4. 激活虚拟环境
source myenv/bin/activate

# 5. 安装依赖
pip install -r requirements.txt
```

## Python 3.12+ 注意事项

Python 3.12移除了distutils，需要使用setuptools：

```bash
# 安装setuptools
pip install setuptools

# 或在requirements.txt中添加
setuptools>=65.0.0
```

## 使用pyenv管理多版本

```bash
# 安装pyenv
curl https://pyenv.run | bash

# 安装Python版本
pyenv install 3.8.18
pyenv install 3.10.13

# 设置全局版本
pyenv global 3.10.13

# 创建虚拟环境
pyenv virtualenv 3.8.18 myenv38
pyenv activate myenv38
```

## 最佳实践

1. **使用venv**：Python 3.3+推荐使用venv而不是virtualenv
2. **明确Python版本**：在项目中指定Python版本要求
3. **使用requirements.txt**：明确依赖和版本
4. **Docker环境**：使用Docker确保环境一致性
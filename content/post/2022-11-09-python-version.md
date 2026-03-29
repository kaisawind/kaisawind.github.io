---
layout: post
title:  "ubuntu安装不同版本python"
date: 2022-11-09 14:08:54
lastmod: 2026-03-19
categories: [编程语言,python]
tags: [python]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "ubuntu安装不同版本python"
---
ubuntu安装不同版本python
<!--more-->

在 Ubuntu 系统中，不同项目可能需要不同版本的 Python。默认情况下，Ubuntu 只安装了系统版本的 Python（如 Python 3.10）。本文介绍多种在 Ubuntu 上安装和管理多个 Python 版本的方法。

> **提示**: Python 3.12已发布，建议使用Python 3.8+版本。

## Python 版本管理概述

### 为什么需要多个 Python 版本

- 不同项目依赖不同的 Python 版本
- 测试代码在不同 Python 版本下的兼容性
- 某些库只支持特定 Python 版本
- 开发和生产环境使用不同版本

### 版本管理工具对比

| 工具 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| PPA | 简单直接 | 版本有限 | 常用版本 |
| deadsnakes PPA | 版本丰富 | 需要手动配置 | 多版本共存 |
| pyenv | 完全隔离 | 编译较慢 | 开发环境 |
| conda | 包管理一体 | 体积较大 | 数据科学 |
| docker | 完全隔离 | 资源消耗大 | CI/CD |

## 方法一：使用 PPA（推荐）

### 安装 deadsnakes PPA

```bash
# 1. 安装必要的工具
sudo apt-get update
sudo apt-get install -y software-properties-common

# 2. 添加 deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update

# 3. 安装特定版本的 Python
sudo apt install python3.8

# 4. 验证安装
python3.8 --version
```

### 安装多个版本

```bash
# 安装多个 Python 版本
sudo apt install python3.8 python3.9 python3.10 python3.11

# 查看已安装的版本
ls -la /usr/bin/python3.*

# 输出示例:
# /usr/bin/python3.8
# /usr/bin/python3.9
# /usr/bin/python3.10
# /usr/bin/python3.11
```

### 安装配套工具

```bash
# 为 Python 3.8 安装 pip
sudo apt install python3.8-distutils
curl https://bootstrap.pypa.io/get-pip.py | sudo python3.8

# 为 Python 3.9 安装 pip
sudo apt install python3.9-distutils
curl https://bootstrap.pypa.io/get-pip.py | sudo python3.9

# 安装 venv 模块
sudo apt install python3.8-venv
sudo apt install python3.9-venv

# 验证
python3.8 -m pip --version
python3.8 -m venv --help
```

## 方法二：使用 pyenv（推荐开发环境）

### 安装 pyenv

```bash
# 1. 安装依赖
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
    liblzma-dev python-openssl git

# 2. 使用 curl 安装
curl https://pyenv.run | bash

# 或使用 git 克隆
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# 3. 配置环境变量
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# 4. 重新加载配置
source ~/.bashrc

# 5. 验证安装
pyenv --version
```

### 使用 pyenv 安装 Python

```bash
# 查看可用的 Python 版本
pyenv install --list | grep "  3\."

# 安装特定版本
pyenv install 3.8.18
pyenv install 3.9.18
pyenv install 3.10.13
pyenv install 3.11.6
pyenv install 3.12.0

# 查看已安装的版本
pyenv versions

# 设置全局默认版本
pyenv global 3.11.6

# 设置当前目录的版本
cd /path/to/project
pyenv local 3.10.13

# 验证
python --version
```

### pyenv 高级用法

```bash
# 查看当前设置的版本
pyenv version

# 列出所有可安装的版本
pyenv install --list

# 卸载版本
pyenv uninstall 3.8.18

# 更新 pyenv
cd ~/.pyenv && git pull

# 查看版本历史
pyenv history
```

### pyenv 插件

```bash
# 安装 pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# 创建虚拟环境
pyenv virtualenv 3.11.6 myproject-venv

# 激活虚拟环境
pyenv activate myproject-venv

# 退出虚拟环境
pyenv deactivate

# 列出所有虚拟环境
pyenv virtualenvs

# 删除虚拟环境
pyenv uninstall myproject-venv
```

## 方法三：使用 conda（推荐数据科学）

### 安装 Miniconda

```bash
# 1. 下载 Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 2. 安装
bash Miniconda3-latest-Linux-x86_64.sh

# 3. 重新加载配置
source ~/.bashrc

# 4. 验证安装
conda --version
```

### 使用 conda 管理 Python 版本

```bash
# 创建 Python 3.8 环境
conda create -n py38 python=3.8

# 创建 Python 3.10 环境
conda create -n py310 python=3.10

# 激活环境
conda activate py38

# 查看环境
conda env list

# 删除环境
conda remove -n py38 --all

# 安装包
conda install numpy pandas matplotlib

# 从 requirements.txt 安装
conda install --file requirements.txt
```

### conda 配置

```bash
# 添加清华镜像源（加速下载）
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

# 显示安装来源
conda config --set show_channel_urls yes

# 自动确认安装
conda config --set always_yes yes

# 更新 conda
conda update conda
```

## 方法四：使用 Docker（推荐生产环境）

### Docker 安装 Python

```dockerfile
# Dockerfile - Python 3.8
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### 使用不同 Python 版本

```bash
# 运行 Python 3.8 容器
docker run -it --rm python:3.8 python --version

# 运行 Python 3.10 容器
docker run -it --rm python:3.10 python --version

# 挂载本地目录
docker run -it --rm -v $(pwd):/app python:3.8 bash

# 在容器中运行脚本
docker run -it --rm -v $(pwd):/app python:3.8 python /app/script.py
```

### Docker Compose 多版本

```yaml
# docker-compose.yml
version: '3.8'

services:
  app38:
    image: python:3.8
    working_dir: /app
    volumes:
      - ./app:/app
    command: python main.py

  app310:
    image: python:3.10
    working_dir: /app
    volumes:
      - ./app:/app
    command: python main.py
```

## 实际应用场景

### 场景一：开发环境使用 pyenv

```bash
# 项目 A 需要 Python 3.8
cd ~/projects/project-a
pyenv local 3.8.18
python --version  # Python 3.8.18

# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 场景二：数据科学使用 conda

```bash
# 创建数据科学环境
conda create -n datascience python=3.10

conda activate datascience

# 安装科学计算包
conda install numpy pandas matplotlib scipy scikit-learn

# 安装 Jupyter
conda install jupyterlab

# 启动 Jupyter
jupyter lab
```

### 场景三：生产环境使用 Docker

```bash
# 构建 Docker 镜像
docker build -t myapp:3.8 .

# 运行容器
docker run -d -p 8000:8000 --name myapp myapp:3.8

# 查看日志
docker logs -f myapp
```

### 场景四：CI/CD 使用多版本测试

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest tests/
```

## 常见问题和解决方案

### 1. pip 安装失败

**问题**: 新安装的 Python 无法使用 pip

**解决方案**:

```bash
# 安装 distutils
sudo apt install python3.x-distutils

# 使用 get-pip.py 安装 pip
curl https://bootstrap.pypa.io/get-pip.py | python3.x

# 或使用 ensurepip
python3.x -m ensurepip --upgrade
```

### 2. 编译 pyenv 时出错

**问题**: pyenv install 编译失败

**解决方案**:

```bash
# 安装完整的编译依赖
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
    liblzma-dev python-openssl git

# 清理之前的构建
rm -rf ~/.pyenv/versions/3.x.x

# 重新安装
CFLAGS="-I/usr/include/openssl" LDFLAGS="-L/usr/lib" pyenv install 3.x.x
```

### 3. SSL 证书错误

**问题**: pip install 时出现 SSL 错误

**解决方案**:

```bash
# 安装 ca-certificates
sudo apt-get install ca-certificates

# 更新证书
sudo update-ca-certificates

# 或使用 --trusted-host 参数（不推荐）
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package_name
```

### 4. 版本切换不生效

**问题**: python --version 仍然是旧版本

**解决方案**:

```bash
# 对于 pyenv
pyenv global 3.10.13
source ~/.bashrc

# 对于 PPA 安装的版本
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2

# 手动切换
sudo update-alternatives --config python3
```

### 5. 虚拟环境问题

**问题**: venv 创建失败或无法激活

**解决方案**:

```bash
# 确保 venv 模块已安装
sudo apt install python3.x-venv

# 创建虚拟环境
python3.x -m venv myenv

# 激活虚拟环境
source myenv/bin/activate

# 退出虚拟环境
deactivate
```

## 脚本自动化

### 多版本 Python 安装脚本

```bash
#!/bin/bash
# install_python_versions.sh

set -e

PYTHON_VERSIONS=("3.8.18" "3.9.18" "3.10.13" "3.11.6" "3.12.0")

echo "开始安装多个 Python 版本..."

# 安装依赖
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
    liblzma-dev python-openssl git

# 安装 pyenv
if ! command -v pyenv &> /dev/null; then
    echo "安装 pyenv..."
    curl https://pyenv.run | bash
    
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    
    source ~/.bashrc
fi

# 安装 Python 版本
for version in "${PYTHON_VERSIONS[@]}"; do
    if ! pyenv versions | grep -q "$version"; then
        echo "安装 Python $version..."
        pyenv install "$version"
    else
        echo "Python $version 已安装"
    fi
done

# 设置默认版本
pyenv global "${PYTHON_VERSIONS[-1]}"

echo "所有 Python 版本安装完成！"
pyenv versions
```

### 项目环境设置脚本

```bash
#!/bin/bash
# setup_project_env.sh

PROJECT_NAME=$1
PYTHON_VERSION=${2:-3.10.13}

if [ -z "$PROJECT_NAME" ]; then
    echo "用法: $0 <项目名称> [Python版本]"
    exit 1
fi

echo "为项目 $PROJECT_NAME 设置 Python $PYTHON_VERSION 环境..."

# 使用 pyenv 创建虚拟环境
pyenv local "$PYTHON_VERSION"
python -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 升级 pip
pip install --upgrade pip

# 安装常用工具
pip install pip-tools black isort flake8 mypy pytest

# 创建 requirements 文件
touch requirements.txt
touch dev-requirements.txt

echo "环境设置完成！"
echo "激活环境: source venv/bin/activate"
```

## 最佳实践

1. **版本选择**:
   - 生产环境使用最新的稳定版本
   - 避免使用即将 EOL 的版本
   - 关注每个版本的发布周期

2. **环境隔离**:
   - 每个项目使用独立的虚拟环境
   - 不要混用不同项目的依赖
   - 定期清理不需要的虚拟环境

3. **依赖管理**:
   - 使用 requirements.txt 或 pyproject.toml
   - 锁定依赖版本
   - 定期更新依赖包

4. **开发工作流**:
   - 使用 .python-version 文件（pyenv）
   - 配置 CI/CD 测试多个版本
   - 文档化项目依赖

5. **安全性**:
   - 定期更新 Python 版本
   - 及时更新依赖包
   - 使用 pip audit 检查漏洞

## 相关资源

- Python 官方网站: https://www.python.org/
- pyenv GitHub: https://github.com/pyenv/pyenv
- deadsnakes PPA: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
- conda 文档: https://docs.conda.io/
- Docker Hub Python: https://hub.docker.com/_/python

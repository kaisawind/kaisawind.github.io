---
layout: post
title:  "Nvidia Docker安装"
date: 2019-04-24 16:57:44
lastmod: 2026-03-19
categories: [docker]
tags: [docker]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "nvidia-docker是能够直接在容器中使用Nvidia GPU而不需要额外的其他处理。结合k8s的插件k8s-device-plugin能够在k8s集群中使用GPU。"
---

nvidia-docker是能够直接在容器中使用Nvidia GPU而不需要额外的其他处理。结合k8s的插件`k8s-device-plugin`能够在k8s集群中使用GPU。

> **重要更新**: nvidia-docker已废弃，现在推荐使用 **NVIDIA Container Toolkit**。本文档保留作为历史参考。最新安装方法请参考：https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html
<!--more-->

> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [Nvidia Docker安装](#nvidia-docker安装)
	* [1 安装Nvidia驱动](#1-安装nvidia驱动)
		* [1.1 Cudn](#11-cudn)
		* [1.2 Cudnn](#12-cudnn)
	* [2. 安装Nvidia Docker](#2-安装nvidia-docker)
		* [配置nvidia docker仓库](#配置nvidia-docker仓库)
		* [安装nvidia docker](#安装nvidia-docker)
		* [配置docker默认runtime](#配置docker默认runtime)

<!-- /code_chunk_output -->

## 1 安装Nvidia驱动

### 1.1 Cudn

通常情况下cudn中已经包含了driver。

* 下载路径

    [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)

* 安装下载的文件

    例如： cuda_10.1.105_418.39_linux.run

    ```bash
    sudo sh cuda_10.1.105_418.39_linux.run
    ```

    根据提示进行

### 1.2 Cudnn

注意：cudnn需要注册nvidia账号

[https://developer.nvidia.com/rdp/cudnn-download](https://developer.nvidia.com/rdp/cudnn-download)

下载安装时注意Cudn的版本

## 2. 安装NVIDIA Container Toolkit（新方法）

### 2.1 配置package repository

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

### 2.2 安装NVIDIA Container Toolkit

```bash
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

### 2.3 配置Docker

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### 2.4 验证安装

```bash
sudo docker run --rm --runtime=nvidia --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
```

## 3. 旧方法：安装Nvidia Docker（已废弃）

以下是nvidia-docker的旧安装方法，仅供历史参考。新安装请使用上面的NVIDIA Container Toolkit方法。

### 配置nvidia docker仓库

* 追加nvidia docker官方的gpg密钥

    ```bash
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
    sudo apt-key add -
    ```

* 追加nvidia docker仓库

    ```bash
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    ```

### 安装nvidia docker

* 更新`apt`包目录

    ```bash
    sudo apt-get update
    ```

* 安装最新版本的nvidia docker

    ```bash
    sudo apt-get install -y nvidia-docker2
    sudo pkill -SIGHUP dockerd
    ```

* 验证安装

    ```bash
    docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi
    ```

    如果正常输出则说明安装成功

    ```text
    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 418.40.04    Driver Version: 418.40.04    CUDA Version: 10.1     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |===============================+======================+======================|
    |   0  GeForce GTX 1060    On   | 00000000:01:00.0 Off |                  N/A |
    | N/A   50C    P5     6W /  N/A |    901MiB /  6078MiB |      3%      Default |
    +-------------------------------+----------------------+----------------------+
    +-----------------------------------------------------------------------------+
    | Processes:                                                       GPU Memory |
    |  GPU       PID   Type   Process name                             Usage      |
    |=============================================================================|
    +-----------------------------------------------------------------------------+
    ```

### 配置docker默认runtime

nvidia docker安装时会覆盖/etc/docker/daemon.json,为私有镜像库修改的配置将会被覆盖掉，所以需要追加私有镜像库配置。
为了能够让nvidia docker默认运行，需要设置docker的runtime为nvidia。

最终配置:(其中runtimes以实际为准)

```json
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    },
    "insecure-registries": [
        "192.168.1.192:5000","dev.teamx.work"
    ]
}
```
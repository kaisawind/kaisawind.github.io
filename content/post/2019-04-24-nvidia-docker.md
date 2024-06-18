---
layout: post
title:  "Nvidia Docker安装"
date: 2019-04-24 16:57:44
categories: [docker]
tags: [docker]
excerpt_separator: <!--more-->
---

nvidia-docker是能够直接在容器中使用Nvidia GPU而不需要额外的其他处理。结合k8s的插件`k8s-device-plugin`能够在k8s集群中使用GPU。

<!--more-->

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

    ```shell
    sudo sh cuda_10.1.105_418.39_linux.run
    ```

    根据提示进行

### 1.2 Cudnn

注意：cudnn需要注册nvidia账号

[https://developer.nvidia.com/rdp/cudnn-download](https://developer.nvidia.com/rdp/cudnn-download)

下载安装时注意Cudn的版本

## 2. 安装Nvidia Docker

nvidia-docker是能够直接在容器中使用Nvidia GPU而不需要额外的其他处理。结合k8s的插件[k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)能够在k8s集群中使用GPU。

[nvidia-docker](https://github.com/NVIDIA/nvidia-docker)官方安装说明 https://github.com/NVIDIA/nvidia-docker。

### 配置nvidia docker仓库

* 追加nvidia docker官方的gpg密钥

    ```shell
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
    sudo apt-key add -
    ```

* 追加nvidia docker仓库

    ```shell
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    ```

### 安装nvidia docker

* 更新`apt`包目录

    ```shell
    sudo apt-get update
    ```

* 安装最新版本的nvidia docker

    ```shell
    sudo apt-get install -y nvidia-docker2
    sudo pkill -SIGHUP dockerd
    ```

* 验证安装

    ```shell
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
---
layout: post
title:  "manjaro中tensorflow2支持gpu"
date: 2021-06-24 11:05:16
categories: [linux, manjaro]
tags: [linux]
excerpt_separator: <!--more-->
---
manjaro中tensorflow2支持gpu
<!--more-->

## 1. 概述

由于系统是manjaro，使用tensroflow进行模型训练，需要支持GPU训练。

## 2. manjaro安装切换GPU独显

[linux使用wine运行游戏](https://www.kaisawind.com/2020/09/30/2020-09-30-linux-wine/)

使用以下命令进行独显切换
```bash
prime-offload
optimus-manager --switch nvidia
```

## 3. manjaro安装cuda,cudnn

```bash
sudo pacman -S cuda cuda-tools cudnn
```

## 4. 安装tensorflow-gpu

```bash
conda install tensorflow-gpu
```

## 5. 重启

关键一步

## 6. 检查

```bash
(base) [pana@kaisawind-z2 ~]$ nvidia-smi
Thu Jun 24 11:14:00 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 465.31       Driver Version: 465.31       CUDA Version: 11.3     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   56C    P2    29W /  N/A |    895MiB /  6078MiB |     22%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      3140      G   /usr/lib/Xorg                     304MiB |
|    0   N/A  N/A      3226      G   /usr/bin/kwin_x11                 112MiB |
|    0   N/A  N/A      3288      G   /usr/bin/plasmashell               41MiB |
|    0   N/A  N/A      3976      G   /usr/lib/firefox/firefox          108MiB |
|    0   N/A  N/A      4375      C   ...onda/envs/py38/bin/python      175MiB |
|    0   N/A  N/A      4619      G   ...AAAAAAAAA= --shared-files       35MiB |
|    0   N/A  N/A      6594      G   ...AAAAAAAAA= --shared-files      109MiB |
+-----------------------------------------------------------------------------+
```

```python
import tensorflow as tf

tf.__version__

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print("Num CPUs Available: ", len(tf.config.experimental.list_physical_devices('CPU')))
```
Output:
```bash
Num GPUs Available:  1
Num CPUs Available:  1
```

```python
device_name = tf.test.gpu_device_name()
print('Found GPU at: {}'.format(device_name))
```
Output:
```bash
Found GPU at: /device:GPU:0
```
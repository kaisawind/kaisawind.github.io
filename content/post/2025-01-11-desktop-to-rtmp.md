---
layout: post
title:  "ffmpeg录屏转rtmp"
date: 2025-01-11 10:55:00
lastmod: 2026-03-19
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "ffmpeg录屏转rtmp"
---
ffmpeg录屏转rtmp
<!--more-->

## 问题描述

需要将桌面操作或RTMP推流到服务器。

## 解决方法

### 方法1：使用ffmpeg

```bash
ffmpeg -f x11grab -i :0 -framerate 30 -video_size 1920x1080 -i 1        -f flv rtmp://localhost/live/stream_name        -c:v libx264 -preset veryfast -tune zerolatency        -f pulse -i :0 -stream_name out.flv
```

参数说明：
- `-f x11grab` 指定X11抓屏输入
- `-i :0` 设置输入为第0号屏幕
- `-framerate 30` 设置帧率
- `-video_size 1920x1080` 设置视频分辨率
- `-i 1` 使用1个线程
- `-f flv` 设置输出格式为FLV
- `rtmp://localhost/live/stream_name` 设置RTMP地址
- `-c:v libx264` 设置视频编码器
- `-preset veryfast` 设置编码预设
- `-tune zerolatency` 优化延迟
- `-f pulse -i :0` 设置音频输入
- `-stream_name` 设置流名称

- `out.flv` 输出文件名

### 方法2：使用obs-studio

1. 打开OBS Studio
2. 添加"显示器捕获"源
3. 开始录制
4. 选择RTMP作为输出

### 方法3：使用脚本

```bash
#!/bin/bash
# 使用ffmpeg推流桌面
while true; do
    ffmpeg -f x11grab -i :0 -framerate 30 -video_size 1920x1080            -f flv rtmp://your-server/live/stream_key            -c:v libx264 -preset veryfast            -f pulse -i :0 -            out_$(date +%Y%m%d_%H%M%S).flv
    
    sleep 5
done
```

## 最佳实践

1. **控制质量**：调整视频参数平衡质量和带宽
2. **音频设置**：确保音频参数匹配RTMP服务器要求
3. **测试连接**：推流前测试RTMP服务器是否正常接收
4. **监控资源**：使用`htop`监控CPU和内存使用
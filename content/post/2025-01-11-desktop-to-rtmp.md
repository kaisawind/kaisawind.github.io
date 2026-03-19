---
layout: post
title:  "ffmpeg录屏转rtmp"
date: 2025-01-11 10:55:00
lastmod: 2026-03-19
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
---
ffmpeg录屏转rtmp
<!--more-->

> **提示**: FFmpeg版本更新较快，建议使用最新稳定版。



```bash
ffmpeg -f x11grab -framerate 30 -video_size 1280x720 -i :0.0 -c:v libx264 -vf format=yuv420p -c:a copy -f flv rtmp://xxxxx/live
```
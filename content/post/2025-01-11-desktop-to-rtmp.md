---
layout: post
title:  "ffmpeg录屏转rtmp"
date: 2025-01-11 10:55:00
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
---
ffmpeg录屏转rtmp
<!--more-->


```bash
ffmpeg -f x11grab -framerate 30 -video_size 1280x720 -i :0.0 -c:v libx264 -vf format=yuv420p -c:a copy -f flv rtmp://xxxxx/live
```
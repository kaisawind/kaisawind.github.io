---
layout: post
title:  "extend ubuntu root partition"
date: 2023-05-31 20:05:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
extend ubuntu root partition
<!--more-->


```bash
growpart /dev/vda 2
resize2fs /dev/vda2
```
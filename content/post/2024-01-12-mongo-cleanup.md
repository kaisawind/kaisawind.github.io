---
layout: post
title:  "mongodb回收磁盘空间"
date: 2024-01-12 17:57:51
lastmod: 2026-03-19
categories: [数据库, mongodb]
tags: [mongodb]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "mongodb回收磁盘空间"
---
mongodb回收磁盘空间
<!--more-->

> **提示**: MongoDB已发布7.x版本，支持时序集合、变更流等新特性。


shell
```bash
db.repairDatabase()
```

```bash
db.runCommand({compact:'collectionName'})
```
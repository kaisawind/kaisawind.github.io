---
layout: post
title:  "mongodb回收磁盘空间"
date: 2024-01-12 17:57:51
categories: [数据库, mongodb]
tags: [mongodb]
excerpt_separator: <!--more-->
---
mongodb回收磁盘空间
<!--more-->

shell
```bash
db.repairDatabase()
```

```bash
db.runCommand({compact:'collectionName'})
```
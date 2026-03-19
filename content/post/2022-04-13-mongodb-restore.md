---
layout: post
title:  "mongodb备份和恢复"
date: 2022-04-13 14:46:28
lastmod: 2026-03-19
categories: [数据库, mongodb]
tags: [mongodb]
excerpt_separator: <!--more-->
---
mongodb备份和恢复
<!--more-->

> **提示**: MongoDB已发布7.x版本，支持时序集合、变更流等新特性。



### 备份
```bash
mongodump --host="db-mongodb:27017" --archive=/dumps/logr/logr.gz --gzip --db=logr
```

批量备份
```bash
data=$(date +%Y%m%d) && mkdir -p /dumps/$data && for db in "logr" "user" "orgs" "groups" "core";do mongodump --host="db-mongodb:27017" --archive=/dumps/$data/$db.gz --gzip --db=$db;done && ls -al /dumps/$data
```

### 恢复

```bash
mongorestore --drop --gzip --archive=./logr.gz
```
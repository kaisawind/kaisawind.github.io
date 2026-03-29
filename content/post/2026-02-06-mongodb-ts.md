---
layout: post
title:  "MongoDB 时间序列数据库恢复"
date: 2026-02-06 10:57:51
lastmod: 2026-03-19
categories: [数据库, mongodb]
tags: [mongodb]
excerpt_separator: <!--more-->
---
MongoDB 时间序列数据库恢复时会自动清理过期数据，首先需要禁用时间序列自动清理。本文介绍如何安全恢复 MongoDB 时间序列数据。
<!--more-->

> **提示**: MongoDB 已发布 7.x 版本，支持时序集合、变更流等新特性。

## 问题背景

MongoDB 时间序列集合会自动清理过期数据。在恢复数据时，如果 TTL（Time To Live）索引仍然启用，MongoDB 会在数据恢复后立即删除过期数据，导致数据丢失。

## 解决方案

### 方法一：禁用 TTL 索引后恢复

在恢复数据前，先禁用 TTL 索引：

```bash
# 暂停集合的所有TTL索引
mongosh --eval '
db.runCommand({
  "collMod": "your_collection",
  "expireAfterSeconds": -1
})
'
```

然后执行恢复：

```bash
mongorestore --db yourdb --collection metrics /backup/metrics.bson
```

恢复完成后，可以根据需要重新启用 TTL：

```bash
mongosh --eval 'db.runCommand({collMod: "metrics", expireAfterSeconds: 86400})'
```

### 方法二：恢复时不包含索引

如果不需要保留索引，可以使用 `--noIndexRestore` 参数：

```bash
mongorestore --noIndexRestore --db yourdb /backup/directory/
```

恢复后手动创建需要的索引：

```bash
mongosh --eval '
db.metrics.createIndex(
  { "timestamp": 1 },
  { "expireAfterSeconds": 86400 }
)
'
```

### 方法三：完整恢复流程

```bash
# 步骤1: 禁用TTL索引
mongosh --eval 'db.runCommand({collMod: "history", expireAfterSeconds: -1})'

# 步骤2: 执行数据恢复
mongorestore --db yourdb --collection metrics /backup/metrics.bson

# 步骤3: 验证数据
mongosh --eval 'db.metrics.count()'

# 步骤4: 重新启用TTL（可选）
mongosh --eval 'db.runCommand({collMod: "metrics", expireAfterSeconds: 86400})'
```

## 注意事项

1. **备份数据**：在执行任何操作前，确保有完整的备份
2. **测试环境**：建议先在测试环境中验证恢复流程
3. **索引重建**：禁用 TTL 后，需要手动重建索引
4. **数据验证**：恢复后务必验证数据完整性
5. **版本兼容**：确保 MongoDB 版本兼容，特别是使用时间序列特性时

## 常用命令

```bash
# 查看集合信息
db.runCommand({collStats: "metrics"})

# 查看索引
db.metrics.getIndexes()

# 查看当前 TTL 设置
db.runCommand({collMod: "metrics", expireAfterSeconds: -1})

# 查看集合大小
db.metrics.stats()
```

---
layout: post
title:  "MySQL GROUP BY 与 ONLY_FULL_GROUP_BY 错误解决"
date: 2021-01-20 11:08:06
lastmod: 2026-03-19
categories: [数据库, mysql]
tags: [mysql]
excerpt_separator: <!--more>-->
author: "kaisawind"
description: "MySQL 8.0 默认启用 ONLY_FULL_GROUP_BY 模式，使用 GROUP BY 查询时可能会报错。本文介绍问题的原因和解决方法。"
---
MySQL 8.0 默认启用 `ONLY_FULL_GROUP_BY` 模式，使用 GROUP BY 查询时可能会报错。本文介绍问题的原因和解决方法。
<!--more-->

> **注意**: MySQL 8.0 已成为主流版本，本文档可能基于旧版本编写。

## 问题描述

MySQL 8.0.18 版本，使用客户端查询数据时报错：

```
Mysql group by this is incompatible with sql_mode=only_full_group_by.
```

## 问题原因

MySQL 8.0.18 默认 SQL Mode 是：

```
ONLY_FULL_GROUP_BY
STRICT_TRANS_TABLES
NO_ZERO_IN_DATE
NO_ZERO_DATE
ERROR_FOR_DIVISION_BY_ZERO
NO_ENGINE_SUBSTITUTION
```

`ONLY_FULL_GROUP_BY` 模式要求：GROUP BY 子句中出现的所有列必须在 SELECT 列表中出现，或者是聚合函数的一部分。

## 解决方法

### 方法一：临时修改（重启失效）

```sql
SET SESSION sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```

### 方法二：永久修改（推荐）

编辑 MySQL 配置文件（`/etc/mysql/my.cnf` 或 `/etc/my.cnf`）：

```cnf
[mysqld]
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```

修改后重启 MySQL 服务：

```bash
sudo systemctl restart mysql
```

### 方法三：修改查询语句（推荐）

如果不想修改 SQL Mode，可以修改查询语句以符合 `ONLY_FULL_GROUP_BY` 规范：

#### 错误示例

```sql
-- 错误：name 不在 GROUP BY 中
SELECT id, name, COUNT(*)
FROM users
GROUP BY id;
```

#### 正确示例

```sql
-- 方法 1：将所有非聚合列加入 GROUP BY
SELECT id, name, COUNT(*)
FROM users
GROUP BY id, name;

-- 方法 2：使用聚合函数
SELECT id, ANY_VALUE(name), COUNT(*)
FROM users
GROUP BY id;

-- 方法 3：使用 MAX/MIN 函数
SELECT id, MAX(name), COUNT(*)
FROM users
GROUP BY id;
```

## ONLY_FULL_GROUP_BY 说明

### 启用 ONLY_FULL_GROUP_BY

```sql
SET GLOBAL sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,...';
```

### 禁用 ONLY_FULL_GROUP_BY

```sql
SET GLOBAL sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,...';
```

### 查看当前设置

```sql
SELECT @@sql_mode;
```

## 常用聚合函数

| 函数 | 说明 |
|------|------|
| `COUNT()` | 统计行数 |
| `SUM()` | 求和 |
| `AVG()` | 平均值 |
| `MAX()` | 最大值 |
| `MIN()` | 最小值 |
| `ANY_VALUE()` | 任意值（绕过 ONLY_FULL_GROUP_BY 检查） |

## 最佳实践

1. **遵循标准 SQL**：尽量修改查询语句以符合 SQL 标准
2. **明确分组**：在 GROUP BY 中明确指定所有非聚合列
3. **使用聚合函数**：对于不需要精确值的列使用 ANY_VALUE()
4. **全局配置**：如果需要全局禁用，修改配置文件
5. **测试验证**：修改后测试所有相关查询

## 注意事项

1. **性能影响**：GROUP BY 列越多，性能可能越差
2. **数据准确性**：ANY_VALUE() 可能返回不确定的值
3. **兼容性**：不同 MySQL 版本的默认 sql_mode 不同
4. **备份数据**：修改全局配置前备份数据库

## 相关文章

- [MySQL sql_mode 配置错误解决](/2021-01-20-mysql-error/)
- [MySQL 数据转换](/2021-09-08-mysql/)


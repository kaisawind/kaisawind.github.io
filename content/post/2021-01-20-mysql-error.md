---
layout: post
title:  "MySQL sql_mode 配置错误解决"
date: 2021-01-20 11:03:06
lastmod: 2026-03-19
categories: [数据库, mysql]
tags: [mysql]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "MySQL 配置 sql_mode 时报错 unknown variable 'sql_mode=STRICT_TRANS_TABLES,....'.，本文介绍问题的原因和解决方法。"
---
MySQL 配置 sql_mode 时报错 `unknown variable 'sql_mode=STRICT_TRANS_TABLES,....'.`，本文介绍问题的原因和解决方法。
<!--more-->

## 问题描述

MySQL 8.0.18 版本，在 `mysql.cnf` 配置 `sql_mode` 时报错：

```
unknown variable 'sql_mode=STRICT_TRANS_TABLES,....'.
```

## 问题原因

配置文件 `mysql.cnf` 的主字段配置错误，`sql_mode` 需要配置到 `[mysqld]` 段中，而不是直接放在配置文件顶部。

## 解决方法

### 方法一：修改配置文件

编辑 `mysql.cnf`（或 `my.cnf`）文件，将 `sql_mode` 配置放在 `[mysqld]` 段中：

```cnf
[mysqld]
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```

### 方法二：查看当前配置

在修改配置前，可以先查看当前的 sql_mode 设置：

```sql
-- 查看当前 sql_mode
SELECT @@sql_mode;

-- 查看全局 sql_mode
SELECT @@GLOBAL.sql_mode;

-- 查看 session sql_mode
SELECT @@SESSION.sql_mode;
```

### 方法三：临时修改（重启失效）

如果不想修改配置文件，可以临时修改 sql_mode：

```sql
-- 设置全局 sql_mode
SET GLOBAL sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- 设置当前会话 sql_mode
SET SESSION sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```

## 常见 SQL Mode 选项

| 选项 | 说明 |
|------|------|
| `STRICT_TRANS_TABLES` | 启用严格模式，对事务表无效数据拒绝插入 |
| `NO_ZERO_IN_DATE` | 不允许日期或时间为 0 |
| `NO_ZERO_DATE` | 不允许日期为 0000-00-00 |
| `ERROR_FOR_DIVISION_BY_ZERO` | 除以零时产生错误 |
| `NO_ENGINE_SUBSTITUTION` | 不允许使用默认存储引擎替换 |
| `ONLY_FULL_GROUP_BY` | GROUP BY 只能包含选定列或聚合函数 |

## 配置文件说明

MySQL 配置文件位置：

- Linux: `/etc/mysql/my.cnf` 或 `/etc/my.cnf`
- macOS: `/usr/local/etc/my.cnf` 或 `~/.my.cnf`
- Windows: `C:\ProgramData\MySQL\MySQL Server 8.0\my.ini`

## 验证配置

修改配置后，重启 MySQL 服务并验证：

```bash
# 重启 MySQL 服务
sudo systemctl restart mysql

# 或
sudo service mysql restart

# 验证配置
mysql -u root -p -e "SELECT @@sql_mode;"
```

## 注意事项

1. **配置文件位置**：确保修改了正确的配置文件
2. **语法正确**：注意配置文件中的缩进和引号
3. **权限问题**：确保有权限修改配置文件
4. **重启服务**：修改配置后需要重启 MySQL 服务
5. **备份配置**：修改前备份原配置文件
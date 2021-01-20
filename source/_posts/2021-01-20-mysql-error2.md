---
layout: post
title:  "[Warning] World-writable config file '/etc/mysql/mysql.conf.d/mysqld.cnf' is ignored."
date: 2021-01-20 11:08:06
categories: [数据库, mysql]
tags: [mysql, shell]
excerpt_separator: <!--more-->
---
[Warning] World-writable config file '/etc/mysql/mysql.conf.d/mysqld.cnf' is ignored.
<!--more-->
mysql版本8.0.18，添加mysql.cnf一直无效，使用命令行连接mysql.cnf是报警告
`[Warning] World-writable config file '/etc/mysql/mysql.conf.d/mysqld.cnf' is ignored.`

原因:
需要将mysql.conf.d文件通过chmod进行权限降级。

```bash
chmod 644 /etc/mysql/conf.d/mysql.cnf
```
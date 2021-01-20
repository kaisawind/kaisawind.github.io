---
layout: post
title:  "unknown variable 'sql_mode=STRICT_TRANS_TABLES,....'."
date: 2021-01-20 11:03:06
categories: [数据库, mysql]
tags: [mysql, shell]
excerpt_separator: <!--more-->
---
unknown variable 'sql_mode=STRICT_TRANS_TABLES,....'.
<!--more-->
mysql版本8.0.18，在mysql.cnf配置sql_mode报错`unknown variable 'sql_mode=STRICT_TRANS_TABLES,....'.`。

原因:
mysql.cnf的主字段配置错误,需要配置到mysqld中。

```cnf
[mysqld]
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```
---
layout: post
title:  "Mysql group by this is incompatible with sql_mode=only_full_group_by"
date: 2021-01-20 11:08:06
categories: [数据库, mysql]
tags: [mysql]
excerpt_separator: <!--more-->
---
Mysql group by this is incompatible with sql_mode=only_full_group_by
<!--more-->
mysql版本8.0.18，使用客户端查询数据时报错
`Mysql group by this is incompatible with sql_mode=only_full_group_by.`

原因:
mysql 8.0.18默认SQL Mode是`ONLY_FULL_GROUP_BY STRICT_TRANS_TABLES NO_ZERO_IN_DATE NO_ZERO_DATE ERROR_FOR_DIVISION_BY_ZERO NO_ENGINE_SUBSTITUTION`

需要将ONLY_FULL_GROUP_BY去掉

解决1：
重启失效
```bash
set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```

解决2:
配置mysql.cnf
```cnf
[mysqld]
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```


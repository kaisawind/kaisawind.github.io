---
layout: post
title:  "redis数据删除策略"
date: 2021-09-06 11:03:28
categories: [数据库, redis]
tags: [redis]
excerpt_separator: <!--more-->
---
redis数据删除策略
<!--more-->

## 1. 概述
当redis的键值设置过期时间后，redis会按照策略进行删除

## 2. 策略

被动删除：当读/写一个已经过期的key时，会触发惰性删除策略，直接删除掉这个过期key
主动删除：由于惰性删除策略无法保证冷数据被及时删掉，所以Redis会定期主动淘汰一批已过期的key
主动清理：当前已用内存超过maxmemory限定时，触发主动清理策略
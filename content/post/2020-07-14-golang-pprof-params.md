---
layout: post
title:  "golang pprof参数说明"
date: 2020-07-14 15:05:12
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang pprof参数说明
<!--more-->

## 1. top

|列名	|含义|
|---|---|
|flat	|本函数的执行耗时|
|flat%	|flat 占 CPU 总时间的比例。程序总耗时 16.22s, Eat 的 16.19s 占了 99.82%|
|sum%	|前面每一行的 flat 占比总和|
|cum	|累计量。指该函数加上该函数调用的函数总耗时|
|cum%	|cum 占 CPU 总时间的比例|

## 2. 内存

|类型|含义|
|---|---|
|inuse_space	|已分配但尚未释放的内存数量|
|inuse_objects	|已分配但尚未释放的对象数量|
|alloc_space	|分配的内存总量（与释放的内存无关）|
|alloc_objects	|分配的对象总数（与释放对象无关）|
---
layout: post
title:  "Rust语言Derive说明"
date: 2020-04-28 11:38:04 +0800
categories: [rust]
tags: [rust, manjaro, linux]
excerpt_separator: <!--more-->
---
Rust语言Derive说明
<!--more-->

## 1. 概述
编译器可以通过`#[derive(*****)]`为某些特性提供基本的实现。

## 2. 特性

|特性|作用|说明|
|---|---|---|
|Eq|等价关系|比较是否相等|
|PartialEq|局部等价|比较部分是否相等|
|Ord|比较大小|比较大小|
|PartialOrd|部分比较大小|部分比较大小|
|Clone|深拷贝|深拷贝|
|Copy|浅拷贝|浅拷贝|
|Hash|计算Hash值|计算Hash值|
|Default|默认值|默认值|
|Debug|`{:?}`进行格式化|`{:?}`进行格式化|


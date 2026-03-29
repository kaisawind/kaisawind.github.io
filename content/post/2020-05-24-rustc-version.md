---
layout: post
title:  "rustc版本查看"
date: 2020-05-24 15:28:42
lastmod: 2026-03-19
categories: [编程语言,rust]
tags: [rust]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "rustc版本查看"
---
rustc版本查看
<!--more-->

> **提示**: Rust每6周发布一个新版本，建议使用`rustup`保持最新。


```bash
rustc --version --verbose
```

输出
```bash
rustc 1.45.0-nightly (a74d1862d 2020-05-14)
binary: rustc
commit-hash: a74d1862d4d87a56244958416fd05976c58ca1a8
commit-date: 2020-05-14
host: x86_64-unknown-linux-gnu
release: 1.45.0-nightly
LLVM version: 9.0
```
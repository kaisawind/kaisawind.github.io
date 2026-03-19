---
layout: post
title:  "rust清华镜像源"
date: 2021-08-02 16:02:04
lastmod: 2026-03-19
categories: [编程语言,rust]
tags: [rust]
excerpt_separator: <!--more-->
---
rust清华镜像源
<!--more-->

> **提示**: Rust每6周发布一个新版本，建议使用`rustup`保持最新。


编辑 ~/.cargo/config 文件，添加以下内容：

```conf
[source.crates-io]
replace-with = 'tuna'

[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"
```
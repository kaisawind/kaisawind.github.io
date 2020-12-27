---
layout: post
title:  "Rust的alpine的docker编译环境"
date: 2020-10-15 11:30:04
categories: [编程语言,rust]
tags: [rust, manjaro, linux]
excerpt_separator: <!--more-->
---
Rust的docker编译环境
<!--more-->

## 1. 概述
Rust中官方docker镜像只有debian镜像支持跨平台，alpine镜像不支持跨平台。

## 2. 构建

cargo的镜像代理docs/config
```config
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'ustc'

[source.ustc]
registry = "https://mirrors.ustc.edu.cn/crates.io-index"
```

编译镜像构建
```Dockerfile
FROM alpine
ADD docs/config /root/.cargo/config
ENV RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static \
    RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup \
    RUSTFLAGS=-Ctarget-feature=-crt-static
RUN sed -e 's/dl-cdn[.]alpinelinux.org/mirrors.aliyun.com/g' -i~ /etc/apk/repositories \
  && apk add --update --no-cache wget gcc clang-dev musl-dev yaml curl libmicrohttpd libuuid
RUN mkdir deps && \
    wget -O - https://static.rust-lang.org/dist/rust-nightly-$(apk --print-arch)-unknown-linux-musl.tar.gz | tar -C deps -z -x -f - && \
    sh /deps/rust-nightly-$(apk --print-arch)-unknown-linux-musl/install.sh --prefix=/usr && \
    rm -rf /deps
```

* RUSTFLAGS=-Ctarget-feature=-crt-static
https://github.com/rust-lang/rust/issues/31322
默认RUST使用C runtime静态链接？但是alpine musl不能使用静态链接，所以需要去掉编译时静态连接特性。
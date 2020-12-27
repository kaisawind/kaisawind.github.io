---
layout: post
title:  "golang压缩包方式安装"
date: 2020-03-05 14:15:12
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
golang压缩包方式安装
<!--more-->

安装go
```bash
sudo tar -C /usr/lib -xzf go$VERSION.$OS-$ARCH.tar.gz
sudo ln -snf /usr/lib/go/bin/go /usr/local/bin/go
sudo ln -snf /usr/lib/go/bin/gofmt /usr/local/bin/gofmt
go env -w GOPROXY=https://goproxy.io,direct
```

编辑`.bashrc`
```bash
export GOPATH=${HOME}/go
export PATH=${GOPATH}/bin:$PATH
```
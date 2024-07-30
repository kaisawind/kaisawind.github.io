---
layout: post
title: 'yarn出现There appears to be trouble with your network connection. Retrying...'
date: 2024-07-30 14:36:55
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
yarn出现There appears to be trouble with your network connection. Retrying...
<!--more-->

打印yarn日志
```bash
$ yarn --verbose
verbose 0.349088603 Performing "GET" request to "https://yarnpkg.com/latest-version".
[1/4] Resolving packages...
success Already up-to-date.
Done in 0.54s.
info There appears to be trouble with your network connection. Retrying...
verbose 33.431991432 Performing "GET" request to "https://yarnpkg.com/latest-version".
info There appears to be trouble with your network connection. Retrying...
verbose 66.464066132 Performing "GET" request to "https://yarnpkg.com/latest-version".
```

关闭yarn升级检查
```bash
yarn config set disable-self-update-check true
```
---
layout: post
title:  "journalctl日志清理"
date: 2021-03-18 10:13:16
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
journalctl日志清理
<!--more-->

`journalctl --disk-usage`查看日志所用的空间
```bash
# journalctl --disk-usage
Archived and active journals take up 4.0G in the file system.
```

`sudo journalctl --vacuum-size=50M`制定日志的最大空间为50M
```bash
Vacuuming done, freed 3.9G of archived journals from /var/log/journal/ece7bca439b64bc0953aaa4efe9b62c9.
```

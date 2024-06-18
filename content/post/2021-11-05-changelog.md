---
layout: post
title: "CHANGELOG自动生成"
date: 2021-11-05 16:09:16
categories: [linux]
tags: [linux， git]
excerpt_separator: <!--more-->
---
CHANGELOG 自动生成
<!--more-->

安装 github_changelog_generator

```bash
gem install github_changelog_generator
```

`github_changelog_generator -u github_project_namespace -p github_project`

```bash
export CHANGELOG_GITHUB_TOKEN="«your-40-digit-github-token»"
github_changelog_generator -u kaisawind -p iotx
```

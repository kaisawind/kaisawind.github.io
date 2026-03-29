---
layout: post
title:  "ubuntu创建桌面快捷方式"
date: 2024-11-21 11:44:54
lastmod: 2026-03-19
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
author: "kaisawind"
description: "ubuntu创建桌面快捷方式"
---
ubuntu创建桌面快捷方式
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。



创建文件`物联网云平台.desktop`到`～/Desktop/`下
```bash
[Desktop Entry]
Version=1.0
Name=物联网云平台
GenericName=物联网云平台
NoDisplay=true
Exec=chromium-browser --app=https://localhost/iotx/
Terminal=false
X-MultipleArgs=false
Type=Application
Icon=iotx
Categories=Network;WebBrowser;
StartupNotify=true
Actions=NewWindow;
```
添加图标到`～/.local/share/icons`，图标名称与`Icon`相同。
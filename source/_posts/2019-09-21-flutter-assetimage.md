---
layout: post
title:  "image:flutter本地图片"
date: 2019-9-21 16:33:38 +0800
categories: [flutter]
tags: [android, flutter, windows]
excerpt_separator: <!--more-->
---


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 代码模板](#2-代码模板)

<!-- /code_chunk_output -->


## 1. 概述

<img src="https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue" />

`Image`是flutter的图片类，支持本地图片，网络图片。
example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/ba0a200ca24862d318f909189730dba5e1eb1e05)

## 2. 代码模板

```dart
import 'package:flutter/material.dart';
import 'package:flutter_example/resources/image_keys.dart';

class MyAssetImage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: <Widget>[
          ListTile(
            title: Text('Asset Image'),
          ),
          Divider(),
          Image.asset(ImageKeys.avatarAssets),
        ],
      ),
    );
  }
}

```
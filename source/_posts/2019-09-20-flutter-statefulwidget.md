---
layout: post
title:  "StatefulWidget:flutter有状态组件"
date: 2019-9-20 15:27:40 +0800
categories: [flutter]
tags: [android, flutter, windows]
excerpt_separator: <!--more-->
---


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 生命周期](#2-生命周期)
- [3. `State`生命周期函数](#3-state生命周期函数)
- [4. 生命周期阶段](#4-生命周期阶段)
  - [4.1 初期化](#41-初期化)
  - [4.2 `reload`热更新](#42-reload热更新)
  - [4.3 析构](#43-析构)
- [5. 代码模板](#5-代码模板)

<!-- /code_chunk_output -->


## 1. 概述

![GitHub release (latest by date)](https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue)

`StatefulWidget`是flutter的有状态组件，通过`State`类对数据进行管理。
example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/c332a09515764af9cb7a92d9f0264f3a02809e84)

## 2. 生命周期

`State`类最主要管理的是数据的生命周期

Flutter系统架构中关于`State`的说明(需要翻墙)。

![生命周期](/images/微信截图_20190920180226.png)

## 3. `State`生命周期函数

| 函数                    | 描述                                                               |
|-------------------------|------------------------------------------------------------------|
| `State`                 | 构造函数会在最开始被调用                                           |
| `initState`             | `Widget`创建时进行调用，在构造函数之后                              |
| `didChangeDependencies` | 当`State`对象的依赖发生变化时会被调用                              |
| `build`                 | 它用于构建`Widget`子树的,当`setState`触发的时候会被调用            |
| `didUpdateWidget`       | 组件状态改变时候调用                                               |
| `deactivate`            | 当`State`对象从树中被移除时，会调用此回调。                          |
| `dispose`               | 当State对象从树中被永久移除时调用；通常在此回调中释放资源。          |
| `reassemble`            | 在热重载(hot reload)时会被调用，此回调在Release模式下永远不会被调用 |

## 4. 生命周期阶段

### 4.1 初期化

`构造函数`
↓
`initState`
↓
`didChangeDependencies`
↓
`build` 

### 4.2 `reload`热更新

`reassemble` 
↓
`didUpdateWidget`
↓
`build` 

### 4.3 析构

`deactivate`
↓
`dispose`

## 5. 代码模板

```dart
import 'package:flutter/material.dart';

class MyStatefulWidget extends StatefulWidget {
  @override
  _MyStatefulWidgetState createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  _MyStatefulWidgetState() {}

  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text('Stateful Widget'),
      ),
      body: Center(),
    );
  }
}
```
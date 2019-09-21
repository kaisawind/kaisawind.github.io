---
layout: post
title:  "fluro:flutter路由"
date: 2019-9-20 15:35:50 +0800
categories: [flutter]
tags: [android, flutter]
excerpt_separator: <!--more-->
---


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 使用方法](#2-使用方法)
  - [2.1 添加依赖](#21-添加依赖)
  - [2.2 添加路由代码](#22-添加路由代码)
  - [2.3 路由初期化和注册](#23-路由初期化和注册)

<!-- /code_chunk_output -->


## 1. 概述

![Pub](https://img.shields.io/pub/v/fluro)
![GitHub release (latest by date)](https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue)
  
Fluro是flutter的路由插件，能够很方便的进行静态路由导航，和字符串路由传参。

Fluro Github (https://github.com/theyakka/fluro)

example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/a003a9e2733e75dc663b1588bbc5555e9279846c)

## 2. 使用方法

### 2.1 添加依赖

修改
`<project>/pubspec.yaml`

```yaml
dependencies:
  flutter:
    sdk: flutter

  # Fluro is a Flutter routing library that adds flexible routing options like wildcards, named parameters and clear route definitions.
  # git: git://github.com/theyakka/fluro.git
  fluro: ^1.5.1
```

### 2.2 添加路由代码

* 全局路由表`application.dart`

```dart
import 'package:fluro/fluro.dart';

class Application {
    static Router router;
}

```

* 路由与组件结合类`routers.dart`

    `/`为根路由，app默认第一个界面。
    `notFoundHandler`为app找不到页面时所显示的页面。

```dart
import 'package:fluro/fluro.dart';
import 'router_handler.dart';

class Routes {
static String root = "/";
static String home = "/home";

static void configureRoutes(Router router) {
    router.notFoundHandler = notFoundWidgetHandler;
    router.define(root, handler: homePageHandler);
    router.define(home, handler: homePageHandler);
}
}

```

* 组件句柄声明与定义`router_handler.dart`

```dart
import 'package:fluro/fluro.dart';
import 'package:flutter/material.dart';
import 'package:flutter_example/views/my_home_page.dart';
import 'package:flutter_example/widgets//404.dart';

/// 主页
var homePageHandler = new Handler(
handlerFunc: (BuildContext context, Map<String, List<String>> params) {
    String title = params['title']?.first ?? 'my home page';
    return MyHomePage(title: title);
},
);

/// Not Found 页面
var notFoundWidgetHandler = new Handler(handlerFunc: (BuildContext context, Map<String, List<String>> params) {
    return NotFoundWidget();
});
```

### 2.3 路由初期化和注册

`app`类为`StatefulWidget`组件

在`State`的构造函数中对路由进行初期化(flutter声明周期)。
通过`MaterialApp`的`onGenerateRoute`回调函数进行路由注册。

```dart
import 'package:flutter/material.dart';
import 'package:fluro/fluro.dart';
import 'package:flutter_example/routers/routers.dart';
import 'package:flutter_example/routers/application.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {

  _MyAppState() {
    // init router
    final router = new Router();    // ☆☆☆☆☆
    Routes.configureRoutes(router); // ☆☆☆☆☆
    Application.router = router;    // ☆☆☆☆☆
  }

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      onGenerateRoute: Application.router.generator, // ☆☆☆☆☆
    );
  }
}
```





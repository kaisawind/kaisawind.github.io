---
layout: post
title:  "image:flutter网络图片"
date: 2019-9-21 16:09:21 +0800
categories: [flutter]
tags: [android, flutter, windows]
excerpt_separator: <!--more-->
---


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 代码模板](#2-代码模板)
- [3. 未认证的证书](#3-未认证的证书)

<!-- /code_chunk_output -->


## 1. 概述

<img src="https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue" />

`Image`是flutter的图片类，支持本地图片，网络图片。
example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/239f305467fc613063fb3906f339c0ef3820e0fc)

## 2. 代码模板

```dart
import 'package:flutter/material.dart';
import 'package:flutter_example/resources/image_keys.dart';

class MyNetworkImage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: <Widget>[
          ListTile(
            title: Text('Network Image'),
          ),
          Divider(),
          Image.network(ImageKeys.avatar),
        ],
      ),
    );
  }
}

```

## 3. 未认证的证书

由于是网络图片，所以当进行访问未认证的https服务器(本地调试)时, 会遇到问题，因此需要跳过证书认证。

[Network Image - Connection closed before full header was received...](https://github.com/flutter/flutter/issues/25107)

```text
flutter: When the exception was thrown, this was the stack:
flutter: #0      NetworkImage._loadAsync (package:flutter/src/painting/image_provider.dart:490:41)
flutter: <asynchronous suspension>
flutter: #1      NetworkImage.load (package:flutter/src/painting/image_provider.dart:471:14)
flutter: #2      ImageProvider.resolve.<anonymous closure>.<anonymous closure> (package:flutter/src/painting/image_provider.dart:267:86)
flutter: #3      ImageCache.putIfAbsent (package:flutter/src/painting/image_cache.dart:143:20)
flutter: #4      ImageProvider.resolve.<anonymous closure> (package:flutter/src/painting/image_provider.dart:267:63)
flutter: #5      SynchronousFuture.then (package:flutter/src/foundation/synchronous_future.dart:38:29)
flutter: #6      ImageProvider.resolve (package:flutter/src/painting/image_provider.dart:265:30)
flutter: #7      _ImageState._resolveImage (package:flutter/src/widgets/image.dart:630:20)
flutter: #8      _ImageState.didChangeDependencies (package:flutter/src/widgets/image.dart:605:5)
flutter: #9      StatefulElement._firstBuild (package:flutter/src/widgets/framework.dart:3846:12)
flutter: #10     ComponentElement.mount (package:flutter/src/widgets/framework.dart:3696:5)
flutter: #11     Element.inflateWidget (package:flutter/src/widgets/framework.dart:2950:14)
flutter: #12     Element.updateChild (package:flutter/src/widgets/framework.dart:2753:12)
```

使用`HttpOverrides`跳过证书认证。example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/60c46100ebabd66daba5221e4bc588f2a1efef5e)


```dart
import 'dart:io';  // ☆☆☆☆☆
import 'package:flutter/material.dart';
import 'package:fluro/fluro.dart';
import 'package:flutter_example/routers/routers.dart';
import 'package:flutter_example/routers/application.dart';

class MyHttpOverrides extends HttpOverrides{
  @override
  HttpClient createHttpClient(SecurityContext context){
    return super.createHttpClient(context)
      ..badCertificateCallback = (X509Certificate cert, String host, int port)=> true;
  }
}

void main() {
  HttpOverrides.global = MyHttpOverrides();  // ☆☆☆☆☆
  runApp(MyApp());
}
```
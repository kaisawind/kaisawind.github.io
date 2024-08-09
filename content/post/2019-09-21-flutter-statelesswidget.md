---
layout: post
title:  "StatelessWidget:flutter无状态组件"
date: 2019-09-21 14:47:47
categories: [flutter]
tags: [flutter]
excerpt_separator: <!--more-->
---
StatelessWidget:flutter无状态组件
<!--more-->
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 代码模板](#2-代码模板)

<!-- /code_chunk_output -->


## 1. 概述

<img src="https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue" />

`StatelessWidget`是flutter的无状态组件，是flutter的静态组件。
example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/3c85212ba1fb819c1fa2033f273bb8d1659bb7a2)

## 2. 代码模板

```dart
import 'package:flutter/material.dart';

class MyStatelessWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Stateless Widget'),
        ),
        body: ListView(),
    );
  }
}
```
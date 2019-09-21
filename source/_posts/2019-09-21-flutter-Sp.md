---
layout: post
title:  "shared_preferences:flutter数据存储"
date: 2019-9-21 20:49:46 +0800
categories: [flutter]
tags: [android, flutter, windows]
excerpt_separator: <!--more-->
---


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 设计概要](#2-设计概要)
  - [2.1 类设计](#21-类设计)
- [3. 代码模板](#3-代码模板)
  - [3.1 `SpKeys`](#31-spkeys)
  - [3.2 `SpUtils`](#32-sputils)
  - [3.3 `my_shared_preferences.dart`](#33-my_shared_preferencesdart)

<!-- /code_chunk_output -->


## 1. 概述

<img src="https://img.shields.io/pub/v/shared_preferences" />
<img src="https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue" />

`shared_preferences`是flutter的简单的本地存储类。
example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/d26ccf85cc04cde8c8eaab901f16244784921e92)

## 2. 设计概要

`shared_preferences`在手机中的存储位置`/data/data/com.kaisawind.flutter_example/shared_prefs/FlutterSharedPreferences.xml`

`shared_preferences`使用xml进行本地存储，所以不能存储复杂的结构。
```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="flutter.datetime">2019-09-21 13:34:54.468565</string>
</map>
```
### 2.1 类设计

创建`SpKeys`类管理存储的键，防止键重复。
创建`SpUtils`类管理存储，可以追加判断，日志等。

## 3. 代码模板

### 3.1 `SpKeys`
```dart
class SpKeys {
  static const datetime = 'datetime';
}
```

### 3.2 `SpUtils`
```dart
import 'dart:async';
import 'package:shared_preferences/shared_preferences.dart';

/// 用来做shared_preferences的存储
class SpUtil {
  static SpUtil _instance;
  static Future<SpUtil> get instance async {
    return await getInstance();
  }

  static SharedPreferences _spf;

  SpUtil._();

  Future _init() async {
    _spf = await SharedPreferences.getInstance();
  }

  static Future<SpUtil> getInstance() async {
    if (_instance == null) {
      _instance = new SpUtil._();
      await _instance._init();
    }
    return _instance;
  }

  static bool _beforeCheck() {
    if (_spf == null) {
      return true;
    }
    return false;
  }

  // 判断是否存在数据
  bool hasKey(String key) {
    Set keys = getKeys();
    return keys.contains(key);
  }

  Set<String> getKeys() {
    if (_beforeCheck()) return null;
    return _spf.getKeys();
  }

  get(String key) {
    if (_beforeCheck()) return null;
    return _spf.get(key);
  }

  getString(String key) {
    if (_beforeCheck()) return null;
    return _spf.getString(key);
  }

  Future<bool> setString(String key, String value) {
    if (_beforeCheck()) return null;
    return _spf.setString(key, value);
  }

  bool getBool(String key) {
    if (_beforeCheck()) return null;
    return _spf.getBool(key);
  }

  Future<bool> setBool(String key, bool value) {
    if (_beforeCheck()) return null;
    return _spf.setBool(key, value);
  }

  int getInt(String key) {
    if (_beforeCheck()) return null;
    return _spf.getInt(key);
  }

  Future<bool> setInt(String key, int value) {
    if (_beforeCheck()) return null;
    return _spf.setInt(key, value);
  }

  double getDouble(String key) {
    if (_beforeCheck()) return null;
    return _spf.getDouble(key);
  }

  Future<bool> setDouble(String key, double value) {
    if (_beforeCheck()) return null;
    return _spf.setDouble(key, value);
  }

  List<String> getStringList(String key) {
    return _spf.getStringList(key);
  }

  Future<bool> setStringList(String key, List<String> value) {
    if (_beforeCheck()) return null;
    return _spf.setStringList(key, value);
  }

  dynamic getDynamic(String key) {
    if (_beforeCheck()) return null;
    return _spf.get(key);
  }

  Future<bool> remove(String key) {
    if (_beforeCheck()) return null;
    return _spf.remove(key);
  }

  Future<bool> clear() {
    if (_beforeCheck()) return null;
    return _spf.clear();
  }
}

```

### 3.3 `my_shared_preferences.dart`
```dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter_example/resources/sp_keys.dart';

class MySharedPreferences extends StatefulWidget {
  @override
  _MySharedPreferencesState createState() => _MySharedPreferencesState();
}

class _MySharedPreferencesState extends State<MySharedPreferences> {
  String _date = '';

  _MySharedPreferencesState() : super();

  @override
  void initState() {
    super.initState();
    setDate();
  }

  void setDate() async {
    DateTime now = DateTime.now();
    SharedPreferences sp = await SharedPreferences.getInstance();
    await sp.setString(SpKeys.datetime, now.toString());
  }

  void updateDate() async {
    SharedPreferences sp = await SharedPreferences.getInstance();
    setState(() {
      _date = sp.getString(SpKeys.datetime);
    });
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
        title: Text('Shared Preferences'),
      ),
      body: ListView(
        children: <Widget>[
          RaisedButton(
            child: Text('setString'),
            onPressed: () {
              setDate();
            },
          ),
          RaisedButton(
            child: Text('getString'),
            onPressed: () {
              updateDate();
            },
          ),
          Container(
            child: Align(
              child: Text(_date),
            ),
          ),
        ],
      ),
    );
  }
}
```
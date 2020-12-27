---
layout: post
title:  "jcenter访问失败(翻墙)"
date: 2019-9-21 21:57:36
categories: [flutter]
tags: [android, flutter, windows]
excerpt_separator: <!--more-->
---


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 使用aliyun代理](#2-使用aliyun代理)

<!-- /code_chunk_output -->


## 1. 概述

<img src="https://img.shields.io/badge/flutter-v1.10.4--pre.53-blue" />

`jcenter`是一个由`bintray.com`维护的Maven仓库,国内访问有时候会出错。
example代码位置: [example](https://github.com/kaisawind/flutter_example/tree/07fe5a387678ae76058813ccd5320ac7bb829a63)

## 2. 使用aliyun代理

```gradle
buildscript {
    ext.kotlin_version = '1.3.50'
    repositories {
        // 阿里云 maven 地址
        maven{ url 'http://maven.aliyun.com/nexus/content/groups/public' }
        maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter' }
        google()
        // jcenter()
    }

    dependencies {
        classpath 'com.android.tools.build:gradle:3.5.0'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}

allprojects {
    repositories {
        // 阿里云 maven 地址
        maven{ url 'http://maven.aliyun.com/nexus/content/groups/public' }
        maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter' }
        google()
        // jcenter()
    }
}

rootProject.buildDir = '../build'
subprojects {
    project.buildDir = "${rootProject.buildDir}/${project.name}"
}
subprojects {
    project.evaluationDependsOn(':app')
}

task clean(type: Delete) {
    delete rootProject.buildDir
}

```
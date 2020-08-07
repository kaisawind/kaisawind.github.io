---
layout: post
title:  "java各版本比较"
date: 2020-02-25 17:20:04 +0800
categories: [编程语言,java]
tags: [java]
excerpt_separator: <!--more-->
---
java各版本比较
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 版本比较](#2-版本比较)
  - [2.1 Java SE、java EE、Java ME](#21-java-se-java-ee-java-me)
  - [2.2 JDK、J2SE、Java SE](#22-jdk-j2se-java-se)
  - [2.3 JDK、JRE、Java SE API](#23-jdk-jre-java-se-api)
  - [2.4 JDK、JRE、JRE、JIT](#24-jdk-jre-jre-jit)
  - [2.5 Java ME、Java SE、Java EE、Java Card](#25-java-me-java-se-java-ee-java-card)

<!-- /code_chunk_output -->


## 1. 概述

java是作为长时间流行的语言，在这过程中出现了很多版本，各版本之间又进行的新的派生，导致版本很多，对于初入java的人来说，会产生混乱。

## 2. 版本比较

### 2.1 Java SE、java EE、Java ME

* java SE（Java Platform，Standard Edition）
Java se 以前称为J2SE。它允许开发和部署在桌面、服务器、嵌入式环境和实时环境中使用的 Java 应用程序。Java SE是基础包，但是也包含了支持 Java Web 服务开发的类，并为 Java Platform，Enterprise Edition（Java EE）提供基础。

* Java EE（Java Platform，Enterprise Edition）
这个版本以前称为 J2EE。企业版本帮助开发和部署可移植、健壮、可伸缩且安全的服务器端 Java 应用程序。Java EE 是在 Java SE 的基础上构建的，它提供 Web 服务、组件模型、管理和通信 API，可以用来实现企业级的面向服务体系结构（service-oriented architecture，SOA）和 Web 2.0 应用程序。

* Java ME（Java Platform，Micro Edition）
这个版本以前称为 J2ME。Java ME 为在移动设备和嵌入式设备（比如手机、PDA、电视机顶盒和打印机）上运行的应用程序提供一个健壮且灵活的环境。Java ME 包括灵活的用户界面、健壮的安全模型、许多内置的网络协议以及对可以动态下载的连网和离线应用程序的丰富支持。基于 Java ME 规范的应用程序只需编写一次，就可以用于许多设备，而且可以利用每个设备的本机功能。

### 2.2 JDK、J2SE、Java SE

1998年12月8日，Sun公司发布了第二代Java平台（简称为Java2）的3个版本：
* J2ME（Java2 Micro Edition，Java2平台的微型版），应用于移动、无线及有限资源的环境；
* J2SE（Java 2 Standard Edition，Java 2平台的标准版），应用于桌面环境；
* J2EE（Java 2Enterprise Edition，Java 2平台的企业版），应用于基于Java的应用服务器。

2004年9月30日，J2SE1.5发布。为了表示该版本的重要性，J2SE 1.5更名为Java SE 5.0（内部版本号1.5.0）

2005年6月，Java SE 6正式发布。此时，Java的各种版本已经更名，已取消其中的数字2（如J2EE更名为JavaEE，J2SE更名为JavaSE，J2ME更名为JavaME）。

### 2.3 JDK、JRE、Java SE API

* JDK
JDK是支持Java开发的最小环境，包括Java程序设计语言，Java虚拟机和Java API类库三部分。

* JRE
JRE是支持Java运行的标准环境，包括Java API中Java SE API和Java虚拟机。

* Java SE API
https://www.oracle.com/cn/java/technologies/java-se-api-doc.html

![](/images/1034114-6b279de22a0c3648.png)

### 2.4 JDK、JRE、JRE、JIT

![](/images/1034114-b7a630ad5b512192.png)

### 2.5 Java ME、Java SE、Java EE、Java Card

* Java Card
支持一些java小程序（Applets），运行在小内存设备上的平台。

* Java ME(Micro Edition)
支持java程序运行在移动终端上的平台。对Java API有所精简，并加入了针对移动终端的支持，这个版本以前叫J2ME。

* Java SE(Standard Edition)
支持面向桌面级应用（如windows下的应用程序）的java平台，提供了完整的java核心API，这个版本以前叫J2SE。

* Java EE(Enterprise Edition)
支持使用多层架构的企业应用（如ERP、CRM应用）的java平台，除了提供Java SE API外，还对其做了大量的扩充（这些扩充一般以javax.*作为包名），并提供了相关的部署支持，这个版本以前叫J2EE。

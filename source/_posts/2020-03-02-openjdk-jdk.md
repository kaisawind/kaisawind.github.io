---
layout: post
title:  "OpenJDK与JDK比较"
date: 2020-03-02 09:40:04 +0800
categories: [编程语言,java]
tags: [java]
excerpt_separator: <!--more-->
---
OpenJDK与JDK比较
<!--more-->

## 1. 概述

OpenJDK与OracleJDK比较

## 2. 比较

OpenJDK与Oracle JDK绝大部分相同，OpenJDK是不包含部署功能，比如：Browser Plugin、Java Web Start、以及Java控制面板。

### 2.1 OracleJDK支持时间

Oracle Java SE Support Roadmap

| Release      | GA Date           | Premier Support Until | Extended Support Until | Sustaining Support |
|--------------|-------------------|-----------------------|------------------------|--------------------|
| 7            | July 2011         | July 2019             | July 2022*****         | Indefinite         |
| 8**          | March 2014        | March 2022            | December 2030          | Indefinite         |
| 9 (non‑LTS)  | September 2017    | March 2018            | Not Available          | Indefinite         |
| 10 (non‑LTS) | March 2018        | September 2018        | Not Available          | Indefinite         |
| 11 (LTS)     | September 2018    | September 2023        | September 2026         | Indefinite         |
| 12 (non‑LTS) | March 2019        | September 2019        | Not Available          | Indefinite         |
| 13 (non‑LTS) | September 2019    | March 2020            | Not Available          | Indefinite         |
| 14 (non‑LTS) | March 2020***     | September 2020        | Not Available          | Indefinite         |
| 15 (non‑LTS) | September 2020*** | March 2021            | Not Available          | Indefinite         |

### 2.2 开源协议对比

* OracleJDK
https://www.oracle.com/downloads/licenses/oracle-javase-license.html
自 2019 年 1 月起，Java SE 8 公开更新将不向没有商用许可证的业务、商用或生产用途提供
https://shop.oracle.com/apex/f?p=700:2:::NO:RP::

| 产品                                  | 港币                    | 人民币                  |
|---------------------------------------|-------------------------|-------------------------|
| Oracle Java SE Desktop Subscription   | HK$116.25-HK$232.50     | CNY$104.11-CNY$208.21   |
| Oracle Java SE Subscription           | HK$1,162.49-HK$2,328.00 | CNY$1041.04-CNY$2084.79 |
| Oracle Java Development Tools Support | HK$9,300.00             | CNY$8328.43             |

![](/images/jdksub.png)

* OpenJDK
https://openjdk.java.net/legal/gplv2+ce.html
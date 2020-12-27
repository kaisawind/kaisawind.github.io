---
layout: post
title:  "rabbitmq exchange理解"
date: 2019-10-11 16:20:05
categories: [消息队列,rabbitmq]
tags: [MQ, rabbitmq]
excerpt_separator: <!--more-->
---
rabbitmq exchange理解
<!--more-->


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. AMQP简介](#2-amqp简介)
- [3. Exchanges类型](#3-exchanges类型)
  - [3.1 Direct exchange](#31-direct-exchange)
  - [3.2 Fanout exchange](#32-fanout-exchange)
  - [3.3 Topic exchange](#33-topic-exchange)
  - [3.4 Headers exchange](#34-headers-exchange)
  - [3.5 Default Exchange](#35-default-exchange)

<!-- /code_chunk_output -->


## 1. 概述

理解rabbitmq各种关键字

## 2. AMQP简介

AMQP（Advanced Message Queuing Protocol，高级消息队列协议），使一致的客户端应用程序可以与一致的消息传递中间件代理进行通信。

![AMQP模型](/images/hello-world-example-routing.webp)


消息发送到路由(`exchanges`)中，路由通过绑定(`binding`)将消息分发到队列中(`queues`).然后，broker分发消息到消费者(`consumers`)订阅的队列中，或者消费者(`consumers`)从队列中按需拉取消息。

* 当发送消息时，有部分元数据会被broker使用，其他的对于broker是不透明的，会直接发送给应用。
* 消息确认概念，是为了应对网络不可靠，或者消息处理失败时的情况。当消息发送给消费者时，消费者会自动或者开发人员主动发送确认消息给broker。只有broker收到确认消息后，才会将消息从队列中删除。
* 当消息无法路由时，消息可能会返回给消费者，或者被破弃，或者被放到`dead letter queue`中(需要配置扩展)。
* 队列(queues)，路由(exchanges)，绑定(binding)被称为AMQP的实体。

## 3. Exchanges类型

### 3.1 Direct exchange

直接交换通过路由key，将消息分发到队列。单播路由最好的选择。

* 队列通过路由key(例如K)绑定到路由上。
* 当消息携带路由key(R)时，路由会将消息分发到路由key(K == R)的队列上。

![Direct exchange](/images/exchange-direct.webp)

### 3.2 Fanout exchange

扇出交换将消息路由到所有与其绑定的队列，路由key将会被忽略。如果将N个队列绑定到扇出交换，那么新消息发送到扇出交换时，会将消息发送到N个副本。扇出路由适合广播路由。

![Fanout exchange](/images/exchange-fanout.webp)

### 3.3 Topic exchange

主题路由将消息分发到通过路由key或者`pattern`绑定的队列上。主题路由适合广播路由。

![Topic exchange](/images/python-five.webp)

### 3.4 Headers exchange

标头交换旨在用于在多个属性上路由，这些属性比路由键更容易表示为消息标头。 标头交换忽略路由键属性。 相反，用于路由的属性取自headers属性。 如果标头的值等于绑定时指定的值，则认为消息匹配。

### 3.5 Default Exchange

默认交换是一种特殊的 Direct Exchange。当你手动创建一个队列时，后台会自动将这个队列绑定到一个名称为空的 Direct Exchange 上，绑定 RoutingKey 与队列名称相同。有了这个默认的交换机和绑定，使我们只关心队列这一层即可，这个比较适合做一些简单的应用。

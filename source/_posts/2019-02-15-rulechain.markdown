---
layout: post
title:  "规则引擎概要"
date: 2019-2-15 15:59:07
categories: [other]
excerpt_separator: <!--more-->
---

## 1.什么是ThingsBoard规则引擎？

Rule Engine是一个易于使用的框架，用于构建基于事件的工作流。

- **Message** - 设备的传入数据，设备生命周期事件，REST API事件，RPC请求等
- **Rule Node** - 对传入的消息进行得操作。
- **Rule Chain** - 节点相互连接的规则链

<!--more-->

## 2.能够解决哪些问题？

- 存储数据库是，对数据进行验证和修改

- 聚合多个设备的信息

- 创建、更新、清除告警

- 设备在线，离线时创建告警

- 对设备的某些阈值进行监控

- 触发对外部系统的api调用

- 达到某种条件时，发送邮件或短信。

- 让用户选择对事件的处理

- 触发对rpc的调用

- 与Kafka，Spark，AWS服务等外部管道集成。

## 3.节点

### 3.1 滤波器

- Check Relation Filter Node
- Message Type Filter Node
- Message Type Switch Node
- Originator Type Filter Node
- Originator Type Switch Node
- Script Filter Node
- Switch Node

### 3.2 属性集

- Customer attributes
- Device attributes
- Originator attributes
- Originator fields
- Related attributes
- Tenant attributes
- Originator telemetry

### 3.3 变换

- Change originator
- Script Transformation Node
- To Email Node

### 3.4 动作

- Create Alarm Node
- Clear Alarm Node
- Delay Node
- Generator Node
- Log Node
- RPC Call Reply Node
- RPC Call Request Node
- Save Attributes Node
- Save Timeseries Node
- Assign To Customer Node
- Unassign From Customer Node
- Create Relation Node
- Delete Relation Node

### 3.5 外部

- AWS SNS Node
- AWS SQS Node
- Kafka Node
- MQTT Node
- RabbitMQ Node
- REST API Call Node
- Send Email Node
- Twilio SMS Node

### 3.6 规则链
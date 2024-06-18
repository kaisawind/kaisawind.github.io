---
layout: post
title:  "rabbitmq queue(队列)参数说明"
date: 2019-10-12 09:44:17
categories: [消息队列,rabbitmq]
tags: [tools]
excerpt_separator: <!--more-->
---
rabbitmq queue(队列)参数说明
<!--more-->

![rabbitmq queue](/images/微信截图_20191012103328.png)

| 参数      | 描述       | 说明                                                                                                                                                                                                                                 |
|-----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| queue     | 队列名称   | ---                                                                                                                                                                                                                                  |
| durable   | 是否持久化 | 队列的声明默认是存放到内存中的，如果rabbitmq重启会丢失，如果想重启之后还存在就要使队列持久化，保存到Erlang自带的Mnesia数据库中，当rabbitmq重启之后会读取该数据库                                                                         |
| exclusive | 是否排外   | 1.当连接关闭时connection.close()该队列是否会自动删除；<br>2.该队列是否是私有的private，如果不是排外的，可以使用两个消费者都访问同一个队列，没有任何问题，如果是排外的，会对当前队列加锁，其他通道channel是不能访问的，如果强制访问会报异常 |
| autoDelete                                         | 是否自动删除           | 1.当Queue中的 autoDelete 属性被设置为true时，那么，当消息接收着宕机，关闭后，消息队列则会删除，消息发送者一直发送消息，当消息接收者重新启动恢复正常后，会接收最新的消息，而宕机期间的消息则会丢失 <br>2.当Quere中的 autoDelete 属性被设置为false时，那么，当消息接收者宕机，关闭后，消息队列不会删除，消息发送者一直发送消息，当消息接收者重新启动恢复正常后，会接收包括宕机期间的消息。|
| Message TTL(x-message-ttl)                         | 消息的生存周期         | 设置队列中的所有消息的生存周期(统一为整个队列的所有消息设置生命周期), 也可以在发布消息的时候单独为某个消息指定剩余生存时间,单位毫秒, 类似于redis中的ttl，生存时间到了，消息会被从队里中删除，注意是消息被删除，而不是队列被删除， 特性Features=TTL |
| Auto Expire(x-expires)                             | 队列定时删除           | 当队列在指定的时间没有被访问(consume, basicGet, queueDeclare…)就会被删除,Features=Exp                                                                                                                                                         |
| Max Length(x-max-length)                           | 队列的消息的最大值长度 | 超过指定长度将会把最早的几条删除掉， 类似于mongodb中的固定集合，例如保存最新的100条消息, Feature=Lim                                                                                                                                            |
| Max Length Bytes(x-max-length-bytes)               | 队列最大占用的空间大小 | 一般受限于内存、磁盘的大小, Features=Lim B                                                                                                                                                                                                     |
| Dead letter exchange(x-dead-letter-exchange)       | ---                    | 当队列消息长度大于最大长度、或者过期的等，将从队列中删除的消息推送到指定的交换机中去而不是丢弃掉,Features=DLX                                                                                                                                   |
| Dead letter routing key(x-dead-letter-routing-key) |                        | 将删除的消息推送到指定交换机的指定路由键的队列中去, Feature=DLK                                                                                                                                                                               |
| Maximum priority(x-max-priority)                   | 优先级队列             | 声明队列时先定义最大优先级值(定义最大值一般不要太大)，在发布消息的时候指定该消息的优先级， 优先级更高（数值更大的）的消息先被消费,                                                                                                                |
| Lazy mode(x-queue-mode=lazy)                       | 消息放到磁盘           | 先将消息保存到磁盘上，不放在内存中，当消费者开始消费的时候才加载到内存中                                                                                                                                                                        |


* autoDelete: 自动删除
    >An auto-delete queue will be deleted when its last consumer is cancelled (e.g. using the basic.cancel in AMQP 0-9-1) or gone (closed channel or connection, or >lost TCP connection with the server).
    >
    >当最后一个订阅者被取消，连接丢失，这个队列会被删除

* exclusive: 排外
    >Exclusive queues are deleted when their declaring connection is closed or gone (e.g. due to underlying TCP connection loss). They therefore are only suitable >for client-specific transient state.
    >
    >当连接被关闭或者丢失，队列会被删除。

* autoDelete和exclusive比较
    1. exclusive自动删除针对的是connection而不是consumer
    2. exclusive的队列只能有一个consumer
    3. autoDelete自动删除针对的是consumer
    4. autoDelete和exclusive可以同时生效
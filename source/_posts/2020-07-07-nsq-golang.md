---
layout: post
title:  "go-nsq简单教程"
date: 2020-07-07 14:38:42 +0800
categories: [消息队列,nsq]
tags: [MQ, nsq, golang]
excerpt_separator: <!--more-->
---
go-nsq简单教程
<!--more-->

## 1. 概述

`go-nsq`是nsq的GO语言客户端。

## 2. 示例

### 2.1 单nsqd

生产者Producer
```go
package main

import (
	"os"
	"os/signal"
	"time"

	"github.com/nsqio/go-nsq"
	"github.com/sirupsen/logrus"
)

func main() {
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt)

	producer, err := nsq.NewProducer("192.168.1.168:4150", nsq.NewConfig())
	if err != nil {
		logrus.WithError(err).Errorln("new producer error")
		return
	}
	defer producer.Stop()
	err = producer.Ping()
	if err != nil {
		logrus.WithError(err).Errorln("producer ping err")
		return
	}
Loop:
	for {
		select {
		case <-c:
			break Loop
		case <-time.Tick(1 * time.Second):
			err = producer.Publish("test", []byte("hello world"))
			if err != nil {
				logrus.WithError(err).Errorln("producer publish error")
				break Loop
			}
			logrus.Infoln("publish ok")
		}
	}
}
```

消费者Consumer
```go
package main

import (
	"github.com/nsqio/go-nsq"
	"github.com/sirupsen/logrus"
)

// MyHandler consumer handler
type MyHandler struct {
	Title string
}

// HandleMessage interface for consumer
func (h *MyHandler) HandleMessage(message *nsq.Message) (err error) {
	logrus.Infoln(message)
	return
}

func main() {
	consumer, err := nsq.NewConsumer("test", "consumer1", nsq.NewConfig())
	if err != nil {
		logrus.WithError(err).Errorln("new consumer error")
		return
	}
	defer consumer.Stop()
	consumer.AddHandler(&MyHandler{Title: "test consumer"})
	err = consumer.ConnectToNSQD("192.168.1.168:4150")
	if err != nil {
		logrus.WithError(err).Errorln("connect to nsq lookup error")
		return
	}
	select {}
}
```

### 2.2 单nsqlookupd

生产者Producer(没变化)
```go
package main

import (
	"os"
	"os/signal"
	"time"

	"github.com/nsqio/go-nsq"
	"github.com/sirupsen/logrus"
)

func main() {
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt)

	producer, err := nsq.NewProducer("192.168.1.168:4150", nsq.NewConfig())
	if err != nil {
		logrus.WithError(err).Errorln("new producer error")
		return
	}
	defer producer.Stop()
	err = producer.Ping()
	if err != nil {
		logrus.WithError(err).Errorln("producer ping err")
		return
	}
Loop:
	for {
		select {
		case <-c:
			break Loop
		case <-time.Tick(1 * time.Second):
			err = producer.Publish("test", []byte("hello world"))
			if err != nil {
				logrus.WithError(err).Errorln("producer publish error")
				break Loop
			}
			logrus.Infoln("publish ok")
		}
	}
}
```

消费者Consumer
```go
package main

import (
	"github.com/nsqio/go-nsq"
	"github.com/sirupsen/logrus"
)

// MyHandler consumer handler
type MyHandler struct {
	Title string
}

// HandleMessage interface for consumer
func (h *MyHandler) HandleMessage(message *nsq.Message) (err error) {
	logrus.Infoln(message)
	return
}

func main() {
	consumer, err := nsq.NewConsumer("test", "consumer1", nsq.NewConfig())
	if err != nil {
		logrus.WithError(err).Errorln("new consumer error")
		return
	}
	defer consumer.Stop()
	consumer.AddHandler(&MyHandler{Title: "test consumer"})
	err = consumer.ConnectToNSQLookupd("192.168.1.168:4161") // different
	if err != nil {
		logrus.WithError(err).Errorln("connect to nsq lookup error")
		return
	}
	select {}
}
```
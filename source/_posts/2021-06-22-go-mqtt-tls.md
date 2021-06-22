---
layout: post
title:  "Mqtt使用tls证书"
date: 2021-06-22 10:19:12
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
Mqtt使用tls证书
<!--more-->

## 1. 概述
MQTT是物联网常用协议，在客户端和服务端进行交互时，通常使用MQTTS(TLS)对数据进行加密。

## 2. 示例

```go
    // Read in the cert file
    rootCrt, err := ioutil.ReadFile(ca)
    if err != nil {
        logrus.WithError(err).Fatalln("root crt file read error")
    }
    rootCAs := x509.NewCertPool()
    // Append our cert to the system pool
    if ok := rootCAs.AppendCertsFromPEM(rootCrt); !ok {
        logrus.Fatalln("root crt append error")
    }
    clientCA, err := tls.LoadX509KeyPair(crt, key)
    if err != nil {
        logrus.WithError(err).Fatalln("client ca file read error")
    }
    // TLS
    t = &tls.Config{
        InsecureSkipVerify: true,
        RootCAs:            rootCAs,
        Certificates: []tls.Certificate{
            clientCA,
        },
    }
    opts.SetTLSConfig(t)
```
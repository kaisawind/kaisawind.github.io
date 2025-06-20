---
layout: post
title: 'openssl证书生成、验证和测试'
date: 2025-05-16 10:38:55
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
openssl证书生成、验证和测试
<!--more-->


### 生成证书

```bash
# root certs
openssl genrsa -out root.key 2048
openssl req -new -key root.key -out root.csr -subj "/C=CN/ST=LiaoNing/L=DaLian/O=kaisawind/OU=wind.kaisa/CN=www.kaisawind.com/emailAddress=wind.kaisa@gmail.com"
openssl x509 -req -sha256 -days 3650 -in root.csr -signkey root.key -out root.crt

# server certs
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/C=CN/ST=LiaoNing/L=DaLian/O=kaisawind/OU=wind.kaisa/CN=server.kaisawind.com/emailAddress=wind.kaisa@gmail.com"
openssl x509 -req -sha256 -days 3650 -in server.csr -CAkey ./root.key -CA ./root.crt -CAserial ./root.srl -out server.crt

# client certs
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/C=CN/ST=LiaoNing/L=DaLian/O=kaisawind/OU=wind.kaisa/CN=client.kaisawind.com/emailAddress=wind.kaisa@gmail.com"
openssl x509 -req -sha256 -days 3650 -in client.csr -CAkey ./root.key -CA ./root.crt -CAserial ./root.srl -out client.crt

# verify certs
openssl verify -CAfile ./root.crt ./server.crt
openssl verify -CAfile ./root.crt ./client.crt

# sign message
openssl dgst -sha256 -sign client.key -out signature.txt client.crt
openssl x509 -in client.crt -pubkey -noout > client.pubkey
#openssl rsa -in client.key -pubout -out client.pubkey
# verify message
openssl dgst -sha256 -verify client.pubkey -signature signature.txt client.crt
```

### 证书测试
```bash
# 启动服务端
openssl s_server -accept 8443 -cert server.crt -key server.key -www -verify 4 -Verify 5 -debug

# 客户端连接测试
openssl s_client -connect localhost:8443 -cert client.crt -key client.key -CAfile root.crt -debug
```

测试结果
```bash
Start Time: 1747362670
Timeout   : 7200 (sec)
Verify return code: 0 (ok)
Extended master secret: no
Max Early Data: 0
```
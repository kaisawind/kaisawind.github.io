---
layout: post
title:  "nginx代理基本配置"
date: 2020-12-14 10:46:23
categories: [nginx]
tags: [linux]
excerpt_separator: <!--more-->
---
nginx代理基本配置
<!--more-->


## 1. 不同后缀区别
### 1.1. proxy_pass带后缀`/`
```nginx
location /proxy/ {
    proxy_pass http://127.0.0.1/;
}
```
->: http://127.0.0.1/test.html

### 1.2. proxy_pass不带后缀`/`
```nginx
location /proxy/ {
    proxy_pass http://127.0.0.1;
}
```
->: http://127.0.0.1/proxy/test.html

### 1.3. proxy_pass带后缀`/aaa/`
```nginx
location /proxy/ {
    proxy_pass http://127.0.0.1/aaa/;
}
```
->: http://127.0.0.1/aaa/test.html

### 1.4. proxy_pass不带后缀`/aaa`
```nginx
location /proxy/ {
    proxy_pass http://127.0.0.1/aaa;
}
```
->: http://127.0.0.1/aaatest.html

## 2. location匹配

|符号|说明|
|---|---|
|= |严格匹配。如果这个查询匹配，那么将停止搜索并立即处理此请求。|
|~ |为区分大小写匹配(可用正则表达式)|
|!~|为区分大小写不匹配|
|~* |为不区分大小写匹配(可用正则表达式)|
|!~*|为不区分大小写不匹配|
|^~ |如果把这个前缀用于一个常规字符串,那么告诉nginx 如果路径匹配那么不测试正则表达式。|

### 2.1. 匹配开头

```nginx
location ^~ /p_w_picpaths/ {
    # 匹配任何已 /p_w_picpaths/ 开头的任何查询并且停止搜索。任何正则表达式将不会被测试。
}
```

### 2.2. 匹配结尾

```nginx
location ~*.(gif|jpg|jpeg)$ {
    # 匹配任何已 gif、jpg 或 jpeg 结尾的请求。
}
```
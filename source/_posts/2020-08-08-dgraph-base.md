---
layout: post
title:  "dgraph增删改查"
date: 2020-08-08 00:32:04 +0800
categories: [数据库, dgraph]
tags: [dgraph]
excerpt_separator: <!--more-->
---
dgraph增删改查
<!--more-->

## 1. 添加一条
```json
{
  "set": [{
    "uid": "_:id",
    "name": "Alice",
    "age": 13,
    "dgraph.type": "User",
  }]
}
```

## 2. 添加多条
```json
{
  "set": [
    {
      "uid": "_:id",
      "name": "Alice",
      "age": 13,
      "dgraph.type": "User",
    },
    {
      "uid": "_:id",
      "name": "Bob",
      "age": 13,
      "dgraph.type": "User",
    },
  ]
}
```

## 3. 查询
```js
{
  users(func: type(User)) @filter(eq(username, "alice")) {
    uid
    expand(_all_)
  }
}
```

## 4. 删除

```js
{
    "delete": [
        "uid": "0x1345"
    ]
}
```

## 5. 分页

```js
{
    ids as users(func: type(User), first:10, offset:0) {
      uid
      expand(_all_)
    }
    
    metrics(func:uid(ids)) {
      count: count(uid)
    }
  }
```
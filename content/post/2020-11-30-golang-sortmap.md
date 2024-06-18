---
layout: post
title:  "golang的map排序方法"
date: 2020-11-30 17:50:12
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang的map排序方法
<!--more-->

## 1. 概述
go语言中map是无序的，也就是说，当第一取数据时，key1在第一个，但当第二次取数据时，key1可能就不在第一个的位置了。

## 2. 字典排序

使用`sort.Strings()`函数对keys进行按字典排序。
最终输出结果是排序之后的json。
```go
// SortDataMap Map排序
func SortDataMap(data map[string]interface{}) (ret string) {
	var keys []string
	for k := range data {
		keys = append(keys, k)
	}
	if len(keys) == 0 {
		return
	}
	sort.Strings(keys)
	var values []string
	for _, key := range keys {
		values = append(values, fmt.Sprintf(`"%s":%v`, key, data[key]))
	}
	ret = strings.Join(values, ",")
	ret = "{" + ret + "}"
	return
}
```
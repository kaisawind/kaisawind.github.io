---
layout: post
title:  "golang设计模式(工厂方法)"
date: 2019-12-10 15:58:00 
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang设计模式(工厂方法)
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 代码](#2-代码)

<!-- /code_chunk_output -->


## 1. 概述

* 意图：
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

* 主要解决：
主要解决接口选择的问题。

* 何时使用：
系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。

* 如何解决：
在一个产品族里面，定义多个产品。

* 关键代码：
在一个工厂里聚合多个同类产品。

* 应用实例：
工作了，为了参加一些聚会，肯定有两套或多套衣服吧，比如说有商务装（成套，一系列具体产品）、时尚装（成套，一系列具体产品），甚至对于一个家庭来说，可能有商务女装、商务男装、时尚女装、时尚男装，这些也都是成套的，即一系列具体产品。假设一种情况（现实中是不存在的，要不然，没法进入共产主义了，但有利于说明抽象工厂模式），在您的家中，某一个衣柜（具体工厂）只能存放某一种这样的衣服（成套，一系列具体产品），每次拿这种成套的衣服时也自然要从这个衣柜中取出了。用 OOP 的思想去理解，所有的衣柜（具体工厂）都是衣柜类的（抽象工厂）某一个，而每一件成套的衣服又包括具体的上衣（某一具体产品），裤子（某一具体产品），这些具体的上衣其实也都是上衣（抽象产品），具体的裤子也都是裤子（另一个抽象产品）。

* 优点：
当一个产品族中的多个对象被设计成一起工作时，它能保证客户端始终只使用同一个产品族中的对象。

* 缺点：
产品族扩展非常困难，要增加一个系列的某一产品，既要在抽象的 Creator 里加代码，又要在具体的里面加代码。

* 使用场景： 
1、QQ 换皮肤，一整套一起换。 
2、生成不同操作系统的程序。

## 2. 代码

```go
package main

import (
	"fmt"
)

// Color 颜色接口类
type Color interface {
	Name() string
}

type Create interface {
	Color() Color
}

type RedCreate struct {
}

func (r *RedCreate) Color() Color {
	return Red{}
}

// Red 红色
type Red struct {
}

// Name 输出颜色名
func (Red) Name() string {
	fmt.Println("Red")
	return "Red"
}

type GreenCreate struct {
}

func (r *GreenCreate) Color() Color {
	return Green{}
}

// Green 绿色
type Green struct {
}

// Name 输出颜色名
func (Green) Name() string {
	fmt.Println("Green")
	return "Green"
}

func main() {
	var color Color
	var create Create

	create = &RedCreate{}
	color = create.Color()
	color.Name()

	create = &GreenCreate{}
	color = create.Color()
	color.Name()
}

```
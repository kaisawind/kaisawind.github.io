---
layout: post
title:  "golang反射三定律"
date: 2020-09-25 09:45:12 +0800
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
golang反射三定律
<!--more-->

## 1. 概述
golang的反射能够获取对象属性列表，对象函数列表，函数参数列表，并能够给它们尽心赋值和调用。

## 2. 类型理解
GO是静态类型的语言。每个变量都有一个静态类型，并且必须在编译之前就已经固定住。


### 2.1. 静态类型
```go
type MyInt int

var i int
var j MyInt
```
如果两个变量具有不同的类型，即使底层类型相同，在不经过转换是不能进行相互赋值的。

### 2.2. interface类型
`interface`类型能够保存任何具体类型(非interface)的值。例如:
```go
// Reader is the interface that wraps the basic Read method.
type Reader interface {
    Read(p []byte) (n int, err error)
}

// Writer is the interface that wraps the basic Write method.
type Writer interface {
    Write(p []byte) (n int, err error)
}
```
任何实现Read(Write)方法的类型都是io.Reader(io.Writer)的实现。io.Reader可以保存具有Read方法的任何值。
```go
var r io.Reader
r = os.Stdin
r = bufio.NewReader(r)
r = new(bytes.Buffer)
// and so on
```
注意:r的类型始终是io.Reader。

### 2.3. interface{}
空接口`interface{}`可以为任何值。虽然存储值的类型可能会变，单它也是静态类型。


### 2.4 变量的表示
* 变量包含两部分:(value, type)
* type包含: static type, concrete type
  static type: int, string, 
  concrete type: runtime识别的类型
* 类型断言是否成功，取决于concrete type

## 3. 反射定律

### 3.1. 第一定律
**反射从接口值到反射对象**
```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	fmt.Println("type:", reflect.TypeOf(x))
	fmt.Println("value:", reflect.ValueOf(x).String())
	v := reflect.ValueOf(x)
	fmt.Println("type:", v.Type())
	fmt.Println("kind is float64:", v.Kind() == reflect.Float64)
	fmt.Println("value:", v.Float())
}
```
output:
```bash
type: float64
value: <float64 Value>
type: float64
kind is float64: true
value: 3.4
```

### 3.2. 第二定律
**反射从反射对象到接口值**
```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	fmt.Println("type:", reflect.TypeOf(x))
	fmt.Println("value:", reflect.ValueOf(x).String())
	v := reflect.ValueOf(x)
	fmt.Println("type:", v.Type())
	fmt.Println("kind is float64:", v.Kind() == reflect.Float64)
	fmt.Println("value:", v.Float())

	fmt.Println("-----------")
	fmt.Printf("value is %7.1e\n", v.Interface())
}
```
output:
```bash
type: float64
value: <float64 Value>
type: float64
kind is float64: true
value: 3.4
-----------
value is 3.4e+00
```

### 3.3. 第三定律
**要修改反射对象，该值必须可设置**
`v := reflect.ValueOf(x)`是获取x的副本，所以无法直接通过v对x赋值。
```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	v := reflect.ValueOf(x)
	fmt.Println("type of v:", v.Type())
	fmt.Println("settability of v:", v.CanSet())
	p := reflect.ValueOf(&x)
	fmt.Println("type of p:", p.Type())
	fmt.Println("settability of p.Elem:", p.Elem().CanSet())
}
```
output:
```bash
type of v: float64
settability of v: false
type of p: *float64
settability of p.Elem: true
```



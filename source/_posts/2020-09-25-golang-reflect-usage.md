---
layout: post
title:  "golang反射的使用"
date: 2020-09-25 09:45:12 +0800
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
golang反射的使用
<!--more-->

## 1. 概述
golang的反射能够获取对象属性列表，对象函数列表，函数参数列表，并能够给它们尽心赋值和调用。

## 2. 对象属性列表

**使用Field函数时，value必须是对象**
`NumField()`获取属性的个数，
`Field(i)`遍历所有属性

```go
package main

import (
	"context"
	"fmt"
	"reflect"
)

type Struct struct {
	IntField    int
	StringField string
	ArrayField  []string
	MapField    map[string]string
	CtxField    context.Context
	PtrField    *Struct
}

func (s *Struct) Child() *Struct {
	return s.PtrField
}

func main() {
	srt := Struct{
		IntField:    1,
		StringField: "123",
		ArrayField:  []string{"1", "2", "3"},
		MapField:    map[string]string{"1": "1", "2": "2", "3": "3"},
		CtxField:    context.TODO(),
		PtrField:    &Struct{},
	}

	v := reflect.ValueOf(srt)
	fmt.Println(v.Kind())
	num := v.NumField()
	for i := 0; i < num; i++ {
		fmt.Println(v.Field(i).Type(), v.Field(i))
	}
}
```
output:
```bash
struct
int 1
string 123
[]string [1 2 3]
map[string]string map[1:1 2:2 3:3]
context.Context context.TODO
*main.Struct &{0  [] map[] <nil> <nil>}
```

## 3. 对象函数列表

**指针对象和对象的函数列表不同**
```go
func (s *Struct) Child() *Struct {
	return s.PtrField
}

func (s Struct) Child2() *Struct {
	return s.PtrField
}
```

指针对象的函数列表包含对象的函数列表
```go
// 获取对象函数列表
v := reflect.ValueOf(srt)
num := v.NumMethod()
fmt.Println("struct method", num)
for i := 0; i < num; i++ {
    fmt.Println(v.Type().Method(i).Name, v.Method(i))
}

// 获取指针函数列表
v = reflect.ValueOf(&srt)
num = v.NumMethod()
fmt.Println("ptr method", num)
for i := 0; i < num; i++ {
    fmt.Println(v.Type().Method(i).Name, v.Method(i))
}
```
output:
```bash
struct method 1
Child2 0x4a8780
ptr method 2
Child 0x4a8780
Child2 0x4a8780
```

## 4. 函数参数列表

```go
// SetContext static function will not change CtxField
func (s Struct) SetContext(ctx context.Context) {
	s.CtxField = ctx
}
func main() {
	srt := Struct{}

	v := reflect.ValueOf(srt)
	fn := v.MethodByName("SetContext")
	num := fn.Type().NumIn()
	for i := 0; i < num; i++ {
		fmt.Println(fn.Type().In(i).String())
	}
}
```

output:
```bash
context.Context
```

## 5. 函数调用

```go
func (s *Struct) SetIntField(val int) {
	s.IntField = val
}
func main() {
	srt := &Struct{}
	v := reflect.ValueOf(srt)
	fn := v.MethodByName("SetIntField")
	fn.Call([]reflect.Value{reflect.ValueOf(10)})

	fmt.Println(srt)
	srt.SetIntField(11)
	fmt.Println(srt)
}
```

output:
```bash
&{10  [] map[] <nil> <nil>}
&{11  [] map[] <nil> <nil>}
```

## 6. 函数入参是结构体指针

```go
func (s *Struct) SetPtrField(ptr *Struct) {
	s.PtrField = ptr
}
var val = Struct{
	IntField:    11,
	StringField: "StringField",
	ArrayField:  []string{"1", "2", "3"},
	MapField:    map[string]string{"1": "1", "2": "2"},
}
func main() {
	jsonData, err := json.Marshal(val)
	if err != nil {
		return
	}
	fmt.Println(string(jsonData))
	srt := &Struct{}
	v := reflect.ValueOf(srt)
	fn := v.MethodByName("SetPtrField")
	arg := fn.Type().In(0)
	ptr := reflect.New(arg)     // **Struct
	instance := ptr.Interface() // *Struct
	err = json.Unmarshal(jsonData, instance)
	if err != nil {
		return
	}
	fn.Call([]reflect.Value{ptr.Elem()})

	fmt.Println(srt.PtrField)
}
```

output:
```bash
{"IntField":11,"StringField":"StringField","ArrayField":["1","2","3"],"MapField":{"1":"1","2":"2"},"CtxField":null,"PtrField":null}
&{11 StringField [1 2 3] map[1:1 2:2] <nil> <nil>}
```

## 7. 修改函数入参的值

```go
func (s *Struct) SetPtrField(ptr *Struct) {
	s.PtrField = ptr
}
var val = Struct{
	IntField:    11,
	StringField: "StringField",
	ArrayField:  []string{"1", "2", "3"},
	MapField:    map[string]string{"1": "1", "2": "2"},
}
func main() {
	jsonData, err := json.Marshal(val)
	if err != nil {
		return
	}
	fmt.Println(string(jsonData))
	srt := &Struct{}
	v := reflect.ValueOf(srt)
	fn := v.MethodByName("SetPtrField")
	arg := fn.Type().In(0)
	ptr := reflect.New(arg)     // **Struct
	instance := ptr.Interface() // *Struct
	err = json.Unmarshal(jsonData, instance)
	if err != nil {
		return
	}
	ptr = ptr.Elem() // *Struct
	ptr = ptr.Elem() // Struct
	if ptr.CanSet() {
		f := ptr.FieldByName("IntField")
		if f.CanSet() {
			f.Set(reflect.ValueOf(1000))
		}
	}
	fn.Call([]reflect.Value{ptr.Addr()})

	fmt.Println(srt.PtrField)
}
```

output:
```bash
{"IntField":11,"StringField":"StringField","ArrayField":["1","2","3"],"MapField":{"1":"1","2":"2"},"CtxField":null,"PtrField":null}
&{1000 StringField [1 2 3] map[1:1 2:2] <nil> <nil>}
```

## 8. 函数返回值

```go
func main() {
	srt := &Struct{
		PtrField: &val,
	}
	v := reflect.ValueOf(srt)
	fn := v.MethodByName("Child")
	values := fn.Call([]reflect.Value{})
	if len(values) == 0 {
		return
	}
	value := values[0]
	ptr := value.Interface().(*Struct)
	fmt.Println(ptr)
}
```

output:
```bash
&{11 StringField [1 2 3] map[1:1 2:2] <nil> <nil>}
```
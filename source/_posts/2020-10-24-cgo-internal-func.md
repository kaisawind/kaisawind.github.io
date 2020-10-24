---
layout: post
title:  "cgo中内置函数"
date: 2020-10-24 19:31:12 +0800
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
cgo中内置函数
<!--more-->

## 1. 概述

cgo中有以下内置函数
```go
// Go string to C string
// The C string is allocated in the C heap using malloc.
// It is the caller's responsibility to arrange for it to be
// freed, such as by calling C.free (be sure to include stdlib.h
// if C.free is needed).
func C.CString(string) *C.char

// Go []byte slice to C array
// The C array is allocated in the C heap using malloc.
// It is the caller's responsibility to arrange for it to be
// freed, such as by calling C.free (be sure to include stdlib.h
// if C.free is needed).
func C.CBytes([]byte) unsafe.Pointer

// C string to Go string
func C.GoString(*C.char) string

// C data with explicit length to Go string
func C.GoStringN(*C.char, C.int) string

// C data with explicit length to Go []byte
func C.GoBytes(unsafe.Pointer, C.int) []byte
```

## 2. 示例

**CString**
注意：必须释放内存
由于使用了`free`函数，所以需要`#include <stdlib.h>`头文件。
```go
sDVRIP := C.CString(ip)
defer C.free(unsafe.Pointer(sDVRIP))
```

**CBytes**
注意：必须释放内存
由于使用了`free`函数，所以需要`#include <stdlib.h>`头文件。
```go
sAddress := C.CBytes(address)
defer C.free(sAddress)
```

**GoString**
指针时
```go
// char* ip = "192.168.1.168"
sAddress := C.GoString(ip)
```
数组时
```go
// char ip[20] = "192.168.1.168"
sAddress := C.GoString(&ip[0])
```
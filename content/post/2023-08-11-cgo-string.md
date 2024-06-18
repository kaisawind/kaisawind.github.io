---
layout: post
title:  "golang cgo字符串转换"
date: 2023-08-11 10:28:59
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang cgo字符床转换
<!--more-->

## 1. string to char*

```go
ptChar := C.CString("hello world")
```

## 2. string to const char*

```c
#include <stdio.h>

void Hello(const char* s) {
    printf("%s\n", s);
}
```

```go
C.Hello(C.CString("Hello, World\n"))
```

## 3. []string to char**

```go
authArray := []*C.char{}
for _, v := range in.AuthArray {
    cs := C.CString(v)
    authArray = append(authArray, cs)
}
defer func() {
	for _, v := range authArray {
		C.free(unsafe.Pointer(v))
	}
}()

ptAuthArray := &authArray[0]
```
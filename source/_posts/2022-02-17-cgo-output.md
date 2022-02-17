---
layout: post
title:  "golang cgo出参"
date: 2022-02-17 10:59:54
categories: [编程语言,golang]
tags: [golang, windows, linux, cgo]
excerpt_separator: <!--more-->
---
golang cgo出参
<!--more-->

```go
//export OutputParameter
func OutputParameter(in0 *C.char, out **C.char) C.int {
    str := C.GoString(in0)
    *out = C.CString(str)
    return 0
}
```
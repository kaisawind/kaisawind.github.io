---
layout: post
title:  "golang cgo出参"
date: 2022-02-17 10:59:54
lastmod: 2026-03-19
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang cgo出参
<!--more-->

## 基本概念

在Go和C之间传递指针参数时，需要注意内存管理。Go的垃圾回收器不会管理C内存，因此需要手动管理。

## 基本示例

### 字符串输出参数

```go
package main

/*
#include <stdlib.h>
#include <string.h>
*/
import "C"
import "unsafe"

//export OutputParameter
func OutputParameter(in0 *C.char, out **C.char) C.int {
    str := C.GoString(in0)
    *out = C.CString(str)
    return 0
}

func main() {}
```

### 使用示例（C端）

```c
#include <stdio.h>
#include <stdlib.h>
#include "output.h"

int main() {
    char *output = NULL;
    OutputParameter("hello", &output);
    printf("Output: %s\n", output);
    free(output);  // 记得释放内存
    return 0;
}
```

## 多种输出参数类型

### 1. 整数输出参数

```go
//export GetInt
func GetInt(out *C.int) C.int {
    *out = 42
    return 0  // 返回值表示错误码
}
```

### 2. 数组输出参数

```go
//export GetArray
func GetArray(out **C.int, size *C.int) C.int {
    arr := []C.int{1, 2, 3, 4, 5}
    *size = C.int(len(arr))
    
    // 分配C内存
    *out = (*C.int)(C.malloc(C.size_t(len(arr) * int(unsafe.Sizeof(C.int(0))))))
    
    // 复制数据
    outSlice := unsafe.Slice(*out, len(arr))
    for i, v := range arr {
        outSlice[i] = v
    }
    
    return 0
}
```

### 3. 结构体输出参数

```go
/*
typedef struct {
    int id;
    char* name;
} Person;
*/
import "C"

//export GetPerson
func GetPerson(out *C.Person) C.int {
    out.id = 1
    out.name = C.CString("Alice")
    return 0
}
```

## 内存管理

### Go分配，C释放

```go
//export AllocateString
func AllocateString(out **C.char) C.int {
    *out = C.CString("allocated in Go")
    return 0
}

// C端需要释放
// free(output);
```

### C分配，Go释放

```go
//export FreeString
func FreeString(s *C.char) {
    C.free(unsafe.Pointer(s))
}
```

### 使用finalizer自动清理

```go
//export NewBuffer
func NewBuffer(size C.int) unsafe.Pointer {
    ptr := C.malloc(C.size_t(size))
    // 设置finalizer，当Go对象被GC时自动调用
    runtime.SetFinalizer(&ptr, func(p *unsafe.Pointer) {
        C.free(*p)
    })
    return ptr
}
```

## 完整示例

```go
package main

/*
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* data;
    int length;
} Buffer;
*/
import "C"
import (
    "fmt"
    "unsafe"
)

//export CreateBuffer
func CreateBuffer(data *C.char, out *C.Buffer) C.int {
    length := C.int(C.strlen(data))
    
    // 分配内存
    out.data = C.CString(C.GoString(data))
    out.length = length
    
    return 0
}

//export FreeBuffer
func FreeBuffer(buf *C.Buffer) {
    C.free(unsafe.Pointer(buf.data))
    buf.data = nil
    buf.length = 0
}

//export PrintBuffer
func PrintBuffer(buf C.Buffer) {
    fmt.Printf("Buffer: %s (length: %d)\n", C.GoString(buf.data), buf.length)
}

func main() {}
```

## 使用示例

```c
#include <stdio.h>
#include "buffer.h"

int main() {
    C.Buffer buf;
    
    // 创建buffer
    CreateBuffer("Hello, CGO!", &buf);
    
    // 使用buffer
    PrintBuffer(buf);
    
    // 释放buffer
    FreeBuffer(&buf);
    
    return 0;
}
```

## 注意事项

1. **内存泄漏**：C.CString分配的内存必须手动释放
2. **指针安全**：检查指针是否为NULL
3. **线程安全**：CGO调用可能切换线程
4. **性能开销**：CGO调用有一定性能开销
5. **错误处理**：使用返回值传递错误信息

## 最佳实践

1. **提供释放函数**：为每个分配函数提供对应的释放函数
2. **文档注释**：明确标注内存管理责任
3. **错误检查**：检查所有C函数调用的返回值
4. **使用包装**：在Go中提供高级封装简化使用
5. **测试覆盖**：编写测试验证内存管理
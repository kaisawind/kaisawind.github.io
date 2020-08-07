---
layout: post
title:  "golang pprof简单使用"
date: 2020-07-14 14:05:12 +0800
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
golang pprof性能分析
<!--more-->

## 1. 概述
pprof是go语言自带的性能监控和分析工具。

## 2. 使用方法

### 2.1 默认使用方法
```go
package main

import (
	"fmt"
	"net/http"
	_ "net/http/pprof"
	"time"
)

func main() {
	go func() {
		_ = http.ListenAndServe(":6060", nil)
	}()

	var timer *time.Timer
	for {
		select {
		case <-time.Tick(1 * time.Second):
			if timer != nil {
				timer.Stop()
				timer = nil
			}
			timer = time.AfterFunc(2*time.Second, timeout)
		}
	}
}

func timeout() {
	fmt.Println("timeout")
}
```

### 2.2 自定义mux方法
```go
package main

import (
    "fmt"
    "github.com/gorilla/mux"
    "math"

    "net/http"
)
import "net/http/pprof"

func AttachProfiler(router *mux.Router) {
    router.HandleFunc("/debug/pprof/", pprof.Index)
    router.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
    router.HandleFunc("/debug/pprof/profile", pprof.Profile)
    router.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
}

func SayHello(w http.ResponseWriter, r *http.Request) {
    for i := 0; i < 1000000; i++ {
        math.Pow(36, 89)
    }
    fmt.Fprint(w, "Hello!")
}

func main() {
    r := mux.NewRouter()
    AttachProfiler(r)
    r.HandleFunc("/hello", SayHello)
    http.ListenAndServe(":6060", r)
}
```

## 3. URL说明

|参数|PATH|EN|CN|
|---|---|---|---|
|allocs|`/debug/pprof/allocs?debug=1`|A sampling of all past memory allocations|过去内存分配情况的采样信息|
|block|`/debug/pprof/block?debug=1`|Stack traces that led to blocking on synchronization primitives|阻塞操作情况的采样信息|
|cmdline|`/debug/pprof/cmdline`|The command line invocation of the current program|显示程序启动命令及参数|
|goroutine|`/debug/pprof/goroutine?debug=1`|Stack traces of all current goroutines|当前所有协程的堆栈信息|
|heap|`/debug/pprof/heap?debug=1`|A sampling of memory allocations of live objects.|活动对象的内存分配的样本|
|mutex|`/debug/pprof/mutex?debug=1`|Stack traces of holders of contended mutexes|互斥锁情况的采样信息|
|profile|`/debug/pprof/profile`|CPU profile. |CPU 占用情况的采样信息|
|threadcreate|`/debug/pprof/threadcreate?debug=1`|Stack traces that led to the creation of new OS threads|系统线程创建情况的采样信息|
|trace|`/debug/pprof/trace`|A trace of execution of the current program.|程序运行跟踪信息|

## 4. 截图
![](/images/深度截图_选择区域_20200714143521.png)
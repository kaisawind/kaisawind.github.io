---
layout: post
title:  "golang errGroup使用"
date: 2019-10-16 14:24:12
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
golang errGroup使用与理解
<!--more-->

## 1. 概述

`errGroup`能够检测协程的是否报错，一般用于多协程时。

## 2. 例子

```go
package main

import (
	"context"
	"fmt"
	"time"

	"golang.org/x/sync/errgroup"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	group, errCtx := errgroup.WithContext(ctx)

	group.Go(func() error {
		go func() {
			select {
			case <-errCtx.Done():
				fmt.Println("errCtx1 Done")
				fmt.Println(errCtx.Err())
			}
		}()
		time.Sleep(3 * time.Second)
		cancel()
		time.Sleep(5 * time.Second)
		return nil
	})

	err := group.Wait()
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("All Done")
	}
}
```

## 3. 说明

1. `errCtx.Done()`和`group.Wait()`会阻塞

2. `cancel`函数会触发`errCtx.Done()`，但协程不会停止

3. `cancel`只能`cancel`一次，第二次没有效果

4. 全协程退出后，会触发`group.Wait()`

5. `group.Wait()`的返回错误，只会有最近一次错误

6. `cancel`和`errCtx.Done()`只能在`group.Go`中有效
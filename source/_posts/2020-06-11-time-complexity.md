---
layout: post
title:  "时间复杂度"
date: 2020-06-11 10:06:12 +0800
categories: [algorithm]
excerpt_separator: <!--more-->
---
时间复杂度
<!--more-->

## 1. 概述
定性描述该算法的运行时间。
时间复杂度常用大O符号表述，不包括这个函数的低阶项和首项系数。使用这种方式时，时间复杂度可被称为是渐近的，亦即考察输入值大小趋近无穷时的情况。例如，如果一个算法对于任何大小为 n （必须比 n0 大）的输入，它至多需要 5n3 + 3n 的时间运行完毕，那么它的渐近时间复杂度是 O(n3)。

## 2. 常用时间复杂度

* $O(1)$
单if判断
```go
if x == 0 {

}
```

* $O(\log n)$
二分法查找
```go
func binarySearch(arr []int, low, high, hkey int) int {
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == hkey {
			return mid
		} else if hkey < arr[mid] {
			high = mid - 1
		} else if hkey > arr[mid] {
			low = mid + 1
		}
	}
	return -1
}
```
* $O(n)$
单for循环
```go
for k, v := range n... {

}
```

* $O(n^{2})$
二重for循环
```go
for k, v := range n... {
    for k, v := range n... {

    }
}
```
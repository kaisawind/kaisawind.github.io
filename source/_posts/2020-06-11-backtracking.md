---
layout: post
title:  "回溯法"
date: 2020-06-11 10:06:12
categories: [算法]
excerpt_separator: <!--more-->
---
回溯法
<!--more-->

## 1. 概述
回溯法是暴力搜索法的一种:cold_sweat:
暴力搜索法通用算法
```
c = first(P)
while c != nil {
    if valid(P, c) {
        output(P, c)
    }
    c = next(P, c)
}
```
回溯法基本思想：
1. 判断当前路径是否正确
2. 如果正确，继续向下进行
3. 如果不正确，回溯到上一步的下一个路径

## 2. 示例
八皇后问题是回溯法经典例子
问题：
如何能够在8×8的国际象棋棋盘上放置八个皇后，使得任何一个皇后都无法直接吃掉其他的皇后？
(任两个皇后都不能处于同一条横行、纵行或斜线上。该问题可以推广为nxn的棋盘上放置n个皇后问题)

穷举法:
根据组合公式:

$$C^{n \times n}_n={n \times n \choose n}$$

,则8×8共有$C^{64}_8=\frac{64!}{(64-8)!8!}=4426165368$

真实解：
92个不同的解，去除旋转和对称，只有12个解

## 3. 解法

* first(P)
所有皇后的位置，一个二维数组，其中第一位是皇后个数(N), 第二维有两个分别为行(row)，列(col).行和列默认初期化为-1
```go
var queens = make([][]int, N)
for k, _ := range queens {
    tmp := []int{-1, -1}
    queens[k] = tmp
}
```
起始位置从第0个皇后，从第一行第一列开始
```go
nQ(0, 0)
```

* c != nil
循环条件 row -> N; 并且没有找到皇后位置
```go
for row < N && !found {
 // ...
}
```

* valid(P, c)
两个皇后都不能处于同一条横行、纵行或斜线上
```go
func valid(row int, col int, currentQueen int) bool {
	for k := 0; k < currentQueen; k++ {
		queen := queens[k]
		if row == queen[0] || col == queen[1] || math.Abs(float64(queen[0]-row)) == math.Abs(float64(queen[1]-col)) {
			return false
		}
	}
	return true
}
```

* output(P, c)
当判断成立时给当前皇后位置赋值，并递归查找下一个皇后
```go
queens[currentQueen][0] = row
queens[currentQueen][1] = currentCol
found = nQ(currentQueen+1, currentCol+1)
```
如果递归失败，会**回溯**到当前行列，并尝试下一行

* c = next(P, c)
通过行进行循环所以，下一个是下一行
```
row++
```

## 4. 完整代码

```go
package main

import (
	"fmt"
	"math"
)

const N = 8

var queens = make([][]int, N)

func main() {
	for k, _ := range queens {
		tmp := []int{-1, -1}
		queens[k] = tmp
	}
	fmt.Println(queens)
	nQ(0, 0)
	fmt.Println(queens)
}

func nQ(currentQueen int, currentCol int) bool {
	if currentQueen >= N {
		return true
	}
	found := false
	row := 0
	for row < N && !found {
		if valid(row, currentCol, currentQueen) {
			queens[currentQueen][0] = row
			queens[currentQueen][1] = currentCol
			found = nQ(currentQueen+1, currentCol+1)
		}
		row++
	}
	return found
}

func valid(row int, col int, currentQueen int) bool {
	for k := 0; k < currentQueen; k++ {
		queen := queens[k]
		if row == queen[0] || col == queen[1] || math.Abs(float64(queen[0]-row)) == math.Abs(float64(queen[1]-col)) {
			return false
		}
	}
	return true
}

```
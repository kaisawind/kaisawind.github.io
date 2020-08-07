---
layout: post
title:  "Rust语言Derive说明"
date: 2020-04-28 11:38:04 +0800
categories: [编程语言,rust]
tags: [rust, manjaro, linux]
excerpt_separator: <!--more-->
---
Rust语言Derive说明
<!--more-->

## 1. 概述
编译器可以通过`#[derive(*****)]`为某些特性提供基本的实现。

## 2. 特性

|特性|作用|说明|
|---|---|---|
|Eq|等价关系|比较是否相等|
|PartialEq|局部等价|比较部分是否相等|
|Ord|比较大小|比较大小|
|PartialOrd|部分比较大小|部分比较大小|
|Clone|深拷贝|深拷贝|
|Copy|浅拷贝|浅拷贝|
|Hash|计算Hash值|计算Hash值|
|Default|默认值|默认值|
|Debug|`{:?}`进行格式化|`{:?}`进行格式化|

## 2.1 Eq VS PartialEq

等价关系需要满足的条件：

* 对称性（Symmetry）：a == b 可推出 b == a
* 传递性（Transitivity）：a == b 且 b == c 可推出 a == c
* 反身性（Reflexivity）：a == a

Rust只实现了PartialEq,由于IEEE规定浮点数和NaN不等于自身，所以反身性不成立。这也导致Eq需要手动进行判断。

对于大多数类型来说，Eq和PartialEq需要同时存在。
原始字段
```rust
enum BookFormat { Paperback, Hardback, Ebook }
struct Book {
    isbn: i32,
    format: BookFormat,
}
```
使用`derive`
```rust
#[derive(PartialEq,Eq)]
enum BookFormat { Paperback, Hardback, Ebook }
#[derive(PartialEq,Eq)]
struct Book {
    isbn: i32,
    format: BookFormat,
}
```
具体实现
```rust

enum BookFormat { Paperback, Hardback, Ebook }

impl PartialEq<BookFormat> for BookFormat {
    fn eq(&self, other: &BookFormat) -> bool {
        self == *other
    }
}
impl Eq for BookFormat {}

struct Book {
    isbn: i32,
    format: BookFormat,
}

impl PartialEq<Book> for Book {
    fn eq(&self, other: &Book) -> bool {
        self.isbn == *other.isbn && self.format == *other.format
    }
}
impl Eq for Book {}
```
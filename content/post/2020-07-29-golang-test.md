---
layout: post
title:  "go test skip some test"
date: 2020-07-29 14:18:12
lastmod: 2026-03-19
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
go test skip some test
<!--more-->

Its easy to skip single test or many test,just add `+build`
```go
// +build all

package tags

import "testing"

func TestA(t *testing.T) {}
```

```go
// +build all feature2

package tags

import "testing"

func TestA(t *testing.T) {}
```

```bash
go test -v -tags all
go test -v -tags "feature1 feature2"
```
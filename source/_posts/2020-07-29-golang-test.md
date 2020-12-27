---
layout: post
title:  "go test skip some test"
date: 2020-07-29 14:18:12
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
go test skip some test
<!--more-->

Its easy to skip single test or many test,just add `+build`
```golang
// +build all

package tags

import "testing"

func TestA(t *testing.T) {}
```

```golang
// +build all feature2

package tags

import "testing"

func TestA(t *testing.T) {}
```

```bash
go test -v -tags all
go test -v -tags "feature1 feature2"
```
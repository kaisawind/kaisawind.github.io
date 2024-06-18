---
layout: post
title:  "Stable Diffusion关键词"
date: 2023-04-01 23:17:16
categories: [ai]
tags: [ai]
excerpt_separator: <!--more-->
---
Stable Diffusion关键词
<!--more-->

https://stable-diffusion-art.com/

* 1. `,`分割关键词，空格，换行不影响分割
    `best quality,ultra-detailed, masterpiece, finely detail, highres, 8k wallpaper`
* 2. `()`加权,`[]`减权
    `(n) = (n:1.1)`
    `((n)) = (n:1.21)`
    `(((n))) = (n:1.331)`
    `((((n)))) = (n:1.4641)`
    `(((((n)))) = (n:1.61051)`
    `((((((n)))))) = (n:1.771561)`
    `[n] = (n:0.9090909090909091)`
    `[[n]] = (n:0.8264462809917355)`
    `[[[n]]] = (n:0.7513148009015778)`
    `[[[[n]]]] = (n:0.6830134553650707)`
    `[[[[[n]]]]] = (n:0.6209213230591552)`
    `[[[[[[n]]]]]] = (n:0.5644739300537775)`

* 3. `+`混淆关键词
    `red+blue water`
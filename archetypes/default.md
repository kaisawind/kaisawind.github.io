---
layout: post
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
date: {{ .Date }}
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
{{ replace .File.ContentBaseName "-" " " | title }}
<!--more-->

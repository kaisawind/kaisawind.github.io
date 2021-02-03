---
layout: post
title:  "linux限制用户ssh登录"
date: 2021-02-03 16:10:16
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
linux限制用户ssh登录
<!--more-->

* /etc/hosts.deny
sshd限制登录策略

https://linux.die.net/man/5/hosts.deny


禁止IP进行所有指令操作
```conf
ALL:142.93.121.236
```

禁止IP进行ssh登录
```conf
sshd:142.93.121.236
```

匹配末尾
```conf
ALL:.tue.nl
```

匹配开头
```conf
ALL:tue.nl.
```

匹配符`*`或`？`
```conf
ALL:tue.nl.*
ALL:tue.*.com
```

* /etc/hosts.allow
sshd允许登录策略
---
layout: post
title:  "华为ensp常用命令"
date: 2020-10-25 22:32:04
categories: [网络工程]
tags: [tools]
excerpt_separator: <!--more-->
---
华为ensp常用命令
<!--more-->

1. quit
命令功能
quit命令用来从当前视图退回到较低级别视图，如果是用户视图，则退出系统。

2. 视图
视图一般可以分为三个级别，由低到高分别为：
用户视图
系统视图
具体业务视图，例如接口视图等
```bash
<HUAWEI> system-view
[HUAWEI] aaa
[HUAWEI-aaa] quit
[HUAWEI] quit
<HUAWEI> quit
```
`<HUAWEI>`: 用户视图
`[HUAWEI]`: 系统视图
`[HUAWEI-aaa]`: 具体业务视图

3. return
命令功能
return命令用来从除用户视图外的其它视图退回到用户视图。
```bash
<HUAWEI> system-view
[HUAWEI] user-interface vty 0
[HUAWEI-ui-vty0] return
<HUAWEI>
```

4. system-view
命令功能
system-view命令用来从用户视图进入系统视图。
```bash
<HUAWEI> system-view
Enter system view, return user view with Ctrl+Z.
[HUAWEI]
```

5. sysname
sysname命令用来设置设备的主机名。
undo sysname命令用来恢复设备的主机名到缺省情况。
```bash
<HUAWEI> system-view
[HUAWEI] sysname HUAWEIA
[HUAWEIA]
```

6. user-interface
user-interface命令用来进入一个用户界面视图或多个用户界面视图。
display user-interface命令用来查看用户界面信息。
进入Console 0用户界面
```bash
<HUAWEI> system-view
[HUAWEI] user-interface console 0
[HUAWEI-ui-console0]
```
进入VTY1用户界面
```bash
<HUAWEI> system-view
[HUAWEI] user-interface vty 1
[HUAWEI-ui-vty1]
```

7. authentication-mode
authentication-mode命令用来设置登录用户界面的验证方式。
undo authentication-mode命令用来删除用户界面的验证方式。
缺省情况下，通过Console口登录设备时，默认认证方式为AAA。其它登录方式缺省没有使用该命令配置验证方式，登录用户界面必须配置验证方式，否则用户无法成功登录设备。
    |参数|参数说明|
    |---|---|
    |aaa|设置进行AAA授权验证方式。|
    |password|设置进行密码验证方式。|
    |none|设置验证方式为不验证。|

8. set authentication password
set authentication password命令用来设置本地验证的密码。
undo set authentication password命令用来取消本地验证的密码。
缺省情况下，设备没有设置本地验证的密码。
    |参数|参数说明|
    |---|---|
    |cipher|指定配置密文密码。|
    |password|指定密码。|

9. interface
interface命令用来进入指定的接口或子接口视图。
undo interface命令用来删除子接口。
    |参数|参数说明|
    |---|---|
    |ethernet|指定进入快速以太网接口视图。|
    |gigabitethernet|指定进入千兆以太网接口视图。|
    |multige|指定进入多千兆以太网接口视图。|
    |xgigabitethernet|指定进入万兆以太网接口视图。|
    |25ge|指定进入二点五万兆以太网接口视图|
    |40ge|指定进入四万兆以太网接口视图。|
    |100ge|指定进入十万兆以太网接口视图。|

10. interface vlanif
interface vlanif命令用来创建VLANIF接口并进入VLANIF接口视图。
undo interface vlanif命令用来删除VLANIF接口。
缺省情况下，VLANIF接口没有被创建。
vlanif(Virtual Local Area Network Interface)

11. un in en
取消消息显示

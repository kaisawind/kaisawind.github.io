---
layout: post
title:  "linux查看上次登录用户"
date: 2021-02-02 10:10:16
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
linux查看上次登录用户
<!--more-->

* /var/log/wtmp
记录每个用户的登录次数和持续时间等信息

可以用last命令输出当中内容：
```bash
debian:/var/log# last
debian   pts/9        221.215.176.148  Thu Oct 17 10:15   still logged in   
debian   pts/8        221.215.176.148  Thu Oct 17 09:56   still logged in   
debian   pts/7        221.215.176.148  Thu Oct 17 09:32 - 10:44  (01:12)    
root     pts/5        114.255.31.253   Thu Oct 17 09:30 - 10:20  (00:50)    
root     pts/4        114.255.31.253   Thu Oct 17 09:30 - 10:20  (00:50)  
```

* /var/log/btmp
记录的登入系统失败的用户名单

可以用lastb命令输出当中内容：
```bash
[root@localhost ~]# lastb -n 10
root     ssh:notty    43.226.153.168   Wed Feb  3 16:12 - 16:12  (00:00)    
root     ssh:notty    43.226.73.164    Wed Feb  3 16:11 - 16:11  (00:00)    
root     ssh:notty    43.226.153.168   Wed Feb  3 16:11 - 16:11  (00:00)    
root     ssh:notty    43.226.153.168   Wed Feb  3 16:09 - 16:09  (00:00)    
root     ssh:notty    43.226.73.164    Wed Feb  3 16:09 - 16:09  (00:00)    
root     ssh:notty    43.226.153.168   Wed Feb  3 16:08 - 16:08  (00:00)    
root     ssh:notty    43.226.153.168   Wed Feb  3 16:07 - 16:07  (00:00)    
root     ssh:notty    43.226.73.164    Wed Feb  3 16:07 - 16:07  (00:00)    
root     ssh:notty    43.226.153.168   Wed Feb  3 16:06 - 16:06  (00:00)    
root     ssh:notty    43.226.153.168   Wed Feb  3 16:05 - 16:05  (00:00)
```
---
layout: post
title:  "linux网络检测命令"
date: 2020-04-13 11:10:16 +0800
categories: [linux,linux]
tags: [linux]
excerpt_separator: <!--more-->
---
linux网络检测命令
<!--more-->

## 1. ifconfig
检查当前环境配置的IP信息
```bash
docker0   Link encap:Ethernet  HWaddr 02:42:68:e5:5b:76  
          inet addr:172.17.0.1  Bcast:172.17.255.255  Mask:255.255.0.0
          inet6 addr: fe80::42:68ff:fee5:5b76/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:23923 errors:0 dropped:0 overruns:0 frame:0
          TX packets:24530 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:62249362 (59.3 MiB)  TX bytes:5538367 (5.2 MiB)

eth0      Link encap:Ethernet  HWaddr 76:8a:29:de:ed:ae  
          inet addr:192.168.8.100  Bcast:192.168.8.255  Mask:255.255.255.0
          inet6 addr: fe80::748a:29ff:fede:edae/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1136217 errors:0 dropped:81 overruns:0 frame:0
          TX packets:1092002 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:333483215 (318.0 MiB)  TX bytes:244400646 (233.0 MiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:1088617 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1088617 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:457161134 (435.9 MiB)  TX bytes:457161134 (435.9 MiB)
```

## 2. ip address
查看本地IP地址的
```bash
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 76:8a:29:de:ed:ae brd ff:ff:ff:ff:ff:ff
    inet 192.168.8.100/24 brd 192.168.8.255 scope global dynamic eth0
       valid_lft 54033sec preferred_lft 54033sec
    inet6 fe80::748a:29ff:fede:edae/64 scope link 
       valid_lft forever preferred_lft forever
```

* lo 全称loopback，是回环地址，经常被分配到127.0.0.1地址上，用于本机通信，经过内核处理后直接返回，不会在任何网络中出现。
* eth0：网卡名，如果有多块网卡，会有多个eth 或其它名称。
* ink/ether：这个是MAC地址，唯一的，一块网卡一个MAC。
* inet：网卡上绑定的IP地址，通常所说的IPV4，一块网卡可以绑定多个IP地址。
    在绑定IP地址时注意：windows主机会提示IP地址冲突，而linux主机无任何提示，在添加新的IP地址时务必检测一下新地址是否和原有地址冲突，避免造成访问不可用。常用检测命令：ping或arping IP；
* inet6：IPV6地址，暂时没有，预留。

## 3. ip route

列出路由
```bash
ip route list
ip route show
ip route
```

```bash
192.168.8.0/24 dev eth0 proto kernel scope link src 192.168.8.100 
192.168.8.1 dev eth0 proto dhcp scope link src 192.168.8.100 metric 1024 
```

## 4. route -n

列出路由表
```bash
route -n
```

```bash
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.8.1     0.0.0.0         UG    1024   0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 vethe7978b8
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 veth19c8f37
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 veth1ee6089
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 veth4510020
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 vethb448582
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
172.18.0.0      0.0.0.0         255.255.0.0     U     0      0        0 br-12ec3d5b4075
192.168.8.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
192.168.8.1     0.0.0.0         255.255.255.255 UH    1024   0        0 eth0
```

## 5. dns配置

```bash
cat /etc/resolv.con
```
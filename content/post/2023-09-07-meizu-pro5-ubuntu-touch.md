---
layout: post
title:  "MeizuPro5安装ubuntu touch"
date: 2023-09-07 10:13:16
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
MeizuPro5安装ubuntu touch
<!--more-->


### 介绍

* ubuntu touch官网网站
https://ubuntu-touch.io/

* 支持的手机列表
https://devices.ubuntu-touch.io/installer/


正常ubuntu touch可以直接使用UBports Installer安装，
但是MeizuPro5不支持直接使用UBports Installer安装。

本文涉及到的文件

https://drive.google.com/drive/folders/15JWmjyai7fiZ6PqSdTxQ2IBPhnceqAS9?usp=sharing


### 1. 国内版切国际版

MeizuPro5有三个版本
```bash
machine_type=M576_unicom_custom - U version = China Unicom
machine_type=M576_mobile_public - A version = Chinese
machine_type=M576_intl_official - I/G version = International
```
需要将中国联通(China Unicom), 中国版(Chinese)切换到国际版(International),才能够刷ubuntu touch固件。

#### 1.1 flyme系统降级到5.1.2.0A
Flyme OS 5.1.2.0A是MeizuPro5出厂系统，也能从官网获取。

https://www.flyme.com/firmwarelist-23.html#3

```txt
版本：Flyme 5.1.2.0A
MD5：201243c2eef790025d8db36311efe558
文件大小：885MB
发布时间：2015-12-29
开发者：Flyme
```

升级方法：
1. 将手机与电脑连接，电脑会多出一个MeizuPro5的磁盘(媒体方式)
2. 将升级包命名为updata.zip放到手机存储的根目录
3. 关机
4. 同时按下[声音+]和[电源键]直到出现刷机界面
![](/images/MeizuPro5Flash.jpeg)

#### 1.2 手机ROOT

MeizuPro5手机需要登录flyme帐号才能root,但是因为固件版本太低，导致无法登录帐号，所以需要升级flyme登录app.

安装[Flyme 帐号-8000004-8.0.4.apk]后,按照以下步骤进行ROOT。
<font color="red">ROOT后重新开机</font>

![](/images/FlymeAccount.jpeg)
![](/images/FlymeAccountLogin.jpeg)
![](/images/FlymeSecurity.jpeg)
![](/images/FlymeRoot.jpeg)
![](/images/FlymeRootConfirm.jpeg)

#### 1.3 开启超级权限

1. 安装[supersu.256.apk], 再安装[supersu_pro_v2.0.5.apk].
打开supersu APP, 提示更新二进制，进行更新；更新之后会提示重启手机，进行重启。
2. 安装[busybox.apk]和[root.browserfree.apk], 打开supersu app授予这两个软件root权限

#### 1.4 修改为国际版

1. 打开browserfree app, 找到文件`/dev/block/platform/15570000.ufs/by-name/proinfo`，
2. 点击[proinfo],
3. 选择[open as],
4. 选择[text file],
5. 选择[RB Text Editor],
6. 将[M576_mobile_public]改为[M576_intl_official]
7. 重启手机
8. 重启之后，查看是否修改成功
![](/images/2023-09-07_11-53.png)

### 2. 刷第三方recovery固件

#### 2.1 打开开发者模式

设置 -> 辅助功能 -> 开发者选项 -> USB调试打开

#### 2.2 进入fastboot

同时按下[音量键－]和[电源键], 直到出现fastboot界面.
注意(unlocked,unrooted)或者(unlocked, rooted),必须是unlocked.
![](/images/MeizuPro5Fastboot.webp)

#### 2.3 电脑端fastboot驱动

安装fastboot驱动
![](/images/MeizuPro5Fastboot1.jpg)
![](/images/MeizuPro5Fastboot2.jpg)
![](/images/MeizuPro5Fastboot3.jpg)
![](/images/MeizuPro5Fastboot4.jpg)
![](/images/MeizuPro5Fastboot5.jpg)
![](/images/MeizuPro5Fastboot6.jpg)
![](/images/MeizuPro5Fastboot7.jpg)
![](/images/MeizuPro5Fastboot8.jpg)
![](/images/MeizuPro5Fastboot9.jpg)
![](/images/MeizuPro5Fastboot10.jpg)

#### 2.4 刷第三方recovery固件

1. 通过fastboot devices确认是否能识别设备
2. `fastboot flash recovery recovery.img`刷入固件
3. 输入完成之后，同时按下[声音+]和[电源键]进入TWRP界面
![](/images/MeizuPro5Fastboot11.jpg)
![](/images/MeizuPro5Fastboot12.jpg)
![](/images/MeizuPro5Fastboot13.jpg)
![](/images/TWRP_3.0.0-0.png)

### 3. 输入ubuntu touch的ROM

#### 3.1 备份方式刷入

0. 同时按下[声音+]和[电源键]进入TWRP界面
1. 将手机与电脑连接，电脑中出现新的磁盘
2. 创建新的文件夹`/TWRP/BACKUPS/M86/Ubports16.04_OTA25`
3. 解压Ubports16.04_OTA3.zip, 将解压之后的文件复制到第2步创建的文件夹中
4. 在手机的TWRP界面中选择Restore, 还原系统。

#### 3.2 adb方式升级系统

这种方法基于还原之后的ubuntu系统

0. 同时按下[声音+]和[电源键]进入TWRP界面
1. 将手机与电脑连接，电脑中出现新的磁盘
2. 在TWRP界面的Mount中挂载system文件系统(一定要挂载)
3. 挂载system之后，进入system文件夹，查看里面是否有文件，如果为空说明没有挂载
4. 在电脑命令行，使用adb连接手机
```bash
adb devices # 确认是否识别手机
```
5. 运行以下命令
```bash
adb push *.tar.xz /sdcard/
```
6. 升级系统
进入手机命令行，将第5步复制的文件覆盖旧文件(或者清空system之后再操作)
```bash
adb shell
cd /
tar -xf /sdcard/version-983.tar.xz
tar -xf /sdcard/device-9362ef8ed39f89be39049802d33244d9f85ad9ebb29bd0b86411f544b0863fe7.tar.xz
tar -xf /sdcard/keyring-4c4e7ef380ebcfa2c31084efa199138e93bfed8fc58aa3eb06bdf75a78af9b57.tar.xz
tar -xf /sdcard/ubports-5c50126bec26731fb3a242845920e01d31e3b2ba823b2f06887c76a70c3ca92e.tar
reboot
```
7. 重启之后已经是升级之后系统

![](/images/screenshot20230907_102024625.png)
![](/images/screenshot20230907_102104799.png)
![](/images/screenshot20230907_102111433.png)
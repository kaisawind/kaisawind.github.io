---
layout: post
title:  "virtualbox与HyperV冲突"
date: 2019-3-5 11:09:04
categories: [虚拟化,virtualbox]
excerpt_separator: <!--more-->
---

Raw-mode is unavailable courtesy of Hyper-V. (VERR_SUPDRV_NO_RAW_MODE_HYPER_V_ROOT).

返回 代码: 
E_FAIL (0x80004005)
组件: 
ConsoleWrap
界面: 
IConsole {872da645-4a9b-1727-bee2-5585105b9eed}

<!--more-->

![微信截图_20190305110438.png](/images/微信截图_20190305110438.png)

### 前提条件

- virtualbox与Docker Desktop for Windows是冲突的

    如果要使用virtualbox必须卸载Docker for Windows

- virtualbox与Hyper-V冲突

    如果要使用virtualbox必须卸载Hyper-V

### 卸载

* 1. 卸载Hyper-V

![微信截图_20190305112653.png](/images/微信截图_20190305112653.png)

* 2. `bcdedit /set hypervisorlaunchtype off`

    需要使用管理员运行

* 3. 重启电脑

* 4. 每次系统更新之后，2-3步命令都需要执行
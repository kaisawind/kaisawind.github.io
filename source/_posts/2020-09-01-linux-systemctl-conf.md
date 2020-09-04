---
layout: post
title:  "systemctl配置文件写法"
date: 2020-09-01 10:30:04 +0800
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
---
systemctl配置文件写法
<!--more-->

## 1. 概述
systemctl配置文件包含一下几种:
* .service
* .socket
* .device
* .mount
* .automount
* .swap
* .target
* .path
* .timer (which can be used as a cron-like job scheduler[54])
* .snapshot
* .slice (used to group and manage processes and resources[55])
* .scope

金步国中文翻译
http://www.jinbuguo.com/systemd/systemd.service.html#

## 2. 整体结构


```conf
[Unit]
Description=Foo

[Service]
ExecStart=/usr/sbin/foo-daemon

[Install]
WantedBy=multi-user.target
```

|主|次|说明|
|---|---|---|
|[Unit]|Description|描述，systemd会用来输出日志|
|[Unit]|Documentation|文档说明|
|[Unit]|Wants|对其他单元的弱依赖|
|[Unit]|Requires|对其他单元的强依赖|
|[Unit]|Requisite||
|[Unit]|BindsTo||
|[Unit]|PartOf||
|[Unit]|Conflicts||
|[Unit]|Before||
|[Unit]|After||
|[Unit]|OnFailure||
|[Unit]|PropagatesReloadTo||
|[Unit]|ReloadPropagatedFrom||
|[Unit]|JoinsNamespaceOf||
|[Unit]|RequiresMountsFor||
|[Unit]|OnFailureJobMode||
|[Unit]|IgnoreOnIsolate||
|[Unit]|StopWhenUnneeded||
|[Unit]|RefuseManualStart||
|[Unit]|RefuseManualStop||
|[Unit]|AllowIsolate||
|[Unit]|DefaultDependencies||
|[Unit]|CollectMode||
|[Unit]|FailureAction||
|[Unit]|SuccessAction||
|[Unit]|FailureActionExitStatus||
|[Unit]|SuccessActionExitStatus||
|[Unit]|JobTimeoutSec||
|[Unit]|JobRunningTimeoutSec||
|[Unit]|JobTimeoutAction||
|[Unit]|JobTimeoutRebootArgument||
|[Unit]|StartLimitIntervalSec||
|[Unit]|StartLimitBurst||
|[Unit]|StartLimitAction||
|[Unit]|RebootArgument||
|[Unit]|SourcePath||
|[Unit]|ConditionArchitecture||
|[Unit]|ConditionVirtualization||
|[Unit]|ConditionHost||
|[Unit]|ConditionEnvironment||
|[Unit]|ConditionSecurity||
|[Unit]|ConditionCapability||
|[Unit]|ConditionACPower||
|[Unit]|ConditionNeedsUpdate||
|[Unit]|ConditionFirstBoot||
|[Unit]|ConditionPathExists||
|[Unit]|ConditionPathExistsGlob||
|[Unit]|ConditionPathIsDirectory||
|[Unit]|ConditionPathIsSymbolicLink||
|[Unit]|ConditionPathIsMountPoint||
|[Unit]|ConditionPathIsReadWrite||
|[Unit]|ConditionPathIsEncrypted||
|[Unit]|ConditionDirectoryNotEmpty||
|[Unit]|ConditionFileNotEmpty||
|[Unit]|ConditionFileIsExecutable||
|[Unit]|ConditionUser||
|[Unit]|ConditionGroup||
|[Unit]|ConditionControlGroupController||
|[Unit]|ConditionMemory||
|[Unit]|ConditionCPUs||
|[Unit]|AssertArchitecture||
|[Unit]|AssertVirtualization||
|[Unit]|AssertHost||
|[Unit]|AssertKernelCommandLine||
|[Unit]|AssertKernelVersion||
|[Unit]|AssertSecurity||
|[Unit]|AssertCapability||
|[Unit]|AssertACPower||
|[Unit]|AssertNeedsUpdate||
|[Unit]|AssertFirstBoot||
|[Unit]|AssertPathExists||
|[Unit]|AssertPathExistsGlob||
|[Unit]|AssertPathIsDirectory||
|[Unit]|AssertPathIsSymbolicLink||
|[Unit]|AssertPathIsMountPoint||
|[Unit]|AssertPathIsReadWrite||
|[Unit]|AssertDirectoryNotEmpty||
|[Unit]|AssertFileNotEmpty||
|[Unit]|AssertFileIsExecutable||
|[Unit]|AssertUser||
|[Unit]|AssertGroup||
|[Unit]|AssertControlGroupController||
|[Install]|Alias||
|[Install]|WantedBy||
|[Install]|RequiredBy||
|[Install]|Also||
|[Install]|DefaultInstance||
|[Service]|Type|设置进程的启动类型|
|[Service]|RemainAfterExit|当该服务的所有进程全部退出之后， 是否依然将此服务视为活动(active)状态。 默认值为 no|
|[Service]|GuessMainPID||
|[Service]|PIDFile||
|[Service]|BusName||
|[Service]|ExecStart||
|[Service]|ExecStartPre||
|[Service]|ExecStartPost||
|[Service]|ExecCondition||
|[Service]|ExecReload||
|[Service]|ExecStop||
|[Service]|ExecStopPost||
|[Service]|RestartSec||
|[Service]|TimeoutStartSec||
|[Service]|TimeoutStopSec||
|[Service]|TimeoutAbortSec||
|[Service]|TimeoutSec||
|[Service]|TimeoutStartFailureMode||
|[Service]|TimeoutStopFailureMode||
|[Service]|RuntimeMaxSec||
|[Service]|WatchdogSec||
|[Service]|Restart||
|[Service]|SuccessExitStatus||
|[Service]|RestartPreventExitStatus||
|[Service]|RestartForceExitStatus||
|[Service]|RootDirectoryStartOnly||
|[Service]|NonBlocking||
|[Service]|NotifyAccess||
|[Service]|Sockets||
|[Service]|FileDescriptorStoreMax||
|[Service]|USBFunctionDescriptors||
|[Service]|USBFunctionStrings||
|[Service]|OOMPolicy||
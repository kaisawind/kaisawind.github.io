---
layout: post
title:  "cgo中callback函数的实现"
date: 2020-10-24 18:25:12
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
cgo中callback函数的实现
<!--more-->

## 1. 概述
cgo是连接C(not C++)和go语言的编译器，但是有很多地方需要转换。

## 2. callback的实现

链接库提供了函数进行回调函数赋值
**HCNetSDK.h**
```C
typedef BOOL (*MSGCallBack_V31)(LONG lCommand, NET_DVR_ALARMER *pAlarmer, char *pAlarmInfo, DWORD dwBufLen, void* pUser);
BOOL NET_DVR_SetDVRMessageCallBack_V31(MSGCallBack_V31 fMessageCallBack, void* pUser);
```

需要使用C语言实现回调函数，并导出回调函数的声明，让go去实现
**cfunctions.go**
```go
// Wrappers for Go callback functions to be passed into C.
package hcnet

/*
#cgo CFLAGS: -I${SRCDIR}
#include "HCNetSDK.h"

// export from go
extern BOOL MSGCallBackV31Go(LONG lCommand, NET_DVR_ALARMER *pAlarmer, char *pAlarmInfo, DWORD dwBufLen, void* pUser);

// WRAP 函数
BOOL MSGCallBackV31Cgo(LONG lCommand, NET_DVR_ALARMER *pAlarmer, char *pAlarmInfo, DWORD dwBufLen, void* pUser)
{
	return MSGCallBackV31Go(lCommand, pAlarmer, pAlarmInfo, dwBufLen, pUser);
}
*/
import "C"
```

go实现函数声明
MSGCallBackV31是函数的全局变量，在导出函数中调用全局变量。
注意export是go导出函数的实现
**common.go**
```go
var MSGCallBackV31 MSGCallBackV31Func

//export MSGCallBackV31Go
func MSGCallBackV31Go(lCommand C.LONG, pAlarmer C.LPNET_DVR_ALARMER, pAlarmInfo *C.char, dwBufLen C.DWORD, pUser unsafe.Pointer) C.BOOL {
	if MSGCallBackV31 != nil {
		buffer := C.GoBytes(unsafe.Pointer(pAlarmInfo), C.int(dwBufLen))
		return C.BOOL(MSGCallBackV31(uint32(lCommand), CgoAlarmer(pAlarmer), buffer, pUser))
	}
	return TRUE
}
```

设置回调函数的实现
真正的回调函数赋值给了全局变量，C的注册函数注册是是cfunctions中的Cgo函数。
Cgo函数调用全局变量函数。
**common.go**
```go
// SetDVRMessageCallBackV31 注册报警信息回调函数
func SetDVRMessageCallBackV31(cb MSGCallBackV31Func, pUserData unsafe.Pointer) (err error) {
	MSGCallBackV31 = cb
	ret := C.NET_DVR_SetDVRMessageCallBack_V31(C.MSGCallBack_V31(C.MSGCallBackV31Cgo), pUserData)
	if ret != TRUE {
		err = GetLastError()
		return
	}
	return
}
```

go中回调函数的声明
**defination.go**
```go
type MSGCallBackV31Func func(lCommand uint32, pAlarmer *Alarmer, pAlarmInfo []byte, pUserData unsafe.Pointer) int32
```
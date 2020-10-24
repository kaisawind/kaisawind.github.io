---
layout: post
title:  "cgo中void*的参数实现"
date: 2020-10-24 18:52:12 +0800
categories: [编程语言,golang]
excerpt_separator: <!--more-->
---
cgo中void*的参数实现
<!--more-->

## 1. 概述
C语言中入参大部分情况下是void*类型的指针，需要转换成go语言相应的类型。

## 2. 当入参是void*时

有如下函数,其中pSendBuf会根据dwDataType类型的不同，传送不同类型的结构体指针;dwBufSize是结构体的大小。
```C
BOOL NET_DVR_SendRemoteConfig(LONG lHandle, DWORD dwDataType, char *pSendBuf, DWORD dwBufSize);
```

以下是cgo的实现
go中的入参是`interface{}`类型，在cgo中通过断言获取data的类型，并转换为C的类型。
**注意C结构体大小的计算方法**
```go
// SendRemoteConfig 发送长连接数据
func SendRemoteConfig(lHandle int32, dwDataType uint32, data interface{}) (err error) {
	var lpInBuffer C.LPVOID
	var inBufferSize uint32
	switch value := data.(type) {
	case *CardCfgV50:
		var temp C.NET_DVR_CARD_CFG_V50
		inBufferSize = uint32(unsafe.Sizeof(temp))
		lpInBuffer = C.LPVOID(unsafe.Pointer(GoCCardCfgV50(value)))
	case *CardCfgSendData:
		var temp C.NET_DVR_CARD_CFG_SEND_DATA
		inBufferSize = uint32(unsafe.Sizeof(temp))
		lpInBuffer = C.LPVOID(unsafe.Pointer(GoCCardCfgSendData(value)))
	default:
		err = fmt.Errorf("data type %T not support now", value)
		return
	}
	ret := C.NET_DVR_SendRemoteConfig(C.LONG(lHandle), C.DWORD(dwDataType), (*C.char)(lpInBuffer), C.DWORD(inBufferSize))
	if ret != TRUE {
		err = GetLastError()
		return
	}
	return
}
```

## 3. 当出参是void*时


有如下函数,其中lpOutBuffer会根据dwCommand类型的不同，传送不同类型的结构体指针;dwOutBufferSize是结构体的大小。
```C
BOOL NET_DVR_GetDVRConfig(LONG lUserID, DWORD dwCommand, LONG lChannel, LPVOID lpOutBuffer, DWORD dwOutBufferSize, LPDWORD lpBytesReturned);
```

以下是cgo的实现
由于没有入参，所以根据dwCommand的类型创建出参的C的结构体指针。
返回时，将C的结构体转换为go的结构体，并作为go的返回参数。
```go
// GetDVRConfig 获取设备的配置信息
func GetDVRConfig(lUserID int, dwCommand uint32, lChannel uint32) (out interface{}, bytesReturned uint32, err error) {
	var lpOutBuffer C.LPVOID
	outBufferSize := uint32(0)
	switch dwCommand {
	case NetDvrGetAcsCfg:
		var temp C.NET_DVR_ACS_CFG
		outBufferSize = uint32(unsafe.Sizeof(temp)) // 单纯计算size， 无法使用类型计算
		lpOutBuffer = C.LPVOID(unsafe.Pointer(&C.NET_DVR_ACS_CFG{}))
	case NetDvrGetDoorCfg:
		var temp C.NET_DVR_DOOR_CFG
		outBufferSize = uint32(unsafe.Sizeof(temp)) // 单纯计算size， 无法使用类型计算
		lpOutBuffer = C.LPVOID(unsafe.Pointer(&C.NET_DVR_DOOR_CFG{}))
	case NetDvrGetAcsWorkStatusV50:
		var temp C.NET_DVR_ACS_WORK_STATUS_V50
		outBufferSize = uint32(unsafe.Sizeof(temp)) // 单纯计算size， 无法使用类型计算
		lpOutBuffer = C.LPVOID(unsafe.Pointer(&C.NET_DVR_ACS_WORK_STATUS_V50{}))
	default:
		err = fmt.Errorf("command %d not support now", dwCommand)
		return
	}
	cBytesReturned := C.DWORD(0)
	ret := C.NET_DVR_GetDVRConfig(C.LONG(lUserID), C.DWORD(dwCommand), C.LONG(lChannel), lpOutBuffer, C.DWORD(outBufferSize), &cBytesReturned)
	if ret != TRUE {
		err = GetLastError()
		return
	}
	bytesReturned = uint32(cBytesReturned)
	switch dwCommand {
	case NetDvrGetAcsCfg:
		out = CgoDvrAcsCfg(C.LPNET_DVR_ACS_CFG(lpOutBuffer))
	case NetDvrGetDoorCfg:
		out = CgoDoorCfg(C.LPNET_DVR_DOOR_CFG(lpOutBuffer))
	case NetDvrGetAcsWorkStatusV50:
		out = CgoAcsWorkStatusV50(C.LPNET_DVR_ACS_WORK_STATUS_V50(lpOutBuffer))
	default:
		err = fmt.Errorf("command %d not support now", dwCommand)
		return
	}
	return
}
```
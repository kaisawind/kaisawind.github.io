---
layout: post
title:  "golang cgo pinner的使用"
date: 2023-09-06 18:40:59
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
golang cgo pinner的使用
<!--more-->


go 1.21添加了Pinner用于控制cgo中go内存的同步
* 注意： 只能用于控制go中的指针，不能控制c指针。pin时需要将c指针排除。
```golang
func (o *IEC61850) ControlCancelWithShortAddr(sAddr string, ptSelectValue *DataAttributeData, ptParam *ControlParameters) (err error) {
	var pin runtime.Pinner
	defer pin.Unpin()
	cptSelectValue, malloc := gocDataAttributeData(ptSelectValue)
	cptParam := gocControlParameters(ptParam)
	if cptSelectValue.pvData != nil && !malloc {
		pin.Pin(cptSelectValue.pvData)
	}
	if cptParam.operTm != nil {
		pin.Pin(cptParam.operTm)
	}
	pAddr := C.CString(sAddr)
	defer C.free(unsafe.Pointer(pAddr))
	code := C.IEC61850_ControlCancelWithShortAddr(o.iec61850, pAddr, cptSelectValue, cptParam)
	if ErrorCodes(code) != IEC61850_ERROR_NONE {
		err = ErrorCodes(code).Error()
		return
	}
	return
}
```
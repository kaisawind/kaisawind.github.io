---
layout: post
title:  "go的websocket应用"
date: 2021-06-22 09:49:12
categories: [编程语言,golang]
tags: [golang]
excerpt_separator: <!--more-->
---
go的websocket应用
<!--more-->

## 1. 概述
go中会用到websocket,简述一下`github.com/go-swagger/go-swagger`和`github.com/gorilla/websocket`结合使用。

go-swagger会根据swagger文件生成代码的整体结构，能够预定义好很多特性。例如：TLS,middleware等。

websocket在go-swagger中不会预定义，只会被定义为普通http接口，需要对接口重新实现。

## 2. 示例

```go
func (h *Handler) Websocket(params xterm.WebsocketParams) middleware.Responder {
	logrus.Infoln("Websocket", params)
	var upgrade = websocket.Upgrader{
		Subprotocols: []string{"tty"},
	}
	upgrade.CheckOrigin = func(r *http.Request) bool {
		return true
	}
	id := xid.New().String()
	session := fmt.Sprintf("/%s/%s/%s", params.ProductID, params.DeviceName, id)
	chans := make(chan []byte, 10)
	h.sessions.Store(session, chans)
	h.LogSession()
	return middleware.ResponderFunc(func(rw http.ResponseWriter, pr runtime.Producer) {
		defer func() {
			h.sessions.Delete(session)
			close(chans)
			h.LogSession()
		}()
		webConn, err := upgrade.Upgrade(rw, params.HTTPRequest, nil)
		if err != nil || webConn == nil {
			return
		}
		defer webConn.Close()
		logrus.Infoln("webConn", webConn.RemoteAddr())

		var wg sync.WaitGroup
		done := make(chan struct{})
		wg.Add(1)
		go func() {
			defer wg.Done()
			for {
				select {
				case <-done:
					return
				case payload, ok := <-chans:
					if !ok {
						return
					}
					data := append([]byte{byte(Output)}, payload...)
					err = webConn.WriteMessage(websocket.BinaryMessage, data)
					if err != nil {
						logrus.WithError(err).Errorln("WriteMessage error")
						return
					}
				}
			}
		}()
		wg.Add(1)
		go func() {
			defer wg.Done()
			data := []byte{0x30, 0x0d}
			_ = h.ReadMessage(data, params.ProductID, params.DeviceName)
			for {
				_, data, err = webConn.ReadMessage()
				if err != nil {
					done <- struct{}{}
					logrus.WithError(err).Errorln("ReadMessage error")
					return
				}
				err = h.ReadMessage(data, params.ProductID, params.DeviceName)
				if err != nil {
					continue
				}
			}
		}()
		wg.Wait()
	})
}
```

当客户端定义了子协议，服务端也需要进行定义，否则会有1006错误
```go
var upgrade = websocket.Upgrader{
		Subprotocols: []string{"tty"},
	}
```

跨域检查，当跨域时通过检查
```go
upgrade.CheckOrigin = func(r *http.Request) bool {
		return true
	}
```
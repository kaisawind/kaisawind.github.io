---
layout: post
title:  "go mod使用私有库"
date: 2020-06-04 14:11:12 +0800
categories: [编程语言,golang]
tags: [编程语言,golang, git, docker]
excerpt_separator: <!--more-->
---
go mod使用私有库
<!--more-->

Dockerfile
```Dockerfile
FROM golang:alpine AS builder
ARG username
ARG password
ENV GO111MODULE=on
WORKDIR /go/src/dev.yunxing.tech/edgex/app-service-pdiot

RUN sed -e 's/dl-cdn[.]alpinelinux.org/mirrors.aliyun.com/g' -i~ /etc/apk/repositories

# add git for go modules
RUN apk update && apk add make git upx
RUN echo "https://$username:$password@dev.yunxing.tech" > ~/.git-credentials
RUN git config --global credential.helper store
RUN go env -w GOPROXY=https://goproxy.io
RUN go env -w GOPRIVATE=dev.yunxing.tech

COPY . .

RUN make
```

congfig.mk
```Makefile
username := xxxx
password := xxxx
```

Makefile
```Makefile
## include config file ##
file := .config.mk
ifeq ($(file), $(wildcard $(file)))
include $(file)
endif

docker:
	docker buildx build \
		--platform=linux/arm64,linux/amd64 \
		--push \
		--build-arg username=$(username) \
		--build-arg password=$(password) \
		-f scripts/Dockerfile \
		-t csedge/docker-app-service-pdiot:$(DOCKER_TAG) .
```
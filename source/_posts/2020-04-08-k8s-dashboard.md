---
layout: post
title:  "k8s的dashboard使用非安全端口"
date: 2020-04-08 10:34:16
categories: [k8s]
tags: [k8s, linux]
excerpt_separator: <!--more-->
---
k8s的dashboard使用非安全端口
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. dashboard的配置参数](#2-dashboard的配置参数)
- [3. 服务修改](#3-服务修改)
- [4. ingress修改](#4-ingress修改)

<!-- /code_chunk_output -->


## 1. 概述
k8s的dashboard默认使用安全端口，但是nginx-ingress在低版本时需要使用非安全端口进行代理。

## 2. dashboard的配置参数

此时9090为默认的非安全端口
```yaml
        - name: kubernetes-dashboard
          image: 'kubernetesui/dashboard:v2.0.0-beta1'
          args:
            - '--namespace=kubernetes-dashboard'
            - '--enable-insecure-login'
            - '--token-ttl=0'
          ports:
            - containerPort: 8443
              protocol: TCP
            - containerPort: 9090
              protocol: TCP
```

## 3. 服务修改

```yaml
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9090
  selector:
    k8s-app: kubernetes-dashboard
  clusterIP: 10.106.115.173
  type: ClusterIP
  sessionAffinity: None
```

## 4. ingress修改

```yaml
kind: Ingress
apiVersion: extensions/v1beta1
metadata:
  name: dashboard-ingress
  namespace: kubernetes-dashboard
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-body-size: '0'
    nginx.ingress.kubernetes.io/proxy-read-timeout: '600'
    nginx.ingress.kubernetes.io/proxy-redirect-from: /
    nginx.ingress.kubernetes.io/proxy-redirect-to: $location_path/
    nginx.ingress.kubernetes.io/proxy-send-timeout: '600'
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/service-upstream: 'true'
spec:
  rules:
    - http:
        paths:
          - path: /dashboard
            backend:
              serviceName: kubernetes-dashboard
              servicePort: 80
```
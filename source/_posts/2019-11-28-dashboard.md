---
layout: post
title:  "k8s添加dashboard web ui"
date: 2019-11-28 12:05:54 +0800
categories: [k8s]
tags: [k8s, linux]
excerpt_separator: <!--more-->
---
k8s添加dashboard web ui
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 部署dashboard](#1-部署dashboard)
- [2. 创建用户](#2-创建用户)
- [3. 获取token](#3-获取token)
- [4. 替换证书](#4-替换证书)

<!-- /code_chunk_output -->


## 1. 部署dashboard

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta6/aio/deploy/recommended.yaml
```

## 2. 创建用户

创建用户
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
```

修改deployment替换用户
```bash
kubectl edit deployment kubernetes-dashboard -n kubernetes-dashboard
```

```yaml
serviceAccountName: kubernetes-dashboard
serviceAccount: kubernetes-dashboard
```
替换为
```yaml
serviceAccountName: admin-user
serviceAccount: admin-user
```

## 3. 获取token

使用token登录时会用到
```bash
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
```

```bash
Name:         admin-user-token-knszj
Namespace:    kubernetes-dashboard
Labels:       <none>
Annotations:  kubernetes.io/service-account.name: admin-user
              kubernetes.io/service-account.uid: 9261550a-4faf-42d5-82d3-b4af0b988f37

Type:  kubernetes.io/service-account-token

Data
====
ca.crt:     1025 bytes
namespace:  20 bytes
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6ImhCRWFzbzNObVcxLW9EeUZZVnNzLXM4ZnRDZWlYdVhDUXEwM0RhbGNjaGsifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWtuc3pqIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI5MjYxNTUwYS00ZmFmLTQyZDUtODJkMy1iNGFmMGI5ODhmMzciLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.UrZkVn17uOnSR7naFq3i7W1LwCl1meQyOefKaPHZudHEswfdcMhP1vfffPLTl80OLQ4D_3BgKlXly19BgILVCKvXbKc-3RtiSMdqddB48PxIItorwaOVh96ZYJvo6MFNdh_zL1x-QAuVoUrh368VnAqHUGM_ba-7WF1JK3FyRCS097H7B7wbMN9Aa9C_lOoVYn8cawSdE-yRa9LLcEiVLam-EnKSnz3CJUghiW96oj4cyHxSyo4XT2TYBH4xRjMw8rqs4Rg3tS-kL5dHNAY6X-NjmY_BwMAaxMi1lA7FECZYPAx_sQr2A4aqYNWI4CT1bRUhRIBqPpz9KK8RYUsPUA
```

## 4. 替换证书

删除以前的证书
```bash
kubectl delete secret kubernetes-dashboard-certs -n kubernetes-dashboard
```

创建新的证书
```bash
mkdir certs
openssl req -nodes -newkey rsa:2048 -keyout certs/dashboard.key -out certs/dashboard.csr -subj "/C=/ST=/L=/O=/OU=/CN=kubernetes-dashboard"
openssl x509 -req -sha256 -days 365 -in certs/dashboard.csr -signkey certs/dashboard.key -out certs/dashboard.crt
kubectl create secret generic kubernetes-dashboard-certs --from-file=certs -n kubernetes-dashboard
```


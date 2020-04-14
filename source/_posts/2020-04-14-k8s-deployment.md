---
layout: post
title:  "k8s批量更新deployment"
date: 2020-04-14 18:52:16 +0800
categories: [k8s]
tags: [k8s, linux]
excerpt_separator: <!--more-->
---
k8s批量更新deployment
<!--more-->

```bash
kubectl patch deployment $(kubectl get deployment -n iot | grep mns | awk '{print $1}') -n iot -p '{"spec":{"template":{"spec":{"containers":[{"name": "iotx-foundry-mns","image":"docker.io/csiot/iotx-foundry-mns:latest"}]}}}}'
```
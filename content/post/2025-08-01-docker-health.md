---
layout: post
title:  "docker添加health检查"
date: 2025-08-01 10:49:54
categories: [linux,ubuntu,docker]
tags: [ubuntu, docker]
draft: false
excerpt_separator: <!--more-->
---
docker添加health检查
<!--more-->

Dockerfile中添加
```bash
HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost/v1/health || exit 1
```

定义health接口
```yaml
  /v1/health:
    get:
      tags:
      - system
      summary: 获取系统健康状态
      description: 获取系统健康状态
      operationId: GetHealth
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    required:
                    - status
                    type: object
                    properties:
                      status:
                        type: string
                        description: 系统健康状态
                        default: ok
                  error:
                    type: string
                  code:
                    type: integer
                    default: 200
                  success:
                    type: boolean
                    default: true
        "503":
          description: 系统不健康
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      status:
                        type: string
                        description: 系统健康状态
                        default: unhealthy
                  error:
                    type: string
                  code:
                    type: integer
                    default: 503
                  success:
                    type: boolean
                    default: false

```
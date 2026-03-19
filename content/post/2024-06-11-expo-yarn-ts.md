---
layout: post
title:  "yarn创建基于typescript的expo app"
date: 2024-06-11 16:13:42
lastmod: 2026-03-19
categories: [前端,react]
tags: [react]
excerpt_separator: <!--more-->
## 快速创建

使用yarn创建基于TypeScript的Expo应用：

```bash
# 创建项目
yarn create expo-app -t blank-typescript

# 进入项目目录
cd my-app

# 预构建（生成native代码）
yarn expo prebuild

# 安装常用依赖
yarn add expo-system-ui
```

## 可用模板

```bash
blank              # 空白项目
blank-typescript   # TypeScript空白项目（推荐）
tabs               # 带底部导航的项目
tabs-typescript    # TypeScript带导航项目
```

## 开发命令

```bash
# 启动开发服务器
yarn start

# 在iOS模拟器运行
yarn ios

# 在Android模拟器运行
yarn android

# 在Web浏览器运行
yarn web
```

## 项目结构

```
my-app/
├── app.json          # Expo配置
├── App.tsx           # 应用入口
├── tsconfig.json     # TypeScript配置
├── package.json      # 依赖配置
└── src/              # 源代码
    ├── components/
    ├── screens/
    └── utils/
```

## 最佳实践

1. **使用TypeScript**：强类型约束，减少运行时错误
2. **组件化开发**：将UI拆分为可复用的组件
3. **状态管理**：使用Zustand或React Query管理状态

---
yarn创建基于typescript的expo app
<!--more-->

```bash
yarn create expo-app -t blank-typescript
yarn expo prebuild
yarn add expo-system-ui
```
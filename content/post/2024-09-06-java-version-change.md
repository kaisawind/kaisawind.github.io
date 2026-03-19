---
layout: post
title:  "java版本管理"
date: 2024-09-06 13:03:54
lastmod: 2026-03-19
categories: [编程语言,java,ubuntu]
tags: [java,ubuntu]
draft: false
excerpt_separator: <!--more-->
---
java版本管理
<!--more-->

## 基本用法

```bash
# 安装OpenJDK
sudo apt-get update
sudo apt-get install openjdk-11-jdk

# 切换Java版本
sudo update-alternatives --config java
```

## 安装多个Java版本

```bash
# 安装不同版本
sudo apt-get install openjdk-8-jdk
sudo apt-get install openjdk-11-jdk
sudo apt-get install openjdk-17-jdk
sudo apt-get install openjdk-21-jdk

# 查看已安装版本
update-alternatives --list java
```

## 切换Java版本

### 方法1：使用update-alternatives

```bash
# 交互式切换
sudo update-alternatives --config java

# 切换javac编译器
sudo update-alternatives --config javac

# 切换jar
sudo update-alternatives --config jar
```

### 方法2：设置JAVA_HOME

```bash
# 编辑~/.bashrc
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# 生效
source ~/.bashrc
```

### 方法3：使用jenv（推荐）

```bash
# 安装jenv
git clone https://github.com/jenv/jenv.git ~/.jenv

# 配置环境
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(jenv init -)"' >> ~/.bashrc
source ~/.bashrc

# 添加Java版本
jenv add /usr/lib/jvm/java-8-openjdk-amd64
jenv add /usr/lib/jvm/java-11-openjdk-amd64
jenv add /usr/lib/jvm/java-17-openjdk-amd64

# 查看版本
jenv versions

# 设置全局版本
jenv global 11.0

# 设置项目版本
cd myproject
jenv local 8.0
```

## 使用SDKMAN

```bash
# 安装SDKMAN
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# 安装Java版本
sdk install java 11.0.11-open
sdk install java 17.0.1-open
sdk install java 21.0.1-open

# 列出可用版本
sdk list java

# 切换版本
sdk use java 11.0.11-open
sdk default java 17.0.1-open
```

## 验证配置

```bash
# 查看Java版本
java -version

# 查看javac版本
javac -version

# 查看JAVA_HOME
echo $JAVA_HOME

# 查看所有Java相关alternatives
update-alternatives --display java
```

## 项目级版本管理

### 使用Maven

```xml
<properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
</properties>
```

### 使用Gradle

```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(11)
    }
}
```

## 最佳实践

1. **使用jenv或SDKMAN**：便于多版本管理
2. **项目级配置**：在项目中明确Java版本要求
3. **CI/CD一致性**：确保开发环境与CI环境一致
4. **LTS版本**：生产环境优先使用LTS版本（8, 11, 17, 21）
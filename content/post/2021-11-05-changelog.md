---
layout: post
title: "CHANGELOG自动生成"
date: 2021-11-05 16:09:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux, git]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "CHANGELOG 自动生成"
---
CHANGELOG 自动生成
<!--more-->

CHANGELOG 是软件开发中非常重要的文档，用于记录项目每个版本的变更内容。手动维护 CHANGELOG 既繁琐又容易出错，使用自动化工具可以大大提高效率。

## 什么是 CHANGELOG

CHANGELOG 是一个有序的记录文件，包含了项目的每个版本的所有重要变更。良好的 CHANGELOG 应该包括：
- 新增功能
- 修复的 Bug
- 重大变更
- 弃用警告
- 安全更新

## 安装 github_changelog_generator

`github_changelog_generator` 是一个强大的工具，可以根据 GitHub 上的 Issues 和 Pull Requests 自动生成 CHANGELOG。

### 前置要求

- Ruby 环境 (建议使用 2.5 或更高版本)
- GitHub 账户和访问令牌

### 安装步骤

```bash
gem install github_changelog_generator
```

如果遇到权限问题，可以使用 `sudo`：

```bash
sudo gem install github_changelog_generator
```

或者使用 Bundler 管理依赖：

在 Gemfile 中添加：
```ruby
gem 'github_changelog_generator'
```

然后执行：
```bash
bundle install
```

## 配置和使用

### 获取 GitHub Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token" (classic)
3. 选择需要的权限（至少需要 `repo` 权限）
4. 生成并复制 40 位 token

### 基本使用

```bash
export CHANGELOG_GITHUB_TOKEN="«your-40-digit-github-token»"
github_changelog_generator -u kaisawind -p iotx
```

参数说明：
- `-u`: GitHub 用户名或组织名
- `-p`: 仓库名称

### 常用参数

```bash
# 指定输出文件
github_changelog_generator -u kaisawind -p iotx -o CHANGELOG.md

# 指定起始版本
github_changelog_generator -u kaisawind -p iotx --since-tag v1.0.0

# 指定截止版本
github_changelog_generator -u kaisawind -p iotx --future-release v2.0.0

# 包含所有 Issues（默认只包含关闭的）
github_changelog_generator -u kaisawind -p iotx --include-labels bug,enhancement

# 排除特定标签
github_changelog_generator -u kaisawind -p iotx --exclude-labels duplicate,wontfix

# 自定义头部信息
github_changelog_generator -u kaisawind -p iotx --header-label="# 更新日志"

# 指定最大问题数量（避免 API 限流）
github_changelog_generator -u kaisawind -p iotx --max-issues 500
```

### 高级配置文件

创建 `.github_changelog_generator` 配置文件：

```ruby
# .github_changelog_generator
user: "kaisawind"
project: "iotx"
header: "# 更新日志"
exclude-labels: ["duplicate", "question", "invalid", "wontfix", "duplicate", "question", "invalid", "wontfix"]
author: true
issues: true
issue-line-labels: ["bug", "enhancement", "question"]
add-pr-warnings: true
compare-link: true
enhancement-label: ["Enhancement", "Type: Enhancement"]
bug-label: ["Bug", "Type: Bug"]
breaking-label: ["Breaking", "Breaking Change"]
max-issues: 500
```

然后直接运行：

```bash
github_changelog_generator
```

## 标签约定

为了生成更好的 CHANGELOG，建议在 Pull Request 中使用以下标签约定：

- `bug` 或 `Type: Bug`: Bug 修复
- `enhancement` 或 `Type: Enhancement`: 功能增强
- `breaking` 或 `Breaking Change`: 破坏性变更
- `documentation`: 文档更新
- `maintenance`: 维护性变更

## 示例输出

生成的 CHANGELOG.md 格式如下：

```markdown
# 更新日志

## [v2.0.0](https://github.com/kaisawind/iotx/tree/v2.0.0) (2021-11-05)

[Full Changelog](https://github.com/kaisawind/iotx/compare/v1.0.0...v2.0.0)

**Implemented enhancements:**

- Added new feature X [#123](https://github.com/kaisawind/iotx/pull/123)

**Fixed bugs:**

- Fixed memory leak in module Y [#124](https://github.com/kaisawind/iotx/pull/124)

**Merged pull requests:**

- Update documentation [#125](https://github.com/kaisawind/iotx/pull/125)

## [v1.0.0](https://github.com/kaisawind/iotx/tree/v1.0.0) (2021-01-01)

[Full Changelog](https://github.com/kaisawind/iotx/compare/v0.9.0...v1.0.0)

**Implemented enhancements:**

- Initial release [#1](https://github.com/kaisawind/iotx/pull/1)
```

## 常见问题和解决方案

### 1. GitHub API 限流

**问题**: 遇到 `API rate limit exceeded` 错误

**解决方案**:
- 确保 GitHub Token 有正确的权限
- 减少 `--max-issues` 参数值
- 等待一小时后重试（GitHub API 每小时限制 5000 次请求）

### 2. 未找到 Releases

**问题**: 生成的 CHANGELOG 为空或缺少某些版本

**解决方案**:
```bash
# 强制从第一个 tag 开始生成
github_changelog_generator --first-release
```

### 3. SSL 证书错误

**问题**: 证书验证失败

**解决方案**:
```bash
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
```

### 4. 权限问题

**问题**: 无法写入 CHANGELOG 文件

**解决方案**:
```bash
sudo chown $USER:$USER CHANGELOG.md
```

## 最佳实践

1. **定期更新**: 在每次发布新版本后自动生成 CHANGELOG
2. **版本标签**: 为每个版本打上 Git 标签（如 v1.0.0）
3. **Pull Request 标签**: 规范使用标签来分类变更
4. **详细描述**: 在 PR 中提供清晰的变更说明
5. **版本控制**: 将生成的 CHANGELOG.md 提交到版本控制
6. **自动化集成**: 可以在 CI/CD 流程中自动生成 CHANGELOG

## 自动化脚本示例

创建 `generate_changelog.sh`:

```bash
#!/bin/bash

set -e

if [ -z "$CHANGELOG_GITHUB_TOKEN" ]; then
    echo "Error: CHANGELOG_GITHUB_TOKEN environment variable is not set"
    exit 1
fi

# 获取最新版本
LATEST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")

if [ -n "$LATEST_TAG" ]; then
    echo "Generating CHANGELOG since $LATEST_TAG"
    github_changelog_generator --since-tag "$LATEST_TAG" -o CHANGELOG.md
else
    echo "Generating full CHANGELOG"
    github_changelog_generator -o CHANGELOG.md
fi

echo "CHANGELOG generated successfully"
```

使用方法：

```bash
chmod +x generate_changelog.sh
export CHANGELOG_GITHUB_TOKEN="your_token"
./generate_changelog.sh
```

## 其他替代工具

除了 `github_changelog_generator`，还可以考虑：

1. **conventional-changelog**: 基于 Conventional Commits 规范
2. **git-cliff**: 使用 Rust 编写，性能优异
3. **release-drafter**: GitHub Action 自动生成 Release Notes

选择工具时应根据团队习惯和项目需求来决定。

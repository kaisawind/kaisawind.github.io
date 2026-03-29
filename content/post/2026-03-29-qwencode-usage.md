---
layout: post
title:  "QWencode 使用方法指南"
date: 2026-03-29 16:00:00
lastmod: 2026-03-29
categories: [工具, AI]
tags: [AI, 工具]
excerpt_separator: <!--more>-->
author: "kaisawind"
description: "QWencode 是一个轻量级但功能强大的 AI 辅助编程工具，专注于提高开发者的编码效率。本文详细介绍 QWencode 的安装、配置和使用方法。"
---
QWencode 是一个轻量级但功能强大的 AI 辅助编程工具，专注于提高开发者的编码效率。本文详细介绍 QWencode 的安装、配置和使用方法。
<!--more-->

> **提示**: QWencode 持续更新中，建议定期查看官方文档以获取最新功能。

## 什么是 QWencode

QWencode 是一个简洁高效的 AI 编程助手，具有以下特点：

- 🚀 **快速响应**: 优化的性能，秒级响应
- 🎯 **精准理解**: 准确理解开发意图
- 💡 **智能建议**: 提供实用的代码建议
- 🔧 **多语言支持**: 支持 20+ 种编程语言
- 📦 **轻量设计**: 最小化依赖，易于部署
- 🔒 **安全优先**: 本地优先，数据安全有保障

## 安装 QWencode

### 前置要求

- Node.js 16+ 或 Python 3.7+
- API 密钥（OpenAI、Claude 或兼容的 API）
- 终端支持 ANSI 颜色代码

### 通过 npm 安装

```bash
npm install -g qwencode
```

### 通过 pip 安装

```bash
pip install qwencode
```

### 通过 Docker 安装

```bash
docker pull qwencode/qwencode:latest
docker run -it --rm -v $(pwd):/app qwencode/qwencode
```

### 验证安装

```bash
qwencode --version
```

预期输出：
```
QWencode v2.5.0
```

## 初始化配置

### 获取 API 密钥

支持多种 API 服务：

**OpenAI**
1. 访问 [OpenAI API Keys](https://platform.openai.com/api-keys)
2. 创建 API 密钥

**Anthropic Claude**
1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 创建 API 密钥

**其他兼容服务**
- Azure OpenAI
- Google PaLM
- 本地模型（Ollama、LocalAI）

### 初始化配置

```bash
qwencode init
```

按提示完成配置：

```
╔══════════════════════════════════╗
║     QWencode Configuration Wizard      ║
╚══════════════════════════════════╝

Select API Provider:
  1. OpenAI
  2. Anthropic Claude
  3. Azure OpenAI
  4. Custom Endpoint
Enter your choice [1]: 1

Enter API Key: sk-...

Select Model:
  1. gpt-4-turbo (推荐)
  2. gpt-3.5-turbo
  3. gpt-4
Enter your choice [1]: 1

Workspace Directory [/current/dir]: /path/to/project
```

### 配置文件位置

- Linux/macOS: `~/.qwencode/config.yaml`
- Windows: `%USERPROFILE%\.qwencode\config.yaml`

### 手动配置

创建或编辑 `~/.qwencode/config.yaml`：

```yaml
api:
  provider: openai
  apiKey: sk-...
  model: gpt-4-turbo
  baseURL: https://api.openai.com/v1
  temperature: 0.7
  maxTokens: 4096

workspace: /path/to/project

preferences:
  theme: dark
  language: zh-CN
  autoSave: true
  showLineNumbers: true
  
ignore:
  - node_modules
  - dist
  - build
  - .git
  - "*.log"

features:
  codeCompletion: true
  errorDetection: true
  testGeneration: true
  documentation: true
```

## 基本使用

### 启动 QWencode

```bash
cd /path/to/your/project
qwencode
```

### 常用命令

| 命令 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `/read` | `/r` | 读取文件 | `/read src/main.ts` |
| `/write` | `/w` | 写入文件 | `/write new-file.ts` |
| `/edit` | `/e` | 编辑文件 | `/edit package.json` |
| `/search` | `/s` | 搜索代码 | `/s "function" --type js` |
| `/run` | `/` | 运行命令 | `/run npm test` |
| `/diff` | `/d` | 查看差异 | `/diff` |
| `/undo` | `/u` | 撤销修改 | `/undo` |
| `/redo` | `/r` | 重做修改 | `/redo` |
| `/help` | `/h` | 显示帮助 | `/help` |
| `/clear` | `/c` | 清除历史 | `/clear` |
| `/config` | `/cfg` | 显示配置 | `/config` |
| `/exit` | `/q` | 退出 | `/exit` |

### 自然语言交互

```bash
# 用户输入
帮我理解这个项目的架构

# QWencode 响应
项目架构分析：

技术栈：
- 前端：React + TypeScript
- 后端：Node.js + Express
- 数据库：PostgreSQL
- 缓存：Redis

目录结构：
├── src/
│   ├── components/     # React 组件
│   ├── services/       # API 服务
│   ├── utils/          # 工具函数
│   └── types/         # TypeScript 类型定义
├── tests/             # 测试文件
└── docs/              # 文档

核心模块：
- AuthModule: 用户认证
- UserModule: 用户管理
- DataModule: 数据处理
```

## 代码分析

### 项目结构分析

```bash
qwencode
# 输入: 分析项目结构
```

QWencode 会提供：
- 完整的目录树
- 文件类型统计
- 依赖关系图
- 技术栈识别

### 代码复杂度分析

```bash
qwencode
# 输入: 分析 src/utils.js 的复杂度
```

输出示例：
```markdown
代码复杂度报告
==================

函数：processData
- 圈复杂度：12 (高)
- 认知复杂度：8 (中)
- 代码行数：45

问题：
1. 嵌套层级过深（5 层）
2. 多个职责耦合
3. 难以测试

建议：
- 提取子函数降低复杂度
- 使用策略模式替代多重条件
- 增加单元测试覆盖
```

## Bug 修复

### 智能错误诊断

```bash
qwencode
# 输入: 修复这个错误
```

### 示例：修复类型错误

```typescript
// 错误代码
function calculateTotal(items: Item[]) {
  let total = 0;
  for (let item of items) {
    total += item.price;
  }
  return total;
}
```

QWencode 诊断：
```markdown
发现问题：
类型不匹配错误

问题分析：
- total 初始化为 number
- items.price 可能是 string 类型
- TypeScript 编译时无法确定类型

修复方案：
function calculateTotal(items: Item[]) {
  return items.reduce((sum, item) => {
    return sum + Number(item.price);
  }, 0);
}

改进：
- 使用 reduce 更简洁
- 明确类型转换
- 函数式编程风格
```

### 运行时错误修复

```bash
qwencode
# 输入: 运行应用并修复崩溃问题
```

QWencode 会：
1. 分析错误日志
2. 定位问题代码
3. 提供修复方案
4. 验证修复效果

## 功能开发

### 根据需求生成功能

```bash
qwencode
# 输入: 实现用户权限管理功能
```

QWencode 会生成：
- 权限模型定义
- 权限验证中间件
- 角色管理 API
- 数据库迁移文件
- 单元测试用例

### 生成的代码示例

```typescript
// src/auth/permissions.ts
export enum Permission {
  READ_USERS = 'users:read',
  WRITE_USERS = 'users:write',
  DELETE_USERS = 'users:delete',
  ADMIN = 'admin:all'
}

export enum Role {
  USER = 'user',
  MODERATOR = 'moderator',
  ADMIN = 'admin'
}

export const rolePermissions: Record<Role, Permission[]> = {
  [Role.USER]: [Permission.READ_USERS],
  [Role.MODERATOR]: [
    Permission.READ_USERS,
    Permission.WRITE_USERS
  ],
  [Role.ADMIN]: [
    Permission.READ_USERS,
    Permission.WRITE_USERS,
    Permission.DELETE_USERS,
    Permission.ADMIN
  ]
};

export function hasPermission(
  userRole: Role,
  requiredPermission: Permission
): boolean {
  return rolePermissions[userRole].includes(requiredPermission);
}

// src/middleware/permission.ts
import { Request, Response, NextFunction } from 'express';
import { Permission, Role, hasPermission } from '../auth/permissions';

export function requirePermission(permission: Permission) {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = req.user;
    
    if (!user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    
    if (!hasPermission(user.role, permission)) {
      return res.status(403).json({ 
        error: 'Forbidden',
        message: 'Insufficient permissions'
      });
    }
    
    next();
  };
}

// src/routes/users.ts
import express from 'express';
import { requirePermission, Permission } from '../middleware/permission';

const router = express.Router();

router.get(
  '/api/users',
  requirePermission(Permission.READ_USERS),
  async (req, res) => {
    const users = await User.findAll();
    res.json(users);
  }
);

router.post(
  '/api/users',
  requirePermission(Permission.WRITE_USERS),
  async (req, res) => {
    const user = await User.create(req.body);
    res.status(201).json(user);
  }
);

router.delete(
  '/api/users/:id',
  requirePermission(Permission.DELETE_USERS),
  async (req, res) => {
    await User.destroy({ where: { id: req.params.id } });
    res.status(204).send();
  }
);

export default router;
```

## 代码搜索

### 智能代码搜索

```bash
qwencode
# 输入: 搜索所有未使用的变量
```

### 高级搜索模式

```bash
# 搜索代码异味
搜索所有超过 100 行的函数

# 搜索安全问题
查找所有未经验证的用户输入

# 搜索性能问题
查找所有在循环中的数据库查询

# 搜索重复代码
查找重复的代码块
```

## 测试生成

### 自动生成测试

```bash
qwencode
# 输入: 为 AuthService 生成完整的测试
```

### 生成的测试示例

```typescript
// tests/services/auth.test.ts
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { AuthService } from '../../src/services/AuthService';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

describe('AuthService', () => {
  let authService: AuthService;
  let mockDb: any;

  beforeEach(() => {
    mockDb = {
      findUserByEmail: vi.fn(),
      createUser: vi.fn(),
      updateUser: vi.fn()
    };
    authService = new AuthService(mockDb);
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  describe('register', () => {
    it('should register a new user successfully', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'SecurePass123!'
      };
      
      mockDb.findUserByEmail.mockResolvedValue(null);
      mockDb.createUser.mockResolvedValue({
        id: '1',
        email: userData.email,
        role: 'user'
      });

      const result = await authService.register(userData);

      expect(result).toHaveProperty('id');
      expect(result.email).toBe(userData.email);
      expect(mockDb.createUser).toHaveBeenCalledWith(
        expect.objectContaining({
          email: userData.email
        })
      );
    });

    it('should hash password before storing', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'password123'
      };
      
      mockDb.findUserByEmail.mockResolvedValue(null);
      const hashSpy = vi.spyOn(bcrypt, 'hash');
      
      await authService.register(userData);

      expect(hashSpy).toHaveBeenCalledWith(
        userData.password,
        expect.any(Number)
      );
    });

    it('should throw error if email already exists', async () => {
      const userData = {
        email: 'existing@example.com',
        password: 'password123'
      };
      
      mockDb.findUserByEmail.mockResolvedValue({
        email: userData.email
      });

      await expect(authService.register(userData))
        .rejects.toThrow('Email already registered');
    });

    it('should validate email format', async () => {
      const userData = {
        email: 'invalid-email',
        password: 'password123'
      };

      await expect(authService.register(userData))
        .rejects.toThrow('Invalid email format');
    });

    it('should validate password strength', async () => {
      const userData = {
        email: 'test@example.com',
        password: '123'
      };

      await expect(authService.register(userData))
        .rejects.toThrow('Password too weak');
    });
  });

  describe('login', () => {
    it('should authenticate user with valid credentials', async () => {
      const credentials = {
        email: 'test@example.com',
        password: 'password123'
      };
      
      const mockUser = {
        id: '1',
        email: credentials.email,
        password: await bcrypt.hash(credentials.password, 10)
      };
      
      mockDb.findUserByEmail.mockResolvedValue(mockUser);
      
      const result = await authService.login(credentials);

      expect(result).toHaveProperty('token');
      expect(result).toHaveProperty('user');
      expect(result.user.email).toBe(credentials.email);
    });

    it('should throw error for invalid credentials', async () => {
      const credentials = {
        email: 'test@example.com',
        password: 'wrongpassword'
      };
      
      const mockUser = {
        id: '1',
        email: credentials.email,
        password: await bcrypt.hash('correctpassword', 10)
      };
      
      mockDb.findUserByEmail.mockResolvedValue(mockUser);

      await expect(authService.login(credentials))
        .rejects.toThrow('Invalid credentials');
    });

    it('should throw error for non-existent user', async () => {
      const credentials = {
        email: 'nonexistent@example.com',
        password: 'password123'
      };
      
      mockDb.findUserByEmail.mockResolvedValue(null);

      await expect(authService.login(credentials))
        .rejects.toThrow('User not found');
    });
  });

  describe('verifyToken', () => {
    it('should verify valid token', async () => {
      const mockUser = { id: '1', email: 'test@example.com' };
      const token = jwt.sign(mockUser, process.env.JWT_SECRET!);
      
      const result = await authService.verifyToken(token);

      expect(result).toEqual(mockUser);
    });

    it('should throw error for invalid token', async () => {
      await expect(authService.verifyToken('invalid-token'))
        .rejects.toThrow('Invalid token');
    });

    it('should throw error for expired token', async () => {
      const mockUser = { id: '1', email: 'test@example.com' };
      const token = jwt.sign(
        mockUser, 
        process.env.JWT_SECRET!,
        { expiresIn: '-1h' }
      );

      await expect(authService.verifyToken(token))
        .rejects.toThrow('Token expired');
    });
  });
});
```

## 最佳实践

### 1. 明确的需求描述

✅ 好的提示：
```
实现一个 REST API 端点，用于：
- 创建新用户（验证邮箱格式）
- 更新用户信息（需要认证）
- 删除用户（需要管理员权限）
- 查询用户列表（分页、排序）
```

❌ 不好的提示：
```
实现用户 API
```

### 2. 逐步迭代

```bash
# 分步骤实现
第一步：创建数据库模型
第二步：实现基础 CRUD
第三步：添加认证和授权
第四步：添加输入验证
第五步：编写测试
第六步：编写文档
```

### 3. 充分的上下文

```bash
# 提供相关文件
先读取 package.json 了解项目配置
然后读取 tsconfig.json 了解类型配置
最后实现新的 API 端点
```

### 4. 验证和测试

```bash
# 每次修改后验证
修改后运行：npm test
确保所有测试通过
```

## 高级功能

### 1. 代码重构

```bash
qwencode
# 输入: 重构这段代码，应用设计模式
```

### 2. 性能优化

```bash
qwencode
# 输入: 优化这段代码的性能
```

优化示例：
```javascript
// 优化前
function findUsersByName(users, name) {
  const results = [];
  for (let i = 0; i < users.length; i++) {
    if (users[i].name.toLowerCase().includes(name.toLowerCase())) {
      results.push(users[i]);
    }
  }
  return results;
}

// 优化后
function findUsersByName(users, name) {
  const searchTerm = name.toLowerCase();
  return users.filter(user => 
    user.name.toLowerCase().includes(searchTerm)
  );
}

// 进一步优化（如果多次搜索）
class UserSearcher {
  constructor(users) {
    this.index = new Map();
    users.forEach(user => {
      const key = user.name.toLowerCase();
      if (!this.index.has(key)) {
        this.index.set(key, []);
      }
      this.index.get(key).push(user);
    });
  }
  
  search(name) {
    return this.index.get(name.toLowerCase()) || [];
  }
}
```

### 3. 代码文档生成

```bash
qwencode
# 输入: 为这个模块生成 JSDoc 文档
```

### 4. 代码迁移

```bash
qwencode
# 输入: 将这段代码迁移到 TypeScript
```

## 配置文件详解

### .qwencodeignore

```
# 依赖目录
node_modules/
dist/
build/
.target/

# 敏感文件
.env
.env.local
*.key
*.pem
secrets/

# 日志
*.log
logs/
npm-debug.log*
yarn-debug.log*

# IDE 和编辑器
.vscode/
.idea/
*.swp
*.swo
*~

# 操作系统
.DS_Store
Thumbs.db

# 临时文件
*.tmp
.cache/
*.bak
```

### config.yaml 完整配置

```yaml
# API 配置
api:
  provider: openai              # openai, anthropic, azure, custom
  apiKey: sk-...             # API 密钥
  model: gpt-4-turbo          # 模型名称
  baseURL: https://api.openai.com/v1  # API 端点
  temperature: 0.7            # 生成温度 (0-2)
  maxTokens: 4096            # 最大 token 数
  timeout: 60000             # 请求超时（毫秒）

# 工作空间配置
workspace: /path/to/project    # 项目根目录
watch: true                   # 监控文件变化
autoSave: true               # 自动保存

# 界面偏好
preferences:
  theme: dark                 # light, dark, auto
  language: zh-CN            # 界面语言
  showLineNumbers: true      # 显示行号
  syntaxHighlight: true       # 语法高亮
  fontSize: 14              # 字体大小

# 忽略模式
ignore:
  - node_modules
  - dist
  - build
  - .git
  - "*.log"
  - "*.tmp"

# 功能开关
features:
  codeCompletion: true       # 代码补全
  errorDetection: true        # 错误检测
  testGeneration: true       # 测试生成
  documentation: true        # 文档生成
  refactoring: true         # 重构建议
  securityScan: false       # 安全扫描

# 集成配置
integrations:
  git:
    enabled: true
    autoCommit: false       # 自动提交
    commitTemplate: |       # 提交信息模板
      {{type}}: {{message}}
  github:
    enabled: false
    token: ghp_...
    createPR: false
  gitlab:
    enabled: false
    token: glpat-...
  jira:
    enabled: false
    url: https://your-domain.atlassian.net
    token: ...

# 性能配置
performance:
  cacheEnabled: true         # 启用缓存
  cacheSize: 100           # 缓存大小 (MB)
  parallelRequests: 3       # 并发请求数
  streamResponse: false      # 流式响应

# 日志配置
logging:
  level: info              # debug, info, warn, error
  file: ~/.qwencode/logs/qwencode.log
  maxFileSize: 10          # MB
  maxFiles: 5
```

## 常见问题

### Q: QWencode 支持哪些 API 提供商？

A: QWencode 支持多种 API 提供商：
- OpenAI (GPT-3.5, GPT-4)
- Anthropic Claude
- Azure OpenAI
- Google PaLM
- 本地模型（Ollama, LocalAI）
- 自定义兼容 API

### Q: 如何提高代码质量？

A: 
- 使用具体的需求描述
- 要求 QWencode 解释代码
- 让它生成测试用例
- 应用它的重构建议
- 使用代码审查功能

### Q: 数据安全如何保障？

A:
- 默认不存储代码到云端
- API 通信使用 HTTPS
- 支持 API 密钥加密存储
- 完全离线模式（使用本地模型）
- 详细的安全审计日志

### Q: 如何处理大型项目？

A:
- 使用 `.qwencodeignore` 排除不必要的文件
- 分模块处理
- 使用缓存功能
- 使用 `--context-limit` 控制上下文大小
- 定期清理缓存

### Q: QWencode 与其他工具的区别？

A:
- 更快的响应速度（优化的性能）
- 更轻量的设计（最小依赖）
- 更灵活的 API 集成
- 更好的本地化支持
- 更详细的自定义选项

## 性能优化

### 1. 启用缓存

```bash
qwencode --cache
```

### 2. 使用本地模型

```yaml
# config.yaml
api:
  provider: local
  baseURL: http://localhost:11434/api  # Ollama
  model: codellama:7b
```

### 3. 批量操作

```bash
# 一次性处理多个任务
生成所有组件的测试和文档
```

### 4. 调整并发数

```yaml
# config.yaml
performance:
  parallelRequests: 5  # 根据网络情况调整
```

### 5. 使用流式响应

```yaml
# config.yaml
performance:
  streamResponse: true  # 更快的响应
```

## IDE 集成

### VS Code 扩展

1. 安装 "QWencode" 扩展
2. 配置 API 密钥
3. 自定义快捷键：

```json
// settings.json
{
  "qwencode.apiKey": "sk-...",
  "qwencode.model": "gpt-4-turbo",
  "qwencode.shortcuts": {
    "openPanel": "ctrl+shift+q",
    "explainCode": "ctrl+shift+e",
    "fixCode": "ctrl+shift+f",
    "generateTest": "ctrl+shift+t"
  }
}
```

### JetBrains 插件

1. 在插件市场搜索 "QWencode"
2. 安装并重启
3. 配置：
   - File → Settings → Tools → QWencode
   - 输入 API 密钥
   - 选择模型

### Vim/Neovim

```vim
" .vimrc
" 打开 QWencode
nnoremap <leader>qc :QWencode<CR>

" 解释选中代码
vnoremap <leader>qe :QWencodeExplain<CR>

" 修复选中代码
vnoremap <leader>qf :QWencodeFix<CR>

" 生成测试
vnoremap <leader>qt :QWencodeTest<CR>
```

### Emacs

```elisp
;; .emacs
(require 'qwencode)

(define-key global-map (kbd "C-c q") 'qwencode-open)
(define-key global-map (kbd "C-c e") 'qwencode-explain)
(define-key global-map (kbd "C-c f") 'qwencode-fix)
(define-key global-map (kbd "C-c t") 'qwencode-test)
```

### Sublime Text

```python
# ~/.config/sublime-text-3/Packages/User/qwencode.sublime-keymap
[
  {
    "keys": ["ctrl+shift+q"],
    "command": "qwencode_open_panel"
  },
  {
    "keys": ["ctrl+shift+e"],
    "command": "qwencode_explain"
  },
  {
    "keys": ["ctrl+shift+f"],
    "command": "qwencode_fix"
  }
]
```

## 团队协作

### 共享配置

创建团队配置文件：

```yaml
# .qwencode/team-config.yaml
team:
  name: "Development Team"
  codingStyle:
    indentation: 2
    quotes: single
    semicolons: true
    trailingComma: es5
  reviewGuidelines:
    requireTests: true
    requireDocs: true
    maxComplexity: 15
    enforceLinting: true
  namingConventions:
    variables: camelCase
    functions: camelCase
    classes: PascalCase
    constants: UPPER_SNAKE_CASE
    privatePrefix: _
```

### CI/CD 集成

```yaml
# .github/workflows/qwencode-review.yml
name: QWencode Code Review

on:
  pull_request:
    branches: [main]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install QWencode
        run: npm install -g qwencode
      
      - name: Run Code Review
        env:
          QWENCODE_API_KEY: ${{ secrets.QWENCODE_API_KEY }}
        run: |
          qwencode review \
            --pr-number ${{ github.event.number }} \
            --output review-report.md
      
      - name: Comment Review
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('review-report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

## 工作流程示例

### 场景 1：从零开发新功能

```bash
# 1. 启动 QWencode
qwencode

# 2. 需求分析
帮我实现一个任务管理功能，包括：
- 创建任务
- 更新任务状态
- 删除任务
- 任务列表查询（支持筛选和排序）
- 任务分配

# 3. 数据库设计
生成任务的数据库模型

# 4. API 实现
实现 REST API 端点

# 5. 前端实现
生成 React 组件

# 6. 测试生成
为所有功能生成测试

# 7. 运行测试
/run npm test

# 8. 修复问题
修复测试失败的问题

# 9. 文档生成
生成 API 文档
```

### 场景 2：调试复杂 Bug

```bash
# 1. 描述问题
用户报告：批量导入用户时偶尔失败，错误信息不明确

# 2. 代码分析
分析 src/services/userImport.ts

# 3. 诊断问题
找出潜在的竞争条件和异常处理问题

# 4. 修复代码
应用修复方案

# 5. 添加日志
添加详细的错误日志

# 6. 测试验证
创建测试用例验证修复

# 7. 性能优化
优化批量导入性能
```

### 场景 3：代码审查和重构

```bash
# 1. 审查代码
审查 src/utils/ 目录下的所有代码

# 2. 分析报告
# QWencode 提供详细的审查报告：
# - 代码风格
# - 潜在问题
# - 性能建议
# - 重构建议

# 3. 应用建议
逐步应用重构建议

# 4. 验证效果
确保重构后功能正常
```

## 高级技巧

### 1. 使用模板

创建自定义代码模板：

```yaml
# .qwencode/templates/rest-api.yaml
name: REST API Endpoint
description: Generate a REST API endpoint with authentication
files:
  - path: "src/routes/{{name}}.ts"
    template: |
      import express from 'express';
      import { authenticate } from '../middleware/auth';
      
      const router = express.Router();
      
      router.post('/api/{{name}}s', authenticate, async (req, res) => {
        // Implementation
      });
      
      router.get('/api/{{name}}s/:id', authenticate, async (req, res) => {
        // Implementation
      });
      
      export default router;
  - path: "tests/{{name}}.test.ts"
    template: |
      import { describe, it, expect } from 'vitest';
      
      describe('{{name}} API', () => {
        // Tests
      });
```

使用模板：
```bash
qwencode template --name rest-api --variable name=product
```

### 2. 自定义命令

在 `config.yaml` 中定义自定义命令：

```yaml
customCommands:
  deploy:
    description: 部署应用到生产环境
    steps:
      - run: npm run build
      - run: docker build -t myapp .
      - run: docker push myapp:latest
      - run: kubectl set image deployment/myapp myapp=myapp:latest
  
  setup:
    description: 初始化开发环境
    steps:
      - run: npm install
      - run: npm run db:migrate
      - run: cp .env.example .env
```

使用自定义命令：
```bash
qwencode deploy
qwencode setup
```

### 3. 批量处理

```bash
# 批量生成测试
qwencode batch --pattern "src/**/*.ts" --action generate-tests

# 批量重构
qwencode batch --pattern "src/**/*.js" --action refactor

# 批量文档生成
qwencode batch --pattern "src/**/*.ts" --action generate-docs
```

### 4. 集成 Git Hooks

```bash
# 安装 git hooks
qwencode git-hooks install

# 这会创建：
# - pre-commit: 自动检查代码
# - pre-push: 运行测试
# - commit-msg: 验证提交信息
```

## 总结

QWencode 是一个强大且灵活的 AI 编程助手，可以显著提升开发效率。关键要点：

- ✅ **明确需求**: 提供清晰、具体的需求
- ✅ **提供上下文**: 让 QWencode 了解项目
- ✅ **逐步迭代**: 分步骤实现功能
- ✅ **验证结果**: 测试每次修改
- ✅ **利用特性**: 使用模板、自定义命令等高级功能
- ✅ **团队协作**: 使用共享配置和 CI/CD 集成

## 相关资源

- [QWencode 官方文档](https://qwencode.dev/docs)
- [GitHub 仓库](https://github.com/qwencode/qwencode)
- [问题反馈](https://github.com/qwencode/qwencode/issues)
- [社区讨论](https://github.com/qwencode/qwencode/discussions)
- [示例项目](https://github.com/qwencode/examples)
- [API 文档](https://api.qwencode.dev)
- [插件市场](https://plugins.qwencode.dev)
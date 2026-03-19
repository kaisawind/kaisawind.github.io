#!/usr/bin/env python3
"""
扩充简短的博客文章
"""

import os
from pathlib import Path

# 简短文章扩充内容模板
EXPANSIONS = {
    "2024-10-10-flathub.md": """
## 问题背景

Flathub是Flatpak的官方应用仓库，但在中国大陆访问速度较慢。使用国内镜像源可以大幅提升下载速度。

## 配置镜像源

### 上交镜像源（推荐）

```bash
sudo flatpak remote-modify flathub --url=https://mirror.sjtu.edu.cn/flathub
```

### 其他可用镜像源

```bash
# 上交镜像
sudo flatpak remote-modify flathub --url=https://mirror.sjtu.edu.cn/flathub

# 清华镜像
sudo flatpak remote-modify flathub --url=https://mirrors.tuna.tsinghua.edu.cn/flathub

# 中科大镜像
sudo flatpak remote-modify flathub --url=https://mirrors.ustc.edu.cn/flathub
```

## Flatpak基本使用

### 安装Flatpak

Ubuntu/Debian：
```bash
sudo apt update
sudo apt install flatpak
```

### 搜索和安装应用

```bash
# 搜索应用
flatpak search <app-name>

# 安装应用
flatpak install flathub <app-id>

# 常用应用示例
flatpak install flathub com.visualstudio.code  # VSCode
flatpak install flathub com.spotify.Client     # Spotify
```

### 管理已安装应用

```bash
# 列出已安装的应用
flatpak list

# 更新所有应用
flatpak update

# 卸载应用
flatpak uninstall <app-id>

# 清理未使用的运行时
flatpak uninstall --unused
```

## 最佳实践

1. **使用镜像源**：配置国内镜像源加速下载
2. **定期更新**：使用`flatpak update`保持应用最新
3. **清理空间**：定期运行`flatpak uninstall --unused`
""",
    "2024-06-11-expo-yarn-ts.md": """
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
""",
    "2021-10-09-chrome.md": """
## 问题背景

Chrome浏览器默认会阻止某些非标准端口的访问，这是为了防止安全风险。当尝试访问这些端口时会显示"ERR_UNSAFE_PORT"错误。

## 解决方法

### 方法1：允许特定端口（推荐）

启动Chrome时添加允许的端口参数：

```bash
# Linux
google-chrome-stable --explicitly-allowed-ports=80,10080

# macOS
/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --explicitly-allowed-ports=80,10080

# Windows
chrome.exe --explicitly-allowed-ports=80,10080
```

### 方法2：修改端口

将服务改为使用标准端口（80, 443, 8080等）。

### 方法3：使用其他浏览器

某些浏览器对端口限制较宽松，可以尝试使用Firefox等浏览器。

## Chrome默认禁止的端口

Chrome默认禁止以下端口：
- 7 (echo)
- 9 (discard)
- 11 (systat)
- 13 (daytime)
- 15 (netstat)
- 17 (qotd)
- 19 (chargen)
- 20 (ftp data)
- 21 (ftp control)
- 22 (ssh)
- 23 (telnet)
- 25 (smtp)
- 37 (time)
- 42 (name)
- 43 (nicname)
- 53 (domain)
- 77 (priv-rjs)
- 79 (finger)
- 87 (ttylink)
- 95 (supdup)
- 101 (hostriame)
- 102 (iso-tsap)
- 103 (gppitnp)
- 104 (acr-nema)
- 109 (pop2)
- 110 (pop3)
- 111 (sunrpc)
- 113 (auth)
- 115 (sftp)
- 117 (uucp-path)
- 119 (nntp)
- 123 (ntp)
- 135 (loc-srv/epmap)
- 139 (netbios)
- 143 (imap2)
- 179 (bgp)
- 389 (ldap)
- 465 (smtp+ssl)
- 512 (print/exec)
- 513 (login)
- 514 (shell)
- 515 (printer)
- 526 (tempo)
- 530 (courier)
- 531 (chat)
- 532 (netnews)
- 540 (uucp)
- 556 (remotefs)
- 563 (nntp+ssl)
- 587 (smtp+tls)
- 601 (syslog-conn)
- 636 (ldap+ssl)
- 993 (imap+ssl)
- 995 (pop3+ssl)
- 2049 (nfs)
- 3659 (apple-sasl)
- 4045 (lockd)
- 6000 (x11)
- 6665-6669 (irc)
- 6697 (irc+ssl)

## 安全建议

1. **避免使用非标准端口**：尽量使用标准的HTTP/HTTPS端口
2. **生产环境**：在生产环境中配置反向代理使用标准端口
3. **开发环境**：仅在开发环境允许特定端口
""",
    "2020-11-30-golang-md5.md": """
## 快速使用

```go
package main

import (
    "crypto/md5"
    "encoding/hex"
    "fmt"
)

func main() {
    // 方法1：使用fmt.Sprintf
    data := []byte("hello world")
    hash := md5.Sum(data)
    hashStr := fmt.Sprintf("%x", hash)
    fmt.Println(hashStr)
    
    // 方法2：使用hex.EncodeToString
    hashStr2 := hex.EncodeToString(hash[:])
    fmt.Println(hashStr2)
}
```

## 封装MD5函数

```go
package main

import (
    "crypto/md5"
    "encoding/hex"
)

// MD5 计算字符串的MD5哈希值
func MD5(str string) string {
    hash := md5.Sum([]byte(str))
    return hex.EncodeToString(hash[:])
}

// MD5Bytes 计算字节切片的MD5哈希值
func MD5Bytes(data []byte) string {
    hash := md5.Sum(data)
    return hex.EncodeToString(hash[:])
}

// MD5File 计算文件的MD5哈希值
func MD5File(filePath string) (string, error) {
    data, err := os.ReadFile(filePath)
    if err != nil {
        return "", err
    }
    return MD5Bytes(data), nil
}
```

## 大文件MD5计算

```go
func MD5LargeFile(filePath string) (string, error) {
    file, err := os.Open(filePath)
    if err != nil {
        return "", err
    }
    defer file.Close()
    
    hash := md5.New()
    if _, err := io.Copy(hash, file); err != nil {
        return "", err
    }
    
    return hex.EncodeToString(hash.Sum(nil)), nil
}
```

## 使用场景

1. **文件校验**：验证文件完整性
2. **密码存储**：不推荐，建议使用bcrypt
3. **数据去重**：基于哈希值判断数据是否相同
4. **缓存键**：生成唯一标识符

## 注意事项

> **安全警告**: MD5已被证明存在碰撞漏洞，不应用于安全敏感场景。对于密码存储，建议使用bcrypt或argon2。

1. **不适用于密码**：使用bcrypt或argon2替代
2. **存在碰撞风险**：不同输入可能产生相同输出
3. **性能考虑**：MD5速度较快，适合非安全场景
""",
}


def expand_article(filepath):
    """扩充单篇文章"""
    filename = os.path.basename(filepath)

    if filename not in EXPANSIONS:
        return False, "无扩充模板"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 找到<!--more-->位置
        if "<!--more-->" not in content:
            return False, "无more标记"

        # 检查是否已经扩充
        if "## 问题背景" in content or "## 快速使用" in content:
            return False, "已扩充"

        # 插入扩充内容
        parts = content.split("<!--more-->", 1)
        new_content = parts[0] + "<!--more-->" + EXPANSIONS[filename] + parts[1]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True, "已扩充"

    except Exception as e:
        return False, f"错误: {str(e)}"


def main():
    post_dir = Path("content/post")

    # 处理指定文章
    for filename in EXPANSIONS.keys():
        filepath = post_dir / filename
        if filepath.exists():
            success, message = expand_article(filepath)
            print(f"{'✓' if success else '✗'} {filename}: {message}")


if __name__ == "__main__":
    main()

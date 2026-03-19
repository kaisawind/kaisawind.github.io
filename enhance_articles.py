#!/usr/bin/env python3
"""
智能博客文章更新工具
自动检测和更新过时的技术内容
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

# 定义更新规则
UPDATE_RULES = {
    # 链接更新
    "links": [
        (r"https?://golang\.org/(?!doc/)", "https://go.dev/"),
        (r"https?://golang\.org/doc/", "https://go.dev/doc/"),
        (r"https?://blog\.golang\.org/", "https://go.dev/blog/"),
    ],
    # 版本警告（根据关键词添加）
    "version_warnings": {
        "k8s": {
            "pattern": r"kubeadm.*?(?:init|install)",
            "versions": ["1.16", "1.17", "1.18", "1.19", "1.20"],
            "message": "> **注意**: Kubernetes版本更新较快，建议使用最新的稳定版本。",
        },
        "docker": {
            "pattern": r"docker\s+(?:run|build|pull)",
            "old_commands": ["docker rmi", "docker rm", "docker images"],
            "message": "> **提示**: Docker命令已更新，推荐使用 `docker image` 和 `docker container` 子命令。",
        },
    },
    # 代码块语言标记
    "code_blocks": [
        (r"```mongo\n", "```javascript\n"),  # MongoDB shell使用JavaScript
        (r"```golang\n", "```go\n"),  # 标准化Go语言标记
        (r"```shell\n", "```bash\n"),  # 统一使用bash
    ],
    # 命令更新
    "commands": {
        "docker": [
            (r"docker rmi \$\(docker images", "docker image prune"),
            (r"docker rm \$\(docker ps", "docker container prune"),
        ]
    },
}


def add_version_warning(content, title):
    """为过时内容添加版本警告"""
    warnings = []

    # 检查Kubernetes版本
    if "k8s" in title.lower() or "kubernetes" in title.lower():
        if re.search(r"\d+\.\d+", title):
            warnings.append(
                "> **注意**: Kubernetes版本更新较快，建议参考[官方文档](https://kubernetes.io/docs/setup/)使用最新版本。"
            )

    # 检查Docker相关
    if "docker" in title.lower():
        if "docker-compose" not in title.lower():
            warnings.append(
                "> **提示**: Docker已推出新的命令结构，建议使用 `docker image` 和 `docker container` 子命令。"
            )

    return warnings


def update_links(content):
    """更新过时的链接"""
    for pattern, replacement in UPDATE_RULES["links"]:
        content = re.sub(pattern, replacement, content)
    return content


def update_code_blocks(content):
    """更新代码块标记"""
    for pattern, replacement in UPDATE_RULES["code_blocks"]:
        content = re.sub(pattern, replacement, content)
    return content


def enhance_article(filepath):
    """增强文章内容"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content
        changes = []

        # 提取front matter
        if not content.startswith("---"):
            return False, "No front matter"

        parts = content.split("---", 2)
        if len(parts) < 3:
            return False, "Invalid front matter"

        front_matter = parts[1]
        body = parts[2]

        # 提取标题
        title_match = re.search(r'title:\s*"?([^"\n]+)"?', front_matter)
        title = title_match.group(1) if title_match else ""

        # 更新链接
        new_body = update_links(body)
        if new_body != body:
            changes.append("更新过时链接")
            body = new_body

        # 更新代码块
        new_body = update_code_blocks(body)
        if new_body != body:
            changes.append("标准化代码块标记")
            body = new_body

        # 检查是否需要添加版本警告
        if not body.strip().startswith(">") and not body.strip().startswith("##"):
            warnings = add_version_warning(body, title)
            if warnings:
                # 在<!--more-->后添加警告
                if "<!--more-->" in body:
                    body = body.replace(
                        "<!--more-->", "<!--more-->\n\n" + "\n\n".join(warnings) + "\n"
                    )
                    changes.append("添加版本警告")

        if changes:
            new_content = f"---{front_matter}---{body}"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, ", ".join(changes)

        return False, "No changes needed"

    except Exception as e:
        return False, f"Error: {str(e)}"


def process_year(year):
    """处理指定年份的所有文章"""
    post_dir = Path("content/post")
    pattern = f"{year}-*.md"
    files = sorted(post_dir.glob(pattern))

    print(f"\n处理 {year} 年文章 ({len(files)} 篇)...")

    updated = 0
    for filepath in files:
        success, message = enhance_article(filepath)
        if success:
            updated += 1
            print(f"  ✓ {filepath.name}: {message}")

    return updated


if __name__ == "__main__":
    if len(sys.argv) > 1:
        year = sys.argv[1]
        process_year(year)
    else:
        # 处理所有年份
        for year in range(2019, 2027):
            process_year(year)

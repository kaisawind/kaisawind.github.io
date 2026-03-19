#!/usr/bin/env python3
"""
批量内容增强工具
针对不同技术主题进行内容增强
"""

import os
import re
from pathlib import Path

# 技术主题增强规则
TOPIC_ENHANCEMENTS = {
    "redis": {
        "keywords": ["redis", "reids"],
        "additions": [
            "> **提示**: Redis已发布7.x版本，带来了许多新特性。建议参考官方文档了解最新功能。"
        ],
    },
    "mysql": {
        "keywords": ["mysql"],
        "additions": [
            "> **注意**: MySQL 8.0已成为主流版本，本文档可能基于旧版本编写。"
        ],
    },
    "mongodb": {
        "keywords": ["mongo"],
        "additions": [
            "> **提示**: MongoDB已发布7.x版本，支持时序集合、变更流等新特性。"
        ],
    },
    "nginx": {
        "keywords": ["nginx"],
        "additions": ["> **提示**: Nginx已支持HTTP/3和QUIC协议。"],
    },
    "ffmpeg": {
        "keywords": ["ffmpeg"],
        "additions": ["> **提示**: FFmpeg版本更新较快，建议使用最新稳定版。"],
    },
    "rust": {
        "keywords": ["rust", "cargo"],
        "additions": [
            "> **提示**: Rust每6周发布一个新版本，建议使用`rustup`保持最新。"
        ],
    },
    "flutter": {
        "keywords": ["flutter"],
        "additions": ["> **注意**: Flutter版本更新频繁，API可能有变化。"],
    },
    "vue": {
        "keywords": ["vue"],
        "additions": ["> **提示**: Vue 3已成为默认版本，本文档可能基于Vue 2编写。"],
    },
    "react": {
        "keywords": ["react"],
        "additions": ["> **提示**: React 18引入了并发特性，建议使用函数组件和Hooks。"],
    },
    "python": {
        "keywords": ["python"],
        "additions": ["> **提示**: Python 3.12已发布，建议使用Python 3.8+版本。"],
    },
    "linux": {
        "keywords": ["linux", "centos", "ubuntu", "debian"],
        "additions": ["> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。"],
    },
}


def should_add_topic_warning(content, topic):
    """检查是否应该添加主题警告"""
    keywords = TOPIC_ENHANCEMENTS[topic]["keywords"]
    title = content.split("\n")[0:10]
    title_str = " ".join(title).lower()

    for keyword in keywords:
        if keyword in title_str:
            # 检查是否已经有警告
            if not content.startswith("> **", 10) and "> **提示" not in content[:500]:
                return True
    return False


def enhance_topic_content(filepath):
    """增强主题内容"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 检查是否已经有版本警告
        if "> **注意" in content or "> **提示" in content:
            return False, "已有版本警告"

        # 分割front matter和body
        if not content.startswith("---"):
            return False, "无front matter"

        parts = content.split("---", 2)
        if len(parts) < 3:
            return False, "格式错误"

        front_matter = parts[1]
        body = parts[2]

        # 提取标题
        title_match = re.search(r'title:\s*"?([^"\n]+)"?', front_matter)
        title = title_match.group(1).lower() if title_match else ""

        # 检查主题
        additions = []
        for topic, config in TOPIC_ENHANCEMENTS.items():
            for keyword in config["keywords"]:
                if keyword in title:
                    additions = config["additions"]
                    break
            if additions:
                break

        if not additions:
            return False, "无需增强"

        # 在<!--more-->后添加警告
        if "<!--more-->" in body:
            enhanced_body = body.replace(
                "<!--more-->", "<!--more-->\n\n" + "\n\n".join(additions) + "\n"
            )
            new_content = f"---{front_matter}---{enhanced_body}"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            return True, f"添加{topic}主题提示"

        return False, "无<!--more-->标记"

    except Exception as e:
        return False, f"错误: {str(e)}"


def process_all_posts():
    """处理所有文章"""
    post_dir = Path("content/post")
    md_files = sorted(post_dir.glob("*.md"))

    print(f"处理所有文章 ({len(md_files)} 篇)...")

    updated = 0
    skipped = 0

    for filepath in md_files:
        success, message = enhance_topic_content(filepath)
        if success:
            updated += 1
            print(f"  ✓ {filepath.name}: {message}")
        else:
            skipped += 1

    print(f"\n总计: 更新 {updated} 篇, 跳过 {skipped} 篇")
    return updated


if __name__ == "__main__":
    process_all_posts()

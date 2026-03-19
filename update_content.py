#!/usr/bin/env python3
"""
自动更新博客文章中的过时内容
"""

import os
import re
from pathlib import Path

# 定义替换规则
REPLACEMENTS = [
    # 更新golang链接
    (r"https://golang\.org/", "https://go.dev/"),
    # 更新Docker Hub链接
    (r"docker\.io", "docker.io"),
    # 更新Kubernetes链接
    (
        r"https?://kubernetes\.io/docs/setup/independent/",
        "https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/",
    ),
]


def process_file(filepath):
    """处理单个文件"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        modified = False

        for pattern, replacement in REPLACEMENTS:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True, "Updated"

        return False, "No changes needed"
    except Exception as e:
        return False, str(e)


def main():
    post_dir = Path("content/post")
    if not post_dir.exists():
        print("Error: content/post directory not found")
        return

    md_files = list(post_dir.glob("*.md"))
    print(f"Found {len(md_files)} markdown files")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for filepath in md_files:
        success, message = process_file(filepath)
        if success:
            updated_count += 1
            print(f"✓ {filepath.name}: {message}")
        elif "No changes" in message:
            skipped_count += 1
        else:
            error_count += 1
            print(f"✗ {filepath.name}: {message}")

    print(f"\nSummary:")
    print(f"  Updated: {updated_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
批量更新Hugo博客文章的lastmod字段
"""

import os
import re
from datetime import datetime
from pathlib import Path

LASTMOD_DATE = "2026-03-19"


def parse_front_matter(content):
    """解析markdown文件的front matter"""
    if not content.startswith("---"):
        return None, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content

    front_matter = parts[1].strip()
    body = parts[2]

    return front_matter, body


def update_front_matter(front_matter_text):
    """更新front matter，添加或更新lastmod字段"""
    lines = front_matter_text.split("\n")
    new_lines = []
    has_lastmod = False
    date_line_idx = -1

    for i, line in enumerate(lines):
        if line.startswith("date:"):
            date_line_idx = i
        elif line.startswith("lastmod:"):
            has_lastmod = True
            new_lines.append(f"lastmod: {LASTMOD_DATE}")
            continue
        new_lines.append(line)

    if not has_lastmod and date_line_idx >= 0:
        new_lines.insert(date_line_idx + 1, f"lastmod: {LASTMOD_DATE}")

    return "\n".join(new_lines)


def process_file(filepath):
    """处理单个文件"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        front_matter, body = parse_front_matter(content)
        if front_matter is None:
            return False, "No front matter found"

        if f"lastmod: {LASTMOD_DATE}" in front_matter:
            return False, "Already has lastmod"

        new_front_matter = update_front_matter(front_matter)
        new_content = f"---\n{new_front_matter}\n---{body}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True, "Updated"
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
        else:
            if "Already has lastmod" in message:
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

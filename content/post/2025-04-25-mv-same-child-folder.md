---
layout: post
title:  "批量移动与父文件夹相同的子文件夹"
date: 2025-04-25 10:12:00
categories: [linux,ubuntu]
tags: [ubuntu]
draft: false
excerpt_separator: <!--more-->
---
批量移动与父文件夹相同的子文件夹
<!--more-->


```bash
#!/bin/bash

# 遍历所有父文件夹
find "$1" -type d -print0 | while IFS= read -r -d '' parent_dir; do
    # 获取子文件夹列表（仅直接子文件夹）
    subdirs=("$parent_dir"/*/)

    # 检查子文件夹数量是否为1，且名称与父文件夹相同
    if [ ${#subdirs[@]} -eq 1 ]; then
        subdir="${subdirs[0]}"
        parent_name=$(basename "$parent_dir")
        subdir_name=$(basename "$subdir")

        if [ "$parent_name" = "$subdir_name" ]; then
            echo "处理文件夹: $parent_dir"
            # 移动子文件夹内容到父文件夹（包括隐藏文件）
            mv "$subdir"/* "$subdir"/.* "$parent_dir"/ 2>/dev/null
            # 删除空子文件夹
            rmdir "$subdir"
        fi
    fi
done
```

```bash
./merge_folders.sh /path/to/your/directory/*
```
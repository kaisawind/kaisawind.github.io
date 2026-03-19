---
layout: post
title: 'Linux Mv Files to Folder'
date: 2024-06-21T16:38:55Z
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
linux通过find查找文件并移动到指定文件夹
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。

## 基本用法

```bash
# 查找并移动文件
find path_a -type f -name "some_name" ! -path "**/.@__thumb/*" -print0 | xargs -0 -I {} mv {} path_b
```

参数说明：
- `-type f`：只查找文件
- `-name "some_name"`：匹配文件名
- `! -path "**/.@__thumb/*"`：排除特定路径
- `-print0`：以null分隔输出
- `xargs -0`：处理null分隔的输入
- `-I {}`：使用{}作为占位符
- `mv {} path_b`：移动到目标目录

## 常用场景

### 根据文件名移动

```bash
# 移动所有jpg文件
find /source -type f -name "*.jpg" -exec mv {} /dest/ \;

# 或使用xargs
find /source -type f -name "*.jpg" | xargs -I {} mv {} /dest/
```

### 根据文件大小移动

```bash
# 移动大于100M的文件
find /source -type f -size +100M -exec mv {} /large_files/ \;

# 移动小于1M的文件
find /source -type f -size -1M -exec mv {} /small_files/ \;
```

### 根据修改时间移动

```bash
# 移动7天内修改的文件
find /source -type f -mtime -7 -exec mv {} /recent/ \;

# 移动30天前的文件
find /source -type f -mtime +30 -exec mv {} /archive/ \;
```

### 排除特定目录

```bash
# 排除.git目录
find /source -type f -name "*.py" ! -path "*/.git/*" -exec mv {} /dest/ \;

# 排除多个目录
find /source -type f ! -path "*/node_modules/*" ! -path "*/.git/*" -exec mv {} /dest/ \;
```

## 安全移动

### 先预览再执行

```bash
# 预览要移动的文件
find /source -type f -name "*.jpg" | head -10

# 确认无误后执行
find /source -type f -name "*.jpg" -exec mv {} /dest/ \;
```

### 使用mv -n避免覆盖

```bash
# 不覆盖已存在的文件
find /source -type f -name "*.jpg" -exec mv -n {} /dest/ \;

# 交互模式
find /source -type f -name "*.jpg" -exec mv -i {} /dest/ \;
```

### 备份原文件

```bash
# 先复制后移动
find /source -type f -name "*.jpg" -exec cp {} /backup/ \;
find /source -type f -name "*.jpg" -exec mv {} /dest/ \;
```

## 批量移动脚本

```bash
#!/bin/bash
# move_files.sh

SOURCE="/source/path"
DEST="/dest/path"
PATTERN="*.jpg"

# 创建目标目录
mkdir -p "$DEST"

# 统计文件数量
count=$(find "$SOURCE" -type f -name "$PATTERN" | wc -l)
echo "Found $count files to move"

# 移动文件
find "$SOURCE" -type f -name "$PATTERN" -print0 | while IFS= read -r -d '' file; do
    mv "$file" "$DEST/"
    echo "Moved: $file"
done

echo "Done!"
```

## 常见问题

### Q: 文件名包含空格？

使用`-print0`和`xargs -0`：

```bash
find /source -type f -name "*.jpg" -print0 | xargs -0 -I {} mv {} /dest/
```

### Q: 目标目录不存在？

```bash
# 先创建目录
mkdir -p /dest/path

# 再移动
find /source -type f -exec mv {} /dest/path/ \;
```

### Q: 权限不足？

```bash
sudo find /source -type f -name "*.jpg" -exec sudo mv {} /dest/ \;
```

## 最佳实践

1. **先预览**：使用echo或head预览要移动的文件
2. **测试小批量**：先用少量文件测试
3. **使用-print0**：处理包含空格或特殊字符的文件名
4. **备份重要数据**：批量操作前备份
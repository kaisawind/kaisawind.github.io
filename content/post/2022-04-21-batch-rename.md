---
layout: post
title:  "linux批量重命名文件"
date: 2022-04-21 20:00:16
lastmod: 2026-03-19
categories: [linux]
tags: [linux]
excerpt_separator: <!--more-->
author: "kaisawind"
description: "linux批量重命名文件"
---
linux批量重命名文件
<!--more-->

> **提示**: Linux发行版更新较快，命令可能因版本不同而有差异。

## 方法1：使用for循环

```bash
ls | cat -n | while read n f; do mv "$f" `printf "%012d.jpg" $n`; done
```

## 方法2：使用rename命令

```bash
# 安装rename（如果没有）
sudo apt install rename  # Debian/Ubuntu
sudo yum install rename  # CentOS/RHEL

# 将所有.txt改为.md
rename 's/\.txt$/.md/' *.txt

# 添加前缀
rename 's/^/prefix_/' *.jpg

# 添加后缀
rename 's/$/_suffix/' *.jpg

# 替换空格为下划线
rename 's/ /_/g' *
```

## 方法3：使用mmv

```bash
# 安装mmv
sudo apt install mmv

# 将所有*.jpg重命名为image_*.jpg
mmv '*.jpg' 'image_#1.jpg'
```

## 方法4：使用mv配合通配符

```bash
# 批量添加前缀
for f in *.jpg; do mv "$f" "prefix_$f"; done

# 批量添加后缀
for f in *; do mv "$f" "${f%.*}_suffix.${f##*.}"; done

# 批量替换字符串
for f in *old*; do mv "$f" "${f//old/new}"; done
```

## 方法5：使用Python脚本

```python
import os
import glob

# 添加序号
for i, f in enumerate(sorted(glob.glob('*.jpg'))):
    os.rename(f, f'{i:04d}.jpg')

# 替换字符串
for f in glob.glob('*'):
    new_name = f.replace('old', 'new')
    os.rename(f, new_name)
```

## 实用示例

### 按序号重命名

```bash
# 1.jpg, 2.jpg, 3.jpg...
i=1; for f in *.jpg; do mv "$f" "$i.jpg"; ((i++)); done

# 0001.jpg, 0002.jpg, 0003.jpg...
i=1; for f in *.jpg; do mv "$f" "$(printf '%04d.jpg' $i)"; ((i++)); done
```

### 添加时间戳

```bash
for f in *.jpg; do mv "$f" "$(date +%Y%m%d)_$f"; done
```

### 大小写转换

```bash
# 转小写
rename 'y/A-Z/a-z/' *

# 转大写
rename 'y/a-z/A-Z/' *
```

### 移除特殊字符

```bash
# 移除空格
rename 's/ //g' *

# 只保留字母、数字和下划线
rename 's/[^a-zA-Z0-9_.-]//g' *
```

## 预览修改（安全模式）

```bash
# 使用rename的-n参数预览
rename -n 's/\.txt$/.md/' *.txt

# 使用mv前先echo
for f in *.txt; do echo mv "$f" "${f%.txt}.md"; done
```

## 最佳实践

1. **先预览再执行**：使用`rename -n`或`echo`预览
2. **备份重要文件**：批量操作前备份
3. **使用版本控制**：对代码文件使用git
4. **测试小批量**：先用少量文件测试
5. **使用通配符小心**：`*`可能匹配意外文件
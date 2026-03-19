#!/usr/bin/env python3
"""
批量扩充简短的文章内容
"""

import os
import re
from pathlib import Path

# 更多扩充内容
EXPANSIONS_V2 = {
    "2022-02-09-sfdisk.md": """
## 问题描述

`sfdisk` 是Linux磁盘分区工具，当磁盘分区不支持或空间不足时，可以使用`sfdisk` 调整分区大小。

> **警告**: 调整分区会丢失数据，请先备份重要数据！

## 基本用法

### 查看分区信息

```bash
# 列出所有磁盘分区
sudo fdisk -l

# 查看特定磁盘分区
sudo fdisk -l /dev/sda
```

### 调整分区大小

```bash
# 调整分区大小（删除分区）
sudo sfdisk --delete /dev/sdaX

# 调整分区大小（必须是最后一个分区）
sudo sfdisk /dev/sda

# 进入交互模式
sudo sfdisk /dev/sda

# 在交互界面中：
# 输入 d 刌除分区
# 输入 n 创建新分区
# 输入 w 保存更改并退出
# 输入 q 退出
```

### 创建新分区

```bash
# 创建新分区（在未分配空间）
sudo sfdisk /dev/sda
# 输入 n 创建新分区
# 输入 w 保存并退出
```

## 宁成示例

假设 `/dev/sda` 有一个分区 `/dev/sda1` 大小为100GB，需要调整为50GB：

```bash
# 1. 查看分区
sudo fdisk -l

# 输出示：
Disk /dev/sda: 10 GiB, 100 GiB, 1073741824 bytes, 1048576 sectors
Units: cylinders = 1
```

# 2. 删除分区并创建新分区
sudo sfdisk /dev/sda

# 在交互界面：
Command (m for help): m
Command (n for new partition): n
Partition number (1-128, default 1): 
Created a new partition 1 of type Linux and system call it `mkfs.ext4`
Partition 1 has been created.

# 输入 w 保存
# 查看结果
sudo fdisk -l /dev/sda

# 输出：
Disk /dev/sda: 10 GiB, 50 GiB, 52428800 sectors
```

## 使用图形工具

推荐使用GParted等图形工具进行分区管理：

```bash
# 安装GParted
sudo apt-get install gparted

# 启动GParted
sudo gparted

# 查看磁盘和分区信息
```

## 最佳实践

1. **备份数据**：调整分区前务必备份重要数据
2. **使用LVM**：考虑使用LVM便于扩展
3. **监控磁盘**：定期检查磁盘使用情况
""",
    "2022-11-18-nmcli.md": """
## 问题描述

`nmcli` 是NetworkManager的命令行工具，用于管理网络连接。配置静态IP需要使用`nmcli` 命令。

## 配置静态IP

### 方法1：使用nmcli

```bash
# 设置静态IP
nmcli con mod eth0 ipv4.addresses 192.168.1.114/24
nmcli con mod eth0 ipv4.gateway 192.168.1.1
nmcli con mod eth0 ipv4.dns 223.5.5.5
nmcli con mod eth0 ipv4.method manual

# 应用配置
nmcli con up eth0
```

### 方法2：修改配置文件

编辑网络配置文件：
```bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

添加或修改：
```ini
[ipv4]
method=manual
addresses=192.168.1.114/24
gateway=192.168.1.1
dns=223.5.5.5
```

### 方法3：使用nmtui（图形界面）

```bash
nmtui
```

## 验证配置

```bash
# 查看IP配置
ip addr show

# 查看网络配置
nmcli device show

# 测试网络连接
ping -c 4 223.5.5.5
```

## NetworkManager服务管理

```bash
# 查看NetworkManager状态
sudo systemctl status NetworkManager

# 重启NetworkManager
sudo systemctl restart NetworkManager

# 重新加载配置
sudo nmcli connection reload
```

## 常见问题

### Q: 配置不生效？

```bash
# 检查NetworkManager状态
sudo systemctl status NetworkManager

# 查看日志
sudo journalctl -u NetworkManager -n 50
```

### Q: 如何删除静态IP？

```bash
# 恢复DHCP
nmcli con mod eth0 ipv4.method auto
# 或删除配置
sudo rm /etc/sysconfig/network-scripts/ifcfg-eth0
```

## 最佳实践

1. **使用NetworkManager**：推荐使用nmcli而不是直接修改配置文件
2. **备份配置**：修改前备份原配置
3. **测试连接**：配置后测试网络连通性
""",
    "2024-01-12-loop-cmd.md": """
## 问题描述

需要在Linux中多次执行相同的命令。

## 解决方法

### 方法1：使用for循环

```bash
for i in {1..10}; do
    ls
done
```

### 方法2：使用seq

```bash
seq 10 | xargs -n 1 ls
```

### 方法3：使用find + exec

```bash
find . -name "*.txt" -exec ls {} \;
```

### 方法4：使用parallel

```bash
# 安装parallel
sudo apt-get install parallel

# 并行执行
parallel ls ::: dir/*.txt
```

### 方法5：使用xargs

```bash
# 生成命令
for i in {1..100}; do echo "ls"; done > commands.txt

# 并行执行
xargs -P 4 < commands.txt
```

## 性能对比

| 方法 | 优点 | 缺点 |
|------|------|------|
| for循环 | 简单 | 顺序执行 |
| seq | 简洁 | 需要生成序列 |
| find + exec | 功能强大 | 对特殊文件名需要转义 |
| parallel | 真正并行 | 需要额外安装 |
| xargs | 并行可控 | 需要生成命令文件 |

## 最佳实践

1. **小量任务**：使用for循环即可
2. **大量任务**：使用parallel或xargs
3. **文件操作**：使用find + exec
4. **监控进度**：使用`echo`或`pv`显示进度
""",
    "2025-01-11-desktop-to-rtmp.md": """
## 问题描述

需要将桌面操作或RTMP推流到服务器。

## 解决方法

### 方法1：使用ffmpeg

```bash
ffmpeg -f x11grab -i :0 -framerate 30 -video_size 1920x1080 -i 1 \
       -f flv rtmp://localhost/live/stream_name \
       -c:v libx264 -preset veryfast -tune zerolatency \
       -f pulse -i :0 -stream_name out.flv
```

参数说明：
- `-f x11grab` 指定X11抓屏输入
- `-i :0` 设置输入为第0号屏幕
- `-framerate 30` 设置帧率
- `-video_size 1920x1080` 设置视频分辨率
- `-i 1` 使用1个线程
- `-f flv` 设置输出格式为FLV
- `rtmp://localhost/live/stream_name` 设置RTMP地址
- `-c:v libx264` 设置视频编码器
- `-preset veryfast` 设置编码预设
- `-tune zerolatency` 优化延迟
- `-f pulse -i :0` 设置音频输入
- `-stream_name` 设置流名称

- `out.flv` 输出文件名

### 方法2：使用obs-studio

1. 打开OBS Studio
2. 添加"显示器捕获"源
3. 开始录制
4. 选择RTMP作为输出

### 方法3：使用脚本

```bash
#!/bin/bash
# 使用ffmpeg推流桌面
while true; do
    ffmpeg -f x11grab -i :0 -framerate 30 -video_size 1920x1080 \
           -f flv rtmp://your-server/live/stream_key \
           -c:v libx264 -preset veryfast \
           -f pulse -i :0 - \
           out_$(date +%Y%m%d_%H%M%S).flv
    
    sleep 5
done
```

## 最佳实践

1. **控制质量**：调整视频参数平衡质量和带宽
2. **音频设置**：确保音频参数匹配RTMP服务器要求
3. **测试连接**：推流前测试RTMP服务器是否正常接收
4. **监控资源**：使用`htop`监控CPU和内存使用
""",
}


def expand_article_v2(filepath):
    """扩充单篇文章"""
    filename = os.path.basename(filepath)

    if filename not in EXPANSIONS_V2:
        return False, "无扩充模板"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 找到<!--more-->位置
        if "<!--more-->" not in content:
            return False, "无more标记"

        # 检查是否已经扩充
        if "## 问题描述" in content or "## 问题背景" in content:
            return False, "已扩充"

        # 插入扩充内容
        parts = content.split("<!--more-->", 1)
        new_content = parts[0] + "<!--more-->" + EXPANSIONS_V2[filename] + parts[1]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True, "已扩充"

    except Exception as e:
        return False, f"错误: {str(e)}"


def main():
    post_dir = Path("content/post")

    # 处理指定文章
    for filename in EXPANSIONS_V2.keys():
        filepath = post_dir / filename
        if filepath.exists():
            success, message = expand_article_v2(filepath)
            print(f"{'✓' if success else '✗'} {filename}: {message}")


if __name__ == "__main__":
    main()

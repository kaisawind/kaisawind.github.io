---
layout: post
title:  "diskpart删除450 MB的恢复分区"
date: 2024-04-01 15:59:16
categories: [windows]
tags: [windows]
excerpt_separator: <!--more-->
---
Windows 10下删除450 MB的恢复分区
<!--more-->

```bash
PS C:> diskpart

Microsoft DiskPart 版本 10.0.19041.3636

Copyright (C) Microsoft Corporation.
在计算机上: DESKTOP-EJOVI9D

DISKPART> list disk

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              200 GB   100 GB

DISKPART> select disk 0

磁盘 0 现在是所选磁盘。

  卷 ###      LTR  标签         FS     类型        大小     状态       信息
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  卷     0     D   VBox_GAs_7.  CDFS   CD-ROM        50 MB  正常
  卷     1         系统保留         NTFS   磁盘分区          50 MB  正常         系统
  卷     2     C                NTFS   磁盘分区          99 GB  正常         启动
  卷     3                      NTFS   磁盘分区         570 MB  正常         已隐藏

DISKPART> select volume 3

卷 3 是所选卷。

DISKPART> delete part override

DiskPart 成功地删除了所选分区。

DISKPART> exit

退出 DiskPart...
```
---
layout: post
title:  "pyinstaller打包工具"
date: 2020-08-21 14:59:04
categories: [编程语言,python]
excerpt_separator: <!--more-->
---
pyinstaller打包工具
<!--more-->

## 1. 概述
pyinstaller是python的打包工具，能够将python打包成单独的可执行文件，从而减少对运行环境的依赖。

## 2. 使用

* 本地运行
注意本地python环境的大小，python会打包所有site-packages中的包

```bash
pip install pyinstaller
pyinstaller main.py
```

* docker
```bash
docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app  python:3.8.5 /bin/bash -c "pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
pip install --upgrade pip && \
pip install pyinstaller && \
pip install -r requirements.txt && \
pyinstaller -F main.spec --distpath bin && \
exit"
```

## 3. spec文件说明

spec文件是pyinstaller嵌入的python文件，最终会被执行。

Analysis：添加所有需要打包的py文件。
hiddenimports：添加未自动识别的包名
excludes：刨除不需要打包的文件
```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py',
             'server/__init__.py',
             'server/circuit.py',
             'server/server.py',
             'proto/__init__.py',
             'proto/algorithm_pb2.py',
             'proto/algorithm_pb2_grpc.py'
             ],
             pathex=['./'],
             binaries=[],
             datas=[],
             hiddenimports=['proto', 'server', 'algorithm_pb2', 'proto.algorithm_pb2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['apiserver', 'bin', 'docs', ''],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
```

## 4. 坑

alpine使用的是musl,所以在alpine上打包和运行打包之后的文件会有问题。(ubuntu没有问题)
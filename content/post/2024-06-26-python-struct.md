---
layout: post
title: 'python项目文件夹结构'
date: 2024-06-26T14:12:13+08:00
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
python项目文件夹结构
<!--more-->

## 1. 通用结构

```bash
myproject/
├── myproject/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   └── ...
├── docs/
├── README.md
├── requirements.txt
└── setup.py
```

* `myproject/`：项目的根目录，也是Python包的根目录。
* `myproject/__init__.py`：一个空的__init__.py文件，用于将myproject目录标记为一个Python包。
* `myproject/module1.py`、`myproject/module2.py`等：项目的模块文件，包含项目的核心代码。
* `tests/`：测试目录，包含用于测试项目代码的测试文件。
* `docs/`：文档目录，包含项目的文档文件。
* `README.md`：项目的说明文档，通常使用Markdown格式编写。
* `requirements.txt`：项目的依赖文件，列出了项目所需的所有依赖包及其版本号。
* `setup.py`：项目的安装文件，用于将项目打包为可安装的Python包。

## 2. Flask项目结构

```bash
myflaskproject/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── ...
│   └── static/
│       ├── css/
│       ├── js/
│       └── ...
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

* `app/`：应用程序目录，包含应用程序的核心代码。
* `app/__init__.py`：应用程序的初始化文件，创建Flask应用对象并配置应用程序。
* `app/models.py`：应用程序的模型文件，包含数据库模型定义。
* `app/views.py`：应用程序的视图文件，包含路由和视图函数的定义。
* `app/templates/`：模板目录，包含应用程序的HTML模板文件。
* `app/static/`：静态文件目录，包含应用程序的静态资源文件，如CSS、JavaScript等。
* `config.py`：配置文件，包含应用程序的配置信息。
* `requirements.txt`：项目的依赖文件，列出了项目所需的所有依赖包及其版本号。
* `run.py`：应用程序的入口文件，用于启动应用程序。
* `README.md`：项目的说明文档，通常使用Markdown格式编写。

## 3. RESTful API项目目录

```bash
project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── resources/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   └── ...
│   ├── routes.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_post.py
│   └── ...
├── config.py
├── requirements.txt
└── run.py
```

* `app/`：应用程序目录，包含应用程序的核心代码。
* `app/__init__.py`：应用程序的初始化文件，创建Flask应用对象并配置应用程序。
* `app/models.py`：应用程序的模型文件，包含数据库模型定义。
* `app/resources/`：目录用于存放RESTful API的资源文件，每个资源对应一个文件。
* `app/routes.py`: 文件用于定义路由和视图函数。
* `app/utils.py`: 文件用于存放一些辅助函数或工具函数。
* `app/tests/`: 目录用于存放测试代码。
* `config.py`：配置文件，包含应用程序的配置信息。
* `requirements.txt`：项目的依赖文件，列出了项目所需的所有依赖包及其版本号。
* `run.py`：应用程序的入口文件，用于启动应用程序。
* `README.md`：项目的说明文档，通常使用Markdown格式编写。

---
layout: post
title:  "release编译:flutter android编译release版"
date: 2019-9-23 10:28:16
categories: [flutter]
tags: [flutter]
excerpt_separator: <!--more-->
---
release编译:flutter android编译release版
<!--more-->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 概述](#1-概述)
- [2. 添加启动图标](#2-添加启动图标)
  - [2.1 启动图标设计规范](#21-启动图标设计规范)
  - [2.2 启动图标存储位置](#22-启动图标存储位置)
  - [2.3 修改`AndroidManifest`](#23-修改androidmanifest)
  - [2.4 验证是否替换成功](#24-验证是否替换成功)
- [3. App认证](#3-app认证)
  - [3.1 创建key](#31-创建key)
  - [3.2 添加`key.properties`](#32-添加keyproperties)
  - [3.3 修正`build.gradle`](#33-修正buildgradle)
- [4. 启用规则缩小apk大小](#4-启用规则缩小apk大小)
  - [4.1 创建规则](#41-创建规则)
  - [4.2 app关联规则](#42-app关联规则)
- [5. 额外项检查](#5-额外项检查)
  - [5.1 外网访问权限](#51-外网访问权限)
  - [5.2 app名](#52-app名)
  - [5.3 检查编译配置项](#53-检查编译配置项)
- [6. 编译release版本](#6-编译release版本)
  - [6.1 flutter编译](#61-flutter编译)
  - [6.2 Android Studio编译](#62-android-studio编译)

<!-- /code_chunk_output -->


## 1. 概述

debug是用来调试的版本，会输出很多日志，加载不必要的插件，release版中会去掉这些内容，使app更稳定，更小，更快。

Flutter官网：[Preparing an Android app for release](https://flutter.dev/docs/deployment/android)

Flutter中文网： [发布Android版APP](https://flutterchina.club/android-release/)

## 2. 添加启动图标

### 2.1 启动图标设计规范

[Material Design product icons guidelines](https://material.io/design/iconography/#grid-keyline-shapes)

### 2.2 启动图标存储位置

`<app dir>/android/app/src/main/res/`通过不同的文件夹，区分屏幕分表率

|Android手机屏幕标准|对应图标尺寸标准|屏幕密度|比例|
|---|---|---|---|
|xxxhdpi|3840*2160|192*192|640|16|
|xxhdpi|1920*1080|144*144|480|12|
|xhdpi|1280*720|96*96|320|8|
|hdpi|480*800|72*72|240|6|
|mdpi|480*320|48*48|160|4|
|ldpi|320*240|36*36|120|3|

### 2.3 修改`AndroidManifest`

`android/app/src/main/AndroidManifest.xml`

```xml
<application
        android:name="io.flutter.app.FlutterApplication"
        android:label="flutter_example"
        android:icon="@mipmap/ic_launcher">
</application>
```
其中
`android:icon="@mipmap/ic_launcher"`为关联的图标名

### 2.4 验证是否替换成功

启动模拟器查看

<img src="/images/Screenshot_1569209856.png" width="400" height="711" alt="icon替换" align=center>

## 3. App认证

### 3.1 创建key

Mac/Linux
```shell
keytool -genkey -v -keystore ~/key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias key
```

Windows
```shell
keytool -genkey -v -keystore c:/Users/USER_NAME/key.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias key
```

### 3.2 添加`key.properties`

```
storePassword=<password from previous step>
keyPassword=<password from previous step>
keyAlias=key
storeFile=<location of the key store file, such as /Users/<user name>/key.jks>
```

不要把`key.properties`放到共有代码中

### 3.3 修正`build.gradle`

变量的声明与定义
```
   def keystoreProperties = new Properties()
   def keystorePropertiesFile = rootProject.file('key.properties')
   if (keystorePropertiesFile.exists()) {
       keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
   }

   android {
```

配置编译类型
```
    signingConfigs {
       release {
           keyAlias keystoreProperties['keyAlias']
           keyPassword keystoreProperties['keyPassword']
           storeFile file(keystoreProperties['storeFile'])
           storePassword keystoreProperties['storePassword']
       }
   }
   buildTypes {
       release {
           signingConfig signingConfigs.release
       }
   }
```

## 4. 启用规则缩小apk大小

### 4.1 创建规则


`/android/app/proguard-rules.pro`

```
## Flutter wrapper
-keep class io.flutter.app.** { *; }
-keep class io.flutter.plugin.**  { *; }
-keep class io.flutter.util.**  { *; }
-keep class io.flutter.view.**  { *; }
-keep class io.flutter.**  { *; }
-keep class io.flutter.plugins.**  { *; }
-dontwarn io.flutter.embedding.**
```

### 4.2 app关联规则

`/android/app/build.gradle`

```
android {

    ...

    buildTypes {

        release {

            signingConfig signingConfigs.release

            minifyEnabled true
            useProguard true

            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'

        }
    }
}
```

## 5. 额外项检查

### 5.1 外网访问权限

`<app dir>/android/app/src/main/AndroidManifest.xml`添加
`<uses-permission android:name="android.permission.INTERNET"/>`

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.kaisawind.flutter_example">

    <!-- io.flutter.app.FlutterApplication is an android.app.Application that
         calls FlutterMain.startInitialization(this); in its onCreate method.
         In most cases you can leave this as-is, but you if you want to provide
         additional functionality it is fine to subclass or reimplement
         FlutterApplication and put your custom class here. -->
    <uses-permission android:name="android.permission.INTERNET"/>
    <application
        android:name="io.flutter.app.FlutterApplication"
        android:label="flutter_example"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <!-- This keeps the window background of the activity showing
                 until Flutter renders its first frame. It can be removed if
                 there is no splash screen (such as the default splash screen
                 defined in @style/LaunchTheme). -->
            <meta-data
                android:name="io.flutter.app.android.SplashScreenUntilFirstFrame"
                android:value="true" />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>

```

### 5.2 app名

`android:label="flutter_example"`为app名称
```xml
<application
        android:name="io.flutter.app.FlutterApplication"
        android:label="flutter_example"
        android:icon="@mipmap/ic_launcher">
</application>
```

### 5.3 检查编译配置项

`<app dir>/android/app/build.gradle`

```
    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId "com.kaisawind.flutter_example"
        minSdkVersion 16
        targetSdkVersion 28
        versionCode flutterVersionCode.toInteger()
        versionName flutterVersionName
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
```

* `applicationId`: 唯一的appID

## 6. 编译release版本

### 6.1 flutter编译


apk拆分
```shell
flutter build apk --split-per-abi
```

output

* `<app dir>/build/app/outputs/apk/release/app-armeabi-v7a-release.apk`
* `<app dir>/build/app/outputs/apk/release/app-arm64-v8a-release.apk`


多合一版本
```shell
flutter build apk
```

output

* `<app dir>/build/app/outputs/apk/release/app-release.apk`

### 6.2 Android Studio编译

* 从项目中打开Android Studio

![Android](/images/微信截图_20190923140712.png)
![Android](/images/微信截图_20190923140734.png)

* 配置编译选项

[Build]-[Generate Signed Bundle/APK]
![Android](/images/微信截图_20190923141441.png)
![Android](/images/微信截图_20190923141521.png)
![Android](/images/微信截图_20190923141533.png)

output

* `<app dir>/android/app/release/app-release.apk`
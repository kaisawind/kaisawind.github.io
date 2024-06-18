---
layout: post
title:  "flutter路由2.0"
date: 2020-12-01 09:43:12
categories: [flutter]
tags: [flutter]
excerpt_separator: <!--more-->
---

## 1. 概述
flutter开始支持web页面，同时基于以前的路由1.0在web上会有问题。
由于web能够使用url直接定位到子页面,基于路由1.0是无法实现的。
所以有两种解决办法:
1. 把浏览器url完全隐藏掉(google正在做)
2. 支持url跳转子页面

## 2. 路由2.0

基于web页面，有两种时序。我们需要路由2.0的实现满足这两种时序
1. 通过按钮点击进入子页面
2. 通过url进入子页面

具体实现

### 2.1 状态管理
`app_router.dart`
AppState是路由状态管理器，维护一个全局的路由状态。
```dart
class AppState extends ChangeNotifier {
  AppRoutePath _currentPath = RootPath();

  AppRoutePath get currentPath => _currentPath;
  set currentPath(AppRoutePath path) {
    print('currentPath ${path.path}');
    _currentPath = path;
    notifyListeners();
  }
}
```

### 2.2 路由管理

由于是全局状态，所以每个有路由迁移的页面都需要保存appState
appState作为`RootPage(appState)`的参数进行了入参。
当appState发生变化时，会触发currentConfiguration的更新，重新描画页面。(时序1)
当从url切换页面时，会触发`setNewRoutePath`切换新的页面(时序2)
```dart
class AppRouterDelegate extends RouterDelegate<AppRoutePath>
    with ChangeNotifier, PopNavigatorRouterDelegateMixin<AppRoutePath> {
  final GlobalKey<NavigatorState> navigatorKey;

  AppState appState = AppState();

  AppRouterDelegate() : navigatorKey = GlobalKey<NavigatorState>() {
    appState.addListener(notifyListeners);
  }

  AppRoutePath get currentConfiguration {
    print("currentConfiguration ${appState.currentPath}");
    return appState.currentPath;
  }

  @override
  Widget build(BuildContext context) {
    return Navigator(
      key: navigatorKey,
      pages: [
        MaterialPage(
          child: RootPage(appState),
        ),
      ],
      onPopPage: (route, result) {
        if (!route.didPop(result)) {
          return false;
        }
        return true;
      },
    );
  }

  @override
  Future<void> setNewRoutePath(AppRoutePath path) async {
    print("setNewRoutePath ${path.path}");
    appState.currentPath = path;
  }
}
```

`root_page.dart`
页面入参实例
```dart
class RootPage extends StatefulWidget {
  final AppState appState;
  RootPage(
    this.appState,
  );

  @override
  _RootPageState createState() => _RootPageState();
}
```

### 2.3 url转appState

`parseRouteInformation`是url传过来的参数，通过解析参数初始化appState，进行页面的切换。
```dart
class AppRouteInformationParser extends RouteInformationParser<AppRoutePath> {
  @override
  Future<AppRoutePath> parseRouteInformation(RouteInformation routeInformation) async {
    final uri = Uri.parse(routeInformation.location);
    print('parseRouteInformation ${routeInformation.location}');
    switch (uri.path) {
      case Routes.home:
        return HomePath();
      case Routes.productList:
        return ProductListPath();
      case Routes.productDetail:
        return ProductDetailPath(id: uri.queryParameters['id']);
      case Routes.deviceList:
        return DeviceListPath();
      case Routes.deviceDetail:
        return DeviceDetailPath();
      case Routes.userList:
        return UserListPath();
      case Routes.userDetail:
        return UserDetailPath();
      case Routes.setting:
        return SettingPath();
      default:
        return HomePath();
    }
  }

  @override
  RouteInformation restoreRouteInformation(AppRoutePath configuration) {
    return RouteInformation(location: configuration.path);
  }
}
```

## 3. 详细时序

### 3.1 时序1

1. AppState.currentPath
2. AppRouterDelegate.currentConfiguration

### 3.2 时序2

1. AppRouteInformationParser.parseRouteInformation
2. AppRouterDelegate.setNewRoutePath
3. AppState.currentPath
4. AppRouterDelegate.currentConfiguration
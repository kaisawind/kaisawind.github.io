---
layout: post
title:  "react-redux的connect函数"
date: 2021-01-09 15:26:42
categories: [前端,react]
excerpt_separator: <!--more-->
---
react-redux的connect函数
<!--more-->

## 1. 概述

connect方法将state和dispatch绑定到Connect组件的参数上，然后Connect组件将你当前的App组件封装起来，使得App组件可以通过props获取到父组件Connect传递的state和props。

## 2. 函数说明

```typescript
connect([mapStateToProps], [mapDispatchToProps], [mergeProps], [options])
```

### 2.1 mapStateToProps

`[mapStateToProps(state, [ownProps]): stateProps] (Function)`: 如果定义该参数，组件将会监听 Redux store 的变化。任何时候，只要 Redux store 发生改变，mapStateToProps 函数就会被调用。该回调函数必须返回一个纯对象，这个对象会与组件的 props 合并。如果你省略了这个参数，你的组件将不会监听 Redux store。如果指定了该回调函数中的第二个参数 ownProps，则该参数的值为传递到组件的 props，而且只要组件接收到新的 props，mapStateToProps 也会被调用（例如，当 props 接收到来自父组件一个小小的改动，那么你所使用的 ownProps 参数，mapStateToProps 都会被重新计算）。


### 2.2 mapDispatchToProps

`[mapDispatchToProps(dispatch, [ownProps]): dispatchProps] (Object or Function)`: 如果传递的是一个对象，那么每个定义在该对象的函数都将被当作 Redux action creator，对象所定义的方法名将作为属性名；每个方法将返回一个新的函数，函数中dispatch方法会将action creator的返回值作为参数执行。这些属性会被合并到组件的 props 中。

## 3. 示例

### 3.1 mapStateToProps定义

* 以下定义ownProps参数无效

```typescript
function mapStateToProps(state) {
  console.log(state); // state
  console.log(arguments[1]); // undefined
}
```

```typescript
const mapStateToProps = (state, ownProps = {}) => {
  console.log(state); // state
  console.log(ownProps); // undefined
}
```

* 以下定义ownProps参数有效

```typescript
const mapStateToProps = (state, ownProps) => {
  console.log(state); // state
  console.log(ownProps); // ownProps
}
```

```typescript
function mapStateToProps() {
  console.log(arguments[0]); // state
  console.log(arguments[1]); // ownProps
}
```

```typescript
const mapStateToProps = (...args) => {
  console.log(args[0]); // state
  console.log(args[1]); // ownProps
}
```

### 3.2 实例

```typescript
const mapStateToProps = ({
  listProduct,
  loading,
}: {
  listProduct: StateType;
  loading: {
    models: { [key: string]: boolean };
  };
}) => {
  return {
    listProduct,
    loading: loading.models.listProduct,
  }
};

export default connect(
  mapStateToProps,
)(CardList);
```

说明：
mapStateToProps入参
其中`{}:{}`为指定类型解构
`let {a,b}:{a:string,b:number}=o;`
其中`loading:{}`为对象展开
其中`models: { [key: string]: boolean }`为对象键值类型声明
```typescript
{
  listProduct,
  loading,
}: {
  listProduct: StateType;
  loading: {
    models: { [key: string]: boolean };
  };
}
```
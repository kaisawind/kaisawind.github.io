---
layout: post
title:  "typescript assert enum"
date: 2023-03-06 14:08:54
categories: [编程语言,typescript]
tags: [typescript, linux]
excerpt_separator: <!--more-->
---
typescript assert enum
<!--more-->

```typescript
enum Animal {
  Cat = "cat",
  Dog = "dog",
}

const isAnimal(value: string): value is Animal {
  return Object.values<string>(Animal).includes(value);
}

if (isAnimal(someInputValue)) {
    // TODO
}
```
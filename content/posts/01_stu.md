---
title: "01_stu"
date: 2022-11-27T17:47:50+08:00
draft: false
tags: ['stu','数据结构','sql']
categories: ["stu"]

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: true
hiddenFromSearch: false
twemoji: true
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true

---


## 01_03题
旋转 转置  
遍历  
栈存方法（学习）
```python
matrix = [[7,4],[9,5],[6,3]]


nn = []
print(list(zip(*matrix))[::-1])
matrix = map(list, zip(*matrix))
print(matrix)


 i = 1
 while matrix != []:
     if i%4 == 1:
         aa = matrix.pop(0)
         for a in range(len(aa)):
             nn.append(aa.pop(0))
     if i%4 == 3:
         bb = matrix.pop(-1)
         for a in range(len(bb)):
             nn.append(bb.pop(-1))
     if (i+1)%4 == 3:
         for a in range(len(matrix)):
             nn.append(matrix[a].pop(-1))
     if (i+1)%4 == 1:
         for a in range(len(matrix))[::-1]:
             nn.append(matrix[a].pop(0))
     i += 1
     while [] in matrix:
         matrix.remove([])

 print(nn)
 print(matrix)
```
---
```sql
sql 题目
只有 Ture False unknow  
有NULL 要判断NULL
```


<!-- 


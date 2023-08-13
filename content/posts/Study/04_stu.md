---
title: "04_stu"
date: 2022-11-27T23:32:54+08:00
draft: false
tags: ['数据结构']
categories: ["stu"]

summary: "" # 文章简介 #
author: ["Jaywxl"] # 作者 #

cover:
    image: "" # 图片链接 #
    alt: "" # 图片名称 #
    hidden: false # 文章内不显示/显示 #

weight: false # 置顶 一般置顶 10（同weight参考时间）#

katex: false # 数学公式 #
mermaid: true # 流程图 #
hidemeta: false # 隐藏页面元素如：作者、时间等 #
# description: "Desc Text." # 单页面标题 #
---

---
## 01_数组切片分组
```python
mat = [[1,2],[3,4],[5,6]]
r,c = 2,3
ans = [[0]*c for _ in range(r)]

a = []
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) == r*c :
            for i in mat:
                a +=i
            return [a[i:i + c] for i in range(0, len(a), c)]
        else: return mat
```
## 02_杨辉三角
> 杨辉三角  
> 弄清yieid 和 return 区别 yieid可迭代
```python
class Solution:
    def triangles(b):
        L = [1]
        i = 0              #定义L为一个只包含一个元素的列表
        while i < b:
            i += 1
            yield L          #定义为生成器函数
            L =[1] + [L[n] + L[n-1] for n in range(1,len(L))] + [1]
    def generate(self, numRows: int) -> list[list[int]]:
        n = []
        for a in Solution.triangles(numRows):
            print(a)
            n.append(a)
        return n

# 方法二 简化
        L = [1]
        i = 0              #定义L为一个只包含一个元素的列表
        n = []
        while i < b:
            i += 1
            n.append(L)
            L =[1] + [L[n] + L[n-1] for n in range(1,len(L))] + [1]
        return n
```
<!--


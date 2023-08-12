---
title: "13_stu"
date: 2022-12-11T23:34:11+08:00
draft: false
tags: ['二分法','z字型搜索']
categories: ['stu']
description:

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: true
hiddenFromSearch: false
twemoji: false
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true

  # ...
---

<!--more-->
写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。

每列的元素从上到下升序排列。
 
![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg)

来源：力扣（LeetCode）

链接：https://leetcode.cn/problems/search-a-2d-matrix-ii

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```python
"""
* 二分法
* z字型搜索 从右上角 两个边界数值 一大一小的地方 开启搜索 各向异性
"""

Method_二分法

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False

Method_z字型法则

"""
从右上角 或 左下角 开始搜索 满足两个方向的不同
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
```
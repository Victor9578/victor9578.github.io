---
title: "10_stu"
date: 2022-12-03T15:39:25+08:00
draft: false
tags: ['二叉树']
categories: ['数据结构']
description: '二叉树递归、迭代的学习'

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
# 二叉树

![img](https://m.360buyimg.com/babel/jfs/t1/11877/31/20745/150895/638b3faeEfcb34dfc/3f604924123fd457.png "")

{{<admonition note>}}
最重点的内容就是：不管是先序中序还是后序，查找流程都是从上到下，先左后右。只是输出的时机不同。

先序就是发现了先输出，再先左后右。

中序就是发现了先存着，当左边遍历完了，再把存着的输出出来。

后序就是发现了先存着，当左边和右边都遍历完了，再把存着的输出出来。
{{</admonition>}}

## 01_二叉树前序

Method:迭代

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack  = [root]
        res = []
        while stack :
            p = stack.pop()
            res.append(p.val)
            if p.right: stack.append(p.right)
            if p.left: stack.append(p.left)
        return res
```

## 02_二叉树中序

Method:递归

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=list()
        def midorder(root:TreeNode):
            if not root:
                return
            midorder(root.left)
            res.append(root.val)
            midorder(root.right)
        midorder(root)
        return res
```
## 03_二叉树后序

Method:迭代

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        node=root
        stack=[]
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node=node.right
            node=stack.pop()
            node=node.left

        return res[::-1]
```

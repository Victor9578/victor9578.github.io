---
title: "11_stu"
date: 2022-12-05T20:22:14+08:00
draft: false
tags: ["动态规划"]
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
description: "动态规划之最少趟数"
---
---

<!--more-->

{{<admonition note "Target">}}

- [X] see 动态规划
- [ ] init github"stock_trade" and ReadMe

{{</admonition>}}

## 02_路径总和

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if root:
#             targetSum = targetSum - root.val
#         else:
#             return False
#         stack = []
#         sum = []
#         while root:
#             print(root)
#             a,b = float('-inf'),float('-inf')
#             if root.left: a = root.left.val
#             if root.right: b = root.right.val
#             if root.right and root.left:
#                 stack.append(root)
#                 sum.append(targetSum)
#             if a > b :
#                 targetSum -= a
#                 root = root.left
#             else:
#                 targetSum -= b
#                 root = root.right
#             print(root)
#             if targetSum != 0 and not root.left and not root.right and  stack:
#                 root = stack.pop()
#                 targetSum = sum.pop()
#                 if root.right.val > root.left.val:
#                     root.right = None
#                 else:
#                     root.left = None
#             elif targetSum == 0 and not root.left and not root.right:
#                 return True 
#             elif targetSum != 0 and not root.left and not root.right:
#                 return False
"""
最终被击溃在两个子节点数值相等的问题上导致无法回溯，可以优化存在栈里面回溯的treenode，将选择的一边设为None
"""
Method_递归
class Solution(object):
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
```

## 02_搜索二叉树

> 搜索二叉树满足对于任意节点 root 而言，左子树（如果存在）上所有节点的值均小于 \textit{root.val}root.val，右子树（如果存在）上所有节点的值均大于 \textit{root.val}root.val，且它们都是二叉搜索树。
递归

## init_stock_trade
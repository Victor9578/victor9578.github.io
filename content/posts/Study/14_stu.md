---
title: "14_stu"
date: 2022-12-12T21:43:13+08:00
draft: false
tags: ['前缀和法']
categories: ['stu']

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
description:
---
---

<!--more-->

## 数组之求和为k的连续子数组数量

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

示例 1：

输入：nums = [1,1,1], k = 2
输出：2

示例 2：

输入：nums = [1,2,3], k = 3
输出：2

来源：力扣（LeetCode）

链接：https://leetcode.cn/problems/subarray-sum-equals-k

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

***

> 使用的原理就是 presum-k 若在 之前哈希表中的 presum 出现过 那么 必定有连续的数组和为k  
> 因为之前统计的presum为一段连续数组，现如今的presum同为连续数组，两个连续数组相减，和为k的数组也必为连续数组  
> 若presum在哈希表中不唯一 表示连续数组中出现了和为0的子数组。


![111](https://pic.leetcode-cn.com/1650818225-XIUNgx-image.png)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prehash = dict()
        prehash[0] = 1
        preSum = 0
        count = 0
        for num in nums:
            preSum += num

            if preSum - k in prehash:
                count += prehash[preSum - k]

            if preSum not in prehash:
                prehash[preSum] = 1
            else:
                prehash[preSum] += 1
            
        return count
```
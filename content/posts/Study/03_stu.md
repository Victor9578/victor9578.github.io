---
title: "03_stu"
date: 2022-11-27T18:14:59+08:00
draft: false
tags: ['stu','数据结构','sql']
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
## 01_返回交集
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。   

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```python
from collections import Counter
import collections

nums1 = [1,2,1,3]
nums2 = [2,2,3]

nn = []
n = 1

count = Counter(nums1)
print(count[4])
ans = []
for num in nums2:
    if count[num] != 0:
        print(count)
        ans.append(num)
        count[num] -= 1
print(ans)
c = (collections.Counter(nums1)&collections.Counter(nums2)).elements() # 一行代码
print(c)
d = nums1&nums2
print(d)

```
---
## 02_concat_upper_lower_sql
```sql
CONCAT # 拼接字符串
LEFT,RIGHT
UPPER,LOWER # 大写，小写
select user_id, CONCAT(UPPER(left(name, 1)), LOWER(RIGHT(name, length(name) - 1))) as name
from Users
order by user_id;
```
---
## 03_sql
```sql
-- group_concat 字符串连接
-- group by 分组
-- count 统计
-- distinct 去重
select sell_date, count(distinct(product)) as num_sold, group_concat(distinct product order by product asc separator ',') as products
from Activities
group by sell_date;
```
---
## 04_sql
``` sql
select patient_id,patient_name,conditions
from PAtients
where conditions regexp '^DIAB1|\\sDIAB1'; # 正则表达式
where conditions like 'DIAB1%' or conditions like '% DIAB1%' #like的匹配得有百分号（类似于*） 否则该语句等同于=
```
 


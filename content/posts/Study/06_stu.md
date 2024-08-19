---
title: "06_stu"
date: 2022-11-29T14:07:55+08:00
draft: false
tags: ['sql']
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
# description: "Desc Text." # 单页面标题 #
---

---
## 01_adddate
~~~
输入：  
Weather 表：  
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
输出：
+----+
| id |
+----+
| 2  |
| 4  |
+----+
解释：
2015-01-02 的温度比前一天高（10 -> 25）
2015-01-04 的温度比前一天高（20 -> 30）

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/rising-temperature
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

```sql
-- ADDDATE函数日期增加
-- inner join内连接 会删除没有匹配的项 不会保留null
SELECT id
from Weather w1 left join (SELECT ADDDATE(recordDate,1) as uid,Temperature as t from Weather)w2 on w1.recordDate = w2.uid
WHERE Temperature > t; 
```
---

## 02_判断两个字符串中元素是否一样多

```python
import collections
s = "ab"
t = "ba"
class Solution:
    def firstUniqChar( s: str, t: str) -> bool:
        # print(sorted(collections.Counter(t).most_common()))
        # print(collections.Counter(t).most_common())      sorted()排序
        return sorted(collections.Counter(s).most_common()) == sorted(collections.Counter(t).most_common())

print(Solution.firstUniqChar(s,t))
```
 


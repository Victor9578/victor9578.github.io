---
title: "15_stu"
date: 2022-12-15T21:44:43+08:00
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
description:
---
---

<!--more-->

## sql_Rank()函数

编写 SQL 查询对分数进行排序。排名按以下规则计算:

分数应按从高到低排列。
如果两个分数相等，那么两个分数的排名应该相同。
在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。
按 score 降序返回结果表。

查询结果格式如下所示。

 
~~~
示例 1:

输入: 
Scores 表:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
输出: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

~~~

来源：力扣（LeetCode）

链接：https://leetcode.cn/problems/rank-scores

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

![rank](https://m.360buyimg.com/babel/jfs/t1/166268/22/29671/167571/639b2505Ea125be86/b722e14504a2c62c.png)

rank()相关函数的使用

```sql
# Write your MySQL query statement below
select score, dense_rank() over (order by score desc) as 'rank'  #这个rank之所以要加引号，因为rank本身是个函数，直接写rank会报错
from scores;

-- 异或这种count1前面的数据

select a.Score,(select count(distinct b.Score) from Scores b where b.Score >= a.Score) as 'rank'
from Scores a
order by a.Score DESC;

```

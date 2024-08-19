---
title: "02_stu"
date: 2022-11-27T18:14:53+08:00
draft: false
tags: ['stu','数据结构','sql']
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




## 01_找出出现一次的元素(reduce)
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。  

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。  

来源：力扣（LeetCode）  
链接：https://leetcode.cn/problems/single-number  
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。  


> reduce函数累计 a^b^c^d^....  
> 异或  不同输出本身  时间复杂度O(1)   空间复杂度O(n) 

```python
from functools import reduce
nums = [1,2,3,4,4,3,2]
class Solution:
    def singleNumber(nums: list[int]) -> int:
        return reduce(lambda x,y : x^y,nums)

print(Solution.singleNumber(nums))
```

---
## 02_update_sql方法(ascii,if方法,case when)
Salary 表：

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id 是这个表的主键。
sex 这一列的值是 ENUM 类型，只能从 ('m', 'f') 中取。
本表包含公司雇员的信息。
 

请你编写一个 SQL 查询来交换所有的 'f' 和 'm' （即，将所有 'f' 变为 'm' ，反之亦然），仅使用 单个 update 语句 ，且不产生中间临时表。

注意，你必须仅使用一条 update 语句，且 不能 使用 select 语句。

查询结果如下例所示。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/swap-salary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```sql
update salary set sex = char(ascii('m') + ascii('f') - ascii(sex));
-- 使用ascii码值的变换 sql语法特点
```

```sql
-- 方法一：MySql中的if语句
update salary set sex = if(sex = 'm', 'f', 'm')

-- 方法二：case when语法
update salary set sex = case sex when 'm' then 'f' else 'm' end;
```
---
## 03_delect_sql(建立两个表格)
输入: 
Person 表:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
输出: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
解释: john@example.com重复两次。我们保留最小的Id = 1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/delete-duplicate-emails
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~
## 删除重复项目 使用 sql自连接 
```sql
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
```
 


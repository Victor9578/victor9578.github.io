---
title: "05_stu"
date: 2022-11-28T16:55:58+08:00
draft: false
tags: ['sql']
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

  # ...

---
## 01_sql
~~~
给定一个表 tree，id 是树节点的编号， p_id 是它父节点的 id 。

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
树中每个节点属于以下三种类型之一：

叶子：如果这个节点没有任何孩子节点。
根：如果这个节点是整棵树的根，即没有父节点。
内部节点：如果这个节点既不是叶子节点也不是根节点。

写一个查询语句，输出所有节点的编号和节点的类型，并将结果按照节点编号排序。上面样例的结果为：
 
+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/tree-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

```sql
-- case when Method
select id,
        case 
        when p_id is NULL then 'Root'
        when id in (
            select atree.p_id from tree as atree
        ) then 'Inner'
        else 'Leaf'
        end as type
from tree

-- if else Method


SELECT id,
        IF(p_id IS NULL,
        'Root',
        IF(id IN (
                SELECT DISTINCT p_id  FROM tree
                WHERE p_id IS NOT NULL
                    ),'Inner','Leaf')
        ) AS Type
FROM tree


```
---
## 02_limit_offset_sql
~~~
Employee 表：
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id 是这个表的主键。
表的每一行包含员工的工资信息。

编写一个 SQL 查询，获取并返回 Employee 表中第二高的薪水 。如果不存在第二高的薪水，查询应该返回 null 。

查询结果如下例所示。

示例 1：

输入：
Employee 表：
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
输出：
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/second-highest-salary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~
```sql
-- LIMIT 返回一步 OFFSET 跳过一步 DESC 倒序排列
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```
---

## 03_数独游戏

```python

def isValidSudoku():
    board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
'''
哈希算法 row,col,block分别生成的依据是9行*9个数字、9列*9个数字、9块*9个数字
在判断相同行列块中数字是否变成了赋值的1 从而return
不能 使用 [[0] *9]*9 这样第二个九相当于引用了9遍列表[[0] * 9] 会出现修改后数值都变 exp: [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
'''
    row = [[0] * 9 for _ in range(9)]
    col = [[0] * 9 for _ in range(9)]
    block = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = int(board[i][j]) - 1
                print(num)
                b = (i // 3) * 3 + j // 3
                print(b)
                if row[i][num] or col[j][num] or block[b][num]:
                    print(block)
                    return False
                row[i][num] = col[j][num] = block[b][num] = 1
    return True

'''
Method 2 ： 生成三种数组，再将合并成一种数组，遍历其中的counter，看每个的计数情况是否为 0，1
改进 判断哈希赋值 32ms,99%
'''

    # n = list(map(list,zip(*board)))

    # nn,nnn = [],[]
    # for a in board:
    #     nn += a
    # ab = [nn[i:i+3] for i in range(0,len(nn),3)]
    # for b in [0,1,2,9,10,11,18,19,20]:
    #     nnn += [ab[b]+ab[b+3]+ab[b+6]]
    # num = board+n+nnn
    for i in num:
        nnnn = [0]*9
        for a in i:
            if a != '.':
                n = int(a) - 1
                if nnnn[n] == 1:
                    return False
                nnnn[n] = 1
    return True


    # rs = 0
    # for a in range(len(num)):
    #         count = Counter(num[a])
    #         for i in range(1,10):
    #             if count[str(i)] not in [0,1]:
    #                     rs += 1
    #                     return False
    #             else: continue
    # if rs == 0 : return True


```
<!--


---
title: "07_stu"
date: 2022-11-30T16:32:38+08:00
draft: false
tags: ['数据结构','链表']
categories: ['stu']
description: "开启链表的学习主要是快慢指针方法 或者 用哈希表的方法"

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

<!--more-->
## 1_链表_判断是否有环
开启链表的学习主要是快慢指针方法 或者 用哈希表的方法
![leecode_链表](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png "leecode_链表")  
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # 空链表或链表只有一个节点，无环
        if not head or head.next == None:
            return False

        # 初始化快慢指针
        fast = slow = head

        # 如果不存在环，肯定 fast 先指向 null
        # 细节：fast 每次走 2 步，所以要确定 fast 和 fast.next 不为空，不然会报执行出错。
        while fast and fast.next:

            # 快指针移动 2 步，慢指针移动 1 步
            fast = fast.next.next
            slow = slow.next

            # 快慢指针相遇，有环
            if fast == slow:
                return True

        return 
```
## 2_链表递归
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 

示例 1：
![2](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg "链表删除")

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]
示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-linked-list-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        if head.val == val :
            head = self.removeElements(head.next,val)
            return head
        else:
            # self.removeElements(head.next,val)  错误是否需要前面先赋值，否则return的怎么返回 eg下方正确方式
            head.next = self.removeElements(head.next,val) 
            return head
```
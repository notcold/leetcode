#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 分治或者 优先级队列
        length = len(lists) 
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        if length == 2:
            return self.mergeTwo(lists[0], lists[1])
        n = length >> 1
        left = lists[0:n]
        right = lists[n:]
        # 分治，k 个元素做2等分合并
        return self.mergeTwo(self.mergeKLists(left), self.mergeKLists(right))

    def mergeTwo(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = None
        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwo(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTwo(list1, list2.next)

        return head


# @lc code=end


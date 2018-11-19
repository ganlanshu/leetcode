# -*- coding:utf-8 -*-
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre


    def reverseList1(self, head):
        """
        递归方法反转链表
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        reversed_second = self.reverseList(head.next)
        new_node = head.next
        new_node.next = head
        head.next = None
        return reversed_second


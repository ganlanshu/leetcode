#coding=utf-8
"""
203. Remove Linked List Elements
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        current = head
        while current:
            if current.val != val:
                pre = current
            else:
                pre.next = current.next
            current = current.next
        return new_head.next

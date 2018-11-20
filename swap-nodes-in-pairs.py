# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
24. Swap Nodes in Pairs
"""

class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current and current.next:
            temp = current.next
            pre.next = temp
            post = temp.next
            temp.next = current
            current.next = post
            pre = current
            current = post
        return dummy.next
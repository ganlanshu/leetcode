#coding=utf-8
"""
83. Remove Duplicates from Sorted List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        current = head
        while current and current.next:
            next = current.next
            if current.val == next.val:
                current.next = next.next
            else:
                current = current.next
        return head

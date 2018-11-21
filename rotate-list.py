# coding=utf-8

"""
61. Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        length = self.get_link_length(head)
        if k >= length:
            k = k % length
        if k == 0:
            return head

        current = head
        count = 1
        while count < length - k:
            current = current.next
            count += 1
        new_head = current.next
        current = new_head
        while current:
            pre = current
            current = current.next
        pre.next = head
        return new_head


    def get_link_length(self, head):
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        return length

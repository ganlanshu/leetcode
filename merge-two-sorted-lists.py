#coding=utf-8
# Definition for singly-linked list.

"""
21. Merge Two Sorted Lists
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        merged_list = l1 if l1.val <= l2.val else l2
        greater = l1 if l1.val > l2.val else l2
        smaller = merged_list

        pre = None
        while smaller and greater:
            if smaller.val <= greater.val:
                pre = smaller
                temp_1 = smaller.next
                smaller = temp_1
            else:
                temp_2 = greater.next
                pre.next = greater
                pre = greater
                greater.next = smaller
                greater = temp_2
        if greater:
            pre.next = greater
        return merged_list


    def mergeTwoLists1(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        new_head = ListNode(0)
        current = new_head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return new_head.next


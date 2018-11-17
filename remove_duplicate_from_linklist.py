#coding=utf-8
"""
83. Remove Duplicates from Sorted List
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

    def deleteDuplicates1(self, head):
        """
        82. Remove Duplicates from Sorted List II
        Given a sorted linked list, delete all nodes that have duplicate numbers,
        leaving only distinct numbers from the original list. 参考以下
        https://blog.csdn.net/gatieme/article/details/51604199
        :param head:
        :return:

        """
        if not head:
            return
        if not head.next:
            return head
        fake_head = ListNode(0)
        fake_head.next = head
        pre = fake_head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
                pre.next = current
            else:
                pre = current
                current = current.next
        return fake_head.next

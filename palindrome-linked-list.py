#coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pass

    def _reverse_linklist(self, head):
        pre = None
        current = head
        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre

    def middleNode(self, head):
        """
        876. Middle of the Linked List
        :param head:
        :return:
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

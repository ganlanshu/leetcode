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
        if not head:
            return True
        if not head.next:
            return True
        current = head
        mid_node = self.find_middlenode_and_slice(current)
        right_link = self._reverse_linklist(mid_node)
        left_link = current
        while left_link and right_link:
            if left_link.val != right_link.val:
                return False
        return True

    def _reverse_linklist(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    def find_middlenode_and_slice(self, head):
        """
        判断是否是回文时,找到中间节点,把中间节点以前的阶段
        :param head:
        :return:
        """
        slow = fast = pre = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None
        return slow

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

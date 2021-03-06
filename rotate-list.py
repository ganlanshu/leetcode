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
        length, end = self.get_link_length_and_end(head)
        k = k % length
        if k == 0:
            return head
        current = head
        count = 1
        while count < length - k:
            current = current.next
            count += 1
        new_head = current.next
        current.next = None
        end.next = head
        return new_head

    def get_link_length_and_end(self, head):
        if not head:
            return 0, head
        if not head.next:
            return 1, head
        ptr = head
        length = 1
        while ptr.next:
            length += 1
            ptr = ptr.next
        return length, ptr

    def FindKthToTail(self, head, k):
        """
        链表中倒数第k个结点,如果倒数第k不存在,就返回空,倒数第0也是空
        :param head:
        :return:
        """
        if not head or k <= 0:
            return
        length, end = self.get_link_length_and_end(head)
        if k > length:
            return
        current = head
        count = 0
        while count < length-k:
            count += 1
            current = current.next
        return current

    def removeNthFromEnd(self, head, n):
        """
        19. Remove Nth Node From End of List
        two pass algorithm
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n <= 0:
            return
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if n > length:
            return
        length -= n
        pre = dummy
        while length > 0:
            pre = pre.next
            length -= 1
        pre.next = pre.next.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        """
        one pass algorithm
        Maintain two pointers and update one with a delay of n steps.
        :param head:
        :param n:
        :return:
        """
        if not head:
            return
        if n <= 0:
            return
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        count = 0
        while count <= n and fast:
            fast = fast.next
            count += 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

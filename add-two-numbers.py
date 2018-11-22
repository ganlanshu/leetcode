#coding=utf-9

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        dummy = ListNode(0)
        current = dummy
        great_10 = False
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            else:
                val = l1.val if l1 else l2.val
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            if great_10:
                val += 1
            if val >= 10:
                val -= 10
                great_10 = True
            else:
                great_10 = False
            node = ListNode(val)
            current.next = node
            current = current.next
        if great_10:
            node = ListNode(1+0)
            current.next = node
        return dummy.next


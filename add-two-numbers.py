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

    def addTwoNumbers1(self, l1, l2):
        """
        参考solution里的写法
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        greater_10 = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = l1_val + l2_val
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            sum_val += greater_10
            node = ListNode(sum_val % 10)
            current.next = node
            current = current.next
            greater_10 = sum_val / 10

        if greater_10:
            current.next = ListNode(greater_10)
        return dummy.next

    def addTwoNumbers2(self, l1, l2):
        """
        445. Add Two Numbers II
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        link_sum_string = str(self.link_to_decimal(l1) + self.link_to_decimal(l2))
        dummy = ListNode(0)
        pre = dummy
        for i in link_sum_string:
            node = ListNode((i))
            pre.next = node
            pre = pre.next
        return dummy.next

    def link_to_decimal(self, head):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        decimal_num = 0
        current = head
        while length > 0:
            decimal_num += current.val * 10 **(length-1)
            length -= 1
            current = current.next
        return decimal_num

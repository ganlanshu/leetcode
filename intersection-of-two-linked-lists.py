# Definition for singly-linked list.
"""
160. Intersection of Two Linked Lists
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        全部遍历一遍
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        curr_a = headA
        curr_b = headB
        while curr_a:
            if curr_a is curr_b:
                return curr_a
            else:
                if curr_b:
                    curr_b = curr_b.next
                else:
                    curr_a = curr_a.next
                    curr_b = headB
        return


    def getIntersectionNode1(self, headA, headB):
        """
        把headA 每个节点的地址存入set,再检查B中每个节点的地址
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        curr_a = headA
        curr_b = headB
        id_set = set()
        while curr_a:
            id_set.add(id(curr_a))
            curr_a = curr_a.next
        while curr_b:
            if id(curr_b) in id_set:
                return curr_b
            curr_b = curr_b.next
        return

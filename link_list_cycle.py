# coding=utf-8


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        https://leetcode.com/problems/linked-list-cycle/solution/
        提供了两种解决方法,hash 和两个快慢指针
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        node_set = set()
        current = head
        while current:
            if current not in node_set:
                node_set.add(current)
                current = current.next
            else:
                return True
        return False

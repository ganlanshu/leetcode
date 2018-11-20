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

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return
        node_set = set()
        current = head
        while current:
            if current not in node_set:
                node_set.add(current)
                current = current.next
            else:
                return current
        return

    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return
        fast = slow = head
        # 找到快慢指针相遇的点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return
        meet_point = slow
        fast = head
        while fast != meet_point:
            fast = fast.next
            meet_point = meet_point.next
        return meet_point


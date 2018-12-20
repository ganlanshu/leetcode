# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        odd = head
        first_even = even = head.next
        current = even.next
        count = 1
        while current:
            if count%2 == 1:
                odd.next = current
                odd = current

            else:
                even.next = current
                even = current
            current = current.next
            count += 1
        even.next = None
        odd.next = first_even
        return head

    def oddEvenList1(self, head):
        if not (head and head.next):
            return head
        odd = head
        first_even = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = first_even
        return head


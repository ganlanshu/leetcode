#coding=utf-8
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        21. Merge Two Sorted Lists
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        merged_list = l1 if l1.val <= l2.val else l2
        greater = l1 if l1.val > l2.val else l2
        smaller = merged_list

        pre = None
        while smaller and greater:
            if smaller.val <= greater.val:
                pre = smaller
                temp_1 = smaller.next
                smaller = temp_1
            else:
                temp_2 = greater.next
                pre.next = greater
                pre = greater
                greater.next = smaller
                greater = temp_2
        if greater:
            pre.next = greater
        return merged_list


    def mergeTwoLists1(self, l1, l2):
        new_head = ListNode(0)
        current = new_head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return new_head.next

    def mergeKLists(self, lists):
        """
        23. Merge k Sorted Lists
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if not k:
            return
        if k == 1:
            return lists[0]

        def _merge_klists(l, r):
            if l == r:
                return lists[l]
            mid = (l+r)/2
            left_merged_list = _merge_klists(l, mid)
            right_merged_list = _merge_klists(mid+1, r)
            return self.mergeTwoLists1(left_merged_list, right_merged_list)
        return _merge_klists(0, k-1)

    def mergeKLists1(self, lists):
        """
        23. Merge k Sorted Lists
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0:
            return
        if k == 1:
            return lists[0]
        mid = k/2
        left_list = self.mergeKLists(lists[:mid])
        right_list = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left_list, right_list)

    def mergeKLists2(self, lists):
        if not lists:
            return
        k = len(lists)
        step = 1
        while step < k:
            for i in range(0, k-step, 2*step):
                lists[i] = self.mergeTwoLists1(lists[i], lists[i+step])
            step *= 2
        return lists[0]
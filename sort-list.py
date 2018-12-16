# coding=utf-8

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def merge_sort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        mid_node = self.get_mid_node(head)
        right = mid_node.next
        mid_node.next = None
        left = head
        return self.merge_two_sorted_list(self.merge_sort(left), self.merge_sort(right))

    def merge_two_sorted_list(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        pre = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return dummy.next


    def get_mid_node(self, head):
        if not head:
            return
        if not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def select_sort(self, aliast):
        """
        alist是list类型
        :param aliast:
        :return:
        """
        n = len(aliast)
        for i in range(n-1):
            small = aliast[i]
            for j in range(i+1, n):
                if aliast[j] < small:
                    small = aliast[j]
                    small_index = j
            if small != aliast[i]:
                aliast[i], aliast[small_index] = aliast[small_index], aliast[i]
        return aliast

    def quick_sort(self, alist, low, high):
        """
        :param alist:
        :return:
        """
        if low < high:
            partion = self.partion(alist, low, high)
            self.quick_sort(alist, low, partion-1)
            self.quick_sort(alist, partion+1, high)

    def partion(self, alist, low, high):
        pivot = alist[low]
        location = low
        while low < high:
            while high > low and alist[high] >= pivot:
                high -= 1
            while low < high and alist[low] <= pivot:
                low += 1
            if low < high:
                alist[low], alist[high] = alist[high], alist[low]
        alist[location], alist[low] = alist[low], alist[location]
        return low

    def merge_sort1(self, alist):
        """
        对数组alist归并排序
        :param alist:
        :return:
        """
        if len(alist) <= 1:
            return alist
        mid = len(alist)//2
        left_half = self.merge_sort1(alist[:mid])
        right_half = self.merge_sort1(alist[mid:])
        return self.merge1(left_half, right_half)

    def merge1(self, left, right):
        result = []
        left_length = len(left)
        right_length = len(right)
        i = j = 0
        while i < left_length and j < right_length:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


if __name__ == '__main__':
    s = Solution()
    alist = [6,1,2,7,9,3,4,5,10,8]
    print s.merge_sort1(alist)
    print alist
    #s.quick_sort(alist, 0, len(alist)-1)


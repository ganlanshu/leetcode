# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
328. Odd Even Linked List
Given a singly linked list, group all odd nodes together
followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

"""

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

    def oddEvenList2(self, nums):
        """
        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
        使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
        并保证奇数和奇数，偶数和偶数之间的相对位置不变。
        :param nums List[int]:
        :return:
        """
        odd = []
        even = []
        for num in nums:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        odd.extend(even)
        del even
        return odd

    def oddEvenList3(self, nums):
        """
        如果不能使用额外的空间,只能在远处修改的话,可以维护两个指针,从前后夹逼,把奇数,偶数放到该去的位置
        :param nums:
        :return:
        """
        # 下面运用了快排的思想,但排序后奇数的相对顺序被打乱,偶数也是
        odd = 0
        even = len(nums)-1
        while odd < even:
            while odd < even and nums[odd]%2 == 1:
                odd += 1
            while even > odd and nums[even]%2 == 0:
                even -= 1
            if odd < even:
                nums[odd], nums[even] = nums[even], nums[odd]

    def oddEvenList4(self, nums):
        """
        不改变奇数偶数相对位置,不用额外空间,用冒泡的思想
        :param nums:
        :return:
        """
        n = len(nums)
        i = 0
        swap = True
        # n-1趟, 每一趟把偶数放到最后的位置
        while swap and i < n-1:
            # i为偶数,i+1为奇数则交换
            swap = False
            for j in range(n-1-i):
                if nums[j] % 2 == 0 and nums[j+1] % 2 == 1:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            i += 1
        return nums

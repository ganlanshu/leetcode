# coding=utf-8

"""
215. Kth Largest Element in an Array
"""
import heapq

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        最简单粗暴的方法
        """
        if k > len(nums):
            return -1
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k-1]

    def findKthLargest1(self, nums, k):
        """
        用最大堆做,python内置的heapq 的heapify是转为最小堆,
        用了一个trick,取每个元素的相反数,得到最小堆,第一个pop的元素的相反数就是最大值
        :param nums:
        :param k:
        :return:
        """
        if k > len(nums):
            return -1
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest2(self, nums, k):
        """
        利用最小堆
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        if k > n:
            return -1
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, n):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
        return min_heap[0]

    def findKthLargest3(self, nums, k):
        """
        使用快排的思想
        :param nums:
        :param k:
        :return:
        """
        pass

# coding=utf-8

"""
152. Maximum Product Subarray
"""
class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_product = nums[0]
        max_pre = min_pre = nums[0]
        n = len(nums)
        for i in range(1, n):
            max_dpi = max(nums[i] * max_pre, nums[i], nums[i] * min_pre)
            min_dpi = min(nums[i] * max_pre, nums[i], nums[i] * min_pre)
            max_pre = max_dpi
            min_pre = min_dpi
            max_product = max(max_product, max_dpi)
        return max_product

    def maxProduct1(self, nums):
        """
        从discuss看到的,简明写法
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_product = nums[0]
        big = small = nums[0]
        for i in nums[1:]:
            big, small = max(i, i*big, i*small), min(i, i*big, i*small)
            max_product = max(big, max_product)
        return max_product

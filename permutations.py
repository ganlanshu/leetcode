# coding=utf-8
"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.
求给定数组的全排列,数组里没有重复元素
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        用递归方法
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        n = len(nums)
        re = self.permute(nums[1:])
        result = [[nums[0]] + r for r in re]
        for i in range(1, n):
            nums[i], nums[0] = nums[0], nums[i]
            re = self.permute(nums[1:])
            result.extend([[nums[0]]+r for r in re])
        return result













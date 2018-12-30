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
        result = []
        for i in range(n):
            re = self.permute(nums[:i]+nums[i+1:])
            result.extend([[nums[i]]+r for r in re])
        return result

    def permute1(self, nums):
        res = []

        def _permute(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                _permute(nums[:i]+nums[i+1:], path+[nums[i]])
        _permute(nums, [])
        return res




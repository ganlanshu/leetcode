# coding=utf-8

"""
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums[0]], []]
        subset_post = self.subsets(nums[1:])
        new_subset = [[nums[0]] + path for path in subset_post]
        subset_post.extend(new_subset)
        return subset_post


# coding=utf-8

"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red_count = nums.count(0)
        white_count = nums.count(1)
        for i in range(red_count):
            nums[i] = 0
        for i in range(red_count, red_count+white_count):
            nums[i] = 1
        for i in range(red_count+white_count, n):
            nums[i] = 2


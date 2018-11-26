# coding=utf-8

"""
581. Shortest Unsorted Continuous Subarray
"""
import copy
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 0
        nums_copy = copy.copy(nums)
        nums_copy.sort()
        begin = 0
        end = n - 1
        while begin <= end:
            if nums[begin] == nums_copy[begin]:
                begin += 1
            else:
                break
        while begin <= end:
            if nums[end] == nums_copy[end]:
                end -= 1
            else:
                break
        return end-begin+1

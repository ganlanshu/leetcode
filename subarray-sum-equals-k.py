# coding=utf-8

"""
560. Subarray Sum Equals K
Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.
"""

class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        brute force 全部遍历一遍
        """
        n = len(nums)
        count = 0
        for i in range(n):
            sum_num = 0
            hit = False
            for j in range(i, n):
                sum_num += nums[j]
                if sum_num == k:
                    count += 1
                    hit = True
                    break
            while hit and j < n-1 and nums[j+1] == 0:
                count += 1
                j += 1
        return count

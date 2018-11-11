#coding=utf-8
"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray
"""
class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i] = a[i] + dp[i-1] if dp[i-1] > 0 else 0
        """
        if not nums:
            return 0
        max_sum = nums[0]
        n = len(nums)
        pre = nums[0]
        for i in range(1, n):
            dpi = nums[i] + pre if pre > 0 else nums[i]
            pre = dpi
            max_sum = max(dpi, max_sum)
        return max_sum


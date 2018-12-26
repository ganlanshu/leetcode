# coding=utf-8
"""
239. Sliding Window Maximum

"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        先想到一个简单粗暴的方法
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res


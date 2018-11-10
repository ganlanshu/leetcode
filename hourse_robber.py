#coding=utf-8
"""
198. House Robber

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        di = 0
        for num in nums:
            di = max(a + num, b)
            a = b
            b = di
        return di

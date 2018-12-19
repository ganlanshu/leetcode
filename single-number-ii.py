# coding=utf-8
"""
137. Single Number II
Given a non-empty array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        for i in nums:
            if i in hash_map:
                if hash_map[i] == 2:
                    hash_map.pop(i)
                else:
                    hash_map.[i] += 1
            else:
                hash_map[i] = 1
        return hash_map.popitem()[0]


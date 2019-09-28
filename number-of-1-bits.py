"""
191. Number of 1 Bits
Write a function that takes an unsigned integer and return the
number of '1' bits it has (also known as the Hamming weight).
https://leetcode.com/problems/
"""


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hamming_weight(self, n):
        #  一种更快的方法
        res = 0
        while n:
            res += 1
            n &= n-1
        return res


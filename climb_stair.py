#coding=utf-8
"""
70. Climbing Stairs

"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        f0, f1 =  1, 2
        for i in range(2, n):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return fn
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

    def climbStairs_fibnacci(self, n):
        """
        利用斐波那契数列的通项公式
        https://blog.csdn.net/zbl_scnu/article/details/16806325
        :param n:
        :return:
        """
        fibn = int(1/math.sqrt(5) * (((1+math.sqrt(5))/2)**(n+1) - ((1-math.sqrt(5))/2)**(n+1)))
        return fibn

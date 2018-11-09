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

    def climb_n_stairs(self, n):
        """
        一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
        求该青蛙跳上一个n级的台阶总共有多少种跳法
        从 n=1 开始推导
        后面每一次的都是前面所有的和加1
        最后发现是一个等比数列
        :param n:
        :return:
        """
        if n == 0:
            return 0
        return 2**(n-1)


    def minCostClimbingStairs(self, cost):
        """
        用最小成本爬梯子
        https://leetcode.com/problems/min-cost-climbing-stairs
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[-1])

        f0, f1 = 0, cost[n-1]
        for i in range(n-2, 0, -1):
            fi = cost[i] + min(f0, f1)
            f0 = f1
            f1 = fi
        # 最后比较index为0和1的，取最小值
        f0 = cost[0] + min(f0, f1)
        return min(f0, fi)

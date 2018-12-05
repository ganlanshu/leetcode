# coding=utf-8

"""
62. Unique Paths
"""


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)



    def uniquePaths1(self, m, n):
        """
        典型的动态规划 dp[i,j] = dp[i-1,j]+dp[i,j-1]
        :param m:
        :param n:
        :return:
        """
        if m < 1 or n < 1:
            return 0
        if m == 1 or n == 1:
            return 1
        # 先做出一个m*n的矩阵
        result = [
            [1]*n
        ]
        result *= m
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m-1][n-1]

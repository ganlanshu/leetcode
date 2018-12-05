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

    def uniquePaths2(self, m, n):
        """
        其实不需要把每行的数据都存下来,只保留最后一行的数据,就是一位数组,n个元素
        :param m:
        :param n:
        :return:
        """
        # 先声明一个包含n个元素的list,result[0]一直是1,不需要变,
        # 第一行一直是1,不需要改
        result = [1]*n
        for round in range(1, m):
            for index in range(1, n):
                result[index] += result[index-1]
        return result[n-1]

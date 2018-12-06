# coding=utf-8

"""
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right
which minimizes the sum of all numbers along its path.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # 计算第一行的path sum
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        # 计算第一列的path sum
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i][j]+grid[i-1][j], grid[i][j]+grid[i][j-1])
        return grid[m-1][n-1]

    def minPathSum1(self, grid):
        """
        不修改grid,用一个新的list保存每一行的结果
        :param grid:
        :return:
        """
        result = grid[0]
        n = len(result)
        for i in range(1, n):
            result[i] += result[i-1]
        m = len(grid)
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    result[j] += grid[i][j]
                else:
                    result[j] = min(grid[i][j]+result[j], grid[i][j]+result[j-1])
        return result[n-1]


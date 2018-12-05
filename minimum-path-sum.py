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


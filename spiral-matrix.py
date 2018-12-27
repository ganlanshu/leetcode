# coding=utf-8

"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        把一个矩阵用螺旋方式打印出来
        """
        m = len(matrix)
        n = len(matrix[0])
        # 先确定需要旋转的圈数
        circle = min(m, n)
        if circle%2 == 0:
            circle = circle/2
        else:
            circle = circle/2+1
        res = []
        # i表示第i圈
        for i in range(circle):
            # 从左到右
            for col in range(i, n-i):
                res.append(matrix[i][col])
            # 从上到下
            for row in range(i+1, m-i):
                res.append(matrix[row][n-1-i])
            # 从右到左
            if i < m-1-i:
                for col in range(n-2-i, i-1, -1):
                    res.append(matrix[m-1-i][col])
            # 从下到上
            if i< n-1-i:
                for row in range(m-2-i, i, -1):
                    res.append(matrix[row][i])
        return res

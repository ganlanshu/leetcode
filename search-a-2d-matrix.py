# coding=utf-8

"""
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution:

    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)  # 行数
        m = len(matrix[0])  # 列数
        # 从右上角开始遍历
        row = 0
        column = m-1
        while row <= n-1 and column >= 0:
            if target < matrix[row][column]:
                column -= 1
            elif target > matrix[row][column]:
                row += 1
            elif target == matrix[row][column]:
                return True
        return False

    def searchMatrix1(self, matrix, target: int) -> bool:
        # m * n 个元素组成的有序数组，用二分查找最合适了
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1
        while low <= high:
            mid = (low+high)//2
            num = matrix[mid//n][mid%n]
            if num == target:
                return True
            elif num < target:
                low = mid+1
            else:
                high = mid-1
        return False



# -*- coding:utf-8 -*-
"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        rows = len(array)
        cols = len(array[0])

        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if array[row][col] == target:
                return row, col
            if target < array[row][col]:
                col -= 1
            else:
                row += 1
        return False

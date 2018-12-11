# coding=utf-8
"""
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height
where the width of each bar is 1, find the area of largest rectangle
in the histogram.
"""


class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        暴力解法,不能通过时间限制,只是比较容易想到
        """
        max_area = 0
        n = len(heights)
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(heights[j], min_height)
                max_area = max(max_area, min_height*(j-i+1))
        return max_area

    def largestRectangleArea1(self, heights):
        """
        上面方法的优化,对于每一个height,计算索引从0 到当前位置的面积,取最大值
        :param heights:
        :return:
        """
        max_area = 0
        n = len(heights)
        for i in range(n):
            # 如果下一个height比当前值大,那就不需要计算当前的面积,因为下一个算出来的面积更大
            if i+1 < n and heights[i] <= heights[i+1]:
                continue
            min_height = heights[i]
            for j in range(i, -1, -1):
                min_height = min(heights[j], min_height)
                max_area = max(max_area, min_height*(i-j+1))
        return max_area

# coding=utf-8

"""
11. Container With Most Water
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        n = len(height)
        max_area = 0
        for i in range(n-1):
            for j in range(i+1, n):
                area = (j-i)*min(height[i], height[j])
                max_area = max(area, max_area)
        return max_area

    def maxArea1(self, height):
        """
        用左右两个指针,求最大面积, 即 max((i-j)*min(height[i],height[j])),
        """
        n = len(height)
        i, j = 0, n-1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

    def maxArea2(self, height):
        """
        除了两端的指针,中间的, 长度都变短了,因此只有当中间的height更高,才值得往中间夹逼
        这是从discuss里看到的
        :param height:
        :return:
        """
        n = len(height)
        i, j = 0, n-1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            max_area = max(max_area, (j-i)*h)
            # 如果下一个height比上一个更小,不需要计算面积了,直接跳过去,因为长度变短,height如果更小
            # 面积只会更小
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and j > i:
                j -= 1
        return max_area

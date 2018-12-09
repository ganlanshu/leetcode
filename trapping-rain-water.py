# coding=utf-8

"""
42. Trapping Rain Water
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        用两个指针来做
        """
        left = 0
        right = len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max-height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water





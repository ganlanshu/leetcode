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

    def trap1(self, height):
        """
        动态规划, 维护数组dp
        对于height中的每一个元素
        第一次遍历
        dp[i]的值是height[i]左边的最大元素,
        第二次遍历,
        dp[i] 取height[i]中右边最大元素和左边做大元素中较小的
        减去height[i]就是当前元素能存的水
        对于height[i],最终水平面一定是左边做大元素和右边最大元素较小的
        那么height[i]能蓄的水就是水平面减去height[i]的值
        :param height:
        :return:
        """
        left_max = 0
        dp = []
        n = len(height)
        # 先取height中每个元素左边的最大值,放入dp
        for i in range(n):
            dp.append(left_max)
            left_max = max(left_max, height[i])
        # 再取height中每个元素右边的最大值,和上一步得到的值相比,取较小的,存入dp
        right_max = 0
        water = 0
        for i in range(n-1, -1, -1):
            dp[i] = min(dp[i], right_max)
            right_max = max(right_max, height[i])
            if dp[i] > height[i]:
                water += dp[i]-height[i]
        return water



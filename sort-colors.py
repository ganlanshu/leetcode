# coding=utf-8

"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red_count = nums.count(0)
        white_count = nums.count(1)
        for i in range(red_count):
            nums[i] = 0
        for i in range(red_count, red_count+white_count):
            nums[i] = 1
        for i in range(red_count+white_count, n):
            nums[i] = 2

    def sortColors1(self, nums):
        """
        用两个指针来做, red指针指向0, blue指针指向n-1
        从头开始遍历nums,若为0,和red指针交换值,red向后移
        若为2,和blue指针交换值,blue指针向前移
        若为1,继续遍历
        :param nums:
        :return:
        """
        n = len(nums)
        red = 0
        blue = n-1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            elif nums[i] == 1:
                i += 1

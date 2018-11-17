#coding=utf-8
"""
287. Find the Duplicate Number
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution(object):

    def find_duplicate(self, numbers):
        """
        :param numbers: list[int]
        :return: bool
        """
        if not numbers:
            return
        n = len(numbers)
        for i in range(1, n):
            while numbers[i] != i:
                if numbers[i] != numbers[numbers[i]]:
                    numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                else:
                    return numbers[i]
        return numbers[0]

    def find_duplicate(self, nums):
        while nums[nums[0]] != nums[0]:
            nums[0],nums[nums[0]] = nums[nums[0]], nums[0]
        return nums[0]

# coding=utf-8
"""
448. Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
"""

class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        比较容易想到,用了多余的空间
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums_set = set(nums)
        return [i for i in range(1, n+1) if i not in nums_set]

    def findDisappearedNumbers1(self, nums):
        """
        如果是排好序的,则nums[i] = i+1,这样没有重复出现的,也没有不出现的
        对于nums中的每个元素nums[i],如果nums[nums[i]-1] 为正,则改为负,如果是负,不变
        最后剩下的正数的index+1就是没有出现的数字
        :param nums:
        :return:
        """
        for elem in nums:
            elem_neg = nums[abs(elem)-1]
            if elem_neg > 0:
                nums[abs(elem)-1] = -elem_neg
        n = len(nums)
        return [index+1 for index in range(n) if nums[index] > 0]


    def findDisappearedNumbers2(self, nums):
        """
        交换nums[i] 和nums[nums[i]-1]的值 直到两者相等
        在判断nums[i] 和i+1是否相等
        :param nums:
        :return:
        """
        n = len(nums)
        res = []
        for i in range(n):
            while nums[i] != nums[nums[i]-1]:
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        for i in range(n):
            if nums[i] != i+1:
                res.append(i+1)
        return res

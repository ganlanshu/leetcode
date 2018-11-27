# coding=utf-8

"""
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
"""

class Solution(object):

    def findDuplicates(self, nums):
        """
        a[i] = i+1 时没有重复
        对每一个a[i],如果a[a[i]-1] 为正,改为负,如果已经是负数,说明a[a[i]-1]曾被改为负数,
        也就是a[i]重复了
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for elem in nums:
            elem_neg = nums[abs(elem)-1]
            if elem_neg > 0:
                nums[abs(elem)-1] = -elem_neg
            else:
                res.append(abs(elem))
        return res

    def findDuplicates1(self, nums):
        res = []
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i]-1]:
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]

        for i in range(n):
            if nums[i] != nums[i+1]:
                res.append(nums[i])
        return res




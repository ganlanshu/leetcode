# coding=utf-8
"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        n = len(nums)
        count = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                if count == 1:
                    return nums[i-1]
                count = 1
        return nums[-1]

    def singleNumber1(self, nums):
        """
        借助hashmap做,第一次出现的元素放入hashmap,
        第二次出现的pop,最后剩下的就是只出现一次的
        :param nums:
        :return:
        """
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map.pop(i)
        return hash_map.popitem()[0]

    def singleNumber2(self, nums):
        """
        数学公式
        2(a+b+c) - (2*a+2*b+c) = c
        :param nums:
        :return:
        """
        return 2*sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums):
        """
        位运算的异或,
        a^b = b^a
        a^0 = a
        a^a = 0
        偶数个元素异或后成为0,最后剩下的就是奇数元素
        :param nums:
        :return:
        """
        a = 0
        for i in nums:
            a = a^i
        return a

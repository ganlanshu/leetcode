# coding=utf-8
"""
169. Majority Element
"""
import random

class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        hash_map = {}
        size = len(nums)
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
                if hash_map[i] > size/2:
                    return i
            else:
                hash_map[i] = 1
        return nums[0]

    def majorityElement1(self, nums):
        from collections import Counter
        count = Counter(nums)
        return max(count.keys(), key=count.get)

    def majorityElement1(self, nums):
        if not nums:
            return
        nums.sort()
        n = len(nums)
        return nums[n//2]

    def majorityElement1(self, nums):
        """
        从solution里看到的方法
        :param nums:
        :return:
        """
        majority_count = len(nums)//2
        while 1:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate



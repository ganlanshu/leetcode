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
            else:
                hash_map[i] = 1
        for k, v in hash_map.items():
            if v > size // 2:
                return k

    def majorityElement1(self, nums):
        from collections import Counter
        count = Counter(nums)
        return max(count.keys(), key=count.get)

    def majorityElement2(self, nums):
        if not nums:
            return
        nums.sort()
        n = len(nums)
        return nums[n//2]

    def majorityElement3(self, nums):
        """
        从solution里看到的方法, 对于出现次数大于一般的数组来说,随机选一个数字,就是主要数的可能性很大
        :param nums:
        :return:
        """
        majority_count = len(nums)//2
        while 1:
            candidate = random.choice(nums)
            if nums.count(candidate) > majority_count:
                return candidate

    def majorityElement4(self, nums):
        """
        每次从数组中找出一对不同的元素，将它们从数组中删除，直到遍历完整个数组, 剩下的就是majority element
        :param nums:
        :return:
        """
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

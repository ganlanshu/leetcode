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

    def majorityElement4(self, nums):
        """
        题目改为找出出现超过 len(nums)/3 的元素
        这样的元素最多有2个,每次从数组中找出3个不同的元素,删掉,剩下的就是
        :param nums:
        :return:
        """
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        result = []
        if count1 > len(nums)//3:
            result.append(candidate1)
        if count2 > len(nums)//3:
            result.append(candidate2)
        return result

    def majority_element5(self, nums):
        """
        看nums数组的每一个位是0还是1，对于整数来说，统计32个位上每个位出现1和0的次数，一定有一个次数大一些，就是这个bit众数的这个
        bit上一定是出现次数多的（0或1），最后把bit转化成十进制数字
        :param nums:
        :return:
        """
        result = 0
        for i in range(32):
            zeros = ones = 0
            for num in nums:
                if num & (1 << i) != 0:
                    ones += 1
                else:
                    zeros += 1
            if ones > zeros:
                result |= (1 << i)
        return result


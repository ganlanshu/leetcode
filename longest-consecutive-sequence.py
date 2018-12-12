# coding=utf-8

"""
128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the
longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
"""

class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        longest_steak = 1
        current_count = 1
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                if nums[i]+1 == nums[i+1]:
                    current_count += 1
                else:
                    longest_steak = max(current_count, longest_steak)
                    current_count = 1
        return max(current_count, longest_steak)


    def longestConsecutive1(self, nums):
        # 把nums放到set里,这样查找是用hash,更快
        if not nums:
            return 0
        longest_steak = 1
        num_set = set(nums)
        for elem in num_set:
            # 只有前一个elem-1不在nums里时,才需要重新计算,否则跳过for循环
            if elem-1 not in num_set:
                current_count = 1
                while elem+1 in num_set:
                    current_count += 1
                    elem += 1
                    longest_steak = max(longest_steak, current_count)

        return longest_steak

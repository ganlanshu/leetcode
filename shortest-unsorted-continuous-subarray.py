# coding=utf-8
import copy

"""
581. Shortest Unsorted Continuous Subarray
"""

class Solution(object):

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 0
        nums_copy = copy.copy(nums)
        nums_copy.sort()
        begin = 0
        end = n - 1
        while begin <= end:
            if nums[begin] == nums_copy[begin]:
                begin += 1
            else:
                break
        while begin <= end:
            if nums[end] == nums_copy[end]:
                end -= 1
            else:
                break
        return end-begin+1

    def findUnsortedSubarray1(self, nums):
        # 详细解释参考
        # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103066/Ideas-behind-the-O(n)-two-pass-and-one-pass-solutions
        if not nums:
            return 0
        begin = 0
        end = len(nums) - 1
        while begin < end and nums[begin] <= nums[begin+1]:
            begin += 1
        if begin == end:
            return 0
        while nums[end] >= nums[end-1]:
            end -= 1
        max_num = float('-inf')
        min_num = float('inf')
        for k in range(begin, end+1):
            max_num = max(max_num, nums[k])
            min_num = min(min_num, nums[k])

        while begin >= 0 and nums[begin] > min_num:
            begin -= 1
        while end < len(nums) and nums[end] < max_num:
            end += 1
        return end - begin - 1

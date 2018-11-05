#coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_index_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if value_index_map.__contains__(complement):
                return [value_index_map.get(complement), index]
            value_index_map[value] = index

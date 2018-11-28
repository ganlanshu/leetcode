# coding=utf-8

"""
283. Move Zeroes
"""
class Solution(object):

    def moveZeroes(self, nums):
        """
        类似冒泡排序,相邻两个元素交换
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        while j < n:
            if nums[j] != 0:
                j +=1
            else:
                k = j
                while j < n and nums[j] == 0:
                    j += 1
                # nums从j开始后面的都是0
                if j == n:
                    break
                nums[k], nums[j] = nums[j], nums[k]
                # j已经到了最后一位,0已经在最后面了
                if j == n-1:
                    break
                j = k+1

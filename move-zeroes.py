# coding=utf-8

"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
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

    def moveZeroes1(self, nums):
        """
        把所有0移到后面,也就是把所有非0移到前面,
        用两个指针来做,快指针遍历数组,遇到非零元素,
        放到慢指针的后面,快指针遍历结束时,慢指针所在的位置以前都是非0元素,而且顺序不变,
        再从慢指针遍历到数组结束,把包含的元素设为0
        :param nums:
        :return:
        """
        n = len(nums)
        # non_zero做为慢指针,记录非零元素的位置
        non_zero = 0

        # 遍历结束后,non_zero 索引左边的元素全部是非0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1
        # 从non_zero索引开始,后面的元素都要置为0
        for i in range(non_zero, n):
            nums[i] = 0

    def moveZeroes2(self, nums):
        # 利用list内置的方法,先删除0, 再添加的后面
        zero_count = nums.count(0)
        for i in range(zero_count):
            nums.remove(0)
            nums.append(0)

    def moveZeroes3(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

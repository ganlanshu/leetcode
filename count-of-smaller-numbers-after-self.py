# coding=utf-8

"""
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i]
is the number of smaller elements to the right of nums[i].
"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        先用一种简单粗暴的解法
        """
        n = len(nums)
        res = []
        for i in range(n-1):
            count = 0
            for j in range(i, n):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        res.append(0)
        return res

    def countSmaller1(self, nums):
        """
        从nums最后一个元素开始,把元素按照二分查找插入有序的数组,这个元素在有序数组的索引
        就是右边比它小的元素的个数
        :param nums:
        :return:
        """
        n = len(nums)
        res = [0]*n
        binary_list = []
        for i in range(n-1, -1, -1):
            k = nums[i]
            low = 0
            high = len(binary_list)
            while low < high:
                mid = (low+high)//2
                if binary_list[mid] >= k:
                    high = mid
                else:
                    low = mid+1
            binary_list.insert(low, k)
            res[i] = low
        return res

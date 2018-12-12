# coding=utf-8
from collections import deque

"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 合并两个有序列表
        merged_list = []
        nums1 = deque(nums1)
        nums2 = deque(nums2)
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                merged_list.append(nums1.popleft())
            else:
                merged_list.append(nums2.popleft())
        if nums1:
            merged_list.extend(nums1)
        if nums2:
            merged_list.extend(nums2)
        n = len(merged_list)
        if n%2: #  为奇数
            return merged_list[n//2]
        else:
            return float(merged_list[n//2]+merged_list[n//2-1])/2




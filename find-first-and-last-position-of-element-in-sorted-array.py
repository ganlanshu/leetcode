# coding=utf-8

"""
34. Find First and Last Position of Element in Sorted Array
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low = 0
        high = n-1
        found = False
        while low <= high:
            mid = (low+high)//2
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else:
                found = True
                break
        if not found:
            return [-1, -1]
        l = h = mid
        while l > 0 and nums[l-1] == target:
            l -= 1
        while h < n-1 and nums[h+1] == target:
            h += 1
        return [l, h]


def binary_search_upper_bound(alist, target):
    """
    在有序alist中寻找第一个大于target的数
    :param alist:
    :param target:
    :return:
    """
    low = 0
    high = len(alist) - 1
    if low > high:
        return -1
    if alist[high] <= target:
        return -1
    while low < high:
        mid = (low+high)//2
        if alist[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low


def binary_search_lower_bound(alist, target):
    """
    从有序alist寻找比target小的第一个元素
    :param alist:
    :param target:
    :return:
    """
    low = 0
    n = len(alist)
    high = n-1
    if low > high:
        return -1
    if alist[0] >= target:
        return -1
    while low < high:
        mid = (low+high+1)//2
        if alist[mid] < target:
            low = mid
        else:
            high = mid-1
    return low


if __name__ == '__main__':
    a = [2, 3, 4, 6, 7, 8]
    #print binary_search_upper_bound(a, 4)
    print binary_search_lower_bound(a, 6)

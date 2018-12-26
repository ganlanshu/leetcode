# coding=utf-8
"""
239. Sliding Window Maximum

"""
class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        先想到一个简单粗暴的方法
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res

    def maxSlidingWindow1(self, nums, k):
        """
        :param nums:
        :param k:
        :return:
        看了提示,用deque来做
        """
        from collections import deque
        if not nums:
            return []
        queue = deque(nums[:k])
        res = []
        res.append(max(queue))
        n = len(nums)
        for i in range(k, n):
            queue.popleft()
            queue.append(nums[i])
            res.append(max(queue))
        return res



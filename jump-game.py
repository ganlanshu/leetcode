# coding=utf-8

"""
55. Jump Game
"""

class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        如果一个节点可以通过某种方法到达终点,那么只要能到达这个节点就能到达终点,也就是可以把这个节点
        设为新的终点, 如果终点最后index是0,也就可以到达了
        """
        last = len(nums)-1
        for i in range(last-1, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0

    def canJump1(self, nums):
        """
        遍历nums,求每一个节点能够到达的最大距离reach,如果reach大于等于最后一个节点,就可以到达终点
        :param nums:
        :return:
        """
        n = len(nums)
        reach = 0
        for i in range(n):
            if i > reach or reach >= n-1:
                break
            reach = max(reach, i+nums[i])
        return reach >= n-1

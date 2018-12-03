# coding=utf-8

"""
238. Product of Array Except Self
"""
class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 第i个元素的乘积等于他前面所有元素的乘积乘以它后面所有元素的成绩
        n = len(nums)
        product_pre = []
        product_pre.append(1)
        for i in range(1, n):
            product_pre.append(nums[i-1]*product_pre[-1])
        product_post = range(n)
        product_post[-1] = 1
        for i in range(n-2, -1, -1):
            product_post[i] = nums[i+1]*product_post[i+1]
        output = []
        for i in range(n):
            output.append(product_pre[i]*product_post[i])
        return output








# coding=utf-8

"""
560. Subarray Sum Equals K
Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.
"""

class Solution(object):

    def subarraySum1(self, nums, k):
        """
        看了提示想到的,与2sum问题很相似
        sum[i,j] = sum[0,j] - sum[0,i]
        从i到j的和等于从0到j的和减去从0到i的和
        {sum[0,i]: count of sum[0,i]}
        :param nums:
        :param k:
        :return:
        """
        sum_dict = {}
        sum_num = 0
        count = 0
        sum_dict[0] = 1
        for elem in nums:
            sum_num += elem
            count += sum_dict.get(sum_num-k, 0)
            if sum_num in sum_dict:
                sum_dict[sum_num] += 1
            else:
                sum_dict[sum_num] = 1
        return count


    def subarraySum2(self, nums, k):
        """
        先计算出从0到i的和,存入list里,再遍历list两两详见,找到差为k的
        :param nums:
        :param k:
        :return:
        """
        commulative_sum = [0]
        sum = count = 0
        for elem in nums:
            sum += elem
            commulative_sum.append(sum)
        n = len(commulative_sum)
        for i in range(n-1):
            for j in range(i+1, n):
                if commulative_sum[j]-commulative_sum[i] == k:
                    count += 1
        return count






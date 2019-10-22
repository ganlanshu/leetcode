# coding=utf-8
"""
461. Hamming Distance
"""


class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 同一个bit不相等的个数，先求异或运算，再数数结果中bit为1的个数
        z = x ^ y
        count = 0
        while z:
            count += z & 1
            z >>= 1
        return count



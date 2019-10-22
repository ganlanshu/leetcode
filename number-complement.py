# coding=utf-8
"""
476. Number Complement
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        new_num = 0
        i = 0
        while num:
            if num & 1 == 0:
                new_num += 2**i
            num >>= 1
            i += 1
        return new_num



# coding=utf-8
"""
263. Ugly Number
"""

class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
            if num % 2 == 0:
                num = num//2
            elif num % 3 == 0:
                num = num//3
            elif num % 5 == 0:
                num = num//5
            else:
                return False
        return num == 1

    def isUgly1(self, num):
        """
        从讨论区看到的方法
        :param num:
        :return:
        """
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1


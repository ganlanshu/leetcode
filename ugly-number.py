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

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        264. Ugly Number II
        Write a program to find the n-th ugly number.
        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
        """
        if n <= 5:
            return n
        ugly_num_set = set()
        # 1到5 这几个ugly number先放入集合
        for i in range(1, 6):
            ugly_num_set.add(i)
        number = 6
        ugly_count = 5
        while ugly_count < n:
            if number % 2 == 0:
                if number/2 in ugly_num_set:
                    ugly_num_set.add(number)
                    ugly_count += 1
                number += 1
                continue
            if number % 3 == 0:
                if number/3 in ugly_num_set:
                    ugly_num_set.add(number)
                    ugly_count += 1
                number += 1
                continue
            if number % 5 == 0:
                if number/5 in ugly_num_set:
                    ugly_num_set.add(number)
                    ugly_count += 1
                number += 1
                continue
            else:
                number += 1
        return number-1


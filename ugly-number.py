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

    def nthUglyNumber1(self, n):
        """
        看了提示想出来的,每一个丑数都是一个更小的丑数的2,3,5倍,
        维护含有n个丑数的list,[1,2,3,4,5,6,8...]
        two_index,three_index,five_index 都从0开始
        是更小丑数的2倍,two_index递增,是3倍,则three_index后移,5倍则five_index后移
        最后index为n-1的元素是要求的丑数
        :param n:
        :return:
        """
        ugly_num = [1]*n
        two_index = three_index = five_index = 0
        for i in range(1, n):
            ugly_num[i] = min(ugly_num[two_index]*2, ugly_num[three_index]*3, ugly_num[five_index]*5)
            if ugly_num[i] == ugly_num[two_index]*2:
                two_index += 1
            if ugly_num[i] == ugly_num[three_index]*3:
                three_index += 1
            if ugly_num[i] == ugly_num[five_index]*5:
                five_index += 1
        return ugly_num[n-1]



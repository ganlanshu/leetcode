# coding=utf-8
"""
796. Rotate String
"""

class Solution(object):

    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if not A:
            return True
        n = len(A)
        for shift in range(n):
            C = A[shift:] + A[:shift]
            if C == B:
                return True
        return False

    def rotateString1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        下面这种方法先产生一个A+A的字符串,如果B 在这个字符串里, 那一定是A通过旋转得到的,
        好巧妙啊
        """
        if len(A) != len(B):
            return False
        C = A + A
        if B in C:
            return True
        return False

    def rotateString2(self, A, B):
        return len(A) == len(B) and B in A+A

    def rotateString2(self, A, B):
        if A == B:
            return True
        for i in range(len(A)):
            # 每次左移一位,这样会改变A的值
            A = A[1:] + A[0]
            if A == B:
                return True
        return False

    def LeftRotateString(self, s, n):
        """
        字符串左移n位
        :param s:
        :param n:
        :return:
        """
        if not s:
            return s
        N = len(s)
        n = n%N
        return s[n:] + s[:n]

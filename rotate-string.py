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

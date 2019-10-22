# coding=utf-8
"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = bin(n)[2:]
        if len(binary_str) != 32:
            binary_str = '0' * (32 - len(binary_str)) + binary_str
        binary_str = list(binary_str)
        reversed_str = ''
        while binary_str:
            reversed_str += binary_str.pop()
        return int('0b' + reversed_str, 2)



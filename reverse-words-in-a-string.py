# coding=utf-8
"""
151. Reverse Words in a String
Given an input string, reverse the string word by word.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.strip().split()
        s_list.reverse()
        return ' '.join(s_list)

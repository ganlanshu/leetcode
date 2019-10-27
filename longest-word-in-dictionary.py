# coding=utf-8
"""
720. Longest Word in Dictionary
"""


class Solution(object):

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans = ''
        word_set = set(words)
        words.sort(key=lambda c: (-len(c), c))
        # 先排序，若长度最长的word的prefix在word_set里都有，就有了
        for word in words:
            if all(word[:k] in word_set for k in range(1, len(word))):
                return word
        return ans



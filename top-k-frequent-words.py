# coding=utf-8
from collections import Counter
"""
692. Top K Frequent Words
"""


class Solution(object):

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        candidates = count.keys()
        candidates.sort(key=lambda w: (-count[w], w))
        return candidates[:k]

    def topKFrequent1(self, words, k):
        import heapq
        count = Counter(words)
        min_heap = []
        # 用size为k的最小堆，把(fre, word)放入堆里，最小fre出堆，最后剩下的k个就是频率最大的
        for word, fre in count.items():
            heapq.heappush(min_heap, (Word(word, fre), word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res[::-1]


class Word(object):
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre == other.fre:
            return self.word > other.word
        return self.fre < other.fre

    def __eq__(self, other):
        return self.fre == other.fre and self.word == other.word

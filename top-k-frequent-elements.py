# coding=utf-8
"""
347. Top K Frequent Elements
Given a non-empty array of integers,
return the k most frequent elements.
"""

class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0)+1
        # 用一个size为k的最小堆,把n-k个元素放入堆, 最小的元素一直出堆,最后剩下的就是最大的k个
        min_heap = []
        for elem, fre in frequency_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (fre, elem))
            else:
                if fre > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (fre, elem))
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res

    def topKFrequent1(self, nums, k):
        """
        用桶排序,把出现频次为i的元素放在第i个桶里, 最后从尾遍历桶,得到频率最高的k个元素
        :param nums:
        :param k:
        :return:
        """
        # 遍历元素,得到elem-->fre hash_map
        frequency_map = {}
        top_frequency = 0
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0)+1
            top_frequency = max(top_frequency, frequency_map[num])
        bucket = [[] for i in range(top_frequency+1)]
        # 把频率为i的元素放入第i个桶里,可能会有频率相同的,所有用list来存放
        for elem, fre in frequency_map.iteritems():
            bucket[fre].append(elem)
        res = []
        # 逆序遍历bucket,取出最后的k个元素
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) > k:
                break
        return res[:k]





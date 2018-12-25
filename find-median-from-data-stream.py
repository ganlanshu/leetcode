# coding=utf-8

class MedianFinder(object):
    """
    最开始想到的方法,借助heap取第k大的数
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.list.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.list)
        if not n:
            return
        j = n/2
        k = (n-1)/2
        # 转化为求第k大和第j大的数的问题
        import heapq
        # 用最小堆找到第j大的元素
        heap = self.list[:j+1]
        heapq.heapify(heap)
        for i in range(j+1, n):
            if self.list[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, self.list[i])
        if j == k:
            return heap[0]
        else:
            left = heapq.heappop(heap)
            right = heap[0]
            return float(left+right)/2

class MedianFinder1(object):
    """
    用最大堆和最小堆来做,最大堆维护数组中较小的一半,最小堆维护数组中较大的一半,中位数取
    堆顶的两个元素,要保持两个堆数量差最大为1, 尽量让最大堆的元素数多一个,或者两者相等
    """
    def __init(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        import heapq
        # min_heap存较大的那一半,max_heap存较小的那一半,heapq 没有最大堆,取负数就好了
        min_heap, max_heap = self.min_heap, self.max_heap
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0]-self.max_heap[0])/2
        else:
            return float(self.min_heap[0])



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
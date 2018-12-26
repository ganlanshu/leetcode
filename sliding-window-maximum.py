# coding=utf-8
"""
239. Sliding Window Maximum
"""
import collections

class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        先想到一个简单粗暴的方法
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res

    def maxSlidingWindow1(self, nums, k):
        """
        :param nums:
        :param k:
        :return:
        看了提示,用deque来做, 不过时间复杂度并不是O(n)
        """
        if not nums:
            return []
        queue = collections.deque(nums[:k])
        res = []
        res.append(max(queue))
        n = len(nums)
        for i in range(k, n):
            queue.popleft()
            queue.append(nums[i])
            res.append(max(queue))
        return res

    def maxSlidingWindow2(self, nums, k):
        """
        :param nums:
        :param k:
        :return:
        滑动窗口的最大值总是在队列首部,队列里面的数据总是从大到小排列
        遍历数组nums,使用deque维护滑动窗口内有可能成为最大值元素的下表
        记当前下表为i,则滑动窗口的有效下标范围是[i-k+1,i]
        若deque中的元素下标小于 i-k+1,将其从队列头部出队,nums中的元素逐个从
        队尾入队
        这样确保deque中的元素下标在[i-k+1,i]范围内
        当下标i从对位入队是,依次弹出队尾小于等于nums[i]的元素的下标,因为滑动窗口
        里面已经有了更大的元素,这些较小的在当前滑动窗口已经没有意义
        deque的头元素是当前滑动窗口的最大值
        """
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i-k:
                dq.popleft()
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans


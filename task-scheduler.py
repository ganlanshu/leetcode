# coding=utf-8

"""
621. Task Scheduler
"""
from collections import Counter

class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        参考以下python解法
        https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
        参考以下java解法, 这个解释的比较多
        https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
        """
        # 找到出现频率最高的任务的出现次数, 这个频率把所有任务分成 (top_frequency-1)份
        counter = Counter(tasks)
        task_frequency = counter.values()
        top_frequency = max(task_frequency)
        # 在高频任务中间插入n个任务,最后一个高频任务收尾(也可能有多个高频任务,频率相等)
        return max(len(tasks), (top_frequency-1)*(n+1) + task_frequency.count(top_frequency))




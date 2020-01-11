# coding=utf-8
"""
452. Minimum Number of Arrows to Burst Balloons
求数组中产生交集的数组的个数
"""


class Solution(object):

    def findMinArrowShots1(self, points):
        if not points:
            return 0
        points.sort()
        length = len(points)
        interseced_count = 0
        interseced_list = points[0]
        start_index = 1
        points.sort()
        while start_index < length:
            start_value, end_value = interseced_list
            next_start_value, next_end_value = points[start_index]
            if next_start_value <= end_value:
                interseced_list = [next_start_value, min(end_value, next_end_value)]
            else:
                interseced_count += 1
                interseced_list = [next_start_value, next_end_value]
            start_index += 1
        return interseced_count + 1

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort()
        length = len(points)
        ans = 1
        end = points[0][1]
        points.sort()
        for s, e in points[1:]:
            if s <= end:
                end = min(end, e)
            else:
                ans += 1
                end = e
        return ans

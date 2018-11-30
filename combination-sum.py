# coding=utf-8
"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/
"""


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(target, index, path):
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    return
                dfs(target-candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])
        return res

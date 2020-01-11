# coding=utf-8

"""
455. Assign Cookies
"""

class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        max_content_num = 0
        g.sort()
        s.sort()
        child_num = len(g)
        cookie_num = len(s)
        child_index = cookie_index = 0
        while child_index < child_num and cookie_index < cookie_num:
            if s[cookie_index] >= g[child_index]:
                max_content_num += 1
                child_index += 1
            cookie_index += 1
        return max_content_num

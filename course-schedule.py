# coding=utf-8
from collections import deque

"""
207. Course Schedule
发现有向图中是否有环
"""


class Solution(object):

    def canFinish(self, num_courses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 用邻接表表示图
        graph = [[] for _ in range(num_courses)]
        visited = [0 for _ in range(num_courses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(vertex):
            if visited[vertex] == -1:
                return False
            if visited[vertex] == 1:
                return True
            visited[vertex] = -1
            for neighbor in graph[vertex]:
                if not dfs(neighbor):
                    return False
            visited[vertex] = 1
            return True

        for vertex in range(num_courses):
            if not dfs(vertex):
                return False
        return True

    def can_finish_bfs(self, num_courses, prerequisites):
        from collections import deque
        graph = {i: set() for i in range(num_courses)}
        in_degree = {i: 0 for i in range(num_courses)}
        for start, end in prerequisites:
            graph[start].add(end)
            in_degree[end] += 1
        queue = deque([i for i in in_degree if in_degree[i] == 0])
        visits = set(queue)
        while queue:
            x = queue.popleft()
            for nei in graph[x]:
                if nei in visits:
                    return False
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
                    visits.add(nei)
        return len(visits) == num_courses

    def findOrder(self, num_course, prerequisites):
        """
        找到拓扑排序，如果没有，返回空列表，bfs方法
        """
        graph = [[] for i in range(num_course)]
        in_degree = [0] * num_course
        for end, start in prerequisites:
            graph[start].append(end)
            in_degree[end] += 1
        count = 0
        queue = deque([i for i in range(num_course) if in_degree[i] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            neighbors = graph[node]
            for neighbor in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if count != num_course:
            return []
        return res

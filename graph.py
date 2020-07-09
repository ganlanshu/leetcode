# coding=utf-8

"""
图的邻接表
"""
from collections import deque

class Node(object):

    def __init__(self, index, weight, next=None):
        self.index = index
        self.weight = weight
        self.next = next


class AdjacentList(object):

    def __init__(self, number):
        self.number = number
        self.list = [None]*self.number

    def insert(self, origin, index, weight=1):
        # 头插法
        node = Node(index, weight, self.list[origin-1])
        self.list[origin-1] = node


class AdjacentMatrix(object):

    def __init__(self, number):
        self.number = number
        self.list = [[None]*number for i in range(number)]

    def insert(self, origin, index, weight=1):
        self.list[origin-1][index-1] = weight


class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=1):
        self.connected_to[nbr] = weight

    def get_neighbors(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph(object):

    def __init__(self):
        self.vertex_list = []
        self.vertex_num = 0

    def add_vertex(self, key):
        # 创建新节点
        vertex = Vertex(key)
        # 把新节点添加到邻接表里
        self.vertex_list[key] = vertex
        # 节点个数加1
        self.vertex_num += 1
        return vertex

    def get_vertex(self, n):
        return self.vertex_list.get(n, None)

    def add_edge(self, origin, tail, weight=1):
        if origin not in self.vertex_list:
            self.add_vertex(origin)
        if tail not in self.vertex_list:
            self.add_vertex(tail)
        self.vertex_list[origin].add_neighbor(self.vertex_list[tail], weight)


def dfs_traverse(graph):
    res = []

    def dfs(vertex):
        if vertex not in graph:
            return
        res.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in res:
                res.append(neighbor)
                dfs(neighbor)

    for vertex in graph:
        if vertex not in res:
            #res.append(vertex)
            dfs(vertex)
    return res


def dfs_traverse_1(vertex_num, graph):
    visited = [0] * vertex_num

    def dfs(i):
        print(i)
        visited[i] = 1
        for nei in graph[i]:
            if not visited[nei]:
                dfs(nei)


    for i in range(vertex_num):
        if not visited[i]:
            dfs(i)

def bfs_traverse(vertex_num, graph):
    # 邻接表bfs遍历
    visited = [0] * vertex_num
    queue = deque()
    for vertex in graph:
        if not visited[vertex]:
            visited[vertex] = 1
            print(vertex)
            queue.append(vertex)
            while queue:
                current = queue.popleft()

                for nei in graph.get(current, []):
                    if not visited[nei]:
                        visited[nei] = 1
                        print(nei)
                        queue.append(nei)

def dfs_iter(graph, source):
    res = [source]
    stack = [source]
    while stack:
        node = stack.pop()
        for nei in graph[node]:
            if nei not in res:
                stack.append(nei)
                res.append(nei)


if __name__ == '__main__':
    graph = {0: [1, 2],
             1: [2, 3],
             2: [3],
             3: [2, 6, 7],
             4: [5],
             5: [2]}
    print(bfs_traverse(8, graph))

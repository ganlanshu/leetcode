# coding=utf-8
import collections

"""
133. Clone Graph

"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):

    def cloneGraph1(self, node):
        """
        bfs
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        node_copy = Node(node.val, [])
        node_map = {node: node_copy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in node_map:  # neighbor is not visited
                    neighbor_copy = Node(neighbor.val, [])
                    node_map[neighbor] = neighbor_copy
                    node_map[node].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
                else:
                    node_map[node].neighbors.append(node_map[neighbor])
        return node_copy

    def clone_graph2(self, node):
        # dfs 迭代
        if not node:
            return
        node_copy = Node(node.val, [])
        node_map = {node: node_copy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in node_map:
                    neighbor_copy = Node(neighbor.val, [])
                    node_map[neighbor] = neighbor_copy
                    node_map[node].neighbors.append(neighbor_copy)
                    stack.append(neighbor)
                else:
                    node_map[node].neighbors.append(node_map[neighbor])

        return node_copy

    def clone_graph3(self, node):
        # dfs recursive
        if not node:
            return
        node_copy = Node(node.val, [])
        node_map = {node: node_copy}
        self.dfs(node, node_map)
        return node_copy

    def dfs(self, node, node_map):
        for neighbor in node.neighbors:
            if neighbor not in node_map:
                neighbor_copy = Node(neighbor.val, [])
                node_map[neighbor] = neighbor_copy
                node_map[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor, node_map)
            else:
                node_map[node].neighbors.append(node_map[neighbor])




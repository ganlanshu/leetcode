#coding=utf-8
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root):
        """
        用层序遍历找出深度
        :param root:
        :return:
        """
        if not root:
            return 0
        depth = 0
        queue = deque([])
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                head = queue.popleft()
                left = head.left
                right = head.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            depth += 1
        return depth

    def minDepth(self, root):
        """
        计算最小深度
        :param root:
        :return:
        """
        if not root:
            return 0
        depth_l = self.minDepth(root.left)
        depth_r = self.minDepth(root.right)
        if depth_l and depth_r:
            return 1 + min(depth_l, depth_r)
        if depth_l == 0 and depth_r == 0:
            return 1
        return 1 + max(depth_l, depth_r)

    def minDepth1(self, root):
        if not root:
            return 0
        children = [root.left, root.right]
        if not any(children):
            return 1
        min_depth = float('inf')
        for child in children:
            if child:
                min_depth = min(self.minDepth1(child), min_depth)
        return 1+min_depth

    def minDepth2(self, root):
        """
        用层序遍历,如果某个节点没有left和right,就是leaf节点
        :param root:
        :return:
        """
        if not root:
            return 0
        depth = 0
        queue = deque([])
        queue.append(root)
        reach_leaf = False
        while queue and not reach_leaf:
            n = len(queue)
            for i in range(n):
                head = queue.popleft()
                left = head.left
                right = head.right
                if not left and not right:
                    reach_leaf = True
                    break
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            depth += 1
        return depth

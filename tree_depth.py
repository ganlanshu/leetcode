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


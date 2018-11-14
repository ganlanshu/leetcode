#coding=utf-8
"""
257. Binary Tree Paths
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        children = [root.left, root.right]
        if not any(children):
            return [str(root.val)]
        result = []
        for child in children:
            if child:
                result += self.binaryTreePaths(child)
        return [str(root.val) + '->' + value for value in result]

#coding=utf-8
"""
700. Search in a Binary Search Tree

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        if root.val == val:
            return root
        if root.val > val:
            root = root.left
            return self.searchBST(root, val)
        else:
            root = root.right
            return self.searchBST(root, val)

    def searchBST2(self, root, val):
        """
        不使用递归方法
        """
        if not root:
            return []
        while root:
            if root.val == val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return []

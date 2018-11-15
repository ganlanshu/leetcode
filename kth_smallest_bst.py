#coding=utf8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        230. Kth Smallest Element in a BST
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            k -= 1
            if k == 0:
                return top.val
            root = top.right

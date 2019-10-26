# coding=utf-8

"""
965. Univalued Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = root.left
        right = root.right
        if not left and not right:
            return True
        if left and right:
            return root.val == left.val and root.val == right.val and self.isUnivalTree(left) \
                   and self.isUnivalTree(right)
        child = left or right
        return root.val == child.val and self.isUnivalTree(child)

    def isUnivalTree1(self, root):

        def traverse(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return traverse(node.left, val) and traverse(node.right, val)
        return traverse(root, root.val if root else None)

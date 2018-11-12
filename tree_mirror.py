#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉树的镜像
class Solution(object):

    def mirror(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = root.left
        right = root.right
        root.left = self.mirror(right)
        root.right = self.mirror(left)
        return root

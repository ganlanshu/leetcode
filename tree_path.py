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

    def hasPathSum(self, root, sum):
        """
        112. Path Sum
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        if self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val):
            return True
        return False

    def hasPathSum1(self, root, sum):
        if not root:
            return False
        stack = []
        stack.append((root, sum))
        while stack:
            top, _sum = stack.pop()
            if not top.left and not top.right and top.val == _sum:
                return True
            if top.right:
                stack.append((top.right, _sum-top.val))
            if top.left:
                stack.append((top.left, _sum-top.val))
        return False

    def pathSum(self, root, sum):
        """
        113. Path Sum II
        Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return []
        children = [root.left, root.right]
        if not any(children):
            if root.val == sum:
                return [[root.val]]
            return []
        path = []
        if root.left:
            left_path = self.pathSum(root.left, sum-root.val)
            if left_path:
                path.extend([[root.val] + p for p in left_path])
        if root.right:
            right_path = self.pathSum(root.right, sum-root.val)
            if right_path:
                path.extend([[root.val] + p for p in right_path])
        return path

    def pathSum1(self, root, sum):
        """
        113. Path Sum II
        Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return []
        children = [root.left, root.right]
        if not any(children) and root.val == sum:
            return [[root.val]]
        tmp = self.pathSum1(root.left, sum-root.val) + self.pathSum1(root.right, sum-root.val)
        return [[root.val] + p for p in tmp]
#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        判断t是否是s的子树
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.is_same(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, p, q):
        """
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True
        if p and q:
            return p.val == q.val and self.is_same(p.left, q.left) and self.is_same(p.right, q.right)
        return False

    def isSubtree1(self, s, t):
        def convert(s):
            return '^'+str(s.val)+'#' + convert(s.left) + convert(s.right) if s else '$'
        return convert(t) in convert(s)

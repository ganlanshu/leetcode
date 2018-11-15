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

    def is_substructure(self, s, t):
        """
        子结构和子树不一样,看辅助方法就知道,子树需要完全一样
        子结构只要部分一样
        判断t是否是s的子结构,参考
        https://blog.csdn.net/qq_33431368/article/details/79257029
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return False
        return self._substructure(s, t) or self.is_substructure(s.left, t) or self.is_substructure(s.right, t)

    def _substructure(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        return root1.val == root2.val and self._substructure(root1.left, root2.left) and self._substructure(root1.right, root2.right)

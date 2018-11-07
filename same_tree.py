#coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and not q:
            return False
        if q and not p:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)        

    def is_sametree(self, p, q):
        """
        改进后的方法,p is q比上面好多行省事, 不过运行的时候上面更快
        """
        if p and q:
            return p.val == q.val and self.is_sametree(p.left, q.left) and self.is_sametree(p.right, q.right)
        return p is q
        

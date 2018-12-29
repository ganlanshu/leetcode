# coding=utf-8
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def convert(self, root):
        if not root:
            return
        stack = []
        head = pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            root = top.right
            if not head:
                head = top
            if not pre:
                pre = top
            else:
                pre.right = top
                top.left = pre
                pre = top
        return head





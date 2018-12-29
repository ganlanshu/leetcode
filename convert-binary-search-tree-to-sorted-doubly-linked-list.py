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

    def bst_to_doubly_link(self, root):
        """
        这是最先想到的,非递归方法
        :param root:
        :return:
        """
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

    def bst_to_doubly_link1(self, root):
        """
        用递归方法试试
        :param root:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            return root
        # 对左子树递归,得到左子树转为doubly link的头结点
        left = self.bst_to_doubly_link1(root.left)
        tail = left
        # 从头结点找到尾节点
        while tail and tail.right:
            tail = tail.right
        # 有的根节点没有左子树,这是tail就为空
        if tail:
            tail.right = root
            root.left = tail
        right = self.bst_to_doubly_link1(root.right)
        if right:
            root.right = right
            right.left = root
        return left if left else root


    def bst_to_doubly_link2(self, root):
        last_node = None
        self._convert_node(root, last_node)
        # 找到链表最右边的节点,再从这里遍历到头结点
        head = last_node
        while head and head.left:
            head = head.left
        return head

    def _convert_node(self, root, last_node):
        if not root:
            return
        current = root
        if current.left:
            self._convert_node(current.left, last_node)
        current.left = last_node
        if last_node:
            last_node.right = current
        last_node = current
        if current.right:
            self._convert_node(current.right, last_node)



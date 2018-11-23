# coding=utf-8

class Solution(object):

    def flatten(self, root):
        """
        114. Flatten Binary Tree to Linked List
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)
        root.right = left
        root.left = None
        current = root
        while current.right:
            current = current.right
        current.right = right

    def flattern3(self, root):
        """
        114. Flatten Binary Tree to Linked List
        :param root:
        :return:
        """
        if not root:
            return []
        if not root.left and not root.right:
            return
        stack = []
        stack.append(root)
        while stack:
            top = stack.pop()
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
            root.right = top
            root.left = None
            root = root.right

    def flatten1(self, root):
        # 参考discuss里的
        now = root
        while now:
            if now.left:
                pre = now.left
                while pre.right:
                    pre = pre.right
                pre.right = now.right
                now.right = now.left
                now.left = None
            now = now.right

    def flatter2(self, root):
        """
        参考discuss里的, recursion
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre = None
        if not root:
            return
        self.flatten2(root.right)
        self.flatten2(root.left)
        root.right = pre
        root.left = None
        pre = root

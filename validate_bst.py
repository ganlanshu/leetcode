# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
98. Validate Binary Search Tree
"""

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        inorder_traversal = self._inorder_traverse(root)
        n = len(inorder_traversal)
        for i in range(1, n):
            if inorder_traversal[i] <= inorder_traversal[i-1]:
                return False
        return True

    def _inorder_traverse(self, root):
        if not root:
            return []
        return self._inorder_traverse(root.left) + [root.val] + self._inorder_traverse(root.right)

    def is_bst(self, root):
        """
        第一次写的,但是错误的方法
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
            return left.val < root.val < right.val and self.is_bst(left) and self.is_bst(right)
        if left:
            return left.val < root.val and self.is_bst(left)
        if right:
            return root.val < right.val and self.is_bst(right)

    def isValidBST1(self, root):
        # 用极大值和极小值来辅助
        max_value = float('inf')
        min_value = float('-inf')
        return self._valid_helper(root, min_value, max_value)

    def _valid_helper(self, root, min_value, max_value):
        if not root:
            return True
        if root.val < min_value or root.val > max_value:
            return False
        return self._valid_helper(root.left, min_value, root.val-1) \
               and self._valid_helper(root.right, root.val+1, max_value)

    def isValidBST2(self, root):
        """
        中序遍历, 比较前驱节点和当前节点的值
        :param root:
        :return:
        """
        if not root:
            return True
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            if pre and top.val <= pre.val:
                return False
            pre = top
            root = top.right
        return True

    def isValidBST3(self, root):
        pre = None
        def _validate_bst(self, root, pre):
            if not root:
                return True
            if not _validate_bst(root.left, pre):
                return False
            if pre and pre.val >= root.val:
                return False
            pre = root
            return _validate_bst(root.right, pre)
        return _validate_bst(root, pre)
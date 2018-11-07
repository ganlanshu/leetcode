#coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

    def inorder_traverse(self, root):
        return inorder_traverse(root.left) + [root.val] + inorder_traverse(root.right) if root else []

    def inorder_traverse_with_no_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        参考了https://blog.csdn.net/zhangxiangDavaid/article/details/37115355
        """
        if not root:
            return []
        stack = []

        # 用来存遍历后的结果
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                top = stack.pop()
                res.append(top.val)
                root = top.right
        return res

    def level_traversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        层序遍历,用队列实现
        """
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            head = queue.pop(0)
            left = head.left
            right = head.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            res.append(head.val)
        return res

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

    def level_traversal_with_level(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        返回的列表每一层是一个子列表,参考了该网址
        https://blog.csdn.net/OrthocenterChocolate/article/details/37612183
        """
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        # 每一层结束的时候,除了结点,再插入一个特殊标记None,出队的时候遇到None,说明
        这一层结束,在队尾再插入特殊标记None
        queue.append(None)
        level_list = []
        while queue:
            head = queue.pop(0)
            if head:#head是树中的某个结点
                left = head.left
                right = head.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
                level_list.append(head.val)
            else:#head是加的特殊标记None
                if queue:#最后一个结点结束后会有一个None,这时不需要再把特殊标记入队了
                    queue.append(None)
                res.append(level_list)
                level_list = []
        return res

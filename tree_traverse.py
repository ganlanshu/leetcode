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
            #head是树中的某个结点
            if head:
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

    def level_traversal_with_level1(self, root):
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                head = queue.pop(0)
                level.append(head.val)
                left = head.left
                right = head.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            res.append(level)
        return res


    def level_traversal(self, root):
        """
        :param root:
        :return:
        """
        if not root:
            return []
        queue = [[root]]
        for level in queue:
            record = []
            for node in level:
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            if record:
                queue.append(record)
        return [[node.val for node in level] for level in queue]

    def preorder_traversal(self, root):
        """
        用iter方法实现
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.push(root)
                root = root.left
            top = stack.pop()
            root = top.right
        return res

    def preorder_traversal_recursion(self, root):
        if not root:
            return []
        return [root.val] + self.preorder_traversal_recursion(root.left) + self.preorder_traversal_recursion(root.right)

    def preorder_traversal1(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return res

    def level_zigzag_traversal(self, root):
        """
        之字形按层输出
        :param root:
        :return:
        """
        if not root:
            return []
        queue = deque([])
        res = []
        queue.append(root)
        flag = False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                head = queue.popleft()
                left = head.left
                right = head.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
                level.append(head.val)
            if flag:
                level.reverse()
            flag = not flag
            res.append(level)
        return res


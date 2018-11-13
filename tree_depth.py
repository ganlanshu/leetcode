#coding=utf-8
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root):
        """
        用层序遍历找出深度
        :param root:
        :return:
        """
        if not root:
            return 0
        depth = 0
        queue = deque([])
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                head = queue.popleft()
                left = head.left
                right = head.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            depth += 1
        return depth

    def minDepth(self, root):
        """
        计算最小深度
        :param root:
        :return:
        """
        if not root:
            return 0
        depth_l = self.minDepth(root.left)
        depth_r = self.minDepth(root.right)
        if depth_l and depth_r:
            return 1 + min(depth_l, depth_r)
        if depth_l == 0 and depth_r == 0:
            return 1
        return 1 + max(depth_l, depth_r)

    def minDepth1(self, root):
        if not root:
            return 0
        children = [root.left, root.right]
        if not any(children):
            return 1
        min_depth = float('inf')
        for child in children:
            if child:
                min_depth = min(self.minDepth1(child), min_depth)
        return 1+min_depth

    def minDepth2(self, root):
        """
        用层序遍历,如果某个节点没有left和right,就是leaf节点
        :param root:
        :return:
        """
        if not root:
            return 0
        depth = 0
        queue = deque([])
        queue.append(root)
        reach_leaf = False
        while queue and not reach_leaf:
            n = len(queue)
            for i in range(n):
                head = queue.popleft()
                left = head.left
                right = head.right
                if not left and not right:
                    reach_leaf = True
                    break
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            depth += 1
        return depth

    def isBalanced(self, root):
        if not root:
            return True
        left = root.left
        right = root.right
        if abs(self.maxDepth(left) - self.maxDepth(right)) > 1:
            return False
        return self.isBalanced(left) and self.isBalanced(right)

    def isBalanced1(self, root):
        balanced = [True]
        def _get_tree_depth(root, balanced):
            if not root:
                return 0
            depth_l = _get_tree_depth(root.left, balanced)
            depth_r = _get_tree_depth(root.right, balanced)
            if abs(depth_l - depth_r) > 1:
                balanced[0] = False
            return 1 + max(depth_l, depth_r)
        depth = _get_tree_depth(root, balanced)
        if not balanced[0]:
            return False
        return True

    def isBalanced2(self, root):
        return self._depth(root) != -1

    def _depth(self, root):
        """
        当左右子树高度差大于1,返回-1,其他时候返回树的高度
        :param root:
        :return:
        """
        if not root:
            return 0
        depth_l = self._depth(root.left)
        depth_r = self._depth(root.right)
        # 左子树不平衡
        if depth_l == -1:
            return -1
        # 右子树不平衡
        if depth_r == -1:
            return -1
        if abs(depth_l - depth_r) > 1:
            return -1
        return 1 + max(depth_l, depth_r)

    def isBalanced3(self, root):
        depth, balanced = self.get_depth(root)
        return balanced

    def get_depth(self, root):
        if not root:
            return 0, True
        dl, bl = self.get_depth(root.left)
        dr, br = self.get_depth(root.right)
        h = 1 + max(dl, dr)
        b = bl and br and abs(dl-dr) < 2
        return h, b

# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder, inorder):
            if not inorder:
                return
            # 从前序获取根结点
            root_val = preorder.popleft()
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            left = helper(preorder, inorder[:index])
            right = helper(preorder, inorder[index+1:])
            root.left = left
            root.right = right
            return root
        return helper(deque(preorder), inorder)

    def build_tree(self, inorder, postorder):
        """
        用后序中序构建tree
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder:
            return
        root_val = postorder.pop()
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        root.right = self.build_tree(inorder[index+1:], postorder)
        root.left = self.build_tree(inorder[:index], postorder)
        return root

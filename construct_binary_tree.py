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
            root = TreeNode(root)
            index = inorder.index(root_val)
            left = helper(preorder, inorder[:index])
            right = helper(preorder, inorder[index+1:])
            root.left = left
            root.right = right
            return root
        return helper(deque(preorder), inorder)




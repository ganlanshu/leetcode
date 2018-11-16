#coding=utf-8
"""
700. Search in a Binary Search Tree

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        if root.val == val:
            return root
        if root.val > val:
            root = root.left
            return self.searchBST(root, val)
        else:
            root = root.right
            return self.searchBST(root, val)

    def searchBST2(self, root, val):
        """
        不使用递归方法
        """
        if not root:
            return []
        while root:
            if root.val == val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return []

    def sortedArrayToBST(self, nums):
        """
        Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        l = 0
        r = n - 1
        mid= (l + r)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


    def sortedArrayToBST1(self, nums):
        """
        Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = 0
        r = len(nums) - 1
        def convert_list_to_bst(l, r):
            mid = (l+r)/2
            if l > r:
                return None
            root = TreeNode(nums[mid])
            if l == r:
                return root
            root.left = convert_list_to_bst(l, mid-1)
            root.right = convert_list_to_bst(mid+1, r)
            return root
        return convert_list_to_bst(l, r)


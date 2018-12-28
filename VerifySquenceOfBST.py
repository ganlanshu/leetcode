# coding=utf-8
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是,返回True,否则返回False
假设输入的数组的任意两个数字都互不相同。

"""

class Solution:
    def VerifySquenceOfBST(self, nums):
        """
        :param nums:  List[int]
        :return: bool
        """
        # write code here
        # 维基百科二叉搜索树的定义
        """
        一个空树或具有下列特点的二叉树
        1. 若任一节点有左子树,左子树的所有节点的值小于根节点
        2. 若任一节点有右子树,右子树的所有节点的值大于根节点
        3. 任一节点的左子树和右子树都是二叉搜索树
        4. 不存在值相等的节点
        """

        if not nums:
            return True
        n = len(nums)
        if n == 1:
            return True
        root_val = nums[-1]
        index = 0
        # 前面的都是比root小的,是左子树
        while index < n-1 and nums[index]<root_val:
            index += 1
        mid = index
        # mid后面的都是比root大的,是右子树
        while index < n-1 and nums[index] > root_val:
            index += 1
        if index != n-1:
            return False
        left = nums[:mid]
        right = nums[mid:-1]
        return self.VerifySquenceOfBST(left) and self.VerifySquenceOfBST(right)


if __name__ == '__main__':
    nums = [7,9,8,11,10,16,20,18,17]
    s = Solution()
    print s.VerifySquenceOfBST(nums)
#coding=utf-8
"""
303. Range Sum Query - Immutable
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        题中说道多次调用,把每次算出的前面为位的和存起来,方便多次调用
        """
        self.sums = [0]
        for element in nums:
            sums.append(self.sums[-1]+element)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = 0
        for index in range(i, j+1):
            sum += self.nums[index]
        return sum

    def sumrange2(self, i, j):
        """
         sumi = nums[0] + ... + nums[i-1]
         sumij = sum[j+1] - sum[j]
        :param i:
        :param j:
        :return:
        """
        return self.sums[j+1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
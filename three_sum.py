#coding=utf-8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        # 先排序
        result = []
        nums.sort()
        # 固定前面一个数字，找后面的两个数字
        for i in range(length-2):
            # 如果第一个数字就比0大，后面的肯定更大
            if nums[i] > 0:
                break
            # 第一个数字和前面的数字一样的话，防止重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            begin = i + 1
            end = length - 1
            while begin < end:
                three_sum = nums[i] + nums[begin] + nums[end]
                if three_sum == 0:
                    result.append((nums[i],nums[begin],nums[end]))
                    while begin < end and nums[begin] == nums[begin+1]:
                        begin += 1
                    while begin < end and nums[end] == nums[end-1]:
                        end -=1
                    begin += 1
                    end -= 1
                elif three_sum > 0:
                    end -= 1
                else:
                    begin += 1
        return result 

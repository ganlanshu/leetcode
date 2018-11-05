#coding=utf-8
class Solution(object):
    def nsum(self, N, nums, target):
        """
        :type N, int
        :type nums: List[int]
        :type target int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if N == 0 :
            return []
        if length < N:
            return []
        # 假设nums已经排好序了
        if nums[0] * N > target:
            return []
        if nums[-1] * N < target:
            return []
        if N == 1:
            for i in range(length):
                if nums[i] == target:
                    return [nums[i]]
            return []
        elif N == 2:
            begin, end = 0, length - 1
            result = []
            while begin < end:
                two_sum = nums[begin] + nums[end]
                if two_sum > target:
                    end -= 1
                elif two_sum < target:
                    begin += 1
                else:
                    result.append([nums[begin], nums[end]])
                    while begin < end and nums[begin] == nums[begin+1]:
                        begin += 1
                    while begin < end and nums[end] == nums[end-1]:
                        end -= 1
                    begin += 1
                    end -= 1
            return result
        else:
            results = []
            for i in range(length-N+1):
                # 如果第一个数就大,后面的和肯定更大,最后一个同理
                if nums[i] * N > target or nums[-1] * N < target:
                    break
                # 第一个数字不能有重复的
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                # 先取出n-1sum的列表
                result_n_1 = self.nsum(N-1, nums[i+1:], target-nums[i])
                if result_n_1:
                    for element in result_n_1:
                        result = [nums[i]] + element
                        results.append(result)
            return results

    def four_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target int
        :rtype: List[List[int]]
        """
        # 先进行排序
        nums.sort()
        return self.nsum(4, nums, target)

if __name__ == '__main__':
    o = Solution()
    nums = [-1,2,2,-5,0,-1,4]
    nums.sort()
    print o.nsum(4, nums, 3)

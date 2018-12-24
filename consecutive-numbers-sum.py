# coding=utf-8
"""
829. Consecutive Numbers Sum
Given a positive integer N, how many ways can we write it
as a sum of consecutive positive integers?
"""

import math
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        给定N,返回连续和为N的正整数的count
        :type N: int
        :rtype: int
        """
        count = 1
        target = 2*N
        sqrt = int(math.sqrt(target))
        for n in range(sqrt, 1, -1):
            divide = (target-n**2)/n
            if (divide+1)/2 > N/n:
                break
            if (target-n**2)%n == 0:
                if (divide+1)%2 == 0:
                    count += 1
        return count

    def consecutiveNumbersSum1(self, N):
        """
        :param N:
        :return:
        等差数列,公差为1,和为sum
        sum = (a1+an)/2*n
        若n为奇数,(a1+an)/2 就是最中间的那个数,假设为a 此时sum=a*n, sum % n == 0
        若n为偶数,(a1+an)/2 就是最中间的两个偶数的中间值,设为a,小数部分是0.5, 此时(sum % n)*2 = n
        """
        import math
        sum = 2*N
        sqrt = int(math.sqrt(sum))
        count = 1
        for n in range(sqrt, 1, -1):
            # n为奇数,且sum能整除n,奇数&1还是1
            if (n%2 == 1 and N%n == 0) or N%n*2==n:
                count += 1
        return count

    def findContinuousSequence(self, tsum):
        """
        找到和为tsum的连续子数组,返回子数组,按第一个元素大小排列
        :param tsum:
        :return:
        """
        result = []
        target = 2*tsum
        sqrt = int(math.floor(math.sqrt(target)))
        for n in range(sqrt, 1, -1):
            divide = (target-n**2)/n
            if (target-n**2)%n == 0:
                if (divide+1)%2 == 0:
                    a1 = (divide+1)/2
                    res = []
                    for i in range(n):
                        res.append(a1+i)
                    result.append(res)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.findContinuousSequence(200)


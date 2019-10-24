# coding=utf-8


class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        先用异或计算出没有进位的值，再用&计算需要进位的位，并左移一位，直到&的结果为0，
        不需要进位，异或的结果就是所求值
        """
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(10102, 9))



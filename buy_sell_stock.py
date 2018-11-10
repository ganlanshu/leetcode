#coding=utf-8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        profit = 0
        for i in range(1, n):
            if i == 1:
                profit = 0 if prices[1] - prices[0] < 0 else prices[1] - prices[0]
            else:
                f0 = min(prices[i-2],prices[i-1])
                profiti = prices[i] - f0
                prices[i-1] = f0
                if profiti > profit:
                    profit = profiti
        return profit

    def get_max_profit(self, prices):
        """
        这个是答案上写的
        :param prices:
        :return:
        """
        profit = 0
        minimum = float('inf')
        for price in prices:
            minimum = min(price, minimum)
            max_profit = price - minimum
            profit = max(max_profit, profit)
        return profit

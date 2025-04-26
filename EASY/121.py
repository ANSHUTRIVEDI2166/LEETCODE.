class Solution(object):
    def maxProfit(self, prices):
        minbuyprice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minbuyprice:
                minbuyprice = prices[i]
            else:
                p = prices[i] - minbuyprice
                profit = max(p, profit)
        return profit

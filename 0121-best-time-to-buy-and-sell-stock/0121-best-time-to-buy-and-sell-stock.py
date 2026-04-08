class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                profit = i - min_price
                if profit > max_profit:
                    max_profit = profit
            
        return max_profit
        
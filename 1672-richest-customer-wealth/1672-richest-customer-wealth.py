class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for row in accounts:
            current_sum = 0
            for val in row:
                current_sum += val
            max_wealth = max(max_wealth,current_sum)
        return max_wealth
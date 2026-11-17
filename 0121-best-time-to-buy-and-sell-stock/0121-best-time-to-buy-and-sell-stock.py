class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_pro=0
        min_pro=float('inf')
        for i in range(len(prices)):
            min_pro=min(min_pro,prices[i])
            profit=prices[i]-min_pro
            max_pro=max(max_pro,profit)
        return max_pro


        
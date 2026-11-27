
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)
        dp = [0] * (budget + 1)

        min_price = min(price for factor, price in items)

        for i in range(n):
            factor, price = items[i]

            # Count purchased item + free items
            count = 0

            for j in range(n):
                if items[j][0] % factor == 0:
                    count += 1

            # 0/1 Knapsack
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)

        # Use remaining budget to buy cheapest items
        ans = 0

        for i in range(budget + 1):
            extra = (budget - i) // min_price
            ans = max(ans, dp[i] + extra)

        return ans

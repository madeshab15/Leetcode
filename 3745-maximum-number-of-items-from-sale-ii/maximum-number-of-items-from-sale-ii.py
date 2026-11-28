
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Step 1: Count frequency of each factor
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Calculate how many free items each factor can provide
        gain = [0] * (n + 1)

        for i in range(1, n + 1):
            count = freq[i]

            for j in range(i * 2, n + 1, i):
                count += freq[j]

            gain[i] = count - 1

        # Step 3: Sort items by price
        items.sort(key=lambda x: x[1])

        min_price = items[0][1]
        ans = 0

        # Step 4: Buy items that provide a free item
        for factor, price in items:

            if price > 2 * min_price:
                break

            take = min(gain[factor], budget // price)

            ans += take * 2
            budget -= take * price

        # Step 5: Buy cheapest items with remaining budget
        ans += budget // min_price

        return ans

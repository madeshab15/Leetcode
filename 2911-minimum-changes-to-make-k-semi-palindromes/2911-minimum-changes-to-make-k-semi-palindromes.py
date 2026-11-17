
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute minimum changes for every substring
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for rem in range(d):
                        left = l + rem
                        right = l + rem + (groups - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[l][r] = best

        # DP: first i characters divided into j parts
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(2 * (j - 1), i - 1):
                    if dp[p][j - 1] != INF:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[p][j - 1] + cost[p][i - 1]
                        )

        return dp[n][k]

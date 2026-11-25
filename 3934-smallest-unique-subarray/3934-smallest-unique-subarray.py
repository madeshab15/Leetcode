class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Coordinate compression
        values = {v: i for i, v in enumerate(sorted(set(nums)))}
        rank = [values[x] for x in nums]

        # Build suffix array using doubling
        sa = list(range(n))
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for i in range(1, n):
                a, b = sa[i - 1], sa[i]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )

                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build inverse suffix array
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        # Kasai's algorithm: calculate LCP
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1

            lcp[r] = h
            h = max(h - 1, 0)

        # Find minimum unique subarray length
        ans = n

        for r in range(n):
            max_lcp = lcp[r]

            if r + 1 < n:
                max_lcp = max(max_lcp, lcp[r + 1])

            length = max_lcp + 1

            if length <= n - sa[r]:
                ans = min(ans, length)

        return ans
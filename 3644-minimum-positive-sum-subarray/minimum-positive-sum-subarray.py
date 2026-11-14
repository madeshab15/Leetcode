
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, min(i + r, len(nums))):
                curr_sum += nums[j]

                length = j - i + 1

                if l <= length <= r and curr_sum > 0:
                    ans = min(ans, curr_sum)

        return ans if ans != float('inf') else -1

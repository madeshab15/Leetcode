class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            total=0
            count=0
            left=0
            for right in range(len(nums)):
                total+=nums[right]
                while total>k:
                    total-=nums[left]
                    left+=1
                count+=right-left+1
            return count
        return atmost(goal)-atmost(goal-1)
        
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            odd=0
            left=0
            count=0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd+=1
                while odd>k:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count+=right-left+1
            return count
        return atmost(k) - atmost(k-1)

        
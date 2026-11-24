class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_len=0
        for left in range(len(nums)):
            product=1
            g=0
            l=1
            for right in range(left,len(nums)):
                product*=nums[right]
                g=gcd(g,nums[right])
                l=lcm(l,nums[right])
                if product==g*l:
                    max_len=max(max_len,right-left+1)
        return max_len
        

        
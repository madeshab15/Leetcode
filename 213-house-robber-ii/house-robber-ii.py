class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_linear(arr):
            prev=0
            curr=0
            if len(nums)==1:
                return nums[0]
            for money in arr:
                temp=max(curr,prev+money)
                prev=curr
                curr=temp
            return curr
            

        case1=rob_linear(nums[:-1])
        case2=rob_linear(nums[1:])
        return max(case1,case2)
            
        
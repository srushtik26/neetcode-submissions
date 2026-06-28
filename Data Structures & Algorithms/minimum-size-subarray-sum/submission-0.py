class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=0
        mini=float('inf')
        l=0
        for r in range(len(nums)):
            res+=nums[r]
            while res>=target:
                mini=min(mini,r-l+1)
                res-=nums[l]
                l+=1
        return 0 if mini==float('inf') else mini      
        
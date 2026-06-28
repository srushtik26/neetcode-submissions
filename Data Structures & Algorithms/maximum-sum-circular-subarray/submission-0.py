class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax=nums[0]
        gmin=nums[0]
        currmax=0
        currmin=0
        total=0
        for num in nums:
            currmax=max(currmax+num,num)
            currmin=min(currmin+num,num)
            total+=num
            gmax=max(gmax,currmax)
            gmin=min(gmin,currmin)
        return max(gmax,total-gmin)if gmax>0 else gmax
        
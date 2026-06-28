class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currsum=0
        prefixsum={0:1}
        for num in nums:
            currsum+=num
            diff=currsum-k
            
            res+=prefixsum.get(diff,0)
            prefixsum[currsum]=1+prefixsum.get(currsum,0)
        return res    
        # res=0
        # for i in range(len(nums)):
        #     sums=0
        #     for j in range(i,len(nums)):
        #         sums+=nums[j]
        #         if sums==k:
        #             res+=1
        # return res            

 
        
        




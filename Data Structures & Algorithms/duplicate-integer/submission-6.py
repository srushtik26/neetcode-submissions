class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=set(nums)
        if len(num)==len(nums):
            return False
        return True

        # hashmap={}
        # for num in nums:
        #     if num in hashmap:
        #         return True
        #     else:
        #         hashmap[num] = True
        # return False    
           
           
                

        
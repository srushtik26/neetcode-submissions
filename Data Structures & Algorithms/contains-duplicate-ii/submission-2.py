class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        maps={}
        for i,num in enumerate(nums):
            if num in maps and i-maps[num]<=k:
                return True
            maps[num]=i
        return False    
        
        
        
    
        
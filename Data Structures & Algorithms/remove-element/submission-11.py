class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        i=0

        # for i in range (len(nums)):
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)



             
        
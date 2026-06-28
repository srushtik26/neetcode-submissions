from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        most_com=count.most_common(k)
        result=[]
        for items,frequency in most_com:
            result.append(items)
        return result
        
        
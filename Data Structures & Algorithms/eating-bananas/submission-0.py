class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high=max(piles)
        res=0
        while low<=high:
            k=(low+high)//2
            maxtime=0

            for pile in piles:
                
                maxtime+=math.ceil(pile/float(k))
            if maxtime<=h:
                res=k
                high=k-1
            else:
                low=k+1
        return res            


            
        # speed=1
        # while True:
        #     totaltime=0
        #     for pile in piles :
        #         totaltime+=math.ceil(pile/speed)
        #     if totaltime<=h:
        #         return speed

        #     speed+=1
        # return speed    
                    





        
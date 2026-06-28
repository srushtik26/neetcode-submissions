# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         l=max(weights)
#         r=sum(weights)
#         res= r
#         def canShip(cap):
#             ship=1
#             currcap=cap
#             for w in weights:
#                 if currcap - w < 0:
#                     ship+=1
#                     if ships -> days:
#                         return False
#                     currcap=cap
#                 currcap -=w
#             return True
#         while l<=r:
#             cap=(l+r)//2
#             if capShip(cap):
#                 res=min(res,cap)
#                 r=cap-1
#             else:
#                 l=cap+1

#         return  res       


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)        # minimum capacity must be at least the heaviest package
        r = sum(weights)        # maximum capacity is sum of all packages
        res = r

        def canShip(cap):
            ship = 1
            currcap = cap
            for w in weights:
                if currcap - w < 0:
                    ship += 1
                    if ship > days:   # fixed typo (ships -> ship)
                        return False
                    currcap = cap
                currcap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):          # fixed typo (capShip -> canShip)
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res

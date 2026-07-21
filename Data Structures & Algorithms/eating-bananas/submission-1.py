import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2
            for val in piles:
                ratio = sum(math.ceil(pile / mid))
            
            if ratio <= h:
                r -= 1
            else:
                l += 1
            
        return ratio


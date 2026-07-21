import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        for i in range(1,k+1):
            ratio = 0
            for val in piles:
                ratio += math.ceil(val/i)
            if ratio <= h:
                return i
        return ratio


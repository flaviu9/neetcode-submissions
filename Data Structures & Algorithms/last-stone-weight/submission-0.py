class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = 0
            max2 = 0
            for i in range(len(stones)):
                if stones[i] > max1:
                    max2 = max1
                    max1 = stones[i]
                elif stones[i] > max2:
                    max2 = stones[i]
            stones.remove(max1)
            stones.remove(max2)
            if max1 != max2:
                stones.append(max1 - max2)
        if stones:
            return stones[0]
        else:
            return 0
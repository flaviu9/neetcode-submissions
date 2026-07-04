class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n1 = cost[0]
        n2 = cost[1]
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(n1, n2)
            n1 = n2
            n2 = curr
        
        return min(n1,n2)
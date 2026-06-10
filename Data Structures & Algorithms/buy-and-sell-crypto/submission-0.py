class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
        max_index = min_index
        for i in range(min_index, len(prices)):
            if prices[i] > prices[max_index]:
                max_index = i
        print(min_index,max_index)
        if max_index == 0:
            return max_index
        return prices[max_index] - prices[min_index]
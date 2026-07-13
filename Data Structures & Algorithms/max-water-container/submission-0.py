class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0
        for i in range(len(heights)-2):
            for j in range(i,len(heights)-1):
                minimum = min(heights[i],heights[j])
                if maxContainer < minimum * (abs(i-j)):
                    maxContainer = minimum * (abs(i-j))
        return maxContainer
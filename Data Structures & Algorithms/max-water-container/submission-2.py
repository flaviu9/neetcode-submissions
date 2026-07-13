class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            minimum = min(heights[l],heights[r])
            if maxContainer < minimum * (abs(l-r)):
                maxContainer = minimum * (abs(l-r))
            if minimum == heights[l]:
                l += 1
            elif minimum == heights[r]:
                r -= 1
        return maxContainer
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, val in enumerate (temperatures):
            while stack and val > stack[-1][1]:
                prevIdx, prevVal = stack.pop()
                res[prevIdx] = idx - prevIdx
            stack.append((idx, val))
        return res




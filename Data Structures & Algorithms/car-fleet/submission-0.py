class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = 0
        for idx in range(len(position) - 1):
            stack.append((target - position[idx])/speed[idx])
        for idx, val in enumerate(stack):
            if stack[idx] <= stack[idx-1]:
                fleet += 1
        return fleet
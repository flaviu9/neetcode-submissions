class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            value = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                value *= nums[j]
            output.append(value)
        return output
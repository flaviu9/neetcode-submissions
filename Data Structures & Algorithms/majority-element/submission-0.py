class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)
        for val in nums:
            if val in seen:
                seen[val] += 1
            else:
                seen[val] = 1
        for val in seen:
            if seen[val] > n // 2:
                return val
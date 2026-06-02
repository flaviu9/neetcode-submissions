class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, val in enumerate(nums):
            if val in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False
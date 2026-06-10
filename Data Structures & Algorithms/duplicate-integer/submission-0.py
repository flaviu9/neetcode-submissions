class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            d = {i : nums[i]}
            if nums[i] in d:
                return True
        return False

            
        
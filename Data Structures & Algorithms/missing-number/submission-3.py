class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = 0
        for i in range(len(nums)+1):
            check ^= i
        for i in nums:
            check ^= i
        return check
        

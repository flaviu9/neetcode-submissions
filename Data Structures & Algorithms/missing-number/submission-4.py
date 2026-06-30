class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = 0
        hash = {}
        for i in nums:
            hash[i] = 1
        for i in range(len(nums) + 1):
            if i not in hash:
                return i
            else:
                continue
        
        

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        realSum = (n*(n+1))/2
        for elem in range(len(nums)):
            sum += nums[elem]
        if sum != realSum:
            return int(realSum - sum)
        return 0
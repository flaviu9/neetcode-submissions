class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = 99999999999
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] < minn:
                minn = nums[i]
        return minn
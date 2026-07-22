class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = 999999
        for i in range(len(nums)):
            if nums[i] < minn:
                minn = nums[i]
        return minn
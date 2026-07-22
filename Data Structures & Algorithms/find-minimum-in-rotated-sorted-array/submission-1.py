class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = 99999
        for i in range(len(nums) - 1):
            if nums[i] < minn:
                minn = nums[i]
        return minn
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        found = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
                found = 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if not found:
            return l
        else:
            return mid

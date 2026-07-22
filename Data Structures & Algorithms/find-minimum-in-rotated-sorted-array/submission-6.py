class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        found = False

        while not found:
            mid = (l+r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
                found = True
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
                found = True
            else:
                r -= 1
            
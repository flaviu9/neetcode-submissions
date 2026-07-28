class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
     hmap = {}
     for num in range(len(nums)):
        if nums[num] not in hmap:
            hmap[nums[num]] = 1
        else:
            return nums[num]


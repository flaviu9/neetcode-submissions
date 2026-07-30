class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []

        while l <= r:
            if nums[l] + nums[r] == target:
                res.append(l)
                res.append(r)
                return res 
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
            
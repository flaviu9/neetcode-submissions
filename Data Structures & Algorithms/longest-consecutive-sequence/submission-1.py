class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        res = 0
        for elem in vals:
            curr = 1
            while elem + 1 in vals:
                curr += 1
                elem += 1
            res = max(curr,res)
        return res

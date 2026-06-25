class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = 0
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for val in dict:
            if dict[val] == 1:
                return val
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = len(nums)
        elem = 0
        while elem != counter:
            if nums[elem] == val:
                nums[elem] = nums[counter - 1]
                counter -= 1
            else:
                elem += 1
        return counter


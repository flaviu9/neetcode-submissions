class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pwr = len(digits) - 1
        res = []
        number = 0
        for digit in digits:
            number += digit * (10 ** pwr)
            pwr -= 1

        number += 1
        while number:
            res.append(number % 10)
            number = number // 10
        return res[::-1]
        
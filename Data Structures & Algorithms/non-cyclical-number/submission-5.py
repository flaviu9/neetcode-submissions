class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigits(n):
            sum = 0
            while n:
                sum += (n%10) ** 2
                n //= 10
            return sum
        hash = {}
        while True:
            result = sumDigits(n)
            if result == 1:
                return True
            elif result in hash:
                return False
            hash[result] = 1
            n = result
        return False
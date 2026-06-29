class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigits(n):
            sum = 0
            while n:
                sum += (n%10) ** 2
                n //= 10
            return sum
        hash = {}
        while sum not in hash:
            if sumDigits(n) == 1:
                return True
            else:
                hash[n] = hash.get(n, 0)
            n = sum
            return False
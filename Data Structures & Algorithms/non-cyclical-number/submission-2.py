class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigits(n):
            sum = 0
            while n:
                sum += (n%10) ** 2
                n //= 10
            return sum
        hash = {}
        val = 0
        while val not in hash:
            sum = sumDigits(n)
            if sumDigits(n) == 1:
                return True
            else:
                hash[n] = hash.get(sum, 0)
            n = val
            return False
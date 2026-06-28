class Solution:
    def reverseBits(self, n: int) -> int:
        rev = []
        checker = 32
        pwr = 31
        res = 0
        while n or checker:
            rev.append(n%2)
            n //= 2
            checker -= 1
        for i in rev:
            res += i * (2 ** pwr)
            pwr -= 1
        return res
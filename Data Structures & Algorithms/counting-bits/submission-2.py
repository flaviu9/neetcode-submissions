class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for n in range(n + 1):
            counter = 0
            while n:
                if n % 2 != 0:
                    counter += 1
                n >>= 1
            res.append(counter)
        return res
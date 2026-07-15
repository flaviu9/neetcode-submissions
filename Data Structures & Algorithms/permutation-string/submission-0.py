from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls = list(s1)
        perm = permutations(ls)

        for i in perm:
            if ''.join(i) in s2:
                return True
        
        return False
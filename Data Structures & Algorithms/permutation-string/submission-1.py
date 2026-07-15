from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls = list(s1)
        def freqq(ls):
            freq = {}
            for val in ls:
                freq[val] = freq.get(val, 0) + 1
            return freq
        check = freqq(ls)
        for i in range(len(s2) - len(s1) + 1):
            wdw = s2[i:i+len(s1)]
            if freqq(wdw) == check:
                return True
        return False
            
        
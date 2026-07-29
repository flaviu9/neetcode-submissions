class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmapS = {}
        hmapT = {}

        ls = list(s)
        lt = list(t)

        for val in ls:
            hmapS[val] = hmapS.get(val, 0) + 1
        
        for val in lt:
            hmapT[val] = hmapT.get(val, 0) + 1

        return hmapS == hmapT
        


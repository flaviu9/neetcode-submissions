class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = set()
        seenT = set()
        for i in s:
            seenS.add(i)
        for j in t:
            seenT.add(j)
        for elem in seenS:
            if elem not in seenT:
                return False
        return True
        
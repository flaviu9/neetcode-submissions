class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = set()
        setT = set()

        ls = list(s)
        lt = list(t)

        for val in ls:
            setS.add(val)
        
        for val in lt:
            setT.add(val)

        if setT == setS:
            return True
        else:
            return False


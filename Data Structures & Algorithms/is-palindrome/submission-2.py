class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = list(s)
        lsRev = list(s)
        filtered = []

        
        for c in s:
             if c.isalnum():
                filtered.append(c.lower())
        return filtered == filtered[::-1]
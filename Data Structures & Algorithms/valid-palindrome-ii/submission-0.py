class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        keep = 0

        while l <= r:
            if s[l] != s[r]:
                keep += 1
                l += 1
                if keep > 1:
                    return False
            l += 1
            r -= 1
        return True
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        keepL, keepR = 0, 0

        while l <= r:
            if s[l] != s[r]:
                keepL += 1
                l += 1
                keepR += 1
                r -= 1
                if keepL > 1 or keepR > 1:
                    return False
            l += 1
            r -= 1
        return True
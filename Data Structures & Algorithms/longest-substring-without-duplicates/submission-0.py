class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = list(s)
        maxx = 0
        chars = set()
        check = []
        for val in ls:
            
            while val in chars:
                chars.remove(check[0])
                check.pop(0)
            
            chars.add(val)
            check.append(val)
            maxx = max(maxx, len(check))
        return maxx

       

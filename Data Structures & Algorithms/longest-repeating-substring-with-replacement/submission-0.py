class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = list(s)
        maxx = 0
        chars = set()
        check = []
        chars = set(ls)
        for i in chars:
            
            for val in ls:
                while val in chars:
                    chars.remove(check[0])
                    check.pop(0)

                chars.add(val)
                check.append(val)
                maxx = max(maxx, len(check))
        return maxx
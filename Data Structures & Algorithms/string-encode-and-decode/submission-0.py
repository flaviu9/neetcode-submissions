class Solution:
    
    def encode(self, strs: List[str]) -> str:
        message = ""
        for string in strs:
            message += str(len(string)) + '#' + string
        return message
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # acum j e la '#'
            n = int(s[i:j])        # lungimea cuvântului
            res.append(s[j+1:j+1+n])  # cuvântul
            i = j + 1 + n          # mergi la următorul
        return res
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        ref = strs[0]

        for i in range(len(ref)):
            for word in strs[1:]:
                if ref[i] != word[i] or i >= len(word):
                    return prefix
            prefix += word[i]
        
        return prefix


        
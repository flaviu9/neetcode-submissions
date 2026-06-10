class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        ref = strs[0]

        for i in range(len(ref)):
            for word in strs[1:]:
                if i >= len(word) or ref[i] != word[i]:
                    return prefix
            prefix += word[i]
        
        return prefix


        
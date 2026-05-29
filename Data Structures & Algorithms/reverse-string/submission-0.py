class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(0, len(s)//2):
            aux = s[i]
            s[i] = s[n]
            s[n] = aux
            n -= 1
        
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in pairs:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[i]:
                    return False
            else:
                stack.append(i)
        return True

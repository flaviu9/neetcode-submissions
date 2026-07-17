class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
           if elem == '+':
               b = stack.pop()
               a = stack.pop()
               stack.append(a + b)
           elif elem == '-':
               b = stack.pop()
               a = stack.pop()
               stack.append(a - b)
           elif elem == '*':
               b = stack.pop()
               a = stack.pop()
               stack.append(a * b)
           elif elem == '/':
               b = stack.pop()
               a = stack.pop()
               stack.append(a / b)
           else:
               stack.append(int(elem))
        return stack[0]


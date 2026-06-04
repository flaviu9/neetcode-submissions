class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
            elif op == 'D':
                val = stack[-1] * 2
                stack.append(val)
            elif op == 'C':
                stack.pop()
        sum = 0
        for i in stack:
            sum += int(i)
        return sum
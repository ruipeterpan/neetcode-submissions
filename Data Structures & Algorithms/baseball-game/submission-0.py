class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i, op in enumerate(operations):
            if op == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(a + b)
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
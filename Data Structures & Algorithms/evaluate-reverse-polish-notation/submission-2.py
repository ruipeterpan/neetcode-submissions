class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        
        i = 0

        while i < n:
            t = tokens[i]

            if t in ["+", "-", "*", "/"]:  # 
                n2 = stack.pop()
                n1 = stack.pop()
                if t == "+":
                    stack.append(n1 + n2)
                elif t == "-":
                    stack.append(n1 - n2)
                elif t == "*":
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))  # not n1 // n2!
            else:
                stack.append(int(t))

            i += 1
        
        return stack[-1]
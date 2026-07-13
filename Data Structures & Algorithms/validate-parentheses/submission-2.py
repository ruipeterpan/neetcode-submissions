class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ["[", "{", "("]:  # enqueue
                stack.append(ch)
            else:  # dequeue, check for match
                if len(stack) == 0:
                    return False
                other_side = stack.pop()
                if f"{other_side}{ch}" not in ["[]", "{}", "()"]:
                    return False
        return len(stack) == 0
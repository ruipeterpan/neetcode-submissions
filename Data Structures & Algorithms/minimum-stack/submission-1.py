class MinStack:

    def __init__(self):
        self.l = []
        self.min_stack = []  # current minimum after each push

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.min_stack) > 0:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.l.pop(-1)
        self.min_stack.pop(-1)
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.l = 0  # inclusive pointer at leftmost element
        self.r = 0
        self.capacity = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.capacity == 0:
            assert self.l == self.r
            self.queue[self.r] = value
        else:
            self.r = (self.r + 1) % self.k
            self.queue[self.r] = value

        self.capacity += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.capacity == 1:
            pass
        else:
            self.l = (self.l + 1) % self.k
        self.capacity -= 1
        return True
        

    def Front(self) -> int:
        if self.capacity == 0:
            return -1
        return self.queue[self.l]

    def Rear(self) -> int:
        if self.capacity == 0:
            return -1
        return self.queue[self.r]

    def isEmpty(self) -> bool:
        return self.capacity == 0

    def isFull(self) -> bool:
        return self.capacity == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
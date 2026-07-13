import heapq

class MedianFinder:

    def __init__(self):
        self.left_heap = []  # max heap
        self.right_heap = []  # min heap
        # size difference is at most 1.
        # if odd, right is always bigger than left by 1.

        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        # insert
        if not self.right_heap or num >= self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -num)

        # rebalance
        while not ((len(self.left_heap) == len(self.right_heap)) or 
            (len(self.left_heap) + 1 == len(self.right_heap))):
            if len(self.left_heap) > len(self.right_heap):
                el = -heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, el)
            else:
                el = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -el)

        # heapq.heappush(heap, item)

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        elif len(self.left_heap) + 1 == len(self.right_heap):
            return self.right_heap[0]
        else:
            raise ValueError
        
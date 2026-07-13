import math
import heapq

class Solution:
    def distance(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # max heap
        heapq.heapify(heap)
        for p in points:
            x, y = p
            # print(x, y)
            heapq.heappush(heap, (-self.distance(x, y), p))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [v for k, v in heap]

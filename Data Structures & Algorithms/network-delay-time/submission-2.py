import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))  # v: target; w: latency

        pq = []  # key: distance from head, value: node
        heapq.heapify(pq)
        heapq.heappush(pq, (0, k))

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for target, latency in graph[node]:
                if dist[target] > dist[node] + latency:
                    dist[target] = dist[node] + latency
                    heapq.heappush(pq, (dist[target], target))
        
        if max(dist[1:]) == float('inf'):
            return -1
        else:
            return max(dist[1:])




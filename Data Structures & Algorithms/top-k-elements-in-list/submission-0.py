class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        most_to_least = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in most_to_least][:k]
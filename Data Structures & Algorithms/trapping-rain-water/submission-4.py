class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        dp_prefix_max = []  # index i: max before i (excluding i)
        dp_suffix_max = []  # index i: max after i (excluding i)

        prefix_max = float('-inf')
        for i in range(n):
            dp_prefix_max.append(prefix_max)
            prefix_max = max(prefix_max, height[i])
        
        suffix_max = float('-inf')
        for i in range(n-1, -1, -1):
            dp_suffix_max.append(suffix_max)
            suffix_max = max(suffix_max, height[i])
        dp_suffix_max.reverse()

        total = 0

        for i, h in enumerate(height[1:-1], start=1):
            # min_bar = min(max(height[:i]), max(height[i+1:]))
            min_bar = min(dp_prefix_max[i], dp_suffix_max[i])
            total += max(0, min_bar - h)
            print(f"Bar number {i} holds {max(0, min_bar - h)}, min_bar {min_bar}, h {h}")
        
        return total

class Solution:
    def trap(self, height: List[int]) -> int:
        # for each bar: the amount of water it holds is:
        # expand both directions while elevation keeps increasing, 
        # until the first decrease. 
        # take the min of the two, and minus its own height
        
        total = 0
        n = len(height)

        for i, h in enumerate(height[1:-1], start=1):
            # l = i - 1
            # while l - 1 >= 0 and height[l-1] >= height[l]:
            #     l -= 1
            # r = i + 1
            # while r + 1 < n and height[r+1] >= height[r]:
            #     r += 1
            
            # min_bar = min(height[l], height[r])
            min_bar = min(max(height[:i]), max(height[i+1:]))
            total += max(0, min_bar - h)
            print(f"Bar number {i} holds {max(0, min_bar - h)}, min_bar {min_bar}, h {h}")
        
        return total

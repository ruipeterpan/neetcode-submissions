class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        m = -1
        while i < j:
            v = (j - i) * min(heights[i], heights[j])
            if max(m, v) > m:
                m = v
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return m
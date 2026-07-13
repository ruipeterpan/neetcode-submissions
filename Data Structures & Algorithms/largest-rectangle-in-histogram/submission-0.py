class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        # for each position i, find the left/right furthest bar
        # that is not shorter than bar i

        n = len(heights)
        left = [-1] * n  # index of next shorter bar on the left side
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        m = max(heights)

        for i in range(n):
            m = max(m, heights[i] * (right[i] - left[i] - 1))

        return m





        """
        Brute force:
        w: max width of the rectangle is len(heights)
        for i in 1...w:
            sweep over the x axis, height is max of bar heights
        """
class Solution:
    def climbStairs(self, n: int) -> int:
        # l[i] = l[i-1] + l[i-2]

        l = []
        for i in range(n + 1):
            if i == 0:
                l.append(0)
            elif i == 1:
                l.append(1)
            elif i == 2:
                l.append(2)
            else:
                l.append(l[-1] + l[-2])
        
        return l[-1]
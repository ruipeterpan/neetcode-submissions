class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i, t in enumerate(temperatures):
            if i == 0:  # initialization
                stack.append((i, t,))
            else:
                # first check if we can "fill" any previous days
                while stack:
                    past_day, past_temp = stack[-1]

                    if past_temp >= t:
                        break
                    res[past_day] = i - past_day
                    stack.pop()
                 
                stack.append((i, t))
            
        
        return res
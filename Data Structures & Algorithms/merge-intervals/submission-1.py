class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # sort by start time

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                # merge into
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans
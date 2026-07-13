class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # sort by start time

        removed = 0
        prev_end = intervals[0][1]

        for i, (l, r) in enumerate(intervals[1:], start=1):
            if l < prev_end:  # overlap
                # remove the interval with the righter r
                removed += 1
                prev_end = min(prev_end, r)
            else:  # no overlap
                prev_end = r
        return removed
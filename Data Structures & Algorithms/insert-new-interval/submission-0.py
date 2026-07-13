class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # left to right pass. find first interval where
        # it will intersect with the newInterval. merge.
        # then, start from that new interval, and merge it with any of the
        # potential intersections to its right. 
        # stop when the righter interval has no intersections.

        new_l, new_r = newInterval
        res = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < new_l:
            res.append(intervals[i])
            i += 1
        
        # first overlap observed
        while i < n and intervals[i][0] <= new_r:
            new_l = min(new_l, intervals[i][0])
            new_r = max(new_r, intervals[i][1])
            i += 1
        
        res.append([new_l, new_r])

        res += intervals[i:]

        return res



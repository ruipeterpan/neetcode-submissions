"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        num_rooms = 0
        end_ptr = 0

        for i, s in enumerate(start):
            if s < end[end_ptr]:
                # the earliest meeting ends in the future
                # needs a new room
                num_rooms += 1
            else:  # reuse a previously-empty room
                end_ptr += 1
        
        return num_rooms



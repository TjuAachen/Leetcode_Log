class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        end = []
        intervals.sort()
        res, count = 1, 0
        heapq.heappush(end,intervals[0][1])
        for i in intervals[1:]:
            while(end and i[0] >= end[0]):
                heapq.heappop(end)
            heapq.heappush(end,i[1])
            res = max(res, len(end))
        return res            
                
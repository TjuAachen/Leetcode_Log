class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[1] > res[-1][1] and i[0]>res[-1][0]:
                res.append(i)
            if i[1] > res[-1][1] and i[0] == res[-1][0]:
                res[-1][1] = i[1]
        return len(res)
            
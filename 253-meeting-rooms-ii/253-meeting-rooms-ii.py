class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begin = []
        end = []
        for i in intervals:
            begin.append(i[0])
            end.append(i[1])
        begin.sort()
        end.sort()
        i, j =0, 0
        count = 0
        n = len(begin)
        res = 0
        while(i<n and j<n):
            if begin[i] < end[j]:
                count += 1
                i = i + 1
            else:
                count = count - 1
                j = j + 1
            res = max(res, count)
        return res
                
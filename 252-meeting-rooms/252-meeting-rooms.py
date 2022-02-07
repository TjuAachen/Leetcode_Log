class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        begin = []
        end = []
        for i in intervals:
            begin.append(i[0])
            end.append(i[1])
        begin.sort()
        end.sort()
        i, j =0, 0 
        n = len(begin)
        count = 0
        while(i<n and j<n):
            if begin[i] < end[j]:
                count += 1
                i = i + 1
            else:
                count -= 1
                j = j + 1
            if count > 1:
                return False
        return True
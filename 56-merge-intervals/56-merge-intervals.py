class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        
        for i in intervals[1:]:
            if res[-1][1] >= i[0]:
                res[-1][1] = max(i[1],res[-1][1])
            else:
                res.append(i)
        return res
            
            
            
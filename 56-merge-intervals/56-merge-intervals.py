class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        
        for i in intervals[1:]:
            former = res.pop()
            if former[1] >= i[0]:
                former = [former[0],max(i[1],former[1])] 
                res.append(former)
            else:
                res.append(former)
                res.append(i)
        return res
            
            
            
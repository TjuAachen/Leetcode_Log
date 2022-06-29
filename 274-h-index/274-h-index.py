from bisect import *
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        min_h, max_h = citations[0], citations[-1]
        def check(h):
            # exactly val >= h
            i = bisect_left(citations, h,0,n)
            
            #exactly val > h
            j = bisect(citations, h,0,n)
            min_num_less_h = i
            max_num_less_h = j
            if i<=n-h<=j:
                return True
            
        right = min(max_h, n)
        final = -1
        for i in range(0, right + 1):
            if check(i):
                final = max(final, i)
        return final
        
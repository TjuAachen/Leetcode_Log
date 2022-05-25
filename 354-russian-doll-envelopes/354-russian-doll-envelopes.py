from bisect import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        n = len(envelopes)
        sub = []
        for i in range(n):
            pos = bisect_left(sub, envelopes[i][1])
            if pos == len(sub):
                sub.append(envelopes[i][1])
            else:
                sub[pos] = envelopes[i][1]
        return len(sub)
            
        
        
                
        
        
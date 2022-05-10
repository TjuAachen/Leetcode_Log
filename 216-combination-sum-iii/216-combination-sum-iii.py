class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        track, result = [], []
        def combination(start):
            if len(track) == k:
                if sum(track) == n:
                    result.append(track[:])
                return
            for i in range(start,10):
                track.append(i)
                combination(i+1)
                track.pop()
        combination(1)
        return result
            
                
        
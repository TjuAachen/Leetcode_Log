class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        final = []
        n = len(candidates)
        def combine(i):
            if sum(res) == target:
                final.append(res[:])
                return
            if sum(res) > target or len(res) > 150:
                return
            for j in range(i,n):
                res.append(candidates[j])
                combine(j)
                res.pop()
        combine(0)
        return final
        
        
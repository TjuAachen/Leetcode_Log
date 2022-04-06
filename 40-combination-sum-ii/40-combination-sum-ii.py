class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        final = []
        n = len(candidates)
        candidates.sort()
        used = dict()
        def combine(i):
            if sum(res) == target:
                final.append(res[:])
                return
            elif sum(res) > target:
                return
            for j in range(i,n):
                if j == 0  or (candidates[j-1] != candidates[j]) or j-1 in used:
                    used[j] = 1
                    res.append(candidates[j])
                    combine(j+1)
                    res.pop()
                    del used[j]
        combine(0)
        return final
        
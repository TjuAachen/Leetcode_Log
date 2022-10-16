from sortedcontainers import SortedList
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        maxDifficulty = [[0] * n for _ in range(n)]
        curMax = -float('inf')
        for i in range(n):
            curList = SortedList()
            for j in range(i, n):
                curList.add(jobDifficulty[j])
                maxDifficulty[i][j] = curList[-1]
        memo = dict()
        return self.findMinDifficulty(0, jobDifficulty, d, memo, maxDifficulty)
        
        
    def findMinDifficulty(self, start, jobDifficulty, d, memo, maxDifficulty):
        key = tuple([start, d])
        if key in memo:
            return memo[key]
        n = len(jobDifficulty)
        if start == n:
            return float('inf')
        if d == 1:
            return maxDifficulty[start][-1]
        res = float('inf')
        for nxt in range(start, n):
            res = min(res, self.findMinDifficulty(nxt + 1, jobDifficulty, d - 1, memo, maxDifficulty) + maxDifficulty[start][nxt])
        memo[key] = res
        return res
        
        
        
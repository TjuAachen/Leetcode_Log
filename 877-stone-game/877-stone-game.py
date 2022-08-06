class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}
        def dfs(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = max(piles[i] - dfs(i+1, j), piles[j] - dfs(i, j -1))
            memo[(i,j)] = res
            return res
        dfs(0, len(piles) -1)
        
        return memo[(0, len(piles) - 1)] >= 0
        
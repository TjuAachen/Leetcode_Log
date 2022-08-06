class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        n = len(piles)
        
        #prefix sum
        total_sum = sum(piles)
        prefix_sum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + piles[i-1]
        #print(prefix_sum)
        def dfs(i, M):
            if i >= n:
                return 0
            if (i, M) in memo:
                return memo[(i, M)]
            res = 0
            for j in range(1, 2 * M + 1):
                if i + j > n:
                    continue
                res = max(res, prefix_sum[i+j] - prefix_sum[i] + prefix_sum[-1] - prefix_sum[i+j] - dfs(i+j, max(M, j)))
            memo[(i, M)] = res
            return res
        return dfs(0, 1)
        #print(memo)
        
        
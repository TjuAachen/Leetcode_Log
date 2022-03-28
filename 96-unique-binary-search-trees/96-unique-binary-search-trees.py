class Solution:
    def numTrees(self, n: int) -> int:
        memo = dict()
        def backtracking(n):
            count = 0
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            for index in range(n):
                count += backtracking(n-index-1)*backtracking(index)
            memo[n] = count
            return count
        return backtracking(n)
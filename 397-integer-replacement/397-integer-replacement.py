class Solution:
    def integerReplacement(self, n: int) -> int:
        #reversed thinking
        memo = dict()
        def find_res(n):
            if n in memo:
                return memo[n]
            if n == 1:
                memo[n] =0
                return 0
            if n % 2:
                if n != 3:
                    res = min(find_res(n+1), find_res(n-1)) + 1
                else:
                    res = find_res(2) + 1
            else:
                res = find_res(n//2) + 1
            memo[n] = res
            return res
        find_res(n)
        return memo[n]
            
                
        
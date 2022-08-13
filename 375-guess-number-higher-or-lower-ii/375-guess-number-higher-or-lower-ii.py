class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        
        def max_money(start, end):
            if end - start == 1:
                memo[(start, end)] = start
                return start
            if end == start:
                return 0
            res = float('inf')
            if (start, end) in memo:
                return memo[(start, end)]
            mid = (start + end) // 2
           # print(mid, start, end)
            for division in range(mid, end):
                left, right = -float('inf'), -float('inf')
                if (start, division - 1) in memo:
                    left = memo[(start, division - 1)]
                if (division + 1, end) in memo:
                    right = memo[(division+1, end)]
                if left + division > res or right + division > res:
                    continue
                res = min(res, max(max_money(start, division-1), max_money(division+1, end)) + division)
            memo[(start, end)] = res
            return res
        return max_money(1, n)
                
                
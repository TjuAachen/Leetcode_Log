class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        #3 parts
        def find(part):
            average = n // part
            integer_break_result = [average] * part
        
            remainder = n % part
        
            for i in range(1, remainder + 1):
                integer_break_result[i] = average + 1
        
            res = 1
            for i in range(part):
                res *= integer_break_result[i] 
            return res
        prev = None
        for i in range(2, n+1):
            cur = find(i)
            if prev != None and prev >= cur:
                return prev
            else:
                prev = cur
                
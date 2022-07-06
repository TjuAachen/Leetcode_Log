class Solution:
    def fib(self, n: int) -> int:
        prev1 = 0
        prev2 = 1
        if n == 0:
            return prev1
        if n == 1:
            return prev2
        for i in range(2, n + 1):
            value = prev1 + prev2
            prev1, prev2 = prev2, value
        return value
        
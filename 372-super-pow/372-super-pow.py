class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        def power(a, n):
            ans = 1
            base = a
            while(n):
                if n%2:
                    ans = (ans*base)%1337
                base = (base*base)%1337
                n = n>>1
            return ans
                    
            return ans
        for num in reversed(b):
            ans *= power(a, num)
           # print(ans)
            a = power(a, 10)
            ans %= 1337
        return ans
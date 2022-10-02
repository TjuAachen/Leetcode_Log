
class Solution:
    def deleteString(self, s: str) -> int:
        
        @cache
        def fn(i):
            """Return maximum number of steps to delete s[i:]."""
            ans = 1
            lsp = [0]
            k = 0
            for j in range(i+1, len(s)): 
                while k and s[k+i] != s[j]: k = lsp[k-1]
                if s[k+i] == s[j]: k += 1
                lsp.append(k)
                if k*2 == j-i+1: ans = max(ans, 1+fn(i+k))
            return ans 
        
        return fn(0)
        
        
        
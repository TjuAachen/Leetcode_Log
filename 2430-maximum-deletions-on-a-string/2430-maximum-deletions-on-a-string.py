class Solution:
    def deleteString(self, s: str) -> int:
        memo = defaultdict(int)
        self.n = len(s)
        self.deleteNum(s, 0, 0, memo)
        return memo[self.n]
    def deleteNum(self, s, start, count, memo):
        if start == self.n:
            memo[start] = max(memo[start], count)
            return
        if start in memo and memo[start] >= count:
            return
        k = 0
        lsq = [0]
        memo[start] = max(memo[start], count)
        for j in range(1 + start, self.n):
            while(k and s[j] != s[start + k]): 
                k = lsq[k - 1]
            if s[j] == s[start + k] : 
                k += 1
            lsq.append(k)
            if k * 2 == j - start + 1:
                self.deleteNum(s, start + k, count + 1, memo)
        self.deleteNum(s, self.n, count + 1, memo)
        return
        
        
        
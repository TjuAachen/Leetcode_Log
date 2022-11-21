class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        
        length = len(s)
        
        #dp[k + 1][length + 1]
        dp = [[0] * (length + 1) for _ in range(k + 1)]
        
        #initial value
        dp[0][0] = 1
        
        #edge case
        if k * minLength > len(s) or not self.isPrime(0, s) or self.isPrime(len(s) - 1, s):
            return 0
        
        for numPiece in range(1, k + 1):
            tot = 0
            for cur in range(numPiece * minLength, length + 1 - (k - numPiece) * minLength):
                if self.canPartition(cur - minLength, s):
                    tot += dp[numPiece - 1][cur - minLength]%MOD
                if self.canPartition(cur, s):
                    dp[numPiece][cur] = tot%MOD
             #   print(tot)
        return dp[k][length]
                
        
    def canPartition(self, cur, s):
        if cur - 1 < 0 or cur == len(s) or (not self.isPrime(cur - 1, s) and self.isPrime(cur, s)):
            return True
        return False
        
    def isPrime(self, i, s):
        return s[i] in '2357'
    
    
            
        
        
            
        
        
        
        
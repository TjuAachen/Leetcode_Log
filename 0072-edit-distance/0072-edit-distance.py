class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        self.memo = defaultdict()
        return self.calMin(word1, word2, 0, 0)
    
    def calMin(self, word1, word2, p1, p2):
        n1, n2 = len(word1), len(word2)
        
        key = tuple([p1, p2])
        if key in self.memo:
            return self.memo[key]
        
        if p2 == n2:
            return n1 - p1
        if p1 == n1:
            return n2 - p2
        res = float('inf')
        if word1[p1] == word2[p2]:
            res = min(res, self.calMin(word1, word2, p1 + 1, p2 + 1))
        #insert
        res = min(res, self.calMin(word1, word2, p1, p2 + 1) + 1)
        #delete
        res = min(res, self.calMin(word1, word2, p1 + 1, p2) + 1)
        #replace
        res = min(res, self.calMin(word1, word2, p1 + 1, p2 + 1) + 1)
        
        self.memo[key] = res
        
        
        return res
        
        
        
        #delete
        
        #replace
        
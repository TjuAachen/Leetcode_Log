class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        self.memo = defaultdict(int)
        self.ans = 0
        self.k = k
        self.find(len(piles) - 1, k, piles)

        return self.ans
    
    def find(self, i, remainingK,  piles):
        key = tuple([i, remainingK])

        if key in self.memo:
            return self.memo[key]
        
        if i == -1:
            return 0
        if remainingK < 0:
            return 0
        pile = piles[i]
        n = len(pile)
        
        if i == 0 and n < remainingK:
            return 0
        if i == 0:
            self.ans = max(self.ans, sum(pile[:remainingK]))
            self.memo[key] = sum(pile[:remainingK])
            return self.memo[key]
        
        maxSelected = min(n, remainingK)
        curRes = 0
        curSum = 0
        
        for selectedNum in range(maxSelected + 1):
            curVal = 0
            if selectedNum > 0:
                curVal = pile[selectedNum - 1]
            curSum += curVal
            curRes = max(self.find(i - 1, remainingK - selectedNum, piles) + curSum, curRes)

        self.memo[key] = curRes
        
        if remainingK == self.k:
            self.ans = max(self.ans, curRes)
        return curRes
                
            
        
            
    
            
            
        
        
        
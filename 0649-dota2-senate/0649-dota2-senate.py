class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #贪心策略均能找到，但是如何模拟还有下一轮就比较微妙
        q = deque(senate)
        rCount = senate.count('R')
        dCount = senate.count('D')
        bannedD = 0
        bannedR = 0
        
        while rCount and dCount:
            cur = q.popleft()
            if cur == 'D':
                if bannedD:
                    bannedD -= 1
                    dCount -= 1
                else:
                    bannedR += 1
                   # dCount += 1
                    q.append('D')
            else:
                if bannedR:
                    bannedR -= 1
                    rCount -= 1
                else:
                    bannedD += 1
                 #   rCount += 1
                    q.append('R')
        return 'Radiant' if rCount else 'Dire'
        
        
            
            
                    
        
        
                    
        
        
        
        
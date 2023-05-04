class Solution:
    def merge(self, rIdx, dIdx):
        stack = []
        nr = len(rIdx)
        nd = len(dIdx)
        i, j = 0, 0
        while i < nr or j < nd:
            r = float('inf')
            d = float('inf')
            
            if i < nr:
                r = rIdx[i]
            if j < nd:
                d = dIdx[j]
            if r < d:

                stack.append("R")
                i += 1
            else:

                stack.append("D")
                j += 1
        
        return stack
    def predictPartyVictory(self, senate: str) -> str:
        dIdx = deque()
        rIdx = deque()
        
        for i, val in enumerate(senate):
            if val == 'D':
                dIdx.append(i)
            else:
                rIdx.append(i)
        
        stack = list(senate)
        bannedR = 0
        bannedD = 0
        while dIdx and rIdx:
            dIdx = deque()
            rIdx = deque()
            
            for i, e in enumerate(stack):
                if e == 'D':
                    if bannedD:
                        bannedD -= 1
                        continue
                    bannedR += 1
                    dIdx.append(i)
                else:
                    if bannedR:
                        bannedR -= 1
                        continue
                    bannedD += 1
                    rIdx.append(i)
            stack = self.merge(rIdx, dIdx)


        if dIdx:
            return "Dire"
        return "Radiant"
            
            
                    
        
        
                    
        
        
        
        
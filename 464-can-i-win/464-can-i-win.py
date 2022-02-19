class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        final = (maxChoosableInteger+1)*(maxChoosableInteger)/2>=desiredTotal
        result = dict()
        if not final:
            return False
        def helper(state, total):
            for i in range(maxChoosableInteger):
                ith = state & (1<<i)
                if ith == 0:
                    newState = state|(1<<i)
                    newTotal = total + i + 1
                    if (newState,newTotal) not in result:
                        result[(newState, newTotal)] = helper(newState, newTotal)
                        
                    if newTotal >= desiredTotal or result[(newState, newTotal)]:
                        if state == 0: return True
                        return False
                    total = newTotal - i - 1
                    state = newState&~(1<<i)
            if state == 0: return False
            return True
        return helper(0,0)

        
                    
                    
        
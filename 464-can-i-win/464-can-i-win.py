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
                    state = state|(1<<i)
                    total += i + 1
                    if (state,total) not in result:
                        result[(state, total)] = helper(state, total)
                        
                    if total >= desiredTotal or result[(state, total)]:
                        return False
                    total = total - i - 1
                    state = state&~(1<<i)
            return True
        state = 0
        total = 0
        for i in range(maxChoosableInteger):
                ith = state & (1<<i)
                if ith == 0:
                    state = state|(1<<i)
                    total += i + 1
                    if total >= desiredTotal or helper(state, total):
                        return True
                    total = total - i - 1
                    state = state&~(1<<i)
        return False
        
                    
                    
        
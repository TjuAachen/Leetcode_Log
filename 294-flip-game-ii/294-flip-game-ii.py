class Solution:
    def canWin(self, currentState: str) -> bool:
        #record means whether the state guarantee a win
        record = {}
        def generate_nxt(state):
            res = []
            for ind, _ in enumerate(state):
                if state[ind:ind+2] == '++':
                    modified = state[:ind] + '--' + state[ind+2:]
                    res.append(modified)
            return res
        
        def win(state):
            if state in record:
                return record[state]
            res = generate_nxt(state)
            for nxt_state in res:
                if not win(nxt_state):
                    record[state] = True
                    return True
            record[state] = False
            return record[state]
        
        return win(currentState)
        
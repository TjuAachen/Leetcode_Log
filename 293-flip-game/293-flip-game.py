class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        end = len(currentState)
        for ind, state in enumerate(currentState):
            if currentState[ind:ind+2] == '++':
                modified = currentState[:ind] + '--' + currentState[ind+2:]
                res.append(modified)
        return res
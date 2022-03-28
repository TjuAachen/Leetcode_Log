class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        track = []
        global rolling
        rolling = 0
        res = set()
        def backtracking(n):
            global rolling
            if n == 0 and rolling == 0:
                res.add("".join(track))
                return
            elif n == 0:
                return
            for i in ["(",")"]:
                if i == "(":
                    rolling += 1
                    track.append("(")
                    backtracking(n-1)
                    track.pop()
                    rolling -= 1
                elif i == ")" and rolling > 0:
                    rolling -= 1
                    track.append(")")
                    backtracking(n-1)
                    track.pop()
                    rolling += 1
        backtracking(2*n)
        return list(res)
                
                
                
            
        
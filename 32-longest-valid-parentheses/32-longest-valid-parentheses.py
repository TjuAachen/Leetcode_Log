class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = []
        temp = 0
        for char in s:
            if char == "(":
                res.append(temp)
                temp = 0
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    temp += res.pop() + 1
                    stack.pop()
                else:
                    res.append(temp)
                    temp = 0
        res.append(temp)
        return max(res)*2
                
                    
                    
        
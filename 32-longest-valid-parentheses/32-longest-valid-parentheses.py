class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = []
        index = 0
        for char in s:
            if char == '(':
                stack.append(char)
                res.append(index)
                index = 0
            else:
                if stack:
                    index =index + res.pop() + 2
                    stack.pop()
                else:
                    res.append(index)
                    index = 0
        res.append(index)
        return max(res)
                    
                    
        
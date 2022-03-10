class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        record = {}
        stack = []
        for ind, char in enumerate(s):
            if char == "(":
                stack.append(ind)
            else:
                record[stack[-1]] = ind
                stack.pop()
        def count(i,j):
            if j - i == 1:
                return 1
            if record[i] == j:
                return 2*count(i+1,j-1)
            else:
                return count(i,record[i])+count(record[i]+1,j)
        return count(0,len(s)-1)
            
        
        
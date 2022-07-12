class Solution:
    def removeInvalidParentheses(self, s):
        self.res = []
        left, right = self.LeftRightCount(s)
        self.dfs(s, left, right, 0)
        return self.res
        
    def dfs(self, s, left, right, start):
        if left < 0 or right < 0: 
            return
        
        if left==0 and right==0:
            if self.isvalid(s):
                self.res.append(s)
            return
        
        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]:
                continue
            if s[i] == '(':
                self.dfs(s[:i]+s[i+1:], left-1, right, i)
            if s[i] == ')':
                self.dfs(s[:i]+s[i+1:], left, right-1, i)
    
    def isvalid(self, s):
        left, right = self.LeftRightCount(s)
        return left==0 and right==0
    
    def LeftRightCount(self, s):
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

class Solution(object):
    def isValid(self, s):
        left, right = self.minimum_removal(s)
        return left == 0 and right == 0
    
    def minimum_removal(self, s):
        stack  = []
        minimum_number = 0
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    minimum_number += 1
        left, right = len(stack), minimum_number
        return left, right
    
    def remove(self, s, start, left, right):
        global res
        if left < 0 or right < 0:
            return
        if left == right == 0:
            if self.isValid(s):
                res.append(s)
            return
        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]:
                continue
            if s[i] == '(':
                self.remove(s[:i] + s[i+1:], i, left-1, right)
            elif s[i] == ')':
                self.remove(s[:i] + s[i+1:], i, left, right - 1)
    
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        global res
        res = []
        left, right = self.minimum_removal(s)
        self.remove(s, 0, left, right)
        return res
        #duplicate need not to be traversed in the same level
        #it can be considered as a problem of combination with duplicates
    
        
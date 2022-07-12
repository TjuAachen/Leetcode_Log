class Solution(object):
    def isValid(self, s):
        return self.minimum_removal(s) == 0
    
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
        return minimum_number + len(stack)
    
    def remove(self, s, start, minimum_removal):
        global res
        if minimum_removal == 0:
            if self.isValid(s):
                res.append(s)
            return
        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]:
                continue
            if s[i] == '(' or s[i] == ')':
                self.remove(s[:i] + s[i+1:], i, minimum_removal - 1)
                
    
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        global res
        res = []
        minimum_num = self.minimum_removal(s)
        self.remove(s, 0, minimum_num)
        return res
        #duplicate need not to be traversed in the same level
        #it can be considered as a problem of combination with duplicates
    
        
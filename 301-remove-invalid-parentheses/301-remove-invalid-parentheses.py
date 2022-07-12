class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        minimum_number = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')' and not stack:
                minimum_number += 1
            elif char == ')':
                stack.pop()
        minimum_number += len(stack)
        seen = set()
        res = []
        n = len(s)
        def isValid(string, step, number, rolling):
            if number < 0:
                return
            if rolling < 0:
                return
            if step == n:
                if number == 0 and rolling == 0 and string not in seen:
                    res.append(string)
                    seen.add(string)
                return
            #if number > 0, add or remove
            #if number == 0, can only add
            #add
            if s[step] == '(':
                isValid(string + s[step], step + 1, number, rolling + 1)
            elif s[step] == ')':
                isValid(string + s[step], step + 1, number, rolling - 1)      
            else:
                isValid(string + s[step], step + 1, number, rolling) 
                #remove
            if number > 0 and s[step] in ['(', ')']:
                isValid(string, step + 1, number - 1, rolling)
        isValid('', 0, minimum_number, 0)
        return res

                
                
                
            
            
            
        
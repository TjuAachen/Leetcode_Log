class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set()

        #n pairs of parentheses
        def combination(n, stack, temp):
            if n == 0 and not stack:
                res.add(temp)
                return
            #put '('
            if n > 0:
                stack.append('(')
                combination(n - 1, stack, temp + '(')
                stack.pop()
            #put ')'
            if stack:  
                popped = stack.pop()
                combination(n, stack, temp + ')')
                stack.append(popped)
        combination(n, [], '')
        return list(res)
            
            
                
            
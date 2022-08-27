class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set()

        #n pairs of parentheses
        def combination(n, rolling, temp):
            if n == 0 and rolling == 0:
                res.add(temp)
                return
            if n > 0:
                if rolling > 0:
                    combination(n , rolling - 1, temp + ')')
                combination(n - 1, rolling + 1, temp + '(')
            else:
                combination(n, rolling - 1, temp + ')')
        combination(n, 0, '')
        return list(res)
            
            
                
            
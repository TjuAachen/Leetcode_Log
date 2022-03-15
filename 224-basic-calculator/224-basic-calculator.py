class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        sym = 1
        res = 0
        num = 0
        stack = []
        for char in s:
            if '0' <= char <= '9':
                num = num*10 + int(char)
            elif char == '+':
                res = res + sym*num
                sym = 1
                num = 0
            elif char == '-':
                res = res + sym*num
                sym = -1
                num = 0
            elif char == '(':
                stack.append(res)
                stack.append(sym)
                res = 0
                sym = 1
                num = 0
            elif char == ')':
                res = sym*num + res
                num = 0
                sym = 1
                sym_prev = stack.pop()
                res_prev = stack.pop()
                res = sym_prev*res + res_prev
        return res+sym*num

                
                
                
                
                
        
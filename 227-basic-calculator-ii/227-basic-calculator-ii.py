class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        #-1: -; 1: +; 2: /; 3: *.
        ops = 1
        res = 0
        sym = 1
        ops = [sym]
        stack =[]
        s = list(s)
        for ind,char in enumerate(s):
            if '0' <= char <= '9':
                num = num*10 + int(char)
            if char in ['+','-'] or ind == len(s) - 1:
                if sym != 2 and sym != 3:
                    res = res + sym*num

                elif sym == 2:
                    factor = ops.pop()
                    top = stack.pop()
                    res = res + top//num*factor            
                else:
                    factor = ops.pop()
                    top = stack.pop()
                    res = res + factor*top*num
                if char == '-':
                    sym = -1
                else:
                    sym = 1
                num = 0
                ops.append(sym)
            elif char == '/':
                stack.append(num)
                if len(stack) == 2:
                    denominator = stack.pop()
                    numerator = stack.pop()
                    if sym == 2:
                        stack.append(numerator//denominator)
                    elif sym == 3:
                        stack.append(numerator*denominator)
                sym = 2
                num = 0            
            elif char == '*':
                stack.append(num)
                if len(stack) == 2:
                    denominator = stack.pop()
                    numerator = stack.pop()
                    if sym == 2:
                        stack.append(numerator//denominator)
                    elif sym == 3:
                        stack.append(numerator*denominator)
                sym = 3
                num = 0    
                
        return res
                
                            
        
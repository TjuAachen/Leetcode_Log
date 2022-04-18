class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        sym = 1
        symbol = []
        number = []
        total = 0
        n = len(s)
        i = 0
        while(i < n):
            char = s[i]
            if char == '(':
                number.append(cur)
                symbol.append(sym)
                cur = 0
                sym = 1
                i = i + 1
            elif char == ")":
                cur = number.pop() + symbol.pop()*cur
                i = i + 1
            elif '0'<=char<='9':
                integer = 0
                while(i < n and '0' <= s[i] <= '9'):
                    integer = integer*10+ int(s[i])
                    i = i + 1
                cur += sym*integer
            elif char == '+':
                sym = 1
                i = i + 1
            elif char == '-':
                sym = -1
                i = i + 1
            else:
                i = i+1
        return cur
        
        
                
                
            
        
                    
                    
                    
        
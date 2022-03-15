class Solution:
    def calculate(self, s: str) -> int:
        symbol = []
        number = []
        s = list(s)
        index = 0
        n = len(s)
        sym = 1
        num = 0
        ans = 0
        while (index < n):
            char = s[index]
            if char == "+":
                sym = 1
                index += 1
            elif char == "-":
                sym = -1
                index += 1                
            elif char == '(':
                symbol.append(sym)
                number.append(ans)
                ans = 0
                sym = 1
                index = index + 1
            elif char == ')':
                ans = number.pop()+symbol.pop()*ans 
                index = index + 1
            elif '0' <= char <= '9':
                num = 0
                while(index < n):
                    test = s[index]
                    if '0' <= test <= '9':
                        num = num*10 + int(test)
                        index = index + 1
                    else:
                        break
                ans += num*sym
            else:
                index += 1
        return ans
        
                
                
            
        
                    
                    
                    
        